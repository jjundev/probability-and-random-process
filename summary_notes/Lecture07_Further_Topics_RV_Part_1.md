# Lecture07 — Further Topics on Random Variables (Part 1)

> 출처: `notes/Lecture07_Further_Topics_RV_Part_1.pdf`, `STT/260518_Lecture07_Further_Topics_RV_Part_1_.txt`

핵심: Derived distribution ($Y=g(X)$, $Z=g(X,Y)$) · Convolution ($Z=X+Y$) · Covariance.

---

## 1. 핵심 정의

- **Derived distribution**: $X$의 분포를 알 때 $Y = g(X)$ 또는 $Z = g(X,Y)$의 분포를 구하는 문제. (Lecture07, p.5)
- **Covariance**: $\mathrm{cov}(X,Y) = \mathbb{E}\!\left[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\right]$. (Lecture07, p.23)
- **Uncorrelated**: $\mathrm{cov}(X,Y) = 0$인 두 RV $X, Y$의 관계. **독립과 다름** — 독립이면 uncorrelated지만 그 역은 거짓. (Lecture07, p.23; STT 260518, "uncorrelated 돼있다라고 정의해요")

---

## 2. 주요 공식 / 정리

### 2.1 Derived distribution — 핵심 원칙
**무조건 CDF부터 계산하고 미분한다.** (STT 260518, "첫 번째 뭐부터 계산한다? cdf부터 계산한다")

1. Step 1: $F_Y(y) = \mathbb{P}(Y \le y) = \mathbb{P}(g(X) \le y)$
2. Step 2: $f_Y(y) = \dfrac{dF_Y}{dy}(y)$. (Lecture07, p.10)

### 2.2 Discrete case
$$p_Y(y) = \sum_{x:\,g(x)=y} p_X(x), \quad \text{otherwise } p_Y(y)=0$$
(Lecture07, p.6)

### 2.3 Linear $Y = aX+b$, $a \ne 0$, $X$ continuous
$$f_Y(y) = \dfrac{1}{|a|}\,f_X\!\left(\dfrac{y-b}{a}\right), \quad \text{otherwise } f_Y(y) = 0$$
($a>0$이면 $F_Y(y)=F_X((y-b)/a)$, $a<0$이면 $F_Y(y)=1-F_X((y-b)/a)$를 미분; 절댓값으로 묶음.) (Lecture07, p.7)

- **Normal 선형보존**: $X \sim \mathcal{N}(\mu,\sigma^2)$이면 $Y = aX+b \sim \mathcal{N}(a\mu+b,\,a^2\sigma^2)$. (Lecture07, p.9)
- **Exponential 주의**: $b=0,\,a>0$이면 $Y \sim \mathrm{Exp}(\lambda/a)$지만, $b \ne 0$이면 일반적으로 exponential이 아님. (Lecture07, p.8)

### 2.4 일반 $Y = g(X)$ — CDF → 미분
- 예: $Y = X^2 \Rightarrow F_Y(y) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$, $f_Y(y) = \dfrac{1}{2\sqrt{y}}\bigl(f_X(\sqrt{y})+f_X(-\sqrt{y})\bigr)$ for $y\ge0$, otherwise $0$. (Lecture07, p.10)

### 2.5 $Z = g(X,Y)$ — 논리적 변환이 핵심
**$X,Y \sim \mathcal{U}[0,1]$, 독립, $Z = \max(X,Y)$**:
$$F_Z(z) = \mathbb{P}(\max(X,Y)\le z) = \mathbb{P}(X\le z, Y\le z) = z^2,\ \ 0\le z\le1$$
$$f_Z(z) = 2z\ \ (0\le z\le 1),\quad \text{otherwise }= 0$$
핵심 논리: "max이 $z$보다 작다" ⇔ "둘 다 $z$보다 작다". (Lecture07, p.11; STT 260518, "큰 놈이 G보다 작다는 건 작은 놈은 오죽하겠어")

**$\min$의 경우는 CCDF로**: $\mathbb{P}(\min(X,Y) > w) = \mathbb{P}(X>w, Y>w)$가 더 풀기 쉬움 (교집합이 합집합보다 쉽다). (STT 260518, "차라리 얘는 CCDF를 계산하는 게 편해요")

### 2.6 $Z = X+Y$, $X \perp Y$ — Convolution
- **Discrete**:
  $$p_Z(z) = \sum_x p_X(x)\,p_Y(z-x), \quad \text{otherwise }= 0$$
  (Lecture07, p.14)
- **Continuous**:
  $$f_Z(z) = \int_{-\infty}^{\infty} f_X(x)\,f_Y(z-x)\,dx, \quad \text{otherwise }= 0$$
  (Lecture07, p.16)
- 해석: $f_Y$를 좌우 뒤집고 $z$만큼 오른쪽으로 shift한 뒤 $f_X$와 곱해서 적분. (Lecture07, p.15)

### 2.7 Normal + Normal = Normal (독립 전제)
$X \sim \mathcal{N}(\mu_x,\sigma_x^2)$, $Y \sim \mathcal{N}(\mu_y,\sigma_y^2)$, $X \perp Y$이면
$$X+Y \sim \mathcal{N}(\mu_x+\mu_y,\ \sigma_x^2+\sigma_y^2)$$
유한개 독립 정규합도 정규. 잡음 모델링의 근거. (Lecture07, p.18; STT 260518, "노이즈가 더해지는데… 새로 해볼 필요가 있다")

