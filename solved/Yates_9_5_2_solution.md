# 9.5.2 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), Probability_and_Stochastic_Processes_Problems/problems_png/9.5.2.png, 1순위 근거 Lecture09 (CLT), 풀이일 2026-06-17

## 문제 원문

9.5.2 Internet packets can be classified as video (V) or as generic data (D). Based on a lot of observations taken by the Internet service provider, we have the following probability model: P[V] = 3/4, P[D] = 1/4. Data packets and video packets occur independently of one another. The random variable K_n is the number of video packets in a collection of n packets.

(a) What is E[K_100], the expected number of video packets in a set of 100 packets?
(b) What is σ_{K_100}?
(c) Use the central limit theorem to estimate P[K_100 ≥ 18].
(d) Use the central limit theorem to estimate P[16 ≤ K_100 ≤ 24].

## ⚠ 먼저: 교재 자체에 수치 모순

PNG(교재 원본)대로 P[V] = 3/4, K_n = 비디오 패킷 수면 E[K_100] = 75인데, (c)·(d)의 경계값 16·18·24는 평균에서 약 12~14σ 아래라 CLT 추정이 1과 0으로 붕괴(degenerate)한다. 그 경계값들은 명백히 평균 25(즉 p = 1/4인 쪽, 데이터 패킷 수)를 겨냥해 설계된 것 — 교재가 V와 D를 어딘가에서 뒤바꾼 오타로 보인다. 아래는 (1) 문장 그대로(p=3/4)의 충실한 답과 (2) 경계값이 가리키는 의도된 답(p=1/4)을 모두 제시한다.

---

### 1. 문제 정리 (Setup)

X_i = i번째 패킷이 비디오면 1, 아니면 0 (Bernoulli). K_n = X_1 + … + X_n. n = 100. 패킷들은 독립.

| 소문제 | 구할 것 | 문장대로(p=3/4) | 경계가 의도한(p=1/4) |
|---|---|---|---|
| (a) | E[K_100] | 75 | 25 |
| (b) | σ_{K_100} | 4.33 | 4.33 (동일) |
| (c) | CLT로 P[K_100 ≥ 18] | ≈ 1 | ≈ 0.947 |
| (d) | CLT로 P[16 ≤ K_100 ≤ 24] | ≈ 0 | ≈ 0.390 |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

K_100은 i.i.d. Bernoulli 100개의 합 = 이항(binomial) 랜덤변수다 — 강의의 "출석 학생 수" 예시와 정확히 같은 구조 (Lecture09, slide 4). 이항분포의 PMF를 직접 더해 꼬리확률을 구하는 건 번거롭고, 강의의 메시지는 "해석이 막히면 개수를 늘려 합을 가우시안으로 근사"다 (Lecture09, slide 9; STT 260601). 그래서 CLT로 정규근사한다. 이항이라 모수만 알면 평균·분산이 공식으로 바로 나온다.

### 3. 핵심 통찰 (Aha)

> 이항은 "Bernoulli의 합"이므로, 평균 nμ와 표준편차 √(npq)만 구하면 Z = (K − nμ)/√(npq) ≈ N(0,1)로 표준화해 Φ 표로 읽으면 끝. 단, Φ를 찾기 전에 경계가 평균에서 몇 σ 떨어졌는지부터 봐라 — 13σ면 답은 계산 없이 0 또는 1이다.

성분 분포(Bernoulli): P(X_i = 1) = p, P(X_i = 0) = 1 − p, otherwise = 0.

$$P(K_{100}=k)=\binom{100}{k}p^k(1-p)^{100-k},\quad k=0,1,\dots,100;\qquad \text{otherwise }=0$$

### 4. 풀이 (Worked solution)

(a) 기댓값 — Bernoulli 한 개의 평균 μ = p, 합은 n배 (Lecture09, slide 4의 이항 셋업):

$$\mathbb{E}[K_{100}] = np = 100\cdot\tfrac{3}{4} = \boxed{75}$$

(b) 표준편차 — 독립이므로 분산은 더해진다. Bernoulli 한 개의 분산 p(1−p):

$$\sigma_{K_{100}}=\sqrt{np(1-p)}=\sqrt{100\cdot\tfrac34\cdot\tfrac14}=\sqrt{18.75}=\boxed{4.33}$$

(p와 1−p가 곱으로 들어가 대칭이라, p=3/4든 1/4든 σ는 같다.)

(c) CLT로 P[K_100 ≥ 18] — 표준화식 Z = (K − nμ)/(σ√n) 적용 (Lecture09, slide 9):

$$P[K_{100}\ge 18]\approx P\!\left[Z\ge \frac{18-75}{4.33}\right]=P[Z\ge -13.16]=\Phi(13.16)\approx \boxed{1}$$

18은 평균보다 13σ나 아래 → "비디오가 18개 이상"은 사실상 확실.

(d) CLT로 P[16 ≤ K_100 ≤ 24]:

$$P[16\le K_{100}\le 24]\approx \Phi\!\Big(\tfrac{24-75}{4.33}\Big)-\Phi\!\Big(\tfrac{16-75}{4.33}\Big)=\Phi(-11.78)-\Phi(-13.63)\approx \boxed{0}$$

구간 [16,24] 전체가 평균보다 11σ 이상 아래 → 확률 사실상 0.

---

경계가 의도한 버전 (p = 1/4, 평균 25): σ는 그대로 4.33.

$$\text{(c)}\quad P[K\ge18]\approx\Phi\!\Big(\tfrac{25-18}{4.33}\Big)=\Phi(1.62)\approx 0.947$$

$$\text{(d)}\quad P[16\le K\le24]\approx\Phi\!\Big(\tfrac{24-25}{4.33}\Big)-\Phi\!\Big(\tfrac{16-25}{4.33}\Big)=\Phi(-0.231)-\Phi(-2.079)\approx 0.409-0.019=0.390$$

### 5. 검산·직관 (Sanity check)

- σ 대칭성: √(npq)는 p↔q에 불변 → (b)는 어느 해석이든 4.33. ✓
- degenerate 확인: 문장대로면 (c)+(d)가 1·0으로, 두 문제가 동시에 "계산할 게 없는" 답 → 정상적 교재 문제가 아님 → 모순 진단이 맞다.
- 의도된 버전을 정확 이항과 대조 (p=1/4, 직접 계산): P[K≥18] = 0.962 (CLT 0.947), P[16≤K≤24] = 0.451 (CLT 0.390). (c)는 잘 맞고 (d)는 CLT가 다소 과소추정 — 이는 이산→연속 근사의 연속성 보정(continuity correction) 누락 탓이다. [15.5, 24.5]로 보정하면 0.440으로 정확값 0.451에 근접. (연속성 보정은 이번 강의노트엔 없어 보강 사실을 밝힘 — 보통 Yates 풀이도 보정 없이 위 0.390으로 답함.)

### 6. 한 줄 요약

> 이항 = Bernoulli의 합이니 평균 nμ·표준편차 √(npq)로 표준화해 Φ로 읽는다 — 그러나 Φ를 찾기 전에 경계가 평균에서 몇 σ인지부터 봐라. 13σ면 답은 0/1이고, 그게 나온다면 문제의 수치를 의심해야 한다.
