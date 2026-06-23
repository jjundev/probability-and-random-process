# Yates 5.8.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 1순위 근거 Lecture07 (Covariance)·Lecture08 (상관계수), 풀이일 2026-06-09

## 문제 원문

X and Z are independent random variables with E[X]=E[Z]=0 and variance Var[X]=1 and Var[Z]=16. Let Y=X+Z. Find the correlation coefficient ρ of X and Y. Are X and Y independent?

---

### 1. 문제 정리 (Setup)

X⊥Z, E[X]=E[Z]=0, Var[X]=1, Var[Z]=16. Y = X+Z.
구할 것: ρ(X,Y), X와 Y 독립 여부.

---

### 2. 무엇을 묻고 왜 이 도구인가

Y가 X를 포함하므로 Cov(X,Y)가 0이 아닐 것으로 예상. 공분산의 선형성으로 Cov(X, X+Z)를 분해하고, 상관계수로 정규화한다. (Lecture07, p.23–25; Lecture08, p.6)

$$\rho(X,Y) = \frac{\text{cov}(X,Y)}{\sqrt{\text{Var}[X]\cdot\text{Var}[Y]}}$$

---

### 3. 핵심 통찰 (Aha)

Cov(X, X+Z) = Cov(X,X) + Cov(X,Z) = Var[X] + 0 — X⊥Z이므로 Z 항이 사라지고, X 자기 자신과의 공분산만 남는다.

---

### 4. 풀이 (Worked solution)

E[Y] = 0, Var[Y] = Var[X] + Var[Z] = 1 + 16 = 17

$$\text{cov}(X,Y) = \text{cov}(X, X+Z) = \text{Var}[X] + \text{cov}(X,Z) = 1 + 0 = 1$$

$$\rho(X,Y) = \frac{1}{\sqrt{1 \cdot 17}} = \frac{1}{\sqrt{17}} \approx 0.243$$

ρ ≠ 0 → X와 Y는 독립이 아니다.
직관: E[Y|X=x] = x ≠ 0 = E[Y] — X를 알면 Y에 대한 정보가 생김.

---

### 5. 검산·직관 (Sanity check)

- 0 < 1/√17 < 1 ✓
- Var[Z]→∞이면 ρ→0, Var[Z]→0이면 ρ→1 — 잡음이 클수록 X와 Y의 관계가 희석됨 ✓

---

### 6. 한 줄 요약

> Y = X+Z에서 ρ(X,Y) = 1/√17 — X가 Y 안에 들어있으면 공분산이 자동으로 Var[X]가 되고, X와 Y는 독립이 아니다.
