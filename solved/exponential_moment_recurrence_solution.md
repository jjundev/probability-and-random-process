# Exponential(λ) — E[X^n] 점화식 및 닫힌 형태 증명

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

Problem 7. Let X ~ Exponential(λ). Show that

- a. E[X^n] = (n/λ) · E[X^(n−1)], for n = 1, 2, 3, ...
- b. E[X^n] = n!/λ^n, for n = 1, 2, 3, ...

---

### 1. 문제 정리 (Setup)

X ~ Exponential(λ), 즉

$$f_X(x) = \begin{cases} \lambda e^{-\lambda x}, & x \ge 0 \\ 0, & \text{otherwise } (x<0) \end{cases}$$

| 소문항 | 증명할 것 |
|---|---|
| a | E[X^n] = (n/λ) · E[X^(n−1)], n = 1, 2, 3, … |
| b | E[X^n] = n!/λ^n, n = 1, 2, 3, … |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

정리노트는 E[X] = 1/λ, E[X²] = 2/λ² 결과를 **부분적분**으로 유도한다 (Lecture05, p.14; STT 260413, "이거는 인간적으로 손으로 합시다"). 이 문제는 그 기법을 일반 n으로 확장한다. 부분적분의 핵심은 **다항식 차수를 한 단계씩 낮추는** 점화식을 만드는 것이고, (b)는 그 점화식을 n번 반복해 팩토리얼을 얻는 것이다.

### 3. 핵심 통찰 (Aha)

부분적분에서 u = x^n, dv = λe^(−λx)dx로 잡으면 경계항이 0이 되고 피적분함수에 x^(n−1)·λe^(−λx)가 남아 — E[X^(n−1)]이 자동으로 등장한다.

### 4. 풀이 (Worked solution)

**(a) 점화식 증명** — 부분적분 (Lecture05, p.14; STT 260413)

기댓값 규칙 (Lecture05, p.7):

$$\mathbb{E}[X^n] = \int_0^\infty x^n \cdot \lambda e^{-\lambda x}\,dx$$

부분적분 ∫u dv = uv − ∫v du에서

$$u = x^n,\quad dv = \lambda e^{-\lambda x}dx \;\Rightarrow\; du = nx^{n-1}dx,\quad v = -e^{-\lambda x}$$

$$\mathbb{E}[X^n] = \Bigl[-x^n e^{-\lambda x}\Bigr]_0^\infty + \int_0^\infty e^{-\lambda x}\cdot nx^{n-1}\,dx$$

**경계항 = 0**: x→∞에서 지수 감소가 다항 증가를 압도해 x^n e^(−λx)→0; x=0에서 0^n · 1 = 0 (n≥1). 따라서

$$\mathbb{E}[X^n] = 0 + n\int_0^\infty x^{n-1}\cdot e^{-\lambda x}\,dx = \frac{n}{\lambda}\int_0^\infty x^{n-1}\cdot \lambda e^{-\lambda x}\,dx$$

$$\boxed{\mathbb{E}[X^n] = \frac{n}{\lambda}\,\mathbb{E}[X^{n-1}]} \qquad \square$$

---

**(b) 닫힌 형태** — (a)의 점화식을 반복 적용

$$\mathbb{E}[X^n] = \frac{n}{\lambda}\,\mathbb{E}[X^{n-1}] = \frac{n}{\lambda}\cdot\frac{n-1}{\lambda}\,\mathbb{E}[X^{n-2}] = \cdots = \frac{n!}{\lambda^n}\,\mathbb{E}[X^0]$$

E[X^0] = E[1] = 1 (확률 전체의 적분 = 1). 따라서

$$\boxed{\mathbb{E}[X^n] = \frac{n!}{\lambda^n}} \qquad \square$$

### 5. 검산·직관 (Sanity check)

- n=1: E[X] = 1!/λ¹ = 1/λ ✓ (Lecture05, p.14)
- n=2: E[X²] = 2!/λ² = 2/λ² ✓ (Lecture05, p.14)
- n=3: E[X³] = 6/λ³ — 직접 ∫₀^∞ x³·λe^(−λx)dx를 부분적분 3번 해도 같은 결과.
- 팩토리얼 n! 은 점화식 n/λ를 n번 곱한 것: (n/λ)·((n−1)/λ)·…·(1/λ)·1 = n!/λ^n. 인수 개수도 맞다 ✓.

### 6. 한 줄 요약

> 지수분포의 n차 모멘트는 부분적분 한 번으로 점화식 E[X^n] = (n/λ)E[X^(n−1)]을 얻고, 이를 n번 반복하면 E[X^n] = n!/λ^n이 팩토리얼로 나온다.
