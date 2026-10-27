# THE TOKEN-AVERAGING BUG

Advanced | llm-training | loss-functions

**Difficulty:** Hard
**Tags:** LLM Training, Loss Reduction, Padding Masks

---

### Story

A language model trains on padded sequences of different lengths. One loss
implementation averages over every tensor position, including padding,
while the training contract requires averaging over valid tokens only.
Compute that valid-token mean from per-token losses and a mask.

---

### The Math

Given per-position loss `l[i][j]` and binary validity mask `m[i][j]`:

```
L = sum(m * l) / sum(m)
```

If there are no valid tokens, `L = 0`. Masked positions contribute to
neither the numerator nor the denominator.

### Input Format

`losses` (`B x T`), `mask` (`B x T`, 0/1).

### Output Format

`L`, 6 decimal places.

### Constraints

- `1 <= B, T <= 1000`, losses in `[0, 100]`, mask bits are `0` or `1`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
losses = [[1, 2, 100], [3, 100, 100]]
mask   = [[1, 1, 0],   [1, 0, 0]]
```

**Output**

```
2.000000
```

**Explanation:** Only losses `1`, `2`, and `3` are valid; their mean is `2`.
Padding losses are ignored entirely.
