function combinedCode
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [E] = LGBeam(p, l, w_0, xx, yy)
% Generates a Laguerre-Gaussian Beam on coordinates [xx, yy] with parameters 
% p: radial order
% l: topologial charge
% w_0: radius as a percentage
w_0
[phi,r] = cart2pol(xx,yy);
%phi=atan2(yy, xx);
RhoSquareOverWSquare = r.^2 ./ w_0.^2; %optimisation since we always use the squares
%c(p+1)=1;
%La = LaguerreL(c, abs(l), 2*RhoSquareOverWSquare);
La = Laguerre(p, abs(l), 2*RhoSquareOverWSquare);
Clg = sqrt((2*factorial(p)) ./ (pi * factorial(abs(l)+p))) ./ w_0;
E = Clg .* (sqrt(2)*sqrt(RhoSquareOverWSquare)).^abs(l) .* La .* exp(-RhoSquareOverWSquare) .* exp(-1i*l*phi);

%rad_term_1 = ((2*factorial(p))./(pi*factorial(p+abs(l)))).^(1/2);
%rad_term_2 = (sqrt(2).*r./w).^abs(l).*(exp(-(r./w).^2)./w);
%radial_function = rad_term_1.*rad_term_2;
%phase = exp(1i*phi*l);
%slm_mode = radial_function.*phase;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [complexHologram, normalisationFactor] = LGHologram(dimensionsXY, pMatrix, lMatrix, beamRadiusPercent, normaliseZeroOne, rowToColRatio)
% Generates a Laguerre-Gaussian complex hologram normalised from magnitude 0 to 1 and angle -pi to pi.
%
% This function is comprehensive and should not really be used by itself.
% Instead, use one of the "helper" function which automatically set
% several of the parameters ofthis function.
%
% dimensionsXY(1), dimensionsXY(2) : number of pixels along each dimension
%
% pMatrix :     radial Order. Values must be 0 or a matrix the same size as
%               the lMatrix.
% lMatrix :     topological charge. Can be a matrix. [1 2; 5 19] will lay 
%               them in a square.
%
% beamRadiusPercent :   0.5 will fill the hologram
%
% normaliseZeroOne : The complex hologram will be normalised from [0,1] is
% this is true, otherwise the raw hologram is output. Default is true.
%
% rowToColRatio : For use when SLM pixels are not square. 2 means that
% pixels are twice as high as they are wide. Default = 1.
%
% Returns: A complex matrix which contains the LG beam as well as the
% normalisation factor that was used to normalise the beam amplitude to
% [0,1].
%
% Example: 
% mat=LGHologram([512 512],[0],[1],0.5); ComplexFigure(mat);
% mat=LGHologram([512 512],[0],[1],CalculateBeamRadius(512,8,2)); ComplexFigure(mat);

if nargin < 5
    normaliseZeroOne = true;
end
if nargin < 6
    rowToColRatio = 1;
end

grid=size(lMatrix);
N([1 2])=fliplr(dimensionsXY);
points=N./grid;
range=N/min(N)

pMatrix(1:grid(1), 1:grid(2)) = pMatrix;
beamRadiusPercent(1:grid(1), 1:grid(2)) = beamRadiusPercent; 
x=linspace(-range(1), range(1), points(1));
y=linspace(-range(2)/rowToColRatio, range(2)/rowToColRatio, points(2));
[yy,xx]=meshgrid(y,x);


%E(points(1), grid(1), points(2), grid(2)) = 0;
E = zeros(N);
for i=1:grid(1)
    for j=1:grid(2)
        E(:,:,i,j)=LGBeam(pMatrix(i,j), lMatrix(i,j), beamRadiusPercent(i,j), xx, yy);% OAM
        %A(:,i,:,j)=grating(E(:,:,i,j), xx, yy, gratingNumber,
        %gratingAngleDegrees, useAmplitude); % no grating in this function
    end
end
%A=reshape(A, N);
E=reshape(E, N);
%max(max(E))
%normalise from 0 to 1

if normaliseZeroOne == true
    R = abs(E);
    R = R ./ max(max(R));
    Phi = angle(E);
    complexHologram = R .* exp(1i*Phi);
    %sum(sum(E .* conj(E)))

    normalisationFactor = 1 / sum(sum(conj(complexHologram).*complexHologram));
    %warning('Remember to renormalise the measurements to maintain orthonormality! See: Flamm2013.');
else
    fprintf('here')
    complexHologram = E;
    normalisationFactor = 1;
