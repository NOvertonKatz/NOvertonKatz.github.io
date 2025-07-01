---
tags: sphinx
date: "2025-05-29"
category: "Programming"
---
# Debugging
There is a great quote from Albert Einstein that goes something like "In theory, there is no difference between theory and practice. But, in practice, there is.", which is pretty funny coming from a theorist. In engineering when building something, this kind of mismatch between how we think things work and how they actually do are called bugs. We have all seen them, they can takes tons of time to fix, and leave us feel frustrated and demoralized. The thing is, bugs are inevitable. Even the brightest person will not have a perfect mental model, or ability to translate it into reality. The important thing is to learn how to approach bugs effectively.

For software in particular, I have a rough categorization of bugs from a low level working up.
* Syntax bugs - The code written is not valid code. These are usually pretty simple to fix since it produces immediate errors at the location. Syntax checking tools can pick up most of these immediately. For some more 
* Logic bugs - What I think the code does, and what the code actually does are different things. These are bugs the index off by one, floating point inequality, or uninitialized variable kind of bugs. The common theme, is that the theory is all correct, there is just a mistake in execution.  
* Conceptual bugs - What I want the code to do, and the code I have are different. Conceptual bugs are harder, since they result from a significant mismatch between the theory and reality. 
* Algorithm bugs - What I want the code to do is itself wrong. The theory itself is broken, and we discovered only discovered that by building it. These are the most difficult, since you have to rule out  

## Basic tools

### Print statements and defensive programming
Use asserts

### GDB
The standard tools for C++ debugging are GDB and LLVM.

There are tons of references out there for all the commands these have


### Valgrind


## MPI programs
Believe it or not, you can still use GDB just fine with MPI programs. The only trick is getting is started.

The quick thing if you want to use
```
mpirun -np 4 xterm -e gdb my_mpi_application
```


What do you know, getting this

https://www.open-mpi.org/faq/?category=debugging

## Profilers

### NVIDIA NSight Systems and NSight Compute
Why 
