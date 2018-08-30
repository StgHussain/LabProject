testSize = 1;
tic()
toc()
runTimes = [testSize];

for in = 1:testSize
  runTimes(in) = combinedCode(0, 1, 1024);
endfor

fprintf("done");
xlswrite('matlab results.xls', runTimes); 

