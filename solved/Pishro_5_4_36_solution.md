# 5.4.36 풀이

> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), 기말고사 대비/6월 10일/L08_IPSRP_5.4.36.png, 1순위 근거 Lecture07(Cov 성질 p.23)·Lecture08(ρ p.6), 결합정규 선형결합 정규성은 일반 교과서 보강, 풀이일 2026-06-10

**문제 원문 (Problem 36)**
X와 Y는 결합정규 랜덤변수로 모수 μ_X=−1, σ_X²=4, μ_Y=1, σ_Y²=1, ρ=−1/2.
a. P(X+2Y ≤ 3)을 구하라.
b. Cov(X−Y, X+2Y)를 구하라.

### 1. 문제 정리
X, Y 결합정규: μ_X=−1, σ_X²=4 (σ_X=2), μ_Y=1, σ_Y²=1 (σ_Y=1), ρ=−1/2.
(a) P(X+2Y ≤ 3). (b) Cov(X−Y, X+2Y).

### 2. 무엇을 묻고 왜 이 도구인가
(a) 결합정규의 선형결합은 다시 정규 — W=X+2Y의 평균·분산만 구하면 표준화로 끝(강의 밖: 노트는 "독립 정규합=정규"까지만, 종속 결합정규의 선형결합 정규성은 보강). 분산 계산엔 Cov가 필요. (b) 공분산의 쌍선형성으로 전개 (Lecture07, p.23).

### 3. 핵심 통찰
Cov(X,Y) = ρσ_Xσ_Y 한 줄이 (a)의 분산과 (b)를 모두 잠금 해제한다: Cov(X,Y) = (−1/2)(2)(1) = −1.

### 4. 풀이
Cov(X,Y) = ρσ_Xσ_Y = (−1/2)(2)(1) = −1.

**(a)** W = X+2Y는 정규. 평균·분산 (Lecture07, p.23의 var(X+Y)=varX+varY+2cov 확장):

$$\mathbb{E}[W] = -1 + 2(1) = 1$$
$$\mathrm{Var}(W) = \mathrm{Var}(X) + 4\mathrm{Var}(Y) + 4\mathrm{Cov}(X,Y) = 4 + 4 + 4(-1) = 4\ \Rightarrow\ \sigma_W = 2$$

$$P(X+2Y\le 3) = P\!\left(Z \le \frac{3-1}{2}\right) = \Phi(1) \approx 0.8413$$

**(b)** 공분산 쌍선형 전개 (Lecture07, p.23: cov(aX+b,Y)=a·cov, cov(X,Y+Z)=cov+cov):

$$\mathrm{Cov}(X-Y,\ X+2Y) = \mathrm{Var}(X) + 2\mathrm{Cov}(X,Y) - \mathrm{Cov}(Y,X) - 2\mathrm{Var}(Y)$$
$$= \mathrm{Var}(X) + \mathrm{Cov}(X,Y) - 2\mathrm{Var}(Y) = 4 + (-1) - 2(1) = 1$$

### 5. 검산·직관
Var(W)=4>0 ✓. 교차항 부호: ρ<0이라 Cov(X,Y)=−1이 분산을 4+4−4=4로 줄임(음의 상관이 합의 변동을 줄임) — 직관 일치. (b)에서 −Cov(Y,X)와 +2Cov(X,Y)가 합쳐 +Cov(X,Y)=−1로 남는 것 주의.

### 6. 한 줄 요약
> 결합정규의 선형결합은 정규 → 평균·분산만 구해 Φ로; 분산·공분산은 모두 Cov(X,Y)=ρσ_Xσ_Y와 쌍선형성에서 나온다.
