testSize = 1000;

runTimes = [testSize];

#for in = 1:testSize
#  runTimes(in) = combinedCode(0, 1, 1024);
#endfor

fprintf("done")
fileID = fopen('matlab execution results.csv', w);
xlswrite('matlab execution results.csv', runTimes); 

