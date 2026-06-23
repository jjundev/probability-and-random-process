# 7.5.1 풀이

> 출처: Probability and Stochastic Processes (Yates), 기말고사 대비/6월 10일/L08_PSP_7.5.1.png, 1순위 근거 Lecture08, 풀이일 2026-06-10

**문제 원문**
X와 Y의 결합 PDF: f_{X,Y}(x,y) = 2 (0 ≤ y ≤ x ≤ 1), otherwise 0.
주변 PDF f_Y(y), 조건부 PDF f_{X|Y}(x|y), 조건부 기댓값 E[X|Y=y]를 구하라.

### 1. 문제 정리
결합 PDF f_{X,Y}(x,y) = 2 (0 ≤ y ≤ x ≤ 1), otherwise 0. 구할 것: 주변 f_Y(y), 조건부 f_{X|Y}(x|y), 조건부 기댓값 E[X|Y=y].

### 2. 무엇을 묻고 왜 이 도구인가
조건부 기댓값을 구하려면 **조건부 밀도부터** 만들어야 한다: f_{X|Y} = f_{X,Y}/f_Y. 그래서 순서가 강제된다 — ① 주변 f_Y로 분모 확보 → ② 조건부 밀도 → ③ 그 밀도로 기댓값 적분. 정리노트의 막대자르기 예시가 똑같은 구조(f_{X|Y}(x|y)=1/y 균등, E[X|Y=y]=y/2)다 (Lecture08, p.18).

### 3. 핵심 통찰
지지(support) 0 ≤ y ≤ x ≤ 1을 **y 기준으로 슬라이스**하면, y를 고정했을 때 x는 y부터 1까지다. 즉 X | Y=y ~ Uniform[y, 1] — 균등이니 조건부 기댓값은 구간 중점.

### 4. 풀이

주변 밀도 (y 고정, x ∈ [y,1] 적분):

$$f_Y(y) = \int_y^1 2\,dx = 2(1-y),\quad 0\le y\le 1,\qquad \text{otherwise }=0$$

조건부 밀도:

$$f_{X\mid Y}(x\mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{2}{2(1-y)} = \frac{1}{1-y},\quad y\le x\le 1,\qquad \text{otherwise }=0$$

이것은 Uniform[y,1]. 조건부 기댓값:

$$\mathbb{E}[X\mid Y=y] = \int_y^1 x\cdot\frac{1}{1-y}\,dx = \frac{1}{1-y}\cdot\frac{1-y^2}{2} = \frac{1+y}{2},\quad 0\le y<1$$

### 5. 검산·직관
∫₀¹ 2(1−y) dy = 2[y − y²/2]₀¹ = 2·(1/2) = 1 ✓ (정규화). E[X|Y=y] = (1+y)/2 는 구간 [y,1]의 중점 — 균등분포이므로 정확히 직관과 일치. y→1이면 X도 1로 몰려 E→1 ✓.

### 6. 한 줄 요약
> 조건부 기댓값은 "조건부 밀도부터(=결합/주변), 그다음 적분" — 지지가 삼각형이면 한 변수를 고정해 균등 구간으로 환원하라.
