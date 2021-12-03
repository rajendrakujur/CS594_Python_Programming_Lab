
In this week you will learn about file operations in Python

The programing tasks are the following.

1. Write a Python program to do the following
   a) Read the name of a file, open it and print  the first n lines.
   (n is a user input integer)
   b)Read the name of a file, open it and print  the last n lines.
   (n is a user input integer)
   c)Read a string x,  file name y and an integer n. Append  n copies of x to
     the file y.
   d)Read a string x,  file name y and an integer n. Insert  n copies of x  at the beginnning of the file y.
   e)Read a string x,  file name y  an integer n. Insert  x  after the line number n in the file y.

2. Write a Python program to do gaussian elimination. Assume that the input matrix is given in a file. The output should be stored in a file.


3. This  assignment is about implementing a transition system. A transition system has a finite number of states. The state numbered one is the initial state.
  The system constantly receives inputs. The transition table specifies the mechanics of state change.  Your task is to read in the information about the transistion
  system and simulate the behavior of the system on various inputs.

As example of a transition table is given below
Inputs:    a b c d e f g
States:    1 2 3 4 5 6

Transistion Table

  1 2 3 4 5 1 2
  2 3 4 5 1 2 3
  3 4 5 1 2 3 4
  4 5 1 2 3 4 5
  5 1 2 3 4 5 1

The transistion table is a matrix T  and T(i,j) denotes the state to transition to from state i on input j.
 3a. Simulate the behavior of the transition system on an input.
 3b. Simulate the system on n inputs of length k chosen uniformly at random from all strings of length k. Output the fraction of inputs that end up in each state.

All the inputs are to be read from an input file and the output is to be written into an output file.




In all the programs display suitable error messages when the file operations are not permissible.
     
