# Yates 3.2.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 1순위 근거 Lecture03, 풀이일 2026-06-09

## 문제 원문

The random variable N has PMF:

$$P_N(n) = \begin{cases} c(1/2)^n & n = 0, 1, 2, \ldots \\ 0 & \text{otherwise} \end{cases}$$

(a) What is the value of the constant c?
(b) What is P[N ≤ 1]?

---

### 1. 문제 정리 (Setup)

구할 것: (a) c, (b) P[N ≤ 1]

---

### 2. 무엇을 묻고 왜 이 도구인가

PMF의 필수 조건: 모든 n에 대해 합산 = 1 (정규화). (Lecture03, p.6)
c(1/2)^n 꼴의 무한급수는 등비급수로 닫힌 형태로 계산된다.

---

### 3. 핵심 통찰 (Aha)

"PMF의 합 = 1" 조건이 c를 결정한다 — 등비급수 공식 Σ r^n = 1/(1-r) 한 줄로 끝.

---

### 4. 풀이 (Worked solution)

**[a] c 계산**

$$\sum_{n=0}^{\infty} c\!\left(\frac{1}{2}\right)^n = c \cdot \frac{1}{1-1/2} = 2c = 1 \implies c = \frac{1}{2}$$

완성된 PMF:

$$P_N(n) = \begin{cases} \left(\dfrac{1}{2}\right)^{n+1} & n = 0, 1, 2, \ldots \\ 0 & \text{otherwise} \end{cases}$$

**[b] P[N ≤ 1]**

$$P[N \le 1] = P_N(0) + P_N(1) = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}$$

---

### 5. 검산·직관 (Sanity check)

$$\sum_{n=2}^{\infty}\left(\frac{1}{2}\right)^{n+1} = \frac{(1/2)^3}{1-1/2} = \frac{1}{4}$$

P[N≤1] + P[N≥2] = 3/4 + 1/4 = 1 ✓

---

### 6. 한 줄 요약

> PMF 합 = 1 조건 + 등비급수 Σ(1/2)^n = 2 → c = 1/2; P[N≤1] = 3/4.
