# Lecture05 — Continuous RV Part 1

> 출처: `notes/Lecture05_Continuous_RV_Part_1.pdf`, `STT/260413_Lecture05_Continuous_RV_Part_1.txt`

핵심: PDF · CDF · Exponential RV · Geometric↔Exponential 극한 관계.

---

## 1. 핵심 정의

- **연속 RV**: 비음 함수 $f_X$(PDF)가 존재해 모든 부분집합 $B \subseteq \mathbb{R}$에 대해
  $$\mathbb{P}(X \in B) = \int_B f_X(x)\,dx$$
  를 만족하면 $X$는 연속 RV. (Lecture05, p.5)
- **PMF vs PDF 차이**: PMF $p_X(x)$ 자체가 확률이라 $\le 1$이지만, **PDF $f_X(x)$는 밀도라서 1보다 커질 수 있다** — 적분(넓이)이 1이면 충분. (STT 260413, "density가 1보다 커질 수는 있어요")
- **CDF (Cumulative Distribution Function)**: 모든 RV(이산/연속) 공통.
  $$F_X(x) = \mathbb{P}(X \le x) = \begin{cases} \sum_{k \le x} p_X(k), & \text{discrete} \\ \int_{-\infty}^{x} f_X(t)\,dt, & \text{continuous} \end{cases}$$
  (Lecture05, p.9)
- **CCDF (Complementary CDF)**: $\mathbb{P}(X > x) = 1 - F_X(x)$. (Lecture05, p.9)
- **Exponential RV** (parameter $\lambda > 0$):
  $$f_X(x) = \begin{cases} \lambda e^{-\lambda x}, & x \ge 0 \\ 0, & \text{otherwise } (x < 0) \end{cases}$$
  (Lecture05, p.13)

---

## 2. 주요 공식 / 정리

### PDF 성질 (Lecture05, p.5–6)
- $f_X(x) \ge 0$, $\displaystyle \int_{-\infty}^{\infty} f_X(x)\,dx = 1$.
- $\mathbb{P}(a \le X \le b) = \displaystyle \int_a^b f_X(x)\,dx$.
- 작은 $\delta$에서 $\mathbb{P}(a \le X \le a+\delta) \approx f_X(a)\cdot\delta$.
- $\mathbb{P}(X = a) = 0$.

