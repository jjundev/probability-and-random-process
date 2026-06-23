# 12.1.4 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture11 (LMS=조건부 평균 slide 6) + MMSE_조건부평균_유도.md (§3 조건부 평균), 풀이일 2026-06-16

## 문제 원문

X, Y have the joint PDF

f_{X,Y}(x,y) = 6(y − x) for 0 ≤ x ≤ y ≤ 1, and 0 otherwise.

(a) What is f_{X|Y}(x|y)?
(b) What is x̂_M(y), the MMSE estimate of X given Y = y?
(c) What is f_{Y|X}(y|x)?
(d) What is ŷ_M(x), the MMSE estimate of Y given X = x?

---

### 1. 문제 정리 (Setup)

결합 PDF:

$$f_{X,Y}(x,y) = \begin{cases} 6(y-x), & 0 \le x \le y \le 1,\\[2pt] 0, & \text{otherwise.}\end{cases}$$

지지영역은 직선 y = x 위쪽 삼각형. 밀도는 위쪽 꼭짓점에서 0, 경계에서 멀수록 커진다.

| 소문제 | 구할 것 |
|---|---|
| (a) | 조건부 밀도 f_{X|Y}(x|y) |
| (b) | x̂_M(y) = E[X | Y=y] |
| (c) | 조건부 밀도 f_{Y|X}(y|x) |
| (d) | ŷ_M(x) = E[Y | X=x] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

12.1.3은 사건 조건(X>1/2)이었지만, 여기는 변수 관측(Y=y 또는 X=x) 조건이다. 정리노트의 LMS 추정량이 그대로 적용된다 — "θ̂_LMS = E[Θ|X=x]", 즉 관측을 정확히 알 때의 MMSE 추정은 조건부 평균:

> x̂_M(y) = E[X | Y=y].   (Lecture11, slide 6; MMSE_조건부평균_유도.md §3)

그래서 절차가 고정된다: ① 주변밀도로 나눠 조건부 밀도를 만들고 → ② 그 위에서 평균을 낸다. 조건부 밀도 = 결합/주변 이라는 한 줄이 (a)(c)를, 조건부 평균이 (b)(d)를 책임진다.

### 3. 핵심 통찰 (Aha)

> Y=y로 자르면 X는 구간 [0,y]에서 밀도 ∝ (y−x)인 꼭짓점 쪽으로 감소하는 삼각분포가 되고, X=x로 자르면 Y는 [x,1]에서 ∝ (y−x)로 증가하는 삼각분포가 된다 — 선형 삼각분포의 평균은 "긴 변 쪽으로 1/3 지점" 공식 하나로 끝난다.

### 4. 풀이 (Worked solution)

먼저 두 주변밀도(나눗셈의 분모):

$$f_Y(y) = \int_0^y 6(y-x)\,dx = 3y^2,\quad 0\le y\le 1,\qquad \text{otherwise } f_Y(y)=0,$$

$$f_X(x) = \int_x^1 6(y-x)\,dy = 3(1-x)^2,\quad 0\le x\le 1,\qquad \text{otherwise } f_X(x)=0.$$

(a) 조건부 밀도 = 결합 / 주변:

$$f_{X\mid Y}(x\mid y) = \frac{6(y-x)}{3y^2} = \frac{2(y-x)}{y^2},\quad 0\le x\le y,\qquad \text{otherwise } 0.$$

(b) 그 위에서 X의 평균:

$$\hat{x}_M(y) = \int_0^y x\cdot\frac{2(y-x)}{y^2}\,dx = \frac{2}{y^2}\Big[\frac{y x^2}{2}-\frac{x^3}{3}\Big]_0^y = \frac{2}{y^2}\cdot\frac{y^3}{6} = \boxed{\frac{y}{3}}.$$

(c) 같은 방식:

$$f_{Y\mid X}(y\mid x) = \frac{6(y-x)}{3(1-x)^2} = \frac{2(y-x)}{(1-x)^2},\quad x\le y\le 1,\qquad \text{otherwise } 0.$$

(d) Y의 평균. 분자를 인수분해하면 (x−1)²(x+2)가 나와 깔끔히 약분된다:

$$\hat{y}_M(x) = \int_x^1 y\cdot\frac{2(y-x)}{(1-x)^2}\,dy = \frac{2}{(1-x)^2}\cdot\frac{(1-x)^2(x+2)}{6} = \boxed{\frac{x+2}{3}}.$$

### 5. 검산·직관 (Sanity check)

- 정규화: ∫₀ʸ 2(y−x)/y² dx = 1 ✓, ∫ₓ¹ 2(y−x)/(1−x)² dy = 1 ✓.
- 삼각분포 평균 공식 교차검산: [a,b]에서 밀도 ∝ (점에서의 거리)일 때 평균은 짧은 변에서 (2/3)(b−a) 지점. (b) a=0,b=y → 감소형이라 0쪽으로 1/3 → y/3 ✓. (d) a=x,b=1 → 증가형이라 1쪽으로 → x+(2/3)(1−x)=(x+2)/3 ✓.
- 극단값: x̂_M(1)=1/3 (Y=1이면 X~밀도 2(1−x), 평균 1/3) ✓; ŷ_M(0)=2/3 (X=0이면 Y~밀도 2y, 평균 2/3) ✓.
- 단조성: Y가 커질수록 X도 클 여지 → x̂_M(y)=y/3 증가 ✓; X가 커질수록 Y 하한이 올라감 → ŷ_M(x)=(x+2)/3 증가 ✓.

### 6. 한 줄 요약

> MMSE 추정 = 조건부 평균이고, 그 평균은 "결합÷주변으로 조건부 밀도를 만든 뒤 적분" — 여기선 둘 다 선형 삼각분포라 평균이 각각 y/3, (x+2)/3로 떨어진다.
