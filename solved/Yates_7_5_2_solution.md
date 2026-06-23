# 7.5.2 풀이

> 출처: Probability and Stochastic Processes (Yates), 기말고사 대비/6월 10일/L08_PSP_7.5.2.png, 1순위 근거 Lecture08, 풀이일 2026-06-10

**문제 원문**
7.5.1과 같은 결합 PDF f_{X,Y}(x,y) = 2 (0 ≤ y ≤ x ≤ 1), otherwise 0.
주변 PDF f_X(x), 조건부 PDF f_{Y|X}(y|x), 조건부 기댓값 E[Y|X=x]를 구하라.

### 1. 문제 정리
7.5.1과 **같은** 결합 PDF f_{X,Y}(x,y) = 2 (0 ≤ y ≤ x ≤ 1). 이번엔 반대 방향: 주변 f_X(x), 조건부 f_{Y|X}(y|x), E[Y|X=x].

### 2. 무엇을 묻고 왜 이 도구인가
7.5.1의 대칭판. 같은 지지를 이번엔 **x 기준으로 슬라이스**한다. x 고정 시 y는 0부터 x까지.

### 3. 핵심 통찰
0 ≤ y ≤ x ⇒ x 고정하면 Y | X=x ~ Uniform[0, x]. 중점은 x/2.

### 4. 풀이

$$f_X(x) = \int_0^x 2\,dy = 2x,\quad 0\le x\le 1,\qquad \text{otherwise }=0$$

$$f_{Y\mid X}(y\mid x) = \frac{2}{2x} = \frac{1}{x},\quad 0\le y\le x,\qquad \text{otherwise }=0$$

$$\mathbb{E}[Y\mid X=x] = \int_0^x y\cdot\frac{1}{x}\,dy = \frac{1}{x}\cdot\frac{x^2}{2} = \frac{x}{2},\quad 0<x\le 1$$

### 5. 검산·직관
∫₀¹ 2x dx = 1 ✓. Y|X=x ~ Uniform[0,x]의 평균 x/2 ✓. 7.5.1과 합쳐 보면: E[X|Y]=(1+Y)/2, E[Y|X]=X/2 — 두 조건부 평균이 서로 선형, 결합밀도가 평평(=2)한 삼각형의 전형.

### 6. 한 줄 요약
> 같은 결합밀도라도 "어느 변수로 조건 거느냐"에 따라 슬라이스 방향이 바뀐다 — X 고정 → Y~U[0,x], Y 고정 → X~U[y,1].
