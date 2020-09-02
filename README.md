# Overview

Here we have an example implementation of an alogrithm to partition a set of integers based on their parity.
The input is an array of randomly-generated integers, and the output is an array of the same number partitioned such that
all even numbers appear before the first odd numnber. That is, the even numbers are on the left and the odds are on the right.

Similar to a bubble sort, this algorithm compares the target element to it's neighbor and swaps the elements if necessary.
Furthermore, this algorithm is stable and will not swap two elements of the same parity, making it a candidate to be used as
an intermediate step in a larger sorting algorithm.
