# Exponential(λ=4) PDF 문제 풀이

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

Problem 2. Let X be a continuous random variable with the following PDF

f_X(x) = c·e^(−4x)  for x ≥ 0,  0 otherwise

where c is a positive constant.

- a. Find c.
- b. Find the CDF of X, F_X(x).
- c. Find P(2 < X < 5).
- d. Find EX.

---

### 1. 문제 정리 (Setup)

연속 RV X의 PDF: f_X(x) = c·e^(−4x) (x ≥ 0), 그 외 0. c는 양의 상수.

| 소문항 | 구할 것 |
|---|---|
| a | 정규화 상수 c |
| b | CDF F_X(x) |
| c | P(2 < X < 5) |
| d | E[X] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

주어진 PDF는 정리노트의 **Exponential RV** 표준형 f_X(x) = λe^(−λx) (x≥0), otherwise 0 와 완전히 같은 꼴이다 — 즉 c가 곧 λ다 (Lecture05, p.13). 그래서 c만 정하면 b·c·d는 모두 노트의 지수분포 공식에서 흘러나온다.

- a: c는 자유가 아니라 **정규화 ∫f = 1** 이 강제하는 값 (Lecture05, p.5–6).
- c: 구간확률은 노트의 운석(meteorite) 예시처럼 **CCDF로 빼면 가장 빠르다** (Lecture05, p.16).

### 3. 핵심 통찰 (Aha)

c는 고를 수 있는 게 아니라 "넓이 = 1"이 못박는 값이고, 그 c가 그대로 rate λ = 4가 된다 → 나머지는 전부 λ 하나의 함수다.

### 4. 풀이 (Worked solution)

**(a) c 구하기 — 정규화** (Lecture05, p.5–6)

$$\int_0^\infty c\,e^{-4x}\,dx = c\left[-\tfrac14 e^{-4x}\right]_0^\infty = c\left(0-\left(-\tfrac14\right)\right) = \frac{c}{4} = 1 \;\Rightarrow\; \boxed{c = 4}$$

표준형 λe^(−λx)와 비교하면 c = λ = 4. 따라서

$$f_X(x) = \begin{cases} 4e^{-4x}, & x \ge 0 \\ 0, & \text{otherwise } (x<0) \end{cases}$$

**(b) CDF** — 정의 F_X(x) = ∫_{−∞}^x f_X(t)dt (Lecture05, p.9)

x < 0이면 적분 구간에 밀도가 0이라 F_X(x) = 0. x ≥ 0이면

$$F_X(x) = \int_0^x 4e^{-4t}\,dt = \left[-e^{-4t}\right]_0^x = 1 - e^{-4x}$$

$$F_X(x) = \begin{cases} 1 - e^{-4x}, & x \ge 0 \\ 0, & \text{otherwise } (x<0) \end{cases}$$

노트의 지수분포 CDF 공식 F_X(x) = 1 − e^(−λx) (Lecture05, p.13–14)와 λ=4로 일치 ✓.

**(c) P(2 < X < 5)** — CCDF 차로 계산 (Lecture05, p.16, 운석 예시)

연속이라 P(2<X<5) = P(2≤X≤5) (경계 확률 0, Lecture05 p.5).

$$\mathbb{P}(2<X<5) = F_X(5)-F_X(2) = (1-e^{-20})-(1-e^{-8}) = e^{-8}-e^{-20} \approx 3.35\times 10^{-4}$$

(동일하게 CCDF로: P(X>2) − P(X>5) = e^(−8) − e^(−20).)

**(d) E[X]** — 지수분포 평균 공식 (Lecture05, p.14)

$$\mathbb{E}[X] = \frac{1}{\lambda} = \frac{1}{4} = 0.25$$

직접 적분으로도 확인 (부분적분, Lecture05 p.14):

$$\mathbb{E}[X] = \int_0^\infty x\cdot 4e^{-4x}\,dx = \left[-xe^{-4x}\right]_0^\infty + \int_0^\infty e^{-4x}\,dx = 0 + \frac14 = \frac14$$

### 5. 검산·직관 (Sanity check)

- c = 4 > 0 ✓ (문제의 "양의 상수" 조건 만족), ∫₀^∞ 4e^(−4x)dx = 1 ✓.
- F_X(0) = 1 − e⁰ = 0, F_X(∞) = 1, 비감소 ✓ (Lecture05, p.10).
- 평균이 1/λ = 0.25라 질량이 0 근처에 몰려 있다 → 값 2는 이미 평균의 8배(=λ·2) 떨어진 꼬리. 그래서 P(2<X<5) ≈ 0.00034로 아주 작은 게 직관과 일치 ✓.

### 6. 한 줄 요약

> 지수분포는 정규화가 c = λ를 못박는 순간 끝 — CDF·구간확률·평균이 모두 λ 하나에서 공식으로 쏟아진다.
