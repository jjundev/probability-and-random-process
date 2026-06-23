# 7.5.3 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), Probability_and_Stochastic_Processes_Problems/problems_png/7.5.3.png (사용자 첨부 스크린샷으로 확인), 1순위 근거 Lecture08 (조건부기댓값·분산)·Lecture07 (공분산)·Lecture04 (결합·조건부 PMF), 풀이일 2026-06-12

## 문제 원문

**7.5.3** The probability model for random variable A is

$$P_A(a) = \begin{cases} 1/3 & a = -1,\\ 2/3 & a = 1,\\ 0 & \text{otherwise.}\end{cases}$$

The conditional probability model for random variable B given A is:

$$P_{B\mid A}(b\mid -1) = \begin{cases} 1/3 & b = 0,\\ 2/3 & b = 1,\\ 0 & \text{otherwise,}\end{cases} \qquad P_{B\mid A}(b\mid 1) = \begin{cases} 1/2 & b = 0,\\ 1/2 & b = 1,\\ 0 & \text{otherwise.}\end{cases}$$

(a) What is the probability model for random variables A and B? Write the joint PMF P_{A,B}(a,b) as a table.
(b) If A = 1, what is the conditional expected value E[B|A=1]?
(c) If B = 1, what is the conditional PMF P_{A|B}(a|1)?
(d) If B = 1, what is the conditional variance Var[A|B=1] of A?
(e) What is the covariance Cov[A,B]?

---

## 1. 문제 정리 (Setup)

**주어진 것**: 위 P_A(a), P_{B|A}(b|−1), P_{B|A}(b|1).

| 소문항 | 구할 것 | 근거 |
|---|---|---|
| (a) | 결합 PMF P_{A,B}(a,b) 표 | 곱셈규칙 (Lecture04) |
| (b) | E[B\|A=1] | 조건부 기댓값 (Lecture08, p.16) |
| (c) | P_{A\|B}(a\|1) | 조건부 PMF (Lecture04) |
| (d) | Var[A\|B=1] | 조건부 분산 (Lecture08, p.21) |
| (e) | Cov[A,B] | 공분산 (Lecture07, p.23) |

## 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

다섯 소문항이 **결합분포 도구상자를 한 바퀴** 돈다: 주변×조건부로 결합을 짓고(곱셈규칙), 거기서 조건부 기댓값을 읽고, 조건을 뒤집고(P_{B|A} → P_{A|B}, 베이즈), 조건부 분산, 마지막에 공분산. 핵심 엔진은 하나 — **결합 PMF 표를 일단 완성하면 (b)~(e)는 전부 그 표 위의 단순 계산.**

## 3. 핵심 통찰 (Aha)

> 결합 PMF 표 P_{A,B} = P_A·P_{B|A} **하나**를 만들면 나머지는 전부 그 표에서 읽어낸다. 게다가 **A ∈ {−1, 1} ⟹ A² ≡ 1** 이라 분산 계산이 한 줄로 줄어든다.

## 4. 풀이 (Worked solution)

### (a) 결합 PMF — 곱셈규칙 P_{A,B}(a,b) = P_A(a)·P_{B|A}(b|a)

$$P_{A,B}(a,b) = \begin{cases} (1/3)(1/3)=1/9 & (a,b)=(-1,0),\\ (1/3)(2/3)=2/9 & (a,b)=(-1,1),\\ (2/3)(1/2)=1/3 & (a,b)=(1,0),\\ (2/3)(1/2)=1/3 & (a,b)=(1,1),\\ 0 & \text{otherwise.}\end{cases}$$

표로(주변합 포함, 9분모 통일):

| P_{A,B} | b=0 | b=1 | **P_A(a)** |
|---|---|---|---|
| **a=−1** | 1/9 | 2/9 | **3/9** |
| **a=1** | 3/9 | 3/9 | **6/9** |
| **P_B(b)** | **4/9** | **5/9** | **1** |

### (b) E[B|A=1]

A=1이면 B는 {0,1} 균등(각 1/2):

$$\mathbb{E}[B\mid A=1] = 0\cdot\tfrac12 + 1\cdot\tfrac12 = \tfrac12$$

### (c) P_{A|B}(a|1) — 조건을 뒤집기 (베이즈)

정의 P_{A|B}(a|1) = P_{A,B}(a,1) / P_B(1), 그리고 P_B(1) = 2/9 + 3/9 = 5/9:

$$P_{A\mid B}(a\mid 1) = \begin{cases} \dfrac{2/9}{5/9}=\dfrac{2}{5} & a=-1,\\[4pt] \dfrac{3/9}{5/9}=\dfrac{3}{5} & a=1,\\[4pt] 0 & \text{otherwise.}\end{cases}$$

### (d) Var[A|B=1]

(c)의 조건부 PMF 사용. 먼저 조건부 평균:

$$\mathbb{E}[A\mid B=1] = (-1)\tfrac25 + (1)\tfrac35 = \tfrac15$$

A ∈ {−1,1}이므로 A² ≡ 1 ⟹ E[A²|B=1] = 1. 조건부 분산 공식 (Lecture08, p.21):

$$\mathrm{Var}[A\mid B=1] = \mathbb{E}[A^2\mid B=1] - \big(\mathbb{E}[A\mid B=1]\big)^2 = 1 - \left(\tfrac15\right)^2 = \frac{24}{25}$$

### (e) Cov[A,B] = E[AB] − E[A]E[B] (Lecture07, p.23)

주변에서 E[A], E[B]:

$$\mathbb{E}[A] = (-1)\tfrac13 + (1)\tfrac23 = \tfrac13, \qquad \mathbb{E}[B] = 1\cdot P_B(1) = \tfrac59$$

E[AB]는 b=0 항이 0이므로 b=1만 합산:

$$\mathbb{E}[AB] = (-1)(1)\tfrac29 + (1)(1)\tfrac39 = -\tfrac29 + \tfrac39 = \tfrac19$$

$$\mathrm{Cov}[A,B] = \tfrac19 - \tfrac13\cdot\tfrac59 = \tfrac{3}{27} - \tfrac{5}{27} = \boxed{-\dfrac{2}{27}}$$

## 5. 검산·직관 (Sanity check)

- **결합 합 = 1**: 1/9+2/9+3/9+3/9 = 9/9 ✓.
- **(c) 합 = 1**: 2/5 + 3/5 = 1 ✓.
- **(d) 범위**: 0 ≤ Var ≤ 1 (A∈{−1,1}이라 분산 최대 1). 24/25 = 0.96 ✓, 거의 최대 — B=1을 알아도 A는 여전히 −1/1 어느 쪽인지 거의 불확실하니 타당.
- **(e) 부호 직관**: A=−1일 때 P(B=1)=2/3(↑), A=1일 때 P(B=1)=1/2(↓) — A가 커지면 B=1 확률이 줄어듦 → **음의 상관**. Cov = −2/27 < 0 ✓.

## 6. 한 줄 요약

> 결합 PMF 표 하나(P_A·P_{B|A})를 세우면 조건부 기댓값·조건부 PMF·조건부 분산·공분산이 전부 그 표 위의 산수가 되고, A²≡1이 분산을 한 줄로 줄인다.
