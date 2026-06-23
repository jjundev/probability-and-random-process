# PSP 12.2.4 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 기말고사 대비/L12_LLMS_5문제_시험지/문제_L12_LLMS_5문제.pdf (4/5), 1순위 근거 시험지 표지 공식 요약(Lecture 12 LLMS), 풀이일 2026-06-16

## 문제 원문

The random variables X and Y have the joint probability density function

```
f_{X,Y}(x,y) = 2(y+x),  0 ≤ x ≤ y ≤ 1
             = 0,        otherwise
```

What is X̂_L(Y), the linear minimum mean square error estimate of X given Y?

---

### 1. 문제 정리 (Setup)

주어진 것:

$$f_{X,Y}(x,y)=\begin{cases}2(y+x) & 0\le x\le y\le 1\\[2pt]0 & \text{otherwise}\end{cases}$$

- 적분영역: 삼각형 0 ≤ x ≤ y ≤ 1 (대각선 아래, x ≤ y)
- 추정: X̂_L(Y) = aY + b — 관측 = Y, 대상 = X (12.2.1과 같은 방향)
- 필요한 재료: E[X], E[Y], Var[Y], Cov[X,Y] → a*, b*

### 2. 무엇을 묻고 왜 이 도구인가

연속 결합 PDF지만 묻는 건 결국 선형추정 = 1·2차 모멘트만 있으면 끝. 분포 전체를 변환할 필요 없이, 주변밀도와 적분으로 E·Var·Cov 네 수만 뽑아 공식에 넣는다. 핵심 노동은 삼각영역(x ≤ y)에서의 적분 한계 설정. (시험지 표지: "분포 전체 불필요 — 평균·분산·공분산만 알면 설계 가능", "a*=Cov/Var Y, b*=E[X]−a*E[Y]")

### 3. 핵심 통찰 (Aha)

> 연속이든 이산이든 선형추정은 모멘트 게임 — 삼각영역에서 f_Y(y)=∫₀^y f dx 와 적분만 정확히 하면, 나머지는 12.2.1과 똑같이 a*=Cov/Var Y로 떨어진다.

### 4. 풀이 (Worked solution)

**주변밀도** (적분 한계가 핵심 — x는 0~y, y는 x~1):

$$f_Y(y)=\int_0^y 2(x+y)\,dx=\big[x^2+2xy\big]_0^{y}=3y^2\quad(0\le y\le1),\ \text{otherwise}=0$$

$$f_X(x)=\int_x^1 2(x+y)\,dy=1+2x-3x^2\quad(0\le x\le1),\ \text{otherwise}=0$$

(검산: ∫₀¹ 3y² dy = 1 ✓, ∫₀¹(1+2x−3x²)dx = 1 ✓)

**Y의 모멘트** (f_Y = 3y²):

$$E[Y]=\int_0^1 3y^3\,dy=\tfrac34,\quad E[Y^2]=\int_0^1 3y^4\,dy=\tfrac35,\quad \mathrm{Var}[Y]=\tfrac35-\tfrac{9}{16}=\tfrac{3}{80}$$

**X의 평균** (f_X = 1+2x−3x²):

$$E[X]=\int_0^1 x(1+2x-3x^2)\,dx=\tfrac12+\tfrac23-\tfrac34=\tfrac{5}{12}$$

**공분산** — E[XY]를 삼각영역에서 직접:

$$E[XY]=\int_0^1\!\!\int_0^y 2xy(x+y)\,dx\,dy=\int_0^1 \tfrac53 y^4\,dy=\tfrac13$$

$$\mathrm{Cov}[X,Y]=E[XY]-E[X]E[Y]=\tfrac13-\tfrac{5}{12}\cdot\tfrac34=\tfrac{16}{48}-\tfrac{15}{48}=\tfrac{1}{48}$$

**최적 계수** (관측이 Y → 분모 Var(Y)):

$$a^*=\frac{\mathrm{Cov}[X,Y]}{\mathrm{Var}[Y]}=\frac{1/48}{3/80}=\frac{80}{144}=\frac59$$

$$b^*=E[X]-a^*E[Y]=\tfrac{5}{12}-\tfrac59\cdot\tfrac34=\tfrac{5}{12}-\tfrac{5}{12}=0$$

$$\boxed{\hat X_L(Y)=\tfrac59\,Y}$$

### 5. 검산·직관 (Sanity check)

- b*=0이 자연스러운가: a*E[Y] = (5/9)(3/4) = 5/12 = E[X] 라 정확히 상쇄 ✓
- (덤) 최소 MSE: e*_L = Var[X] − Cov²/Var[Y] = 43/720 − (1/48)²/(3/80) = 13/270 ≈ 0.048, 그리고 Var[X]=43/720≈0.0597보다 작음 — Y 관측이 정보를 줬음 ✓
- 단조성 직관: x ≤ y라 Y가 크면 X도 클 여지가 큼 → a*>0 (양의 상관) ✓. ρ² = 25/129 ≈ 0.19로 약한 양의 상관.

### 6. 한 줄 요약

> 연속 결합 PDF의 선형추정도 결국 모멘트 게임 — 삼각영역(x≤y) 적분으로 E·Var·Cov만 뽑으면 X̂_L(Y)=a*Y+b*=(5/9)Y로 이산 문제와 동일하게 떨어진다.
