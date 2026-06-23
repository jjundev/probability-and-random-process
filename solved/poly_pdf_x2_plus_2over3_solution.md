# f_X(x) = x² + 2/3 (0≤x≤1) — E[X^n] 및 분산 풀이

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

Problem 3. Let X be a continuous random variable with PDF

f_X(x) = x² + 2/3  for 0 ≤ x ≤ 1,  0 otherwise

- a. Find E(X^n), for n = 1, 2, 3, ...
- b. Find the variance of X.

---

### 1. 문제 정리 (Setup)

X의 PDF: f_X(x) = x² + 2/3 (0 ≤ x ≤ 1), otherwise 0.

| 소문항 | 구할 것 |
|---|---|
| a | E[X^n], n = 1, 2, 3, … 일반식 |
| b | Var(X) |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

E[X^n]은 기댓값 규칙(expected value rule)의 직접 적용이다. 연속 RV에서 g(x) = x^n으로 놓으면 (Lecture05, p.7):

$$\mathbb{E}[g(X)] = \int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx$$

분산은 Var(X) = E[X²] − (E[X])² — 이를 "제곱의 평균 − 평균의 제곱"으로 외운다. (STT 260413, "제곱의 평균 빼기 평균의 제곱")

### 3. 핵심 통찰 (Aha)

x^n·(x² + 2/3)을 전개하면 x^(n+2)와 x^n 두 항의 적분만 남아 — n 일반식이 한 번에 닫힌 형태로 나온다.

### 4. 풀이 (Worked solution)

**먼저 PDF 검증** (Lecture05, p.5–6)

$$\int_0^1\!\left(x^2+\tfrac{2}{3}\right)dx = \left[\frac{x^3}{3}+\frac{2x}{3}\right]_0^1 = \frac{1}{3}+\frac{2}{3} = 1 \;\checkmark$$

$$f_X(x) = \begin{cases} x^2 + \dfrac{2}{3}, & 0 \le x \le 1 \\ 0, & \text{otherwise } (x<0 \text{ or } x>1) \end{cases}$$

---

**(a) E[X^n] 일반식** (Lecture05, p.7)

$$\mathbb{E}[X^n] = \int_0^1 x^n\!\left(x^2+\frac{2}{3}\right)dx = \int_0^1 x^{n+2}\,dx + \frac{2}{3}\int_0^1 x^n\,dx$$

$$= \frac{1}{n+3} + \frac{2}{3}\cdot\frac{1}{n+1} = \frac{1}{n+3} + \frac{2}{3(n+1)}$$

공통분모 3(n+1)(n+3)으로 통분:

$$= \frac{3(n+1) + 2(n+3)}{3(n+1)(n+3)} = \frac{5n+9}{3(n+1)(n+3)}$$

$$\boxed{\mathbb{E}[X^n] = \frac{5n+9}{3(n+1)(n+3)}}$$

---

**(b) Var(X)** (STT 260413, "제곱의 평균 빼기 평균의 제곱")

n=1 대입: E[X] = (5+9) / [3·2·4] = 14/24 = **7/12**

n=2 대입: E[X²] = (10+9) / [3·3·5] = 19/45

$$\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \frac{19}{45} - \left(\frac{7}{12}\right)^2 = \frac{19}{45} - \frac{49}{144}$$

공통분모 720:

$$= \frac{304}{720} - \frac{245}{720} = \boxed{\frac{59}{720}}$$

### 5. 검산·직관 (Sanity check)

- E[X] = 7/12 ≈ 0.583. f_X(x) = x² + 2/3은 x가 커질수록 밀도↑ → 평균이 중점 0.5보다 오른쪽인 게 직관과 일치 ✓
- Var(X) = 59/720 ≈ 0.082. X는 [0,1] 안에 갇혀 있으므로 분산이 1/12 ≈ 0.083(균등분포)과 비슷한 스케일 ✓
- n=1, n=2 직접 적분으로 위 결과 재확인:
  - ∫₀¹ x(x²+2/3)dx = 1/4 + 1/3 = 7/12 ✓
  - ∫₀¹ x²(x²+2/3)dx = 1/5 + 2/9 = 19/45 ✓

### 6. 한 줄 요약

> x^n · f_X(x)를 전개해 항별 적분하면 모든 n에 대한 E[X^n]이 한 번에 닫힌 형태로 나오고, 분산은 그 n=1, 2 두 값만 꽂으면 끝이다.
