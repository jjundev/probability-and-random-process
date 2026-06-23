# PSP 12.2.3 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 기말고사 대비/L12_LLMS_5문제_시험지/문제_L12_LLMS_5문제.pdf (3/5), 1순위 근거 시험지 표지 공식 요약(Lecture 12 LLMS), 풀이일 2026-06-16

## 문제 원문

Random variables X and Y have joint PMF given by the following table:

```
P_{X,Y}(x,y) | y=-1    y=0     y=1
   x = -1    | 3/16    1/16    0
   x =  0    | 1/6     1/6     1/6
   x =  1    | 0       1/8     1/8
```

We estimate Y by Ŷ_L(X) = aX + b.

(a) Find a and b to minimize the mean square estimation error.
(b) What is the minimum mean square error e*_L?

---

### 1. 문제 정리 (Setup)

추정 모형: Ŷ_L(X) = aX + b — **관측 = X, 추정대상 = Y** (12.2.1·12.2.2와 방향 반대).

| 소문제 | 구할 것 |
|---|---|
| (a) | MSE 최소화 a*, b* |
| (b) | 최소 MSE e*_L |

(합 = 1/4 + 1/2 + 1/4 = 1 ✓)

### 2. 무엇을 묻고 왜 이 도구인가

12.2.1과 같은 표 기반 선형추정이지만, **추정 방향이 X→Y로 뒤집혀** 있다. 공식의 분모가 "관측변수의 분산"이라는 점만 정확히 잡으면 된다 — 여기선 관측이 X이므로 a* = Cov(X,Y)/Var(X), 잔차오차의 출발점은 추정대상 Var(Y). (시험지 표지: "선형추정 a*=Cov/Var, b*=E[X]−a*E[Y]" — 여기서 "X"는 일반화된 관측변수)

### 3. 핵심 통찰 (Aha)

> 추정 방향이 X→Y이므로 공식의 분모는 관측변수 Var(X), 출발 분산은 대상 Var(Y) — "분모 = 내가 보는 것, 빼는 출발점 = 내가 맞히려는 것"만 기억하면 끝.

### 4. 풀이 (Worked solution)

**주변분포** (행 합 = P_X, 열 합 = P_Y):

$$P_X(x)=\begin{cases}1/4 & x=-1\\ 1/2 & x=0\\ 1/4 & x=1\end{cases}\quad\text{otherwise}=0,\qquad P_Y(y)=\begin{cases}17/48 & y=-1\\ 17/48 & y=0\\ 14/48 & y=1\end{cases}\quad\text{otherwise}=0$$

**모멘트.** X는 대칭이라 E[X]=0:

$$E[X]=0,\qquad \mathrm{Var}[X]=E[X^2]=\tfrac14+\tfrac14=\tfrac12$$

$$E[Y]=(-1)\tfrac{17}{48}+0+\,(1)\tfrac{14}{48}=-\tfrac{3}{48}=-\tfrac{1}{16}$$

$$E[Y^2]=\tfrac{17}{48}+\tfrac{14}{48}=\tfrac{31}{48},\qquad \mathrm{Var}[Y]=\tfrac{31}{48}-\left(\tfrac{1}{16}\right)^2=\tfrac{496}{768}-\tfrac{3}{768}=\tfrac{493}{768}$$

**공분산** — xy·P(x,y) 합 (x=0 행과 0인 칸 제외):

$$E[XY]=\underbrace{(-1)(-1)\tfrac{3}{16}}_{x=-1,\,y=-1}+\underbrace{(1)(1)\tfrac18}_{x=1,\,y=1}=\tfrac{3}{16}+\tfrac{2}{16}=\tfrac{5}{16}$$

$$\mathrm{Cov}[X,Y]=E[XY]-E[X]E[Y]=\tfrac{5}{16}-0=\tfrac{5}{16}$$

**(a) 최적 계수** (관측이 X → 분모 Var(X)):

$$a^*=\frac{\mathrm{Cov}[X,Y]}{\mathrm{Var}[X]}=\frac{5/16}{1/2}=\frac58,\qquad b^*=E[Y]-a^*E[X]=-\tfrac{1}{16}-\tfrac58\cdot0=-\tfrac{1}{16}$$

$$\hat Y_L(X)=\tfrac58\,X-\tfrac{1}{16}$$

**(b) 최소 MSE** (대상이 Y → Var(Y)에서 출발):

$$e_L^*=\mathrm{Var}[Y]-\frac{\mathrm{Cov}[X,Y]^2}{\mathrm{Var}[X]}=\frac{493}{768}-\frac{(5/16)^2}{1/2}=\frac{493}{768}-\frac{25}{128}=\frac{493}{768}-\frac{150}{768}=\boxed{\frac{343}{768}\approx0.447}$$

### 5. 검산·직관 (Sanity check)

- (1−ρ²) 형태 교차검증: ρ² = Cov²/(Var X·Var Y) = (25/256)/((1/2)(493/768)) = 150/493 → e*_L = (1−150/493)(493/768) = (343/493)(493/768) = 343/768 ✓
- e*_L = 343/768 ≈ 0.447 < Var[Y] = 493/768 ≈ 0.642: 관측 X가 Y 정보를 일부 줘서 불확실성이 줄었음, 방향 맞음 ✓
- 분모를 실수로 Var(Y)로 쓰면 a*가 틀림 — 여기선 관측이 X라 반드시 Var(X)=1/2 ✓

### 6. 한 줄 요약

> 선형추정 공식은 방향에 종속이다 — Y를 X로 추정하면 a*=Cov(X,Y)/Var(X)(분모=관측 X), e*_L은 Var(Y)(대상)에서 Cov²/Var(X)를 뺀다.
