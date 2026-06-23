# Problem 21 풀이 — 조건부 PDF f_{X|Y}, 조건부 확률, 독립성 판정

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture06 (Continuous RV Part 2) p.18, 풀이일 2026-06-07

## 문제 원문

Let X and Y be two jointly continuous random variables with joint PDF

$$f_{XY}(x,y) = \begin{cases} x^2 + \dfrac{1}{3}y & -1 \le x \le 1,\ 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$

For 0 ≤ y ≤ 1, find the following:

a. The conditional PDF of X given Y = y.  
b. P(X > 0 | Y = y). Does this value depend on y?  
c. Are X and Y independent?

---

### 1. 문제 정리

| | 내용 |
|---|---|
| (a) | 조건부 PDF f_{X|Y}(x|y) |
| (b) | P(X > 0 | Y = y) — y에 의존하는가? |
| (c) | X와 Y는 독립인가? |

---

### 2. 무엇을 묻고 왜 이 도구인가

RV Y에 조건화된 조건부 PDF 공식 (Lecture06, p.18):

$$f_{X|Y}(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)}$$

분모 f_Y(y)를 먼저 주변 PDF로 구한 뒤 대입. 독립성 판정 (Lecture06, p.18):

$$X \perp Y \iff f_{XY}(x,y) = f_X(x)\,f_Y(y) \text{ for all } x,y$$

---

### 3. 핵심 통찰

**조건부 PDF는 결합 PDF를 주변 PDF로 나눠 재정규화한 것 — 분모를 먼저 구하는 것이 전부다.** 독립성은 결합 PDF가 x만의 함수 × y만의 함수 곱으로 분리되는지로 판정한다.

---

### 4. 풀이

#### 사전 계산: 주변 PDF f_Y(y)

$$f_Y(y) = \int_{-1}^{1} \left(x^2 + \frac{y}{3}\right)dx = \left[\frac{x^3}{3} + \frac{y}{3}x\right]_{-1}^{1} = \frac{2(1+y)}{3}$$

$$f_Y(y) = \frac{2(1+y)}{3}, \quad 0 \le y \le 1, \qquad \text{otherwise } = 0$$

검산: ∫₀¹ (2/3)(1+y) dy = (2/3)(3/2) = 1 ✓

---

#### (a) 조건부 PDF f_{X|Y}(x|y)

$$f_{X|Y}(x|y) = \frac{x^2 + \dfrac{y}{3}}{\dfrac{2(1+y)}{3}} = \frac{3x^2 + y}{2(1+y)}$$

$$\boxed{f_{X|Y}(x|y) = \frac{3x^2 + y}{2(1+y)}, \quad -1 \le x \le 1, \qquad \text{otherwise } = 0}$$

검산:

$$\int_{-1}^{1}\frac{3x^2+y}{2(1+y)}\,dx = \frac{1}{2(1+y)}\left[x^3 + yx\right]_{-1}^{1} = \frac{2(1+y)}{2(1+y)} = 1 \checkmark$$

---

#### (b) P(X > 0 | Y = y)

$$P(X>0 \mid Y=y) = \int_0^1 \frac{3x^2+y}{2(1+y)}\,dx = \frac{1}{2(1+y)}\left[x^3+yx\right]_0^1 = \frac{1+y}{2(1+y)} = \boxed{\frac{1}{2}}$$

**y에 의존하지 않는다.** 분자의 (1+y)가 분모와 약분된다.

---

#### (c) 독립성 판정

f_X(x) 계산:

$$f_X(x) = \int_0^1\left(x^2+\frac{y}{3}\right)dy = x^2 + \frac{1}{6}, \quad -1 \le x \le 1, \qquad \text{otherwise } = 0$$

(x, y) = (0, 0)에서 확인:

$$f_{XY}(0,0) = 0, \qquad f_X(0)\cdot f_Y(0) = \frac{1}{6}\cdot\frac{2}{3} = \frac{1}{9} \ne 0$$

$$\boxed{X \text{와 } Y \text{는 독립이 아니다.}}$$

근본 이유: f_XY(x,y) = x² + y/3은 g(x)·h(y) 꼴로 인수분해 불가.

---

### 5. 검산·직관

- f_Y 검산: ∫₀¹ (2/3)(1+y)dy = 1 ✓
- f_{X|Y} 검산: ∫₋₁¹ f_{X|Y}(x|y)dx = 1 ✓
- (b) 직관: f_{X|Y}의 x² 항은 [-1,1]에서 좌우 대칭 → P(X>0|Y=y) = 1/2 필연
- (c) 주의: "P(X>0|Y=y)가 y에 무관"해도 독립이 아닐 수 있다. 독립은 모든 사건에서 무관해야 함.

---

### 6. 한 줄 요약

> 조건부 PDF는 결합 PDF ÷ 주변 PDF로 구하고, 독립성은 결합 PDF가 f_X(x)·f_Y(y)로 곱 분리되는지로 판정한다 — 특정 사건의 확률이 y에 무관해도 독립과는 다른 개념이다.
