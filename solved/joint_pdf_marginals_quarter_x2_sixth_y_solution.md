# 결합 PDF (1/4 x² + 1/6 y) 주변·확률 문제 풀이

> 출처: 사용자 첨부 이미지(Problem 18), 1순위 근거 Lecture06 (Continuous RV Part 2), 풀이일 2026-06-15

## 문제 원문

Let X and Y be two jointly continuous random variables with joint PDF

f_XY(x,y) = (1/4)x² + (1/6)y  for −1 ≤ x ≤ 1, 0 ≤ y ≤ 2, otherwise 0.

- a. Find the marginal PDFs, f_X(x) and f_Y(y).
- b. Find P(X > 0, Y < 1).
- c. Find P(X > 0 or Y < 1).
- d. Find P(X > 0 | Y < 1).
- e. Find P(X + Y > 0).

---

### 1. 문제 정리 (Setup)

결합 PDF:

$$f_{XY}(x,y) = \begin{cases} \dfrac{1}{4}x^2 + \dfrac{1}{6}y, & -1 \le x \le 1,\ 0 \le y \le 2 \\[4pt] 0, & \text{otherwise} \end{cases}$$

| 소문제 | 구할 것 |
|---|---|
| a | 주변 PDF f_X(x), f_Y(y) |
| b | P(X > 0, Y < 1) |
| c | P(X > 0 또는 Y < 1) |
| d | P(X > 0 \| Y < 1) |
| e | P(X + Y > 0) |

먼저 정규화 확인: ∫₋₁¹∫₀² f dy dx = 1 이어야 한다. 안쪽 y적분 = (1/2)x² + 1/3, 바깥 x적분 = 1/3 + 2/3 = **1** ✓.

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

전형적인 **결합 연속확률변수** 문제다. 주변 PDF는 "다른 변수를 적분으로 소거"해서 얻고 — f_X(x) = ∫ f_{X,Y}(x,y) dy (Lecture06, p.11) — 확률은 영역 위 이중적분 P((X,Y)∈B) = ∬_B f dx dy (Lecture06, p.13)로 구한다. (c)는 합집합이라 포함-배제, (d)는 조건부 정의 P(A|B)=P(A∩B)/P(B), (e)는 직선 x+y=0 아래 영역을 적분한다.

### 3. 핵심 통찰 (Aha)

f_{XY}의 **x-부분 ((1/4)x²)은 x에 대해 우함수(even)**다. 그래서 X의 분포는 0을 기준으로 대칭 → P(X>0)=1/2, 그리고 (e)에서 "x+y≤0"은 x≤0(그래야 −x≥0=y의 상한이 양수) 구간에서만 일어난다.

### 4. 풀이 (Worked solution)

**(a) 주변 PDF.** f_X는 y를 0→2로 적분:

$$f_X(x) = \int_0^2 \Big(\tfrac14 x^2 + \tfrac16 y\Big)\,dy = \tfrac14 x^2\cdot 2 + \tfrac16\cdot\tfrac{2^2}{2} = \tfrac12 x^2 + \tfrac13,\quad -1\le x\le 1,\ \ \text{otherwise }=0$$

f_Y는 x를 −1→1로 적분 (∫₋₁¹ x² dx = 2/3, ∫₋₁¹ dx = 2):

$$f_Y(y) = \int_{-1}^{1}\Big(\tfrac14 x^2 + \tfrac16 y\Big)\,dx = \tfrac14\cdot\tfrac23 + \tfrac16 y\cdot 2 = \tfrac16 + \tfrac13 y,\quad 0\le y\le 2,\ \ \text{otherwise }=0$$

**(b) P(X > 0, Y < 1)** — 사각형 (0,1]×[0,1) 위 적분:

$$\int_0^1\!\!\int_0^1\Big(\tfrac14 x^2+\tfrac16 y\Big)dy\,dx = \int_0^1\Big(\tfrac14 x^2 + \tfrac{1}{12}\Big)dx = \tfrac14\cdot\tfrac13 + \tfrac1{12} = \tfrac1{12}+\tfrac1{12}=\boxed{\tfrac16}$$

**(c) P(X > 0 또는 Y < 1)** — 포함-배제:

P(X>0) = ∫₀¹ f_X dx = ∫₀¹ ((1/2)x² + 1/3) dx = 1/6 + 1/3 = 1/2 (x-대칭)
P(Y<1) = ∫₀¹ f_Y dy = ∫₀¹ (1/6 + (1/3)y) dy = 1/6 + 1/6 = 1/3

$$P(X>0 \text{ or } Y<1) = \tfrac12 + \tfrac13 - \tfrac16 = \tfrac{3+2-1}{6} = \boxed{\tfrac23}$$

**(d) P(X > 0 | Y < 1)** — 조건부 정의:

$$P(X>0\mid Y<1) = \frac{P(X>0,\,Y<1)}{P(Y<1)} = \frac{1/6}{1/3} = \boxed{\tfrac12}$$

**(e) P(X + Y > 0).** 여사건 P(X+Y≤0)=P(Y≤−X)를 적분. y≥0이므로 −x≥0, 즉 x∈[−1,0]에서만, y는 0→−x:

$$\int_{-1}^{0}\!\!\int_{0}^{-x}\Big(\tfrac14 x^2+\tfrac16 y\Big)dy\,dx = \int_{-1}^{0}\Big(\!-\tfrac14 x^3 + \tfrac1{12}x^2\Big)dx$$

(안쪽: (1/4)x²·(−x) + (1/6)·((−x)²/2) = −(1/4)x³ + (1/12)x²)

$$= -\tfrac14\cdot\Big[\tfrac{x^4}{4}\Big]_{-1}^0 + \tfrac1{12}\cdot\Big[\tfrac{x^3}{3}\Big]_{-1}^0 = \tfrac1{16} + \tfrac1{36} = \tfrac{9+4}{144} = \tfrac{13}{144}$$

$$P(X+Y>0) = 1 - \tfrac{13}{144} = \boxed{\tfrac{131}{144}} \approx 0.910$$

### 5. 검산·직관 (Sanity check)

- f_X 적분: ∫₋₁¹ ((1/2)x²+1/3)dx = 1/3+2/3 = 1 ✓ / f_Y 적분: 1/3+2/3 = 1 ✓
- (d)가 1/2 = P(X>0)인 건 우연 아님 — Y<1로 잘라도 x-부분이 여전히 우함수라 0 기준 대칭. (단, f_{XY}≠f_X f_Y 이므로 X, Y는 **독립 아님**.)
- (e): X+Y가 음수가 되려면 x∈[−1,0]이고 y가 작은 좁은 삼각 영역뿐 → 0.91은 직관과 일치 ✓
- (b) ≤ min(P(X>0), P(Y<1)) = min(1/2,1/3): 1/6 ≤ 1/3 ✓

### 6. 한 줄 요약

> 결합 연속 RV는 "다른 변수 적분 소거 → 주변, 영역 위 이중적분 → 확률"이 전부고, 합집합은 포함-배제·조건부는 교집합/조건확률·X+Y>0은 직선 아래 여사건으로 처리한다.
