# Yates 4.5.1 풀이 — Uniform(1,5): P[Y > E[Y]], P[Y ≤ Var[Y]]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture05 (Continuous RV Part 1) p.7, 풀이일 2026-06-07

## 문제 원문

Y is a continuous uniform (1, 5) random variable.

(a) What is P[Y > E[Y]]?  
(b) What is P[Y ≤ Var[Y]]?

---

### 1. 문제 정리

Y ~ Uniform(1, 5)

| | 구할 것 |
|---|---|
| (a) | P[Y > E[Y]] |
| (b) | P[Y ≤ Var[Y]] |

$$f_Y(y) = \frac{1}{4}, \quad 1 \le y \le 5, \qquad \text{otherwise } = 0$$

---

### 2. 무엇을 묻고 왜 이 도구인가

균등분포의 E·Var를 먼저 수치로 확정한 뒤, 균등분포 CDF의 선형성으로 확률을 계산. (Lecture05, p.7)

균등 CDF: P[Y ≤ c] = (c − a)/(b − a) for a ≤ c ≤ b

---

### 3. 핵심 통찰

**균등분포의 확률은 구간 길이 비율이다 — E·Var를 수치로 구하면 나머지는 자로 잰다.**

---

### 4. 풀이

**E[Y]와 Var[Y] 계산** (Lecture05, p.7):

$$E[Y] = \frac{a+b}{2} = \frac{1+5}{2} = 3$$

$$\text{Var}[Y] = \frac{(b-a)^2}{12} = \frac{(5-1)^2}{12} = \frac{16}{12} = \frac{4}{3}$$

#### (a) P[Y > E[Y]] = P[Y > 3]

3 ∈ [1, 5]이므로:

$$P[Y > 3] = \frac{5 - 3}{5 - 1} = \frac{2}{4} = \boxed{\frac{1}{2}}$$

#### (b) P[Y ≤ Var[Y]] = P[Y ≤ 4/3]

4/3 ≈ 1.333 ∈ [1, 5]이므로:

$$P\!\left[Y \le \frac{4}{3}\right] = \frac{\dfrac{4}{3} - 1}{5 - 1} = \frac{\dfrac{1}{3}}{4} = \boxed{\frac{1}{12}}$$

---

### 5. 검산·직관

- (a): E[Y] = 3은 [1,5]의 정중앙 → 균등분포에서 P[Y > 중앙] = 1/2 ✓
- (b): Var[Y] = 4/3 ≈ 1.33은 지지 구간의 왼쪽 끝 근처 → 지지의 1/12만 해당 ✓
- 두 경우 모두 c ∈ [1,5] 확인 → CDF 공식 적용 가능 ✓

---

### 6. 한 줄 요약

> 균등분포 확률의 핵심은 구간 길이 비율 — E와 Var를 수치로 확정한 뒤 (c − a)/(b − a)에 대입하면 끝이다.
