# Lecture08 — Further Topics on Random Variables (Part 2)

> 출처: `notes/Lecture08_Further_Topics_RV_Part_2.pdf`
> 보조 STT: `STT/260513_Lecture08_Further_Topics_RV_Part_1.txt` (단, 이 녹취는 derived distribution 복습 위주이며 본 강의의 covariance·conditional expectation·LTV·random sum 내용은 STT에서 직접 확인되지 않음. PDF의 Definition/Theorem/Example 박스를 1차 신호로 사용.)

핵심: Correlation coefficient · Conditional expectation `E[X|Y]` · Conditional variance `var[X|Y]` · Law of total variance · Random number sum.

---

## 1. 핵심 정의

- **Correlation coefficient**: $\rho(X,Y) = \mathbb{E}\!\left[\dfrac{X-\mu_X}{\sigma_X}\cdot\dfrac{Y-\mu_Y}{\sigma_Y}\right] = \dfrac{\mathrm{cov}(X,Y)}{\sqrt{\mathrm{var}[X]\,\mathrm{var}[Y]}}$. 각 RV를 $\sigma$로 정규화한 covariance. (Lecture08, p.6)
- **Conditional expectation as RV**: $\mathbb{E}[X\mid Y]$는 RV $Y$의 함수로 정의되는 **랜덤 베리어블** $g(Y)$로서, $Y=y$일 때 값 $g(y) = \mathbb{E}[X\mid Y=y]$를 가짐. (Lecture08, p.16)
- **Conditional variance as RV**: $\mathrm{var}[X\mid Y]$는 RV $g(Y)$로서, $Y=y$일 때 값 $g(y) = \mathrm{var}[X\mid Y=y] = \mathbb{E}\!\left[(X-\mathbb{E}[X\mid Y=y])^2 \mid Y=y\right]$. (Lecture08, p.21)
- **Uncorrelated**: $\rho(X,Y) = 0$ ⇔ $\mathrm{cov}(X,Y) = 0$.

---

## 2. 주요 공식 / 정리

### 2.1 Correlation coefficient의 두 정리 (Lecture08, p.6)
1. **Bound**: $-1 \le \rho(X,Y) \le 1$.
2. **극단값의 의미**: $|\rho|=1 \iff X-\mu_X = c(Y-\mu_Y)$ for some $c$ ($c>0$일 때 $\rho=1$, $c<0$일 때 $\rho=-1$). 즉 **완전한 선형 관계**.

### 2.2 Cauchy–Schwarz 부등식 (CSI) (Lecture08, p.7)
$$\bigl(\mathbb{E}[XY]\bigr)^2 \le \mathbb{E}[X^2]\,\mathbb{E}[Y^2]$$
- **증명 아이디어**: 임의 상수 $a$에 대해 $0 \le \mathbb{E}\!\left[(X-aY)^2\right] = \mathbb{E}[X^2] - 2a\mathbb{E}[XY] + a^2\mathbb{E}[Y^2]$. $a = \mathbb{E}[XY]/\mathbb{E}[Y^2]$를 대입하면 우변이 $\mathbb{E}[X^2] - (\mathbb{E}[XY])^2/\mathbb{E}[Y^2] \ge 0$.
- **$\rho$ 유계 증명**: $\tilde X = X-\mathbb{E}[X]$, $\tilde Y = Y-\mathbb{E}[Y]$로 두면 $\rho^2 = (\mathbb{E}[\tilde X\tilde Y])^2/(\mathbb{E}[\tilde X^2]\mathbb{E}[\tilde Y^2]) \le 1$.

### 2.3 Law of iterated expectations (Lecture08, p.17)
$$\boxed{\mathbb{E}\!\left[\mathbb{E}[X\mid Y]\right] = \mathbb{E}[X]}$$
증명: $\mathbb{E}[\mathbb{E}[X\mid Y]] = \sum_y \mathbb{E}[X\mid Y=y]\,p_Y(y) = \mathbb{E}[X]$.
(연속의 경우 합 대신 $\int \cdots f_Y(y)\,dy$, 그 외 영역은 $f_Y(y)=0$이라 기여 없음.)

### 2.4 Law of total variance (LTV) (Lecture08, p.23)
$$\boxed{\mathrm{var}[X] = \mathbb{E}\!\left[\mathrm{var}(X\mid Y)\right] + \mathrm{var}\!\left[\mathbb{E}(X\mid Y)\right]}$$
- 증명 (Lecture08, p.23):
  - $\mathrm{var}(X\mid Y) = \mathbb{E}[X^2\mid Y] - (\mathbb{E}[X\mid Y])^2$.
  - 양변에 $\mathbb{E}[\cdot]$ 적용: $\mathbb{E}[\mathrm{var}(X\mid Y)] = \mathbb{E}[X^2] - \mathbb{E}[(\mathbb{E}[X\mid Y])^2]$. ... (1)
  - $\mathrm{var}[\mathbb{E}(X\mid Y)] = \mathbb{E}[(\mathbb{E}[X\mid Y])^2] - (\mathbb{E}[X])^2$. ... (2)
  - (1)+(2) $= \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \mathrm{var}[X]$.

### 2.5 Random number sum (Lecture08, p.27)
$Y = X_1 + X_2 + \cdots + X_N$이고:
- $N$: 랜덤 (방문 가게 수 등)
- $X_i$: i.i.d., 평균 $\mu$, 분산 $\mathrm{var}[X_i]$. $X_i \perp N$, $X_i \perp X_j$ ($i\ne j$).