### 함수의 기댓값 (expected value rule) (Lecture05, p.7; STT 260413)
이산 $\mathbb{E}[g(X)] = \sum_x g(x)\,p_X(x)$의 연속 버전 — **합 → 적분, PMF → PDF**로 바꾸면 끝. (STT 260413, "서메이션 인테그레이션으로 바꾸고 PMF를 PDF로 바꾼 다음에 … DX하면 된다")
$$\mathbb{E}[g(X)] = \int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx$$
- 모멘트는 특수 케이스: $g(x)=x \Rightarrow \mathbb{E}[X]$, $g(x)=x^2 \Rightarrow \mathbb{E}[X^2]$ — 둘 다 $\int x^n f_X(x)\,dx$. (Lecture05, p.7)
- $\mathrm{var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$. (STT 260413, "제곱의 평균 빼기 평균의 제곱")

### 균등분포 $U(a,b)$ — 기대값/분산 (Lecture05, p.7)
PDF: $f_X(x) = \dfrac{1}{b-a}$ for $a \le x \le b$, otherwise $= 0$.
- $\mathbb{E}[X] = \dfrac{b+a}{2}$
- $\mathbb{E}[X^2] = \dfrac{a^2+ab+b^2}{3}$
- $\mathrm{var}[X] = \dfrac{a^2+ab+b^2}{3} - \dfrac{a^2+2ab+b^2}{4}$

### CDF 성질 (Lecture05, p.10)
- 비감소(non-decreasing). 단조증가(increasing)는 아님 — 확률이 0인 영역에서는 일정. (STT 260413, "디크리징 하지는 않는다")
- $F_X(-\infty)=0$, $F_X(\infty)=1$.
- 이산: piecewise 상수, $p_X(k) = F_X(k) - F_X(k-1)$.
- 연속: 연속함수, $f_X(x) = \dfrac{dF_X}{dx}(x)$.

### Exponential RV 공식 (Lecture05, p.13–14)
- CDF: $F_X(x) = 1 - e^{-\lambda x}$ for $x \ge 0$, otherwise $= 0$.
- CCDF: $\mathbb{P}(X > x) = e^{-\lambda x}$ for $x \ge 0$.
- $\mathbb{E}[X] = \dfrac{1}{\lambda}$, $\mathbb{E}[X^2] = \dfrac{2}{\lambda^2}$, $\mathrm{var}[X] = \dfrac{1}{\lambda^2}$.
- 유도는 **부분적분** $\int u\,dv = uv - \int v\,du$ — 다항함수를 $G$, $\lambda e^{-\lambda x}$를 $F'$로 놓는다. (STT 260413, "이거는 인간적으로 손으로 합시다")

### Geometric ↔ Exponential 극한 관계 (Lecture05, p.18–19)
슬롯 길이 $\delta$, 슬롯당 성공확률 $p_\delta = 1 - e^{-\lambda\delta}$로 잡으면:
$$\mathbb{P}(X_\delta^{\text{geo}} \le n) = 1 - (1-p_\delta)^n = 1 - e^{-\lambda\delta n} \xrightarrow{\delta \to 0} \mathbb{P}(X^{\text{exp}} \le x), \quad x = n\delta$$
즉 슬롯 폭을 0으로 줄이는 극한에서 Geometric → Exponential.

---

## 3. 핵심 예시

### 예시 ① — Max of RVs (Lecture05, p.11)
시험을 3번 봐서 최종 점수 $X = \max\{X_1, X_2, X_3\}$, $X_i \in \{1,\dots,10\}$ 균등. PMF $p_X(x)$?
- **어프로치 1 (원소나열)**: $10^3 = 1000$ 케이스 전수조사 — 비효율. (STT 260413, "이거 미친 짓이야")
- **어프로치 2 (CDF 활용)**: 독립이면
$$F_X(x) = \mathbb{P}(X_1 \le x)\mathbb{P}(X_2 \le x)\mathbb{P}(X_3 \le x) = \left(\dfrac{x}{10}\right)^3$$
$$p_X(x) = F_X(x) - F_X(x-1) = \left(\dfrac{x}{10}\right)^3 - \left(\dfrac{x-1}{10}\right)^3, \quad x = 1,\dots,10$$
otherwise $= 0$. 정답이 즉시 나옴.

### 예시 ② — Meteorite Landing (Lecture05, p.16)
지름시간 평균 10일($\mathbb{E}[X] = 10 \Rightarrow \lambda = 1/10$)인 exponential. 자정~다음날 6am–6pm(1/4일~3/4일) 사이에 떨어질 확률은?
$$\mathbb{P}(1/4 \le X \le 3/4) = \mathbb{P}(X \ge 1/4) - \mathbb{P}(X \ge 3/4) = e^{-1/40} - e^{-3/40} \approx 0.0476$$
→ CCDF로 빠르게 계산. (STT 260413 강조: CCDF 활용)

---

## 4. 자주 헷갈리는 포인트

- **$P(X = a) = 0$ (연속)** 이지만 PDF $f_X(a)$는 0이 아닐 수 있다. PDF는 확률이 아니라 밀도.
- CDF는 **항상 well-defined** — 이산이든 연속이든 $\{X \le x\}$ 이벤트의 확률은 늘 계산 가능. (STT 260413, "리얼넘버라는 거는 크기가 존재")
- Exponential의 적분 구간은 $[0, \infty)$ — $x<0$ 영역은 PDF가 0이므로 제외. (otherwise $= 0$)

---

## 5. 시험 / 응용 관점

- **CDF 베이스 도구**: Max/Min RV처럼 직접 PMF 계산이 폭발적일 때, CDF $\to$ PDF/PMF 우회 경로가 핵심 기법. 통신 스케줄링 등 응용. (STT 260413, "CDF Based Scheduling")
- **Exponential = 연속 waiting time 모델**: 메시지 도착, 장비 고장, 전구 수명 등 "다음 사건까지 시간"의 표준 모델. 이산 대응은 Geometric. (Lecture05, p.15)
- 시험 범위 힌트: STT에서 "아마 Gaussian까지는 진도 나가지 않을까" 발언 — Part 1은 PDF·CDF·Exponential까지가 기본 단위. (STT 260413, "exponential까지만 나갈 줄 알았는데")
