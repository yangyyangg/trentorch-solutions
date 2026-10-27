# Asymptotic Big-O

Intermediate | notation | foundations

### The problem, from first principles

"Is this fast enough?" depends on how an algorithm's cost grows as the input grows, not on how it performs at one specific size. `O(n)` and `O(n²)` are the vocabulary for talking about that growth rate directly, independent of any particular machine's speed — and it's exactly the vocabulary the Inference track uses to reason about attention's `O(n²)` cost in sequence length, or a matrix multiply's `O(n³)` cost in dimension. This question makes the connection between "the formula says `O(n)`" and "the code actually does about `n` units of work" concrete, by counting real operations instead of trusting the formula on faith.

### From theory to code

Implement `count_comparisons_linear_search(arr, target)`, returning **both** whether `target` was found **and** how many comparisons the search made, then `count_comparisons_binary_search(sorted_arr, target)`, doing the same for binary search on a sorted array. The signatures and docstrings are already in the editor.

### Constraints

- `arr` / `sorted_arr` is a list of numbers; `sorted_arr` is guaranteed to already be sorted ascending.
- Each function returns a tuple `(found, comparisons)`, where `found` is a `bool` and `comparisons` is the count of element-to-target comparisons actually performed (not counting index bookkeeping like a loop counter).
- `count_comparisons_binary_search` must actually halve its search space each step — a linear scan disguised as a "binary search" that happens to still find the target does not count.

### Hints

<details>
<summary>Hint 1</summary>

Linear search: walk `arr` left to right, comparing each element to `target` and incrementing a counter every time, stopping (and returning `True`) the moment a match is found.

</details>

<details>
<summary>Hint 2</summary>

Binary search: maintain `lo`/`hi` bounds, look at the midpoint, count that one comparison, and narrow to one half or the other based on whether the midpoint is less than, greater than, or equal to `target` — repeat until `lo > hi`.

</details>
