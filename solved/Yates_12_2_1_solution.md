# PSP 12.2.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 기말고사 대비/L12_LLMS_5문제_시험지/문제_L12_LLMS_5문제.pdf (1/5), 1순위 근거 시험지 표지 공식 요약(Lecture 12 LLMS), 풀이일 2026-06-16

## 문제 원문

Random variables X and Y have joint PMF

```
P_{X,Y}(x,y) | y=-3   y=-1   y=1    y=3
   x = -1    | 1/6    1/8    1/24   0
   x =  0    | 1/12   1/12   1/12   1/12
   x =  1    | 0      1/24   1/8    1/6
```

(a) Find the marginal probability mass functions P_X(x) and P_Y(y).
(b) Are X and Y independent?
(c) Find E[X], Var[X], E[Y], Var[Y], and Cov[X,Y].
(d) Let X̂(Y) = aY + b be a linear estimator of X. Find a* and b*, the values of a and b that minimize the mean square error e_L.
(e) What is e*_L, the minimum mean square error of the optimum linear estimate?
(f) Find P_{X|Y}(x|−3), the conditional PMF of X given Y = −3.
(g) Find x̂_M(−3), the optimum (nonlinear) mean square estimator of X given Y = −3.
(h) Find the mean square error e*(−3) = E[(X − x̂_M(−3))² | Y = −3] of this estimate.

---

### 1. 문제 정리 (Setup)

| 소문제 | 구할 것 |
|---|---|
| (a) | 주변 PMF P_X(x), P_Y(y) |
| (b) | X, Y 독립 여부 |
| (c) | E[X], Var[X], E[Y], Var[Y], Cov[X,Y] |
| (d) | 선형추정 X̂=aY+b의 최적 a*, b* |
| (e) | 최소 MSE e*_L |
| (f) | 조건부 PMF P_{X|Y}(x|−3) |
| (g) | 비선형 MMSE 추정 x̂_M(−3)=E[X|Y=−3] |
| (h) | 그 추정의 MSE e*(−3) |

(합 = 1/3 + 1/3 + 1/3 = 1 ✓)

### 2. 무엇을 묻고 왜 이 도구인가

이 문제는 **두 가지 추정**을 한 번에 시험합니다 — (d)(e)는 평균·분산·공분산만으로 만드는 **선형 LMS**, (f)–(h)는 조건부 분포 전체를 쓰는 **비선형 MMSE**. 표지 공식대로 선형추정은 분포 전체가 필요 없고 1·2차 모멘트(E·Var·Cov)만 알면 끝나지만, MMSE는 조건부 PMF가 있어야 합니다. (시험지 표지: "선형추정 a*=Cov/Var, b*=E[X]−a*E[Y]" / "MMSE x̂_M(y)=E[X|Y=y]")

### 3. 핵심 통찰 (Aha)

> 선형추정의 모든 답은 **세 숫자 E[X]=0, Var[Y]=5, Cov[X,Y]=7/6** 에서 나오고, MMSE의 모든 답은 **Y=−3 열을 그 합으로 나눠 만든 조건부 분포** 하나에서 나온다.

### 4. 풀이 (Worked solution)

**(a) 주변 PMF** — 행/열 합산:

$$P_X(x)=\tfrac13\ \ (x\in\{-1,0,1\}),\qquad \text{otherwise }=0$$

$$P_Y(y)=\tfrac14\ \ (y\in\{-3,-1,1,3\}),\qquad \text{otherwise }=0$$

(X도 Y도 균등.)

**(b) 독립?** — 한 칸만 반례 확인:
P_{X,Y}(−1,−3) = 1/6, 그런데 P_X(−1)·P_Y(−3) = (1/3)(1/4) = 1/12 ≠ 1/6.
→ **독립 아님.**

**(c) 모멘트** — X, Y 모두 0 대칭이라 평균 0:

- E[X] = (−1+0+1)/3 = 0
- Var[X] = E[X²] = (1+0+1)/3 = **2/3**
- E[Y] = (−3−1+1+3)/4 = 0
- Var[Y] = E[Y²] = (9+1+1+9)/4 = **5**
- Cov[X,Y] = E[XY] − E[X]E[Y] = E[XY]. x=0 행은 0이므로 x=±1 행만:

$$E[XY]=\underbrace{\tfrac{1}{2}+\tfrac18-\tfrac1{24}}_{x=-1\text{ 행}}+\underbrace{-\tfrac1{24}+\tfrac18+\tfrac12}_{x=1\text{ 행}}=\tfrac{7}{12}+\tfrac{7}{12}=\boxed{\tfrac76}$$

**(d) 최적 선형계수** (표지: a*=Cov/Var Y, b*=E[X]−a*E[Y]):

$$a^*=\frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}[Y]}=\frac{7/6}{5}=\frac{7}{30},\qquad b^*=E[X]-a^*E[Y]=0-\tfrac{7}{30}\cdot0=0$$

$$\hat X(Y)=\tfrac{7}{30}\,Y$$

**(e) 최소 MSE** (표지: e*_L = Var X − Cov²/Var Y):

$$e_L^*=\mathrm{Var}[X]-\frac{\mathrm{Cov}(X,Y)^2}{\mathrm{Var}[Y]}=\frac23-\frac{(7/6)^2}{5}=\frac{120}{180}-\frac{49}{180}=\boxed{\frac{71}{180}\approx0.394}$$

**(f) 조건부 PMF** P_{X|Y}(x|−3) = P_{X,Y}(x,−3)/P_Y(−3), 분모 = 1/4:

$$P_{X\mid Y}(x\mid-3)=\begin{cases}(1/6)/(1/4)=2/3 & x=-1\\[2pt](1/12)/(1/4)=1/3 & x=0\\[2pt]0 & x=1\\[2pt]0 & \text{otherwise}\end{cases}$$

**(g) MMSE 추정** = 조건부 평균:

$$\hat x_M(-3)=E[X\mid Y=-3]=(-1)\tfrac23+(0)\tfrac13+(1)(0)=\boxed{-\tfrac23}$$

**(h) 그 MSE** = 조건부 분산:

$$e^*(-3)=E\!\big[(X-\hat x_M(-3))^2\mid Y=-3\big]=\mathrm{Var}[X\mid Y=-3]$$

$$E[X^2\mid Y=-3]=(1)\tfrac23+0+0=\tfrac23,\qquad e^*(-3)=\tfrac23-\left(-\tfrac23\right)^2=\tfrac69-\tfrac49=\boxed{\tfrac29\approx0.222}$$

### 5. 검산·직관 (Sanity check)

- 조건부 PMF 합: 2/3 + 1/3 + 0 = 1 ✓
- ρ² = Cov²/(Var X·Var Y) = (49/36)/((2/3)(5)) = 49/120 ≈ 0.408 → e*_L = (1−ρ²)Var X = (71/120)(2/3) = 71/180 ✓ (두 공식 일치)
- Y=−3에서 비교: 선형 추정 X̂ = (7/30)(−3) = −0.70, MMSE = −0.667 — 가깝게 일치, 방향(음수)도 같음 ✓
- e*(−3)=2/9≈0.222 < e*_L≈0.394: 특정 Y=−3 조건에선 분포가 두 값(−1,0)에 몰려 불확실성이 작으니 평균 MSE보다 작은 게 자연스러움 ✓

### 6. 한 줄 요약

> 선형 LMS는 (E, Var, Cov) 세 숫자만으로 a*=Cov/Var Y, b*=E[X]−a*E[Y]로 끝나고, 비선형 MMSE는 그 조건부 열(Y=−3)을 정규화한 분포의 평균·분산이 곧 추정값·오차다.
