# Lecture06 — Continuous RV Part 2

> 출처: `notes/Lecture06_Continuous_RV_Part_2.pdf`, `STT/260415_Lecture06_Continuous_RV_Part_2.txt`, `STT/260429_Lecture06_Continuous_RV_Part_2.txt`, `STT/260504_Lecture06_Continuous_RV_Part_2.txt`, `STT/260506_Lecture06_Continuous_RV_Part_2.txt`

핵심: Gaussian RV · Joint/Conditional/Independence · Memoryless · Total Prob./Exp. · Bayes rule.

---

## 1. 핵심 정의

- **표준정규** $\mathcal{N}(0,1)$: $f_X(x) = \dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$, $\mathbb{E}[X]=0$, $\mathrm{var}[X]=1$. (Lecture06, p.5)
- **일반정규** $\mathcal{N}(\mu,\sigma^2)$: $f_X(x) = \dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$, $\mathbb{E}[X]=\mu$, $\mathrm{var}[X]=\sigma^2$. 정의역 전체 $\mathbb{R}$(otherwise는 없음 — 전 실수에서 $>0$). (Lecture06, p.5)
- **결합 PDF (Jointly Continuous)**: 비음 함수 $f_{X,Y}(x,y) \ge 0$이 존재해 모든 $B \subseteq \mathbb{R}^2$에 대해
  $$\mathbb{P}((X,Y)\in B) = \iint_{(x,y)\in B} f_{X,Y}(x,y)\,dx\,dy$$
  (Lecture06, p.11)