그러면:
- $\mathbb{E}[Y] = \mathbb{E}[N]\cdot \mathbb{E}[X_i] = \mu\,\mathbb{E}[N]$.
- $\mathrm{var}[Y] = \mathbb{E}[N]\,\mathrm{var}[X_i] + \mu^2\,\mathrm{var}[N]$.

도출: $\mathbb{E}[Y\mid N] = N\mu$, $\mathrm{var}[Y\mid N] = N\,\mathrm{var}[X_i]$. LTV·iterated expectations 대입.

---

## 3. 핵심 예시

**예시 1. 막대 자르기 (Stick-breaking)** — 조건부 기댓값·분산의 의미 (Lecture08, p.18, p.25)

설정: 길이 $\ell$ 막대를 점 $Y \sim \mathcal{U}[0,\ell]$에서 자르고, 남은 조각 $[0,Y]$에서 다시 점 $X \sim \mathcal{U}[0,Y]$로 자름.
- 분포: $f_Y(y) = 1/\ell$ for $y\in[0,\ell]$, otherwise $= 0$. $f_{X\mid Y}(x\mid y) = 1/y$ for $x\in[0,y]$, otherwise $= 0$.
- $\mathbb{E}[X\mid Y=y] = y/2$ → $\mathbb{E}[X\mid Y] = Y/2$ (RV).
- $\mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X\mid Y]] = \mathbb{E}[Y/2] = \ell/4$.
- $\mathcal{U}[0,\theta]$의 분산 사실: $\theta^2/12$.
- $\mathrm{var}[X\mid Y] = Y^2/12$ → $\mathbb{E}[\mathrm{var}[X\mid Y]] = \tfrac{1}{12}\int_0^\ell \tfrac{1}{\ell}y^2\,dy = \ell^2/36$.
- $\mathrm{var}[\mathbb{E}[X\mid Y]] = \mathrm{var}[Y/2] = \tfrac{1}{4}\cdot\tfrac{\ell^2}{12} = \ell^2/48$.
- **LTV**: $\mathrm{var}[X] = \ell^2/36 + \ell^2/48 = 7\ell^2/144$.

**예시 2. 반별 평균 점수 (Averaging Quiz Scores by Section)** — iterated expectations & LTV의 직관 (Lecture08, p.19, p.24)

설정: $n$명 학생을 $k$개 반($A_1,\dots,A_k$)으로 분할, 반 $s$의 인원 $n_s$, 점수 $x_i$, 반 평균 $m_s = \tfrac{1}{n_s}\sum_{i\in A_s} x_i$, 전체 평균 $m = \tfrac{1}{n}\sum_i x_i$. $X$ = 무작위로 뽑은 학생의 점수, $Y$ = 그 학생의 반.
- **Iterated**: $m = \mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X\mid Y]] = \sum_{s=1}^k m_s\cdot\tfrac{n_s}{n}$ (가중평균).
- **LTV의 해석**:
  - $\mathbb{E}[\mathrm{var}(X\mid Y)] = \sum_s \tfrac{n_s}{n}\mathrm{var}(X\mid Y=s)$ → **반 내부 평균 변동성**.
  - $\mathrm{var}[\mathbb{E}(X\mid Y)]$ → **반들 사이의 평균 변동성**.
  - 합 = 전체 분산.

---

## 4. 자주 헷갈리는 포인트

- **$\mathbb{E}[X\mid Y]$는 RV, $\mathbb{E}[X\mid Y=y]$는 숫자(함수값)**: 표기 혼동 주의. $\mathbb{E}[X\mid Y]$는 분포·기댓값·분산을 모두 갖는 RV. (Lecture08, p.16)
- **`uncorrelated ≠ 독립`**: $\rho=0$이라도 비선형 종속 가능. $|\rho|=1$일 때만 "완전한 선형 종속". (Lecture08, p.6)
- **LTV의 두 성분 부호는 둘 다 ≥ 0**: 둘 다 분산 또는 분산의 기댓값이므로 비음. 한쪽이 크면 다른 쪽이 작아질 수 있으나 둘 다 0 이상.
- **Random sum의 분산 공식 두 항**: $\mathbb{E}[N]\mathrm{var}[X_i]$ (단일 점수의 변동성 × 평균 횟수) + $\mu^2\mathrm{var}[N]$ ($N$ 자체의 변동성). 두 번째 항을 빼먹지 말 것.

---

## 5. 시험 / 응용 관점

- **Correlation coefficient**: 통계학·머신러닝에서 두 변수 간 **선형** 의존성의 표준 지표. PCA·선형회귀의 기반.
- **Iterated expectations**: 단계적으로 정보가 들어올 때 예측값 갱신 (예: 1월 매출 $Y$를 본 후 2월 매출 $X$ 예측 → "Revised forecast" $\mathbb{E}[X\mid Y=y]$). 갱신된 예측의 평균은 원래 평균과 같음. (Lecture08, p.18)
- **LTV**: ANOVA(분산분석)의 수학적 기반 — 전체 분산을 "그룹 내 분산" + "그룹 간 분산"으로 분해.
- **Random sum**: 콜센터 통화 시간 합계, 매장 방문 횟수 × 평균 지출액 등 운영 리서치·보험 청구액 모델링에 직결.
