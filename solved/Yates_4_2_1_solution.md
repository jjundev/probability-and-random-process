# Yates 4.2.1 풀이

> 출처: Yates & Goodman PSP, 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

The cumulative distribution function of random variable X is

F_X(x) = 0          for x < -1
F_X(x) = (x+1)/2   for -1 ≤ x < 1
F_X(x) = 1          for x ≥ 1

(a) What is P[X > 1/2]?
(b) What is P[-1/2 < X ≤ 3/4]?
(c) What is P[|X| ≤ 1/2]?
(d) What is the value of a such that P[X ≤ a] = 0.8?

---

### 1. 문제 정리 (Setup)

$$F_X(x) = \begin{cases} 0, & x < -1 \\ \dfrac{x+1}{2}, & -1 \le x < 1 \\ 1, & x \ge 1 \end{cases}$$

| 소문항 | 구할 것 |
|---|---|
| a | P[X > 1/2] |
| b | P[−1/2 < X ≤ 3/4] |
| c | P[\|X\| ≤ 1/2] |
| d | P[X ≤ a] = 0.8 인 a |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

주어진 것이 PDF가 아니라 **CDF** 이므로, 구간확률을 구하는 표준 도구는 (Lecture05, p.9-10):

- P(X > x) = 1 − F_X(x) (CCDF)
- P(a < X ≤ b) = F_X(b) − F_X(a)
- 연속 RV이므로 P(X = c) = 0 → 등호 있고 없고 확률 변화 없음 (Lecture05, p.5)

(d)는 CDF를 역으로 풀어 **quantile**을 구하는 것.

### 3. 핵심 통찰 (Aha)

F_X(x) = (x+1)/2 는 X ~ Uniform(−1, 1)의 CDF 그 자체 — 모든 구간확률이 구간 길이의 절반이다.

### 4. 풀이 (Worked solution)

**(a) P[X > 1/2]**

$$P[X>1/2] = 1 - F_X(1/2) = 1 - \frac{1/2+1}{2} = 1 - \frac{3}{4} = \boxed{\frac{1}{4}}$$

---

**(b) P[−1/2 < X ≤ 3/4]**

$$P[-1/2 < X \le 3/4] = F_X(3/4) - F_X(-1/2)$$

$$= \frac{3/4+1}{2} - \frac{-1/2+1}{2} = \frac{7}{8} - \frac{1}{4} = \frac{7}{8} - \frac{2}{8} = \boxed{\frac{5}{8}}$$

---

**(c) P[|X| ≤ 1/2]**

|X| ≤ 1/2 ⟺ −1/2 ≤ X ≤ 1/2. 연속 RV이므로 경계 등호 무관 (Lecture05, p.5):

$$P[|X|\le 1/2] = F_X(1/2) - F_X(-1/2) = \frac{3}{4} - \frac{1}{4} = \boxed{\frac{1}{2}}$$

---

**(d) F_X(a) = 0.8 인 a**

0 < 0.8 < 1 이므로 −1 ≤ a < 1 범위에서 해가 존재:

$$\frac{a+1}{2} = 0.8 \;\Rightarrow\; a+1 = 1.6 \;\Rightarrow\; \boxed{a = 0.6}$$

### 5. 검산·직관 (Sanity check)

- X ~ U(−1,1) 이므로 모든 길이-L 구간의 확률 = L/2.
  - (a): [1/2, 1] 길이 = 1/2 → P = 1/4 ✓
  - (b): [−1/2, 3/4] 길이 = 5/4 → P = 5/8 ✓
  - (c): [−1/2, 1/2] 길이 = 1 → P = 1/2 ✓
- (d): a=0.6은 [−1,1] 안에 있고 F_X(0.6)=(1.6)/2=0.8 ✓

### 6. 한 줄 요약

> CDF가 주어지면 구간확률은 F_X(b)−F_X(a) 한 번, 꼬리확률은 1−F_X(x) 한 번, quantile은 방정식 역산 한 번으로 끝난다.
