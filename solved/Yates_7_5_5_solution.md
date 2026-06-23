# 7.5.5 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), Probability_and_Stochastic_Processes_Problems/problems_png/7.5.5.png (사용자 첨부 스크린샷으로 교차확인), 1순위 근거 Lecture08, 풀이일 2026-06-12

## 문제 원문

**7.5.5** Random variables N and K have the joint PMF

$$P_{N,K}(n,k) = \begin{cases} \dfrac{100^{n}\,e^{-100}}{(n+1)!} & n=0,1,2,\dots;\ \ k=0,1,\dots,n,\\[6pt] 0 & \text{otherwise.}\end{cases}$$

(a) Find the marginal PMF P_N(n) and the conditional PMF P_{K|N}(k|n).
(b) Find the conditional expected value E[K|N=n].
(c) Express the random variable E[K|N] as a function of N and use the iterated expectation to find E[K].

---

## 1. 문제 정리 (Setup)

**주어진 것**: 위 N, K의 결합 PMF.

| 소문항 | 구할 것 |
|---|---|
| (a) | 주변 PMF P_N(n)과 조건부 PMF P_{K\|N}(k\|n) |
| (b) | 조건부 기댓값 E[K\|N=n] |
| (c) | E[K\|N]을 N의 함수로 표현 → 반복기댓값으로 E[K] |

## 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

세 소문항이 **조건부 기댓값 사다리를 한 칸씩** 오른다 (Lecture08 흐름): 결합 → 주변 → 조건부 → 조건부 기댓값(숫자) → 조건부 기댓값(RV) → 반복기댓값. (Lecture08, p.16–17)

표준 레시피 둘만 쓰면 된다:
- 주변 PMF: P_N(n) = Σ_k P_{N,K}(n,k).
- 조건부 PMF: P_{K|N}(k|n) = P_{N,K}(n,k) / P_N(n).

## 3. 핵심 통찰 (Aha)

> **결합 PMF가 k에 전혀 의존하지 않는다.** 그래서 N=n을 고정하면 K는 {0,1,…,n} 위의 **균등분포**이고, 주변화는 "k값 개수 (n+1)개"를 곱하는 것뿐.

## 4. 풀이 (Worked solution)

### (a) 주변 P_N(n)과 조건부 P_{K|N}(k|n)

피합수가 k에 무관하고, 고정된 n에서 k는 0부터 n까지 **(n+1)개** 값:

$$P_N(n) = \sum_{k=0}^{n} \frac{100^{n}e^{-100}}{(n+1)!} = (n+1)\cdot\frac{100^{n}e^{-100}}{(n+1)!} = \frac{100^{n}e^{-100}}{n!}$$

$$P_N(n) = \begin{cases} \dfrac{100^{n}\,e^{-100}}{n!} & n=0,1,2,\dots,\\[4pt] 0 & \text{otherwise.}\end{cases}$$

즉 **N ~ Poisson(100)** (E[N]=100, (c)에서 사용).

조건부는 정의대로 나눈다 — 100^n e^{-100} 약분, (n+1)!/n! = n+1:

$$P_{K\mid N}(k\mid n) = \frac{P_{N,K}(n,k)}{P_N(n)} = \frac{100^{n}e^{-100}/(n+1)!}{100^{n}e^{-100}/n!} = \frac{n!}{(n+1)!} = \frac{1}{n+1}$$

$$P_{K\mid N}(k\mid n) = \begin{cases} \dfrac{1}{n+1} & k=0,1,\dots,n,\\[4pt] 0 & \text{otherwise.}\end{cases}$$

→ **K | N=n 은 {0,1,…,n} 위 이산 균등분포**.

### (b) 조건부 기댓값 E[K|N=n]

{0,…,n} 균등분포의 평균. Σ_{k=0}^{n} k = n(n+1)/2:

$$\mathbb{E}[K\mid N=n] = \sum_{k=0}^{n} k\cdot\frac{1}{n+1} = \frac{1}{n+1}\cdot\frac{n(n+1)}{2} = \frac{n}{2}$$

### (c) E[K|N]을 RV로 표현 → 반복기댓값

E[K|N=n] = n/2 이므로, N의 함수로서:

$$\mathbb{E}[K\mid N] = \frac{N}{2} \qquad (\text{N의 함수인 확률변수})$$

반복기댓값 법칙 E[E[K|N]] = E[K] (Lecture08, p.17), E[N]=100 (Poisson):

$$\mathbb{E}[K] = \mathbb{E}\!\left[\mathbb{E}[K\mid N]\right] = \mathbb{E}\!\left[\frac{N}{2}\right] = \frac{1}{2}\mathbb{E}[N] = \frac{1}{2}\cdot 100 = \boxed{50}$$

## 5. 검산·직관 (Sanity check)

- **주변 합 = 1**: Σ_n 100ⁿe⁻¹⁰⁰/n! = e⁻¹⁰⁰·e¹⁰⁰ = 1 ✓ (Poisson 정규화).
- **조건부 합 = 1**: Σ_{k=0}^{n} 1/(n+1) = (n+1)/(n+1) = 1 ✓.
- **경계 점검**: n=0 → K는 0만 가능 → E[K|N=0]=0 ✓. n=1 → K가 {0,1} 균등 → E=1/2 ✓.
- **E[K]=50 직관**: K는 평균적으로 N의 절반(E[K|N]=N/2), N은 평균 100 → K 평균 50.
- **구조 일치**: 정리노트 막대 자르기 예시와 같은 골격 — 거기선 X|Y~U[0,Y]라 E[X|Y]=Y/2 (Lecture08, p.18), 여기선 K|N~Uniform{0..N}이라 E[K|N]=N/2. 균등분포 → "절반" 패턴.

## 6. 한 줄 요약

> 결합 PMF가 k에 무관 ⇒ K|N은 {0…n} 균등 ⇒ E[K|N]=N/2, 반복기댓값으로 E[K]=E[N]/2=50.
