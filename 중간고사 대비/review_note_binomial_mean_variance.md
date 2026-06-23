# Binomial Mean and Variance Review Note

## 1. Basic formula

If

\[
X \sim \mathrm{Binomial}(n,p),
\]

then

\[
E[X]=np
\]

and

\[
\mathrm{Var}(X)=np(1-p).
\]

Also,

\[
\sigma_X=\sqrt{np(1-p)}.
\]

---

## 2. Meaning of a binomial random variable

A binomial random variable counts the number of successes in `n` independent trials, where each trial succeeds with probability `p`.

So you should read

\[
X \sim \mathrm{Binomial}(n,p)
\]

as:

> "repeat the same trial `n` times, each with success probability `p`, and let `X` be the number of successes."

---

## 3. Why the mean is `np`

For each trial, define

\[
X_i=
\begin{cases}
1, & \text{success}\\
0, & \text{failure}
\end{cases}
\]

Then

\[
X=X_1+X_2+\cdots+X_n.
\]

Each `X_i` is a Bernoulli random variable with success probability `p`, so

\[
E[X_i]=1\cdot p+0\cdot(1-p)=p.
\]

By linearity of expectation,

\[
E[X]=E[X_1]+\cdots+E[X_n]=p+\cdots+p=np.
\]

### Memory shortcut

- one trial contributes `p` successes on average
- `n` trials contribute `np` successes on average

So

\[
\boxed{E[X]=np}
\]

---

## 4. Why the variance is `np(1-p)`

First, for one Bernoulli trial `X_i`,

\[
\mathrm{Var}(X_i)=E[X_i^2]-\bigl(E[X_i]\bigr)^2.
\]

Since `X_i` can only be `0` or `1`,

\[
X_i^2=X_i,
\]

so

\[
E[X_i^2]=E[X_i]=p.
\]

Therefore,

\[
\mathrm{Var}(X_i)=p-p^2=p(1-p).
\]

Now the trials are independent, so variances add:

\[
\mathrm{Var}(X)=\mathrm{Var}(X_1)+\cdots+\mathrm{Var}(X_n).
\]

Hence

\[
\mathrm{Var}(X)=np(1-p).
\]

### Memory shortcut

- variance of one Bernoulli trial = `p(1-p)`
- add that over `n` independent trials

So

\[
\boxed{\mathrm{Var}(X)=np(1-p)}
\]

---

## 5. Do we need to compute `E[X^2]` directly?

Usually, no.

For binomial random variables, if the problem asks for the mean or variance, the fastest method is to use

\[
E[X]=np,\qquad \mathrm{Var}(X)=np(1-p).
\]

You do **not** usually need to compute `E[X^2]` directly.

However, `E[X^2]` is still related to variance through

\[
\mathrm{Var}(X)=E[X^2]-\bigl(E[X]\bigr)^2.
\]

So

\[
E[X^2]=\mathrm{Var}(X)+\bigl(E[X]\bigr)^2.
\]

For a binomial random variable,

\[
E[X^2]=np(1-p)+(np)^2.
\]

So the practical rule is:

- if the problem asks only for mean or variance, use the binomial formulas directly
- if the problem asks for `E[X^2]`, then compute it from variance and mean

---

## 6. Example

If

\[
X \sim \mathrm{Binomial}(4,1/2),
\]

then

\[
E[X]=4\cdot \frac12=2
\]

\[
\mathrm{Var}(X)=4\cdot \frac12\cdot \frac12=1
\]

\[
\sigma_X=\sqrt{1}=1.
\]

Also,

\[
E[X^2]=\mathrm{Var}(X)+(E[X])^2=1+2^2=5.
\]

---

## 7. Exam checklist

When you see `X ~ Binomial(n,p)`, immediately write down:

1. `E[X]=np`
2. `Var(X)=np(1-p)`
3. `sigma = sqrt(np(1-p))`

Then check whether the problem really needs:

- only the formula
- or also a probability such as `P(a \le X \le b)`
- or `E[X^2]`

---

## 8. One-line summary

For a binomial random variable,

\[
\boxed{E[X]=np,\qquad \mathrm{Var}(X)=np(1-p),\qquad E[X^2]=np(1-p)+(np)^2}
\]

and in most problems, you do not need to calculate `E[X^2]` separately unless the question explicitly asks for it.