end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [ phaseHologram ] = AddGrating( inputHologram, gratingNumber, gratingAngle, complexAmplitude, gratingType, complexAmplitudeType )
%ADDGRATING Adds a grating to the provided hologram and outputs it as a
%phase-only matrix of doubles normalised to +-1 (origianlly +-pi).
%   gratingType is 'sin' or 'blazed' (defaults to blazed)
%   complexAmplitudeType defaults to 'multiply' but can also be 'sinc'. See: Clark2016 (DOI 10.1364/OE.24.006249)
%   Example: gmat = AddGrating(mat,50,0,false); imagesc(gmat);

if nargin < 5
    gratingType = 'blazed';
end
if nargin < 6
    complexAmplitudeType = 'multiply';
end

%create meshgrid
x=linspace(-pi, pi, size(inputHologram,1));
y=linspace(-pi, pi, size(inputHologram,2));
[yy,xx]=meshgrid(y,x);

theta=pi/180*gratingAngle;
plane=sin(theta)*xx+cos(theta)*yy;
phase=angle(inputHologram);

if strcmp(gratingType, 'sin') == true
    %Sin Grating
    phaseHologram=sin(phase+gratingNumber*plane+pi);
else %strcmp(grating, 'blazed') == true
    % Blazed Grating
    % See: https://en.wikipedia.org/wiki/Blazed_grating
    phaseHologram=mod(phase+gratingNumber*plane, 2*pi)-pi;
end

if (complexAmplitude)
    intensity = abs(inputHologram);
    
    if strcmp(complexAmplitudeType, 'sinc')
        error('Not implemented yet!');
       % phaseHologram = phaseHologram .* (1 - (1/pi)*asinc);
    else
        phaseHologram = phaseHologram .* intensity;        
    end
end

%renormalise to +-1
phaseHologram=(phaseHologram-pi)/(-pi-pi);

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [ beamRadiusPercent ] = CalculateBeamRadius( dimensionPixels, pixelSize_um, beamRadius_mm )
%CALCULATEBEAMRADIUS Converts beamRadius in mm to a percentage of the
%specified dimensionPixels and the pixel size

beamRadiusPercent = 1/((dimensionPixels * pixelSize_um * 1e-6)/(beamRadius_mm*1e-3))

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function y = Laguerre(p,l,x)
%%This file generates the Laguerre functions stired in the variable "y" The
%%inputs are: the indices "p","l" and the vector "x".
y=zeros(p+1,1);
sizeY = size(y);
if p==0
    y=1;
else
for m=0:p
    y(p+1-m)=((-1).^m.*(factorial(p+l)))./(factorial(p-m).*factorial(l+m).*factorial(m));
end
end
y = polyval(y,x);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [ img ] = ShowImage( img, fs, map, filename )
%SHOWIMAGE Show the specified image in a window or fullscreen. Can also
%save the image to the specified path.
%   img : A matrix to show / save as image. Must be 0 to 1
%   fs : The screen to show fullscreen on, if 0 then a window is used
%   filename : The path and filename (can be relative). If not specified
%   then the image is not saved. .png is automatically appended.

dr = [0 255]

if nargin < 2
    fs = 0;
    map=gray(256);
end

if nargin < 3
    if (max(max(img)) > 255)
        %guessing 12 bit (4095)
        map=jet(4096);
        dr = [0 4095];
        warning('Using 12 bit [0,4095] jet colormap.');
    elseif (max(max(img)) <= 1)
        img = img * 255;
    end
end

if nargin == 4
    imwrite(img, map, strcat(filename, '.png'));
end

if fs == 0
    figure; imshow(img,map,'Border','tight','InitialMagnification','fit','DisplayRange',dr); truesize(1);
elseif fs > 0
    if max(max((img ./ dr(2)))) > 1
        error('img max > 1');
    end
    fullscreen(img ./ dr(2),fs);
end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%generates a simple lg hologram with a grating

%[cols rows]
sizeGrid = [1024 1024];

l = [1]
p = [0]
complexAmplitude = true;

gratingNumber = 50;
gratingAngle = 45; %degrees

beamRadius = 1; %mm

%Generate the LG hologram matrix (complex)
mat = LGHologram(sizeGrid,p,l,CalculateBeamRadius(sizeGrid(2),8,beamRadius));
%ComplexFigure(mat);

gratingMat = AddGrating(mat,gratingNumber,gratingAngle,complexAmplitude);

ShowImage(gratingMat);

end