### 2.8 Covariance — 정의식의 동치 표현 및 성질
- **계산식**: $\mathrm{cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$. (Lecture07, p.23)
- **독립 ⇒ uncorrelated**: $X \perp Y \Rightarrow \mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y] \Rightarrow \mathrm{cov}=0$. 역은 거짓. (Lecture07, p.23)
- **주요 항등식** (Lecture07, p.25):
  - $\mathrm{cov}(X,X) = \mathrm{var}(X)$
  - $\mathrm{cov}(aX+b,\,Y) = a\cdot\mathrm{cov}(X,Y)$
  - $\mathrm{cov}(X,\,Y+Z) = \mathrm{cov}(X,Y) + \mathrm{cov}(X,Z)$
  - $\mathrm{var}(X+Y) = \mathrm{var}(X) + \mathrm{var}(Y) + 2\mathrm{cov}(X,Y)$
  - $\mathrm{var}\!\left(\sum_i X_i\right) = \sum_i \mathrm{var}(X_i) + \sum_{i\ne j}\mathrm{cov}(X_i,X_j)$

### 2.9 좋은 Dependence Metric의 3요건 (Lecture07, p.21)
- **R1**: 의존도가 클수록 값이 커지고, 독립이면 $0$.
- **R2**: 부호(+/−)로 방향성 표시.
- **R3**: 차원 없는(dimensionless) 유계량 (예: $[-1,1]$).

→ Covariance는 R1·R2를 만족하지만 R3(유계성)은 만족 못함 → Correlation coefficient로 정규화 필요 (다음 강).

---

## 3. 핵심 예시

**예시 1. $X,Y \sim \mathcal{U}[0,1]$ 독립, $Z = Y/X$의 PDF** (Lecture07, p.12)
- $Z = Y/X$는 원점-점 $(X,Y)$ 사이의 기울기. (STT 260518, "원점에서 그 점을 잇는 직선의 기울기")
- 두 케이스로 분리:
  $$F_Z(z) = \begin{cases} z/2, & 0\le z\le 1 \\ 1 - 1/(2z), & z>1 \\ 0, & \text{otherwise}\end{cases}$$
  $$f_Z(z) = \begin{cases} 1/2, & 0\le z\le 1 \\ 1/(2z^2), & z>1 \\ 0, & \text{otherwise}\end{cases}$$

**예시 2. Uncorrelated이지만 독립이 아닌 사례** (Lecture07, p.24)
- 4점 joint PMF: $p_{X,Y}(1,0)=p_{X,Y}(0,1)=p_{X,Y}(-1,0)=p_{X,Y}(0,-1)=1/4$, otherwise $0$.
- $\mathbb{E}[X]=\mathbb{E}[Y]=0$, $\mathbb{E}[XY]=0$ ($XY \ne 0$인 점이 없음) ⇒ $\mathrm{cov}(X,Y)=0$ (uncorrelated).
- 그러나 $X=1$이면 반드시 $Y=0$이어야 하므로 종속. 검증: $p_{X,Y}(1,0)=1/4 \ne p_X(1)p_Y(0)=(1/4)(1/2)=1/8$. (STT 260518, "통계적으로 독립이 전혀 아니다")

**예시 3 (응용). Hat problem 재방문 — $\mathrm{var}[X]$** (Lecture07, p.26)
- $n$명이 모자를 던지고 무작위로 하나씩 회수, $X$ = 자기 모자 회수자 수.
- $X_i = \mathbb{1}\{i\text{가 자기 모자 회수}\} \sim \mathrm{Bern}(1/n)$, $X = \sum X_i$. $X_i$들은 **종속**.
- $\mathrm{var}(X_i) = \tfrac{1}{n}(1-\tfrac{1}{n})$.
- $i\ne j$: $\mathrm{cov}(X_i,X_j) = \mathbb{P}(X_i=1,X_j=1) - \tfrac{1}{n^2} = \tfrac{1}{n}\cdot\tfrac{1}{n-1} - \tfrac{1}{n^2} = \tfrac{1}{n^2(n-1)}$.
- $\mathrm{var}(X) = n\cdot\tfrac{1}{n}(1-\tfrac{1}{n}) + n(n-1)\cdot\tfrac{1}{n^2(n-1)} = 1$.

---

## 4. 자주 헷갈리는 포인트

- **CDF가 우선** — PDF 적분이 어려워 보여도 항상 CDF부터 풀고 미분. $\min$은 CCDF(여확률)가 더 편함.
- **독립 ↔ Uncorrelated 비대칭**: 독립 ⇒ uncorrelated, 그러나 uncorrelated ⇒ 독립은 거짓. (STT 260518, "내가 이생 살면서 statistically independence보다 더 관련 없는 거는 본 적이 없다")
- **Convolution은 독립 전제**: $f_Z = f_X * f_Y$는 $X \perp Y$일 때만 성립.
- **$\mathrm{cov}(aX+b,Y) = a\cdot\mathrm{cov}(X,Y)$**: 상수 $b$는 무관, $a$는 한 번만 곱해짐 (분산처럼 $a^2$ 아님).
- **Linear preservation은 normal에만 자동 적용**: 지수의 경우 $b\ne0$이면 exponential 보존 안 됨.

---

## 5. 시험 / 응용 관점

- 통신·신호처리: 잡음 $Y$가 신호 $X$에 더해질 때 $Z=X+Y$의 분포 → convolution. 잡음이 Gaussian이면 합도 Gaussian.
- ML/통계: Covariance는 PCA·MVUE 등 모든 2차 통계량의 출발점. 단, 비선형 종속성은 못 잡음(예시 2 참고).
- 시험 출제 단골: $\max/\min$의 PDF 유도, $Z = X+Y$ uniform convolution(삼각형), Hat problem의 $\mathrm{var}$ 유도, "uncorrelated인데 독립 아닌 예" 제시. (STT 260518, "이런 게 이제 시험 문제 내기 딱 좋은")
