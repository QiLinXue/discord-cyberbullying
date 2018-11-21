# Which is Faster, Linear Search or Default Sort + Binary Search?

Given an array, in the worst case scenario, linear search has to match the key against every single item in the array. In short, it looks at every single item *exactly once.*

No matter what sorting algorithm it is, given that the program knows absolutely nothing about how the array is ordered (e.g. it thinks it's random), it has to check every item at LEAST once in the best case scenario. 

We can prove this using a proof by contradiction. Assume that an algorithm can sort an array of length `n` with `n-1` steps, then it can theoretically sort the below array, where `x` can be any value and is the item that the program "skips" over.

```
[5, 7, 4, 6, x]
```

will become

```
[4, 5, 6, 7, x]
```

Since `x` can be anything, if it is over 7, then it is sorted. However, if it is below 7, it is not sorted. Therefore, there is a contradiction