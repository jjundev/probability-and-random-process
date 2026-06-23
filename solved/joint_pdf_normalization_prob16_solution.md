# Problem 16 풀이 — Joint PDF, 정규화 및 영역 확률

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture06 (Continuous RV Part 2), 풀이일 2026-06-07

## 문제 원문

Let X and Y be two jointly continuous random variables with joint PDF

$$f_{XY}(x,y) = \begin{cases} \dfrac{1}{2}e^{-x} + \dfrac{cy}{(1+x)^2} & 0 \le x,\ 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$

a. Find the constant c.  
b. Find P(0 ≤ X ≤ 1, 0 ≤ Y ≤ 1/2).  
c. Find P(0 ≤ X ≤ 1).

---

### 1. 문제 정리

주어진 것:

$$f_{XY}(x,y) = \begin{cases} \dfrac{1}{2}e^{-x} + \dfrac{cy}{(1+x)^2} & 0 \le x,\ 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$

구할 것:

| | 내용 |
|---|---|
| (a) | 상수 c |
| (b) | P(0 ≤ X ≤ 1, 0 ≤ Y ≤ 1/2) |
| (c) | P(0 ≤ X ≤ 1) |

---

### 2. 무엇을 묻고 왜 이 도구인가

결합 PDF의 **정규화 조건** 및 **직사각형 영역 확률** 문제.

결합 PDF는 정의상 전체 지지 영역에서 이중적분이 1이어야 한다: P((X,Y) ∈ B) = ∬_B f_XY(x,y) dx dy. (Lecture06, p.11)

c를 구하려면 이 조건을 방정식으로 세우고 풀면 된다. (b)·(c)는 지정된 직사각형 영역에서 그대로 이중적분.

---

### 3. 핵심 통찰

**결합 PDF를 이중적분할 때, 피적분함수가 f(x) · g(y) + h(x) · k(y) 형태면 각 항을 분리해 x·y 단적분 곱으로 쪼갠다.** 계산량이 크게 줄어든다.

---

### 4. 풀이

#### (a) 정규화로 c 결정

$$\int_0^{\infty}\int_0^{1} \left[\frac{1}{2}e^{-x} + \frac{cy}{(1+x)^2}\right] dy\, dx = 1$$

두 항 분리:

**1항:**

$$\int_0^{\infty} \frac{1}{2}e^{-x} \left(\int_0^1 dy\right) dx = \int_0^{\infty} \frac{1}{2}e^{-x} \cdot 1\, dx = \frac{1}{2} \cdot 1 = \frac{1}{2}$$

**2항:**

$$c \underbrace{\int_0^{\infty}\frac{1}{(1+x)^2}dx}_{I_x}\cdot \underbrace{\int_0^1 y\, dy}_{I_y}$$

$$I_x = \left[-\frac{1}{1+x}\right]_0^{\infty} = 0 - (-1) = 1$$

$$I_y = \left[\frac{y^2}{2}\right]_0^1 = \frac{1}{2}$$

2항 합계 = c · 1 · (1/2) = c/2.

정규화 조건:

$$\frac{1}{2} + \frac{c}{2} = 1 \implies \boxed{c = 1}$$

이후 c = 1을 대입.

$$f_{XY}(x,y) = \begin{cases} \dfrac{1}{2}e^{-x} + \dfrac{y}{(1+x)^2} & 0 \le x,\ 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$

---

#### (b) P(0 ≤ X ≤ 1, 0 ≤ Y ≤ 1/2)

$$P = \int_0^1 \int_0^{1/2}\left[\frac{1}{2}e^{-x} + \frac{y}{(1+x)^2}\right] dy\, dx$$

y에 대해 내부 적분 먼저:

$$\int_0^{1/2}\left[\frac{1}{2}e^{-x} + \frac{y}{(1+x)^2}\right]dy = \left[\frac{1}{2}e^{-x}\cdot y + \frac{y^2}{2(1+x)^2}\right]_0^{1/2}$$

$$= \frac{1}{4}e^{-x} + \frac{1}{8(1+x)^2}$$

x에 대해 적분:

$$P = \int_0^1 \left[\frac{1}{4}e^{-x} + \frac{1}{8(1+x)^2}\right]dx$$

$$= \frac{1}{4}\left[-e^{-x}\right]_0^1 + \frac{1}{8}\left[-\frac{1}{1+x}\right]_0^1$$

$$= \frac{1}{4}(1-e^{-1}) + \frac{1}{8}\left(-\frac{1}{2}+1\right)$$

$$= \frac{1}{4}\left(1-\frac{1}{e}\right) + \frac{1}{16}$$

$$\boxed{P\!\left(0\le X\le 1,\ 0\le Y\le\tfrac{1}{2}\right) = \frac{5}{16} - \frac{1}{4e} \approx 0.2205}$$

---

#### (c) P(0 ≤ X ≤ 1)

X의 범위만 제한하고 Y는 전체 지지 [0,1]에서 적분:

$$P = \int_0^1 \int_0^1 \left[\frac{1}{2}e^{-x} + \frac{y}{(1+x)^2}\right] dy\, dx$$

y 내부 적분:

$$\int_0^1\left[\frac{1}{2}e^{-x} + \frac{y}{(1+x)^2}\right]dy = \frac{1}{2}e^{-x} + \frac{1}{2(1+x)^2}$$

x 적분:

$$P = \int_0^1 \left[\frac{1}{2}e^{-x} + \frac{1}{2(1+x)^2}\right]dx$$

$$= \frac{1}{2}(1-e^{-1}) + \frac{1}{2}\cdot\frac{1}{2}$$

$$\boxed{P(0\le X\le 1) = \frac{3}{4} - \frac{1}{2e} \approx 0.5662}$$

---

### 5. 검산·직관

- **(a) 검산**: c = 1이면 전체 이중적분 = 1/2 + 1/2 = 1 ✓
- **(b) vs (c) 비율**: P(b) ≈ 0.22 < P(c) ≈ 0.57, Y 범위가 절반이면 당연히 작은 값 ✓
- **지지 영역 직사각형**: [0,∞) × [0,1]이므로 적분 한계 교환 자유 ✓
- **흔한 함정** (Lecture06, p.11): 지지 영역이 직사각형이 아닐 때 적분 순서와 한계 설정 오류 — 이 문제는 해당 없음 ✓

---

### 6. 한 줄 요약

> 결합 PDF에서 c는 "전체 이중적분 = 1" 방정식으로, 직사각형 영역 확률은 그 영역에서의 이중적분으로 구한다 — 피적분함수를 x·y 항으로 분리하면 각각 단변수 적분의 곱으로 계산량이 줄어든다.