- **조건부 PDF — 사건 $A$에 조건화**: $f_{X|A}(x)\cdot\delta \approx \mathbb{P}(x \le X \le x+\delta \mid A)$, $\int f_{X|A}(x)\,dx = 1$. (Lecture06, p.13)
- **조건부 PDF — RV $Y$에 조건화**: $f_{X|Y}(x|y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$ (단 $f_Y(y)>0$). (Lecture06, p.18)
- **독립**: $X \perp Y \iff f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for all $x,y$. (Lecture06, p.18)
- **Memoryless**: 임의 $n,m \ge 0$에 대해 $\mathbb{P}(X > n+m \mid X > m) = \mathbb{P}(X > n)$. (Lecture06, p.15)

---

## 2. 주요 공식 / 정리

### Gaussian 핵심 성질
- **선형변환 보존** (Lecture06, p.7): $X \sim \mathcal{N}(\mu,\sigma^2)$, $a\neq 0$이면 $aX+b \sim \mathcal{N}(a\mu+b,\ a^2\sigma^2)$.
- **표준화**: $Y = \dfrac{X-\mu}{\sigma} \sim \mathcal{N}(0,1)$, 표준정규 CDF $\Phi(y) = \dfrac{1}{\sqrt{2\pi}}\int_{-\infty}^{y} e^{-t^2/2}\,dt$를 표로 사용.
- **분산 유도**: $y=(x-\mu)/\sigma$로 치환 후 부분적분 ($u=y$, $dv=ye^{-y^2/2}\,dy$). $\mathrm{var}(X) = \sigma^2$. (Lecture06, p.6)
- **왜 중요한가**: 중심극한정리(CLT) — 어떤 RV들의 합도 정규에 수렴. 통신·ML에서 잡음/파라미터 모델의 표준. (Lecture06, p.9)

### Joint / Marginal / Multiplication
- 주변 PDF: $f_X(x) = \int f_{X,Y}(x,y)\,dy$, $f_Y(y) = \int f_{X,Y}(x,y)\,dx$. (Lecture06, p.11)
- 결합 CDF: $F_{X,Y}(x,y) = \mathbb{P}(X\le x, Y\le y)$, $f_{X,Y}(x,y) = \dfrac{\partial^2 F_{X,Y}}{\partial x\,\partial y}$. (Lecture06, p.12)
- 함수의 기댓값: $\mathbb{E}[g(X,Y)] = \iint g(x,y) f_{X,Y}(x,y)\,dx\,dy$. (Lecture06, p.12)
- 곱셈 규칙: $f_{X,Y}(x,y) = f_Y(y)\,f_{X|Y}(x|y) = f_X(x)\,f_{Y|X}(y|x)$. (Lecture06, p.18)
- 사건 $\{X\in C\}$에 조건화: $f_{X|\{X\in C\}}(x) = \dfrac{f_X(x)}{\mathbb{P}(X\in C)}$ for $x\in C$, otherwise $= 0$. (Lecture06, p.13)

### Memoryless — 지수 RV 전유 (Lecture06, p.15)
증명: $\mathbb{P}(X>x)=e^{-\lambda x}$이므로
$$\mathbb{P}(X>n+m\mid X>m) = \dfrac{e^{-\lambda(n+m)}}{e^{-\lambda m}} = e^{-\lambda n} = \mathbb{P}(X>n)$$
지수법칙 $e^a e^b = e^{a+b}$로 약분되는 게 핵심.

### Total Probability / Expectation (연속) (Lecture06, p.16, p.18)
분할 $A_1,\dots,A_n$ 또는 RV $Y$에 대해:
- $f_X(x) = \sum_i \mathbb{P}(A_i) f_{X|A_i}(x) = \int f_Y(y) f_{X|Y}(x|y)\,dy$
- $\mathbb{E}[X] = \sum_i \mathbb{P}(A_i)\mathbb{E}[X|A_i] = \int f_Y(y)\mathbb{E}[X|Y=y]\,dy$
- $\mathbb{E}[X|Y=y] = \int x f_{X|Y}(x|y)\,dx$

### Bayes 정리 (Lecture06, p.22, p.25)
- **연속**: $f_{X|Y}(x|y) = \dfrac{f_X(x) f_{Y|X}(y|x)}{f_Y(y)}$, $f_Y(y) = \int f_X(x') f_{Y|X}(y|x')\,dx'$.
- **혼합** ($K$ 이산, $Y$ 연속): $p_{K|Y}(k|y) = \dfrac{p_K(k) f_{Y|K}(y|k)}{f_Y(y)}$, $f_Y(y) = \sum_{k'} p_K(k') f_{Y|K}(y|k')$.
- 의미: 사전 $\mathbb{P}(X)$ + 우도 $\mathbb{P}(Y|X)$ → 사후 $\mathbb{P}(X|Y)$. **매개변수 학습**의 기본 구조. (Lecture06, p.24)

---

## 3. 핵심 예시

### 예시 ① — Snowfall (Lecture06, p.8)
$X \sim \mathcal{N}(60, 20^2)$. $\mathbb{P}(X \ge 80)$?
$$Y = \dfrac{X-60}{20} \sim \mathcal{N}(0,1), \quad \mathbb{P}(X\ge 80) = \mathbb{P}(Y\ge 1) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587$$

### 예시 ② — 막대 두 번 부러뜨리기 (Lecture06, p.19–20)
길이 $l$ 막대, $Y \sim U[0,l]$, $X \mid \{Y=y\} \sim U[0,y]$.

**(a) Joint PDF** — 곱셈 규칙:
$$f_{X,Y}(x,y) = \begin{cases} \dfrac{1}{l y}, & 0 \le x \le y \le l \\ 0, & \text{otherwise} \end{cases}$$

**(b) Marginal**: $f_X(x) = \int_x^l \dfrac{1}{ly}\,dy = \dfrac{1}{l}\ln\dfrac{l}{x}$ for $0 \le x \le l$, otherwise $= 0$.

**(c)~(e) $\mathbb{E}[X]$를 세 가지 길로**:
- 직접: $\int_0^l x\cdot\dfrac{1}{l}\ln(l/x)\,dx = l/4$.
- 독립 활용 ($Y \perp X/Y$, $X/Y \sim U[0,1]$): $\mathbb{E}[Y]\mathbb{E}[X/Y] = (l/2)(1/2) = l/4$.
- 전체 기댓값 정리 (TET): $\int_0^l \dfrac{1}{l}\cdot\dfrac{y}{2}\,dy = l/4$.

메시지: "정답에 이르는 길은 여럿 — **최적 경로 선택이 핵심**." (Lecture06, p.20)

### 예시 ③ — Signal Detection (Lecture06, p.27–28)
$K \in \{-1,+1\}$ 등확률, $Y = K + W$, $W \sim \mathcal{N}(0,1)$, $K \perp W$.
- $f_{Y|K}(y|k) = \dfrac{1}{\sqrt{2\pi}}e^{-(y-k)^2/2}$ for $k=\pm 1$, otherwise(다른 $k$) 무관.
- Bayes 정리로:
$$p_{K|Y}(1|y) = \dfrac{1}{1+e^{-2y}}$$
- 판별: $y>0 \Rightarrow K=1$ 추정 ($y<0$이면 $K=-1$).
- 이 결과는 **시그모이드 함수** — ML 이진 분류의 원형.

---

## 4. 자주 헷갈리는 포인트

- 조건부 PDF 분모 $f_Y(y) > 0$ 필수 — 0이면 정의 안 됨.
- 혼합 케이스에서 $p_{K|Y}(k|y)$를 직접 $\mathbb{P}(K=k, Y=y)/\mathbb{P}(Y=y)$로 쓰면 $0/0$. 극한 $\delta\to 0$로 유도하면 $\dfrac{\mathbb{P}(A) f_{Y|A}(y)}{f_Y(y)}$ 형태가 얻어짐. (Lecture06, p.25–26)
- PDF/PMF는 늘 정의역 밖 $\text{otherwise} = 0$ — Gaussian만 예외(전 실수에서 양).

---

## 5. 시험 / 응용 관점

- **Gaussian**: 선형변환 보존 + 표준화 + CLT 세 가지가 통신·ML의 토대. 표준화 후 $\Phi$ 표 한 장으로 모든 확률 계산.
- **베이즈 = 역추론·매개변수 학습**: 분모는 항상 전체 확률 정리로 계산. 전구 수명/Romeo-Juliet 예제(Lecture06, p.23–24)는 같은 구조.
- **신호 탐지 = MAP 추정 + 시그모이드**: 통신/ML의 이진 분류와 직결.
- Review Questions (Lecture06, p.29): continuous의 의미, PDF/CDF 차이, joint/marginal/conditional, Geometric↔Exponential, 정규의 선형보존, Bayes 매개변수 학습, 혼합 Bayes — 시험 대비 7대 점검.
