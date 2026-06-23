# 12.1.3 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 MMSE_조건부평균_유도.md (§2 무조건부=blind, §3 사건 조건부) + Lecture11 (LMS=조건부 평균 slide 6), 풀이일 2026-06-16

## 문제 원문

X, Y have the joint PDF

f_{X,Y}(x,y) = 2 for 0 ≤ x ≤ y ≤ 1, and 0 otherwise.

(a) What is f_X(x)?
(b) What is the blind estimate x̂_B?
(c) What is the minimum mean square error estimate of X given X > 1/2?
(d) What is f_Y(y)?
(e) What is the blind estimate ŷ_B?
(f) What is the minimum mean square error estimate of Y given X > 1/2?

---

### 1. 문제 정리 (Setup)

X, Y의 결합 PDF:

$$f_{X,Y}(x,y) = \begin{cases} 2, & 0 \le x \le y \le 1,\\[2pt] 0, & \text{otherwise.}\end{cases}$$

지지영역은 단위정사각형에서 직선 y = x 위쪽 삼각형(밑변 1, 높이 1, 넓이 1/2 → 밀도 2면 적분 1 ✓).

| 소문제 | 구할 것 |
|---|---|
| (a) | 주변밀도 f_X(x) |
| (b) | blind 추정 x̂_B |
| (c) | X > 1/2 조건에서 X의 MMSE 추정 |
| (d) | 주변밀도 f_Y(y) |
| (e) | blind 추정 ŷ_B |
| (f) | X > 1/2 조건에서 Y의 MMSE 추정 |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

두 가지 추정만 알면 전부 풀린다. 정리노트 직접 인용:

- blind 추정: 관측이 없을 때 상수 c로 X를 맞히면 "E[(X−c)² ] = Var(X) + (E[X]−c)² → c=E[X]에서 최소" → x̂_B = E[X]. (MMSE_조건부평균_유도.md §2; Lecture11 slide 13 "관측 없으면 LMS=E[Θ]")
- MMSE 추정(사건 조건부): "X > 1/2가 일어났다"는 정보가 주어지면 같은 분해가 조건부 분포 위에서 반복 → 최적 추정 = 조건부 평균 E[· | X > 1/2]. (MMSE_조건부평균_유도.md §3; Lecture11 slide 6 "θ̂_LMS = E[Θ|X=x]")

따라서 (a)(d)는 주변화 적분, (b)(e)는 평균, (c)(f)는 조건부 평균.

### 3. 핵심 통찰 (Aha)

> 추정 문제 전체가 "최적 상수 추정 = 평균"이라는 한 사실의 변주다 — 정보가 없으면 무조건부 평균, "X > 1/2"라는 정보가 있으면 그 사건으로 자른 영역의 평균.

주변밀도는 경계 y = x 하나만 정확히 넣으면 된다: 고정된 x에서 y는 x..1, 고정된 y에서 x는 0..y.

### 4. 풀이 (Worked solution)

(a) f_X(x) — y를 x..1로 적분:

$$f_X(x) = \int_x^1 2\,dy = 2(1-x),\quad 0\le x\le 1,\qquad \text{otherwise } f_X(x)=0.$$

(b) x̂_B = E[X]:

$$E[X] = \int_0^1 x\cdot 2(1-x)\,dx = 2\Big(\tfrac12-\tfrac13\Big) = \boxed{\tfrac13}.$$

(c) E[X | X > 1/2] — 먼저 사건 확률:

$$P(X>\tfrac12) = \int_{1/2}^1 2(1-x)\,dx = \tfrac14.$$

$$\int_{1/2}^1 x\cdot 2(1-x)\,dx = \Big[x^2-\tfrac23 x^3\Big]_{1/2}^1 = \tfrac13-\tfrac16 = \tfrac16.$$

$$\hat{x}_{M} = E[X\mid X>\tfrac12] = \frac{1/6}{1/4} = \boxed{\tfrac23}.$$

(d) f_Y(y) — x를 0..y로 적분:

$$f_Y(y) = \int_0^y 2\,dx = 2y,\quad 0\le y\le 1,\qquad \text{otherwise } f_Y(y)=0.$$

(e) ŷ_B = E[Y]:

$$E[Y] = \int_0^1 y\cdot 2y\,dy = 2\cdot\tfrac13 = \boxed{\tfrac23}.$$

(f) E[Y | X > 1/2] — 조건영역은 1/2 < x ≤ y ≤ 1. 분자를 y 고정·x 먼저로 적분:

$$\iint_{\frac12<x\le y\le 1} y\cdot 2\,dx\,dy = \int_{1/2}^1\!\!\Big(\int_{1/2}^{y} 2y\,dx\Big)dy = \int_{1/2}^1 (2y^2 - y)\,dy = \tfrac{5}{24}.$$

$$\hat{y}_{M} = E[Y\mid X>\tfrac12] = \frac{5/24}{1/4} = \boxed{\tfrac56}.$$

### 5. 검산·직관 (Sanity check)

- 정규화: ∫₀¹ 2(1−x)dx = 1 ✓, ∫₀¹ 2y dy = 1 ✓.
- (c) 교차검산: x 먼저 적분으로 분자 5/24를 다시 계산해도 동일 — ∫_{1/2}^1(1−x²)dx = 16/24 − 11/24 = 5/24 ✓.
- 방향성: "X > 1/2"는 X를 오른쪽으로 미는 정보 → E[X|X>1/2]=2/3 > E[X]=1/3 ✓. x ≤ y라 X가 커지면 Y는 더 커져야 하므로 E[Y|X>1/2]=5/6 > E[Y]=2/3 ✓.
- blind 추정은 항상 무조건부 평균과 같다: (b)=E[X], (e)=E[Y] ✓.

### 6. 한 줄 요약

> blind 추정은 "정보 없을 때의 평균(E[X], E[Y])", MMSE 추정은 "주어진 사건으로 잘라낸 영역의 평균(E[·|X>1/2])" — 추정의 본질은 결국 올바른 영역에서의 평균 내기다.
