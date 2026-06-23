# Yates 4.5.13 풀이 — Exponential(λ=1/2): P·CDF·E[X]·Var[X]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture05 (Continuous RV Part 1) p.13–14, 풀이일 2026-06-07

## 문제 원문

The probability density function of random variable X is

$$f_X(x) = \begin{cases} (1/2)e^{-x/2} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$

(a) What is P[1 ≤ X ≤ 2]?  
(b) What is F_X(x), the cumulative distribution function of X?  
(c) What is E[X], the expected value of X?  
(d) What is Var[X], the variance of X?

---

### 1. 문제 정리

| | 구할 것 |
|---|---|
| (a) | P[1 ≤ X ≤ 2] |
| (b) | CDF F_X(x) |
| (c) | E[X] |
| (d) | Var[X] |

---

### 2. 무엇을 묻고 왜 이 도구인가

f_X(x) = (1/2)e^(-x/2)는 λe^(-λx)에서 λ = 1/2인 지수분포다. 이를 식별하는 순간 CDF·E·Var 공식을 그대로 적용할 수 있다. (Lecture05, p.13–14)

---

### 3. 핵심 통찰

**PDF에서 λ = 1/2를 읽어내면 나머지는 공식 대입 — 분포 식별이 전부다.**

---

### 4. 풀이

X ~ Exponential(λ = 1/2) 확정.

#### (a) P[1 ≤ X ≤ 2]

$$P[1 \le X \le 2] = e^{-1/2} - e^{-1} \approx \boxed{0.239}$$

#### (b) CDF F_X(x)

$$F_X(x) = \begin{cases} 1 - e^{-x/2} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$

#### (c) E[X]

$$E[X] = \frac{1}{\lambda} = \frac{1}{1/2} = \boxed{2}$$

#### (d) Var[X]

$$\text{Var}[X] = \frac{1}{\lambda^2} = \frac{1}{(1/2)^2} = \boxed{4}$$

확인: E[X²] = 2/λ² = 8, Var = 8 − 4 = 4 ✓

---

### 5. 검산·직관

- 정규화: ∫₀^∞ (1/2)e^(-x/2) dx = 1 ✓
- F_X(0) = 0, F_X(∞) = 1 ✓
- Exponential에서 항상 Var[X] = (E[X])² — 여기서 Var = 4 = 2² ✓

---

### 6. 한 줄 요약

> PDF에서 λ를 읽어내면 Exponential의 CDF·E·Var는 공식 한 줄씩 — 식별이 곧 풀이다.
