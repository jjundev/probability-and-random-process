# Problem 3.5.16 Review Note

## 1. What this problem is really about

This is not a standard Monty Hall problem.

The host does **not** open a worthless option.  
Instead, the host opens the **larger** of the two unchosen suitcases.

That changes the information structure completely.

So the real topic is:

> choose an optimal strategy using conditional expectation and a partition of cases

---

## 2. Key random events

Let

- `C_3`: you initially choose the suitcase with `$3`
- `C_30`: you initially choose the suitcase with `$30`
- `C_300`: you initially choose the suitcase with `$300`

Each occurs with probability

\[
P(C_3)=P(C_{30})=P(C_{300})=\frac13.
\]

Let `O_i` mean the host opens the suitcase with `$i`.

The host's action is deterministic once your first choice is known:

- if you choose `$3`, the host opens `$300`
- if you choose `$30`, the host opens `$300`
- if you choose `$300`, the host opens `$30`

This is the first key observation.

---

## 3. The right way to organize the problem

Do **not** start by guessing whether switching is good or bad.

Instead:

1. split the experiment according to your initial choice
2. compute the payoff under each strategy in each case
3. combine them using expected value

This is the cleanest structure for all three parts.

---

## 4. Part (a): never switch

If you never switch, your reward is exactly what you first chose.

So

\[
P(D=3)=P(D=30)=P(D=300)=\frac13.
\]

Hence

\[
E[D]=\frac{3+30+300}{3}=111.
\]

### Core lesson

If you keep your original suitcase, the host's action does not matter at all.

---

## 5. Part (b): always switch

Track what happens after the host opens a suitcase:

- choose `$3` first -> switching gives `$30`
- choose `$30` first -> switching gives `$3`
- choose `$300` first -> switching gives `$3`

Therefore

\[
P(D=30)=\frac13,\qquad P(D=3)=\frac23.
\]

So

\[
E[D]=30\cdot\frac13+3\cdot\frac23=12.
\]

### Core lesson

Always switching is terrible here because switching never gives `$300`.

The large prize is only kept when you started with it and refused to switch.

---

## 6. Part (c): strategy depending on the host's action

This is the most important part.

Define:

- `\alpha_{30}` = probability of switching if the host opens `$30`
- `\alpha_{300}` = probability of switching if the host opens `$300`

Now compute the conditional expected reward in each initial-choice case.

### If you first chose `$3`

The host opens `$300`.

- stay -> get `$3`
- switch -> get `$30`

So

\[
E[D\mid C_3]=3(1-\alpha_{300})+30\alpha_{300}=3+27\alpha_{300}.
\]

### If you first chose `$30`

The host opens `$300`.

- stay -> get `$30`
- switch -> get `$3`

So

\[
E[D\mid C_{30}]=30(1-\alpha_{300})+3\alpha_{300}=30-27\alpha_{300}.
\]

### If you first chose `$300`

The host opens `$30`.

- stay -> get `$300`
- switch -> get `$3`

So

\[
E[D\mid C_{300}]=300(1-\alpha_{30})+3\alpha_{30}=300-297\alpha_{30}.
\]

---

## 7. Where Total Expectation Theorem appears

Now combine the three conditional expectations:

\[
E[D]
=E[D\mid C_3]P(C_3)
+E[D\mid C_{30}]P(C_{30})
+E[D\mid C_{300}]P(C_{300}).
\]

Since each initial choice has probability `1/3`,

\[
E[D]
=\frac13\Big[(3+27\alpha_{300})+(30-27\alpha_{300})+(300-297\alpha_{30})\Big].
\]

So

\[
E[D]=111-99\alpha_{30}.
\]

This is exactly the **Total Expectation Theorem**:

\[
E[D]=\sum_i E[D\mid C_i]P(C_i).
\]

---

## 8. The most important simplification

Notice that `\alpha_{300}` disappears:

\[
(3+27\alpha_{300})+(30-27\alpha_{300})=33.
\]

That means:

- when the host opens `$300`, switching and staying cancel out in expectation
- when the host opens `$30`, switching clearly hurts you

So the only decision that matters is what you do when the host opens `$30`.

---

## 9. Optimal strategy

Because

\[
E[D]=111-99\alpha_{30},
\]

the expected reward is maximized by making `\alpha_{30}` as small as possible:

\[
\alpha_{30}=0.
\]

So the optimal rule is:

- if the host opens `$30`, do **not** switch
- if the host opens `$300`, any choice is fine in expectation

The maximum expected reward is

\[
E[D]_{\max}=111.
\]

---

## 10. Fast exam checklist

When you see a problem like this:

1. identify a clean partition of the sample space
2. compute payoff case by case
3. write the strategy with parameters if the decision depends on observations
4. use conditional expectation inside each case
5. apply total expectation to combine the cases
6. optimize the final expression

---

## 11. Common mistakes

### Mistake 1. Treating it like ordinary Monty Hall

This problem is different because the host reveals the **larger remaining prize**, not a worthless option.

### Mistake 2. Ignoring the host's information

The opened suitcase is part of the information and should affect the strategy.

### Mistake 3. Comparing switch vs stay without conditioning

The clean way is to condition on your initial choice first.

### Mistake 4. Forgetting that switching can never get `$300`

In this setup, once `$300` is opened, it is gone.  
If you did not start with `$300`, you can never end with it.

---

## 12. One-line summary

The key lesson from Problem 3.5.16 is:

> partition by the initial choice, compute conditional expected rewards, and use total expectation to find the best switching rule.
