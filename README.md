# Overview

Here we have an example implementation of an alogrithm to partition a set of integers based on their parity.
The input is an array of randomly-generated integers, and the output is an array of the same number partitioned such that
all even numbers appear before the first odd numnber. That is, the even numbers are on the left and the odds are on the right.

Similar to a bubble sort, this algorithm compares the target element to it's neighbor and swaps the elements if necessary.
Furthermore, this algorithm is stable and will not swap two elements of the same parity, making it a candidate to be used as
an intermediate step in a larger sorting algorithm.

# Usage
This program can be easily run in Python3. Three arguments are required to run the program: `--min (-m)`, `--max (-M)`, and 
`--sample-size (-s)`. These arguments affect the composition of the input array that will be partitioned.
The `--min` argument sets the minimum allowed value of an integer in the array, the `--max` argument sets the maximum
allowed value of an integer in the array, and the `--sample-size` argument sets the size of the array that will be generated.
You may provide the arguments in any order.

The following usage will create a 20-element array containing integer values 0-100 and run the partition:

`python3 evenOddPartition.py -m 0 -M 100 -s 20`

Happy sorting!