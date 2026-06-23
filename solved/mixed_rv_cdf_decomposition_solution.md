# Mixed RV CDF 분해 (Problem 13) 풀이

> 출처: 사용자 첨부 이미지 (Problem 13), 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-14

## 문제 원문

Let X be a random variable with the following CDF

$$F_X(x) = \begin{cases} 0 & x < 0 \\ x & 0 \le x < \tfrac14 \\ x + \tfrac12 & \tfrac14 \le x < \tfrac12 \\ 1 & x \ge \tfrac12 \end{cases}$$

- a. Plot F_X(x) and explain why X is a mixed random variable.
- b. Find P(X ≤ 1/3).
- c. Find P(X ≥ 1/4).
- d. Write CDF of X in the form of F_X(x) = C(x) + D(x), where C(x) is a continuous function and D(x) is a staircase function, i.e., D(x) = Σ_k a_k u(x − x_k).
- e. Find c(x) = d/dx C(x).
- f. Find EX using EX = ∫_{−∞}^{∞} x c(x) dx + Σ_k x_k a_k.

---

### 1. 문제 정리 (Setup)

| 부분 | 구할 것 |
|---|---|
| a | F_X 그래프 + X가 mixed인 이유 |
| b | P(X ≤ 1/3) |
| c | P(X ≥ 1/4) |
| d | F_X = C(x) + D(x) 분해 (C 연속, D 계단) |
| e | c(x) = d/dx C(x) |
| f | EX = ∫ x·c(x) dx + Σ x_k a_k |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

정리노트의 CDF 성질이 직접 도구를 준다 (Lecture05, p.10):
- **이산 성분**: CDF의 **점프(불연속)**, 점프 크기 = 그 점의 확률질량 P(X=a).
- **연속 성분**: CDF의 **연속 기울기**, 그 미분 = 밀도 f_X(x) = dF_X/dx.

이 문제 CDF는 **연속 경사 + 점프가 공존** → 두 성분을 분리(C+D)하면 모든 소문항이 풀린다. "CDF는 이산이든 연속이든 항상 well-defined" (Lecture05, p.84).

### 3. 핵심 통찰 (Aha)

> CDF에서 **세로로 뛴 높이(점프)는 그 점에 박힌 확률 덩어리**, **비스듬히 오른 부분의 기울기는 연속 밀도**다. 점프 1/2(@x=1/4) + 경사 면적 1/2 = 전체 1.

### 4. 풀이 (Worked solution)

**경계 점검 (점프/연속 판별):**
- x=0: 좌극한 0, F(0)=0 → 연속 (점프 없음)
- x=1/4: 좌극한 = 1/4, F(1/4)= 1/4+1/2 = 3/4 → **점프 = 3/4 − 1/4 = 1/2**
- x=1/2: 좌극한 = 1/2+1/2 = 1, F(1/2)=1 → 연속 (점프 없음)

**a. 그래프 & mixed 이유.**
- [0, 1/4): 원점에서 기울기 1로 직선 상승, (1/4)⁻에서 높이 1/4 도달
- x=1/4: 높이 1/4 → 3/4 로 **수직 점프 1/2** (●3/4 채움, ○1/4 빔)
- [1/4, 1/2): 3/4에서 다시 기울기 1로 상승, (1/2)⁻에서 높이 1 도달
- x ≥ 1/2: 1로 평평

X가 **mixed**인 이유: F_X가 순수 연속도, 순수 계단(이산)도 아니다. **연속적으로 증가하는 구간**(연속 성분 존재)과 **x=1/4의 점프**(P(X=1/4)=1/2 > 0인 이산 atom)를 **동시에** 가지므로 (Lecture05, p.83의 "연속이면 P(X=a)=0"이 깨짐 → 이산 성분 존재) 혼합형이다.

**b. P(X ≤ 1/3).** 1/3 ∈ [1/4, 1/2) 이므로 해당 식 대입:

$$P(X \le \tfrac13) = F_X(\tfrac13) = \tfrac13 + \tfrac12 = \tfrac{5}{6}$$

**c. P(X ≥ 1/4).** CCDF 변형 — 단, x=1/4의 atom을 포함해야 하므로 좌극한 사용:

$$P(X \ge \tfrac14) = 1 - P(X < \tfrac14) = 1 - F_X(\tfrac14^-) = 1 - \tfrac14 = \tfrac34$$

(만약 P(X>1/4)였다면 1 − F(1/4) = 1/4로 atom 1/2를 잃는다 — 부등호 방향 주의.)

**d. C(x) + D(x) 분해.** 점프만 모은 계단함수:

$$D(x) = \tfrac12\,u\!\left(x - \tfrac14\right) \qquad \Big(x_1 = \tfrac14,\ a_1 = \tfrac12\Big)$$

연속 성분 C(x) = F_X(x) − D(x):

$$C(x) = \begin{cases} 0 & x < 0 \\ x & 0 \le x < \tfrac12 \\ \tfrac12 & x \ge \tfrac12 \end{cases}$$

(검증: 1/4 ≤ x < 1/2 에서 C = (x+1/2) − 1/2 = x → x=1/4에서 좌우 모두 1/4, **연속** ✓)

**e. c(x) = d/dx C(x).**

$$c(x) = \frac{d}{dx}C(x) = \begin{cases} 1 & 0 < x < \tfrac12 \\ 0 & \text{otherwise } = 0 \end{cases}$$

**f. EX.**

$$EX = \int_{-\infty}^{\infty} x\,c(x)\,dx + \sum_k x_k a_k = \int_{0}^{1/2} x\cdot 1\,dx + \Big(\tfrac14\Big)\Big(\tfrac12\Big)$$

$$= \left[\frac{x^2}{2}\right]_0^{1/2} + \frac18 = \frac{1/4}{2} + \frac18 = \frac18 + \frac18 = \boxed{\dfrac14}$$

### 5. 검산·직관 (Sanity check)

- **전체 확률 = 1**: 연속 성분 면적 ∫₀^{1/2} 1 dx = 1/2, 이산 atom 1/2 → 합 1 ✓
- **EX 범위**: X ∈ [0, 1/2], 질량의 절반이 x=1/4에 박혀 있고 나머지 절반은 [0,1/2) 균등 → 평균이 1/4 근방인 것이 직관과 일치 ✓
- **b vs c 경계 함정**: P(X≤1/3)은 점프점 1/4을 이미 지나 atom 포함, P(X≥1/4)은 좌극한을 써야 atom 1/2를 포함 — 둘 다 점검 ✓

### 6. 한 줄 요약

> Mixed RV의 CDF는 **점프 높이 = 이산 atom 확률**, **연속 경사의 미분 = 밀도**로 분해되고, 기댓값은 ∫x·c(x)dx + Σxₖaₖ로 두 성분을 따로 더한다.
