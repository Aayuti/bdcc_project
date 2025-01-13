## Does the BigO Notation remain constant when switching from a single thread to a multi threaded program:

Through the various testing and scripts that demo the use of threads and profiling in a program, we can observe that the BigO notation does not change if we use multiple threads. The BigO notation describes the time complexity relative to the input.
When a program is executed with parallel processes, we can see that this input is divided and we are able to achive a higher level of performance. However this also depends on how efficiently this work has been parallelized. Multi-threading a program has some overhead and if a program requires more overhead to swap threads as compared to running in a single thread, it is more efficient to have program run in a single thread. However in a large I/O based operation, we can see significantly faster times when it comes to running and executing a script.  
This necessarly does not mean that the time will not stay constant, however the speed of execution will increase and the time taken will reduce. This is due to runtime based improvements and real world performance increases. 

### Conclusion: 
The BigO notation stays constant however, the speed of execution of a program will increase resulting to a siginificant real world performance gain.

