# Problem 3.6.6 Review Note

## 1. What this problem is testing

This problem is not mainly about geometric PMF calculation.  
The real point is to convert a random variable `M` into a new random variable `C = g(M)`.

- `M`: monthly minutes used
- `C`: monthly phone bill

So the core topic is:

> find the PMF of a transformed discrete random variable

---

## 2. Given information

`M` is geometric and

\[
E[M] = \frac{1}{p} = 30
\]

so

\[
p = \frac{1}{30}.
\]

Therefore,

\[
P(M=m) = \frac{1}{30}\left(\frac{29}{30}\right)^{m-1}, \qquad m=1,2,3,\dots
\]

The bill rule is:

- base cost: `$20`
- up to `30` minutes included
- each minute after `30` costs `$0.50`

So

\[
C =
\begin{cases}
20, & M \le 30, \\
20 + 0.5(M-30), & M > 30
\end{cases}
\]

---

## 3. Core idea

### Idea 1. Write the new variable as a function of the old variable

Do not jump directly into the PMF of `C`.

First define

\[
C = g(M).
\]

That tells you how each value of `M` maps to a bill.

---

### Idea 2. Check whether multiple values of `M` map to the same value of `C`

This is the most important step.

In this problem:

- `M = 1,2,\dots,30` all give the same bill `C = 20`
- `M = 31` gives `C = 20.5`
- `M = 32` gives `C = 21`
- and so on

So the mapping is:

- many-to-one for `C = 20`
- one-to-one for all values above `20`

That is why

\[
P(C=20) = P(M \le 30)
\]

but for `k=1,2,3,\dots`

\[
P(C=20+0.5k) = P(M=30+k).
\]

---

### Idea 3. Group probabilities correctly

When several values of the original random variable produce the same new value, add those probabilities.

That is the main transformation rule:

\[
P(C=c) = \sum_{m: g(m)=c} P(M=m).
\]

For this problem:

\[
P(C=20) = \sum_{m=1}^{30} P(M=m).
\]

This is the step students most often miss.

---

## 4. PMF result

First,

\[
P(C=20) = P(M \le 30)
= \sum_{m=1}^{30} \frac{1}{30}\left(\frac{29}{30}\right)^{m-1}
= 1 - \left(\frac{29}{30}\right)^{30}.
\]

Next, for `k=1,2,3,\dots`,

\[
P(C=20+0.5k) = P(M=30+k)
= \frac{1}{30}\left(\frac{29}{30}\right)^{29+k}.
\]

So

\[
P_C(c)=
\begin{cases}
1-\left(\frac{29}{30}\right)^{30}, & c=20, \\
\frac{1}{30}\left(\frac{29}{30}\right)^{29+k}, & c=20+0.5k,\; k=1,2,3,\dots, \\
0, & \text{otherwise}.
\end{cases}
\]

---

## 5. Fast exam checklist

When you see a problem like this, use this order:

1. identify the original random variable and its PMF
2. write the new variable as `Y = g(X)`
3. list how values of `X` map to values of `Y`
4. check whether the mapping is one-to-one or many-to-one
5. add probabilities for all original values that produce the same new value

---

## 6. Common mistakes

### Mistake 1. Writing `P(C=20) = P(M=30)`

Wrong.  
`C=20` happens for every `M` from `1` to `30`, not only at `M=30`.

### Mistake 2. Forgetting the support of `M`

For a geometric random variable here, `M` starts at `1`, not `0`.

### Mistake 3. Using expectation only and skipping the PMF structure

The fact that `E[M]=30` only helps us find `p`.  
It does not directly give the PMF of `C`.

---

## 7. One-line summary

The key lesson from Problem 3.6.6 is:

> for a transformed discrete random variable, first understand the mapping `Y=g(X)`, then combine the probabilities of all `X` values that produce the same `Y` value.
