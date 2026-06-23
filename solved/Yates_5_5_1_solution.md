# 5.5.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture06, 풀이일 2026-06-15

## 문제 원문

Random variables X and Y have the joint PDF

f_XY(x,y) = 1/2  for −1 ≤ x ≤ y ≤ 1, otherwise 0.

Sketch the region of nonzero probability and answer the following questions.
- (a) What is P[X > 0]?
- (b) What is f_X(x)?
- (c) What is E[X]?

---

### 1. 문제 정리 (Setup)

결합 PDF:

$$f_{XY}(x,y) = \begin{cases} \dfrac{1}{2}, & -1 \le x \le y \le 1 \\[4pt] 0, & \text{otherwise} \end{cases}$$

영역은 부등식 사슬 −1 ≤ x ≤ y ≤ 1 — 즉 꼭짓점 (−1,−1), (−1,1), (1,1)인 직각삼각형(대각선 y=x 위쪽).

| 소문제 | 구할 것 |
|---|---|
| a | P[X > 0] |
| b | 주변 PDF f_X(x) |
| c | E[X] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

"균등(uniform) 결합분포 = 영역 위 상수 밀도"라, 확률은 사실상 넓이 비율이고 적분이 단순하다. 주변은 다른 변수 적분 소거 f_X(x) = ∫ f_{X,Y}(x,y) dy (Lecture06, p.11), 기댓값은 E[X] = ∫ x·f_X(x) dx. 결정적 포인트는 적분 한계 — 삼각 영역이라 y의 범위가 x에 의존(x ≤ y ≤ 1)한다.

먼저 정규화 확인: 삼각형 넓이 = (1/2)·2·2 = 2, 밀도 1/2 → 전확률 2·(1/2) = 1 ✓.

### 3. 핵심 통찰 (Aha)

−1 ≤ x ≤ y ≤ 1 사슬을 "고정된 x에 대해 y는 x부터 1까지"로 읽는 순간 모든 한계가 정해진다 — y의 아래끝이 상수가 아니라 x라는 게 핵심.

### 4. 풀이 (Worked solution)

**(b) 주변 f_X(x)** (먼저 구하면 a·c에 재활용). 고정 x에서 y를 x→1로 적분:

$$f_X(x) = \int_x^1 \tfrac12\,dy = \tfrac12(1-x), \quad -1\le x\le 1, \qquad \text{otherwise } = 0$$

**(a) P[X > 0]**. f_X를 0→1로 적분:

$$P[X>0] = \int_0^1 \tfrac12(1-x)\,dx = \tfrac12\Big[x-\tfrac{x^2}{2}\Big]_0^1 = \tfrac12\Big(1-\tfrac12\Big) = \boxed{\tfrac14}$$

**(c) E[X]**.

$$E[X] = \int_{-1}^{1} x\cdot\tfrac12(1-x)\,dx = \tfrac12\int_{-1}^1 (x - x^2)\,dx$$

∫₋₁¹ x dx = 0 (기함수), ∫₋₁¹ x² dx = 2/3 이므로:

$$E[X] = \tfrac12\Big(0 - \tfrac23\Big) = \boxed{-\tfrac13}$$

### 5. 검산·직관 (Sanity check)

- f_X 정규화: ∫₋₁¹ (1/2)(1−x) dx = (1/2)·2 = 1 ✓
- P[X>0]=1/4: 삼각형에서 x>0 부분은 작은 삼각형(꼭짓점 (0,0),(0,1),(1,1), 넓이 1/2)이고 1/2·1/2 = 1/4 — 넓이로도 일치 ✓
- E[X]=−1/3 < 0: 항상 X ≤ Y(X가 둘 중 작은 쪽)이라 X가 음수로 치우치는 게 자연스럽다 ✓ (참고로 대칭상 E[Y]=+1/3.)

### 6. 한 줄 요약

> 균등 결합분포는 확률=넓이비율이며, 삼각 영역의 핵심은 "x를 고정하고 y는 x부터 1까지"로 의존 한계를 잡는 것 — 그러면 주변·확률·기댓값이 줄줄이 풀린다.
