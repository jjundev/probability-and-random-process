# 5.4.37 풀이

> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), 기말고사 대비/6월 10일/L08_IPSRP_5.4.37.png, 1순위 근거 Lecture07(독립·Cov p.23·24)·Lecture08, 결합정규 ρ=0⇒독립은 일반 교과서 보강, 풀이일 2026-06-10

**문제 원문 (Problem 37)**
X와 Y는 결합정규 랜덤변수로 모수 μ_X=1, σ_X²=4, μ_Y=1, σ_Y²=1, ρ=0.
a. P(X+2Y > 4)를 구하라.
b. E[X²Y²]를 구하라.

### 1. 문제 정리
X, Y 결합정규: μ_X=1, σ_X²=4, μ_Y=1, σ_Y²=1, ρ=0.
(a) P(X+2Y > 4). (b) E[X²Y²].

### 2. 무엇을 묻고 왜 이 도구인가
ρ=0 + 결합정규 ⇒ X, Y 독립 (강의 밖: 일반적으론 uncorrelated⇏독립이나 [Lecture07, p.24], 결합정규는 예외적으로 동치). 독립이면 (a) W=X+2Y 정규 + (b) E[X²Y²]=E[X²]E[Y²]로 곱이 분리된다.

### 3. 핵심 통찰
"결합정규 + ρ=0 ⇒ 독립"이 이 문제의 전부 — 이게 (b)에서 기댓값의 곱 분리를 정당화한다.

### 4. 풀이
**(a)** W = X+2Y 정규:

$$\mathbb{E}[W] = 1+2(1) = 3,\qquad \mathrm{Var}(W) = 4 + 4(1) + 0 = 8\ \Rightarrow\ \sigma_W = 2\sqrt2$$
$$P(X+2Y>4) = P\!\left(Z > \frac{4-3}{2\sqrt2}\right) = P(Z>0.354) = 1-\Phi(0.354) \approx 0.362$$

**(b)** 독립이므로 (Lecture07, p.23: 독립 ⇒ E[g(X)h(Y)]=E[g(X)]E[h(Y)]):

$$\mathbb{E}[X^2Y^2] = \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$$
$$\mathbb{E}[X^2] = \mathrm{Var}(X)+(\mathbb{E}X)^2 = 4+1 = 5,\qquad \mathbb{E}[Y^2] = 1+1 = 2$$
$$\mathbb{E}[X^2Y^2] = 5\cdot 2 = 10$$

### 5. 검산·직관
ρ=0이라 Var(W)에 교차항 없음 → 8 ✓. E[X²]=σ²+μ² 공식(2차 모멘트=분산+평균²) 정확. 독립이 없으면 E[X²Y²]는 일반적으로 곱으로 안 쪼개짐 — ρ=0+결합정규라는 전제가 핵심 디딤돌.

### 6. 한 줄 요약
> 결합정규에서 ρ=0은 곧 독립 — 이 한 장이 합의 정규성(a)과 기댓값 분리 E[X²Y²]=E[X²]E[Y²](b)를 동시에 연다.
