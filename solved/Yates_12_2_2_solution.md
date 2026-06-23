# PSP 12.2.2 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 기말고사 대비/L12_LLMS_5문제_시험지/문제_L12_LLMS_5문제.pdf (2/5), 1순위 근거 시험지 표지 공식 요약(Lecture 12 LLMS), 풀이일 2026-06-16

## 문제 원문

A telemetry voltage V, transmitted from a position sensor on a ship's rudder, is a random variable with PDF

```
f_V(v) = 1/12,  −6 ≤ v ≤ 6
       = 0,     otherwise
```

A receiver in the ship's control room receives R = V + X. The random variable X is a Gaussian (0, √3) noise voltage that is independent of V. The receiver uses R to calculate a linear estimate of the telemetry voltage: V̂ = aR + b. Find

(a) the expected received voltage E[R],
(b) the variance Var[R] of the received voltage,
(c) the covariance Cov[V, R] of the transmitted and received voltages,
(d) a* and b*, the optimum coefficients in the linear estimate,
(e) e*_L, the minimum mean square error of the estimate.

---

### 1. 문제 정리 (Setup)

주어진 것:
- V ~ Uniform[−6, 6], f_V(v) = 1/12 (−6 ≤ v ≤ 6), otherwise 0
- R = V + X, X ~ Gaussian(0, √3) — Yates 표기 (평균, 표준편차) → σ_X = √3 → Var[X] = 3
- X ⊥ V (독립), 선형추정 V̂ = aR + b

| 소문제 | 구할 것 |
|---|---|
| (a) | E[R] |
| (b) | Var[R] |
| (c) | Cov[V, R] |
| (d) | 최적 선형계수 a*, b* |
| (e) | 최소 MSE e*_L |

### 2. 무엇을 묻고 왜 이 도구인가

12.2.1과 똑같은 선형추정이지만, 이번엔 표가 아니라 **"신호 + 독립 잡음"(R = V + X)** 모형이다. 핵심은 모멘트를 직접 적분으로 구하지 않고 **독립성으로 분해**하는 것 — Var와 Cov가 잡음항을 깔끔히 떼어낸다. (시험지 표지: "선형추정 a*=Cov/Var Y, b*=E[X]−a*E[Y]", "e*_L = Var X − Cov²/Var Y")

### 3. 핵심 통찰 (Aha)

> R = V + X 에서 X가 V와 독립이라, Var[R] = Var[V] + Var[X] 로 더해지고 Cov[V,R] = Var[V] 로 잡음이 완전히 사라진다 — 추정에 필요한 세 수가 즉시 나온다.

### 4. 풀이 (Worked solution)

먼저 균등분포 분산 (Uniform[α,β] → Var = (β−α)²/12):

$$\mathrm{Var}[V]=\frac{(6-(-6))^2}{12}=\frac{144}{12}=12,\qquad \mathrm{Var}[X]=(\sqrt3)^2=3$$

**(a) E[R]** — 평균은 선형이고 둘 다 0:

$$E[R]=E[V]+E[X]=0+0=0$$

**(b) Var[R]** — V ⊥ X 이므로 분산이 더해짐:

$$\mathrm{Var}[R]=\mathrm{Var}[V]+\mathrm{Var}[X]=12+3=15$$

**(c) Cov[V, R]** — 공분산 이중선형 + 독립(Cov[V,X]=0):

$$\mathrm{Cov}[V,R]=\mathrm{Cov}[V,\,V+X]=\mathrm{Var}[V]+\underbrace{\mathrm{Cov}[V,X]}_{=0}=12$$

**(d) 최적 계수** (표지 공식):

$$a^*=\frac{\mathrm{Cov}[V,R]}{\mathrm{Var}[R]}=\frac{12}{15}=\frac45,\qquad b^*=E[V]-a^*E[R]=0-\tfrac45\cdot0=0$$

$$\hat V=\tfrac45\,R$$

**(e) 최소 MSE** (표지: e*_L = Var V − Cov²/Var R):

$$e_L^*=\mathrm{Var}[V]-\frac{\mathrm{Cov}[V,R]^2}{\mathrm{Var}[R]}=12-\frac{12^2}{15}=12-\frac{144}{15}=12-9.6=\boxed{2.4=\tfrac{12}{5}}$$

### 5. 검산·직관 (Sanity check)

- (1−ρ²) 형태로 교차검증: ρ² = Cov²/(Var V·Var R) = 144/(12·15) = 144/180 = 0.8 → e*_L = (1−0.8)·12 = 0.2·12 = 2.4 ✓ (두 형태 일치)
- a* = 4/5 < 1: 받은 R을 그대로 믿지 않고 살짝 0 쪽으로 수축(shrink)시킴 — 잡음이 섞였으니 당연. 잡음이 0(Var X=0)이면 a*=Var V/Var V=1, e*_L=0 (완벽추정) ✓
- e*_L = 2.4 < Var[V] = 12: 관측 R이 V에 대한 정보를 줘서 불확실성이 12 → 2.4로 줄어듦, 방향 맞음 ✓

### 6. 한 줄 요약

> "신호+독립잡음" R=V+X에선 Var[R]=Var V+Var X로 잡음이 더해지고 Cov[V,R]=Var V로 잡음이 사라진다 — 그래서 a*=Var V/(Var V+Var X)<1, 잡음이 클수록 추정을 0으로 더 수축시킨다.
