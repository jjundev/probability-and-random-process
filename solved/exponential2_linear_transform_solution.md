# Exponential(2), Y=2+3X — 구간확률·기댓값·조건부확률 풀이

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

Problem 11. Let X ~ Exponential(2) and Y = 2 + 3X.

- a. Find P(X > 2).
- b. Find EY and Var(Y).
- c. Find P(X > 2 | Y < 11).

---

### 1. 문제 정리 (Setup)

X ~ Exponential(2), Y = 2 + 3X.

$$f_X(x) = \begin{cases} 2e^{-2x}, & x \ge 0 \\ 0, & \text{otherwise } (x<0) \end{cases}$$

| 소문항 | 구할 것 |
|---|---|
| a | P(X > 2) |
| b | E[Y], Var(Y) |
| c | P(X > 2 \| Y < 11) |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

- **(a)**: CCDF P(X > x) = e^(−λx)를 그대로 읽는다 (Lecture05, p.14).
- **(b)**: 기댓값/분산의 선형성 — E[aX+b] = aE[X]+b, Var(aX+b) = a²Var(X). E[X]=1/λ, Var(X)=1/λ² (Lecture05, p.14).
- **(c)**: Y=2+3X는 X의 단조 함수 → "Y < 11"을 X의 조건으로 변환 후 조건부 확률 정의 적용 (Lecture05, p.9).

### 3. 핵심 통찰 (Aha)

Y = 2 + 3X는 X와 1-1 대응이라 "Y < 11"은 그냥 "X < 3"이다 — 확률 계산이 모두 X의 CDF 두 번 뺄셈으로 끝난다.

### 4. 풀이 (Worked solution)

**(a) P(X > 2)** — CCDF (Lecture05, p.14)

$$P(X>2) = e^{-\lambda\cdot 2} = e^{-2\cdot 2} = e^{-4} \approx 0.0183$$

---

**(b) E[Y], Var(Y)** — 선형 변환 (Lecture05, p.7; STT 260413)

E[X] = 1/λ = 1/2, Var(X) = 1/λ² = 1/4.

$$E[Y] = E[2+3X] = 2 + 3\cdot\frac{1}{2} = \boxed{\frac{7}{2}}$$

$$\text{Var}(Y) = \text{Var}(2+3X) = 3^2\cdot\text{Var}(X) = 9\cdot\frac{1}{4} = \boxed{\frac{9}{4}}$$

---

**(c) P(X > 2 | Y < 11)** — 조건 변환 후 조건부 확률 (Lecture05, p.9)

Y < 11 ⟺ 2 + 3X < 11 ⟺ X < 3. 따라서

$$P(X>2\mid Y<11) = P(X>2\mid X<3) = \frac{P(2<X<3)}{P(X<3)}$$

$$P(2<X<3) = F_X(3)-F_X(2) = (1-e^{-6})-(1-e^{-4}) = e^{-4}-e^{-6}$$

$$P(X<3) = F_X(3) = 1-e^{-6}$$

$$\boxed{P(X>2\mid Y<11) = \frac{e^{-4}-e^{-6}}{1-e^{-6}} \approx 0.01592}$$

### 5. 검산·직관 (Sanity check)

- P(X>2) = e^(−4) ≈ 0.018, P(X>2|Y<11) ≈ 0.016 — 조건 "X < 3"을 달면 X가 2보다 커야 하는 여지가 더 줄어드니(2~3 구간만 허용), 확률이 약간 작아지는 게 맞다 ✓.
- 분자 e^(−4)−e^(−6) > 0, 분모 1−e^(−6) < 1 → 결과 > 분자 비율이지만 여전히 e^(−4)보다 작다 ✓.
- Var(Y)=9/4: 상수 2는 분산에 기여 없고 3배 스케일링이 분산을 9배 키움 — 차원 일치 ✓.

### 6. 한 줄 요약

> Y = aX+b 꼴의 선형 변환은 조건 사건을 X 부등식으로 바꿔주고, 이후 계산은 지수분포 CCDF의 차 두 번이면 끝난다.
