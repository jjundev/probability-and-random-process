# Lecture 09 — 랜덤변수의 점근적 거동 (Asymptotic Behaviors)

> 출처: notes/Lecture09_Asymptotic_Behavior_RVs.pdf, STT/260601_Lecture09_Asymptotic_Behavior_RVs.txt

확률론에서 가장 중요한 두 발견: **큰 수의 법칙(LLN)** 과 **중심극한정리(CLT)**. 둘 다 i.i.d. 랜덤변수의 합 $S_n$ 을 어떤 스케일로 나누느냐의 문제다. (Lecture09, slide 2; STT 260601, "굉장히 중요한 발견 두 가지")

## 1. 핵심 정의
- **관심 대상**: $X_1,\dots,X_n$ 이 i.i.d.이고 $\mathbb{E}[X_i]=\mu$, $\mathrm{var}[X_i]=\sigma^2$ 일 때, 합 $S_n = X_1+X_2+\cdots+X_n$ 의 거동. (Lecture09, slide 4)
- **표본평균 (Sample Mean)**: $M_n = \dfrac{S_n}{n} = \dfrac{X_1+\cdots+X_n}{n}$. 이것도 랜덤변수다. (Lecture09, slide 6; STT 260601, "샘플 민도 랜덤 베리어블")
- **확률 수렴 (convergence in probability)**: 랜덤변수가 확률 1로 어떤 상수에 수렴. WLLN에서 사용. (Lecture09, slide 7)
- **분포 수렴 (convergence in distribution)**: 랜덤변수의 분포가 어떤 분포로 수렴. CLT에서 사용. (Lecture09, slide 9)

## 2. 주요 공식 / 정리
- 합의 평균·분산: $\mathbb{E}[S_n] = n\mu$, $\ \mathrm{var}[S_n] = n\sigma^2$ (i.i.d.이므로 분산은 단순 합). (STT 260601, "sigma 제곱을 n으로 곱한 것이 variance Sn")
- 표본평균의 평균·분산: $\mathbb{E}[M_n] = \mu$, $\ \mathrm{var}[M_n] = \dfrac{\sigma^2}{n}$. (Lecture09, slide 6)
  - 유도: 기댓값은 선형 → $\frac{1}{n}\sum \mathbb{E}[X_i] = \frac{1}{n}\cdot n\mu = \mu$. 분산은 $\frac{1}{n^2}$ 이 제곱으로 나오고 i.i.d. 합이라 $\frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$. (STT 260601, "n분의 1 밖으로 나가면서 제곱해서")
- **약한 큰 수의 법칙 (WLLN)**: $n\to\infty$ 이면 $\mathrm{var}[M_n]\to 0$ 이므로 $M_n$ 은 랜덤성을 잃고 $\mu$ 주변에 집중. 즉
  $$M_n \xrightarrow{\text{in prob.}} \mu$$
  $S_n$ 을 $1/n$ 로 스케일하면 **결정론적(deterministic)** 세계로 간다. (Lecture09, slide 7, slide 10; STT 260601, "확률적으로 수렴")
- **중심극한정리 (CLT)**: $Z_n = \dfrac{S_n - n\mu}{\sigma\sqrt{n}}$ 로 표준화하면
  $$Z_n \xrightarrow{\text{in dist.}} Z, \quad Z \sim \mathcal{N}(0,1)$$
  $X_i$ 의 분포가 **무엇이든 상관없이** $Z$ 는 정규분포가 된다. (Lecture09, slide 9; STT 260601, "X1하고 X2가 유니폼이든 익스포네셜이든 상관없이")
- **표준화 일반식**: 평균 $\mu$, 분산 $\sigma^2$ 인 랜덤변수를 $Y=\dfrac{X-\mu}{\sigma}$ 로 바꾸면 평균 0·분산 1. CLT의 $Z_n$ 은 $S_n$(평균 $n\mu$, 분산 $n\sigma^2$)에 이 식을 적용한 것. (STT 260601, "X에서 자기 자신의 평균을 빼고 스탠다드 디비에이션으로 나눠")

## 3. 핵심 예시 (1~2개)
- **출석 학생 수 (이항분포)**: $n$ 명의 학생이 각자 happy(1, 확률 $p$)/sad(0)로 i.i.d. 결정되고 happy인 학생만 출석. 출석 수 $K$ 는 이항 랜덤변수.
  $$P(K=k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k=0,1,\dots,n; \quad \text{otherwise } = 0$$
  모두 출석 확률 $p^n$, 아무도 안 옴 $(1-p)^n$. → $n\to\infty$ 일 때의 거동이 이 강의의 관심. (Lecture09, slide 4; STT 260601, "바이노미얼 랜덤 베리어블")
- **CLT 수렴 그림**: $n=1$ 에서 값 8개짜리 균등 PMF를 $n$ 번 컨볼루션하면, $n=2$ 삼각 펄스 → $n=4$ → $n=32$ 에서 종(bell) 모양 정규분포에 근접. ($S_n$ 을 $\sqrt{n}$ 로 나눈 스케일). MATLAB 수치 실험. (Lecture09, slide 11; STT 260601, "N이 32개가 되면 진짜 가오션 비슷해져요")

## 4. 자주 헷갈리는 포인트
- **스케일링 안경의 차이** (단순화: $\mathbb{E}[X_i]=0$, $\mathrm{var}=1$): $S_n$ 을 $1/n$ 로 나누면 → 결정론적 세계(LLN); $1/\sqrt{n}$ 로 나누면 → 여전히 랜덤이지만 **정규분포** 세계(CLT). (Lecture09, slide 10; STT 260601, "n으로 나누면 디터미니스틱, 루트 n으로 나누면 가오샨")
- **WLLN은 "약한" 버전** = 확률 수렴. 더 강한 strong LLN이 존재하나 해석학이 많이 필요해 이 수업에서는 다루지 않음 (학부 수준에선 weak로 충분). (Lecture09, slide 7; STT 260601, "위클만 알아도 충분")
- CLT는 $X_i$ 의 PDF/PMF가 무엇이든 성립하는 것이 핵심 포인트. 가우시안이 아니어도 합을 표준화하면 가우시안. (Lecture09, slide 9)
- 합 $S_n$ 의 분포를 직접 구하려면 PMF/PDF를 $n$ 번 컨볼루션해야 해서 일반적으로 매우 어려움. 쉬운 예외는 "정규분포의 합 = 정규분포". 그래서 스케일링 접근을 택함. (Lecture09, slide 5; STT 260601, "컨볼루션을 N번 해야 되겠네")

## 5. 시험 / 응용 관점
- 다수의 i.i.d. 노이즈가 더해질 때 $(n \times \text{평균 노이즈})$ 로 근사 → 통신·신호처리의 노이즈 해석. (Lecture09, slide 7; STT 260601, "노이즈 소스들의 합")
- "중앙극한정리"는 통계의 중추 — 해석이 막히면 개수를 늘려 CLT로 분포를 가우시안으로 근사하는 방식이 실제 논문에서도 사용됨. (STT 260601, "센트럴 리밋 디어렘")
- 정보이론의 **typicality** 증명에 WLLN이 사용됨. (STT 260601, "typicality라는 것을 증명하는 데 쓰는 이론이 law of large numbers")

---
*비고: 강의 로드맵에는 (3) WLLN 증명(Markov·Chebyshev 부등식), (4) CLT 증명(MGF)도 있으나, 이번 학기에는 증명을 다루지 않고 결과·의미만 설명함 (STT 260601, "이번 학기에 증명까지는 안 해줄 거고").*
