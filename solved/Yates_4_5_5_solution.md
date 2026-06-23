# Yates 4.5.5 풀이 — Exponential: P[Y > E[Y]], P[Y > 2E[Y]]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture05 (Continuous RV Part 1) p.13–14, 풀이일 2026-06-07

## 문제 원문

The time delay Y (in milliseconds) that your computer needs to connect to an access point is an exponential random variable.

(a) Find P[Y > E[Y]].  
(b) Find P[Y > 2E[Y]].

---

### 1. 문제 정리

Y ~ Exponential(λ), 파라미터 미지수.

$$f_Y(y) = \lambda e^{-\lambda y}, \quad y \ge 0, \qquad \text{otherwise } = 0$$

| | 구할 것 |
|---|---|
| (a) | P[Y > E[Y]] |
| (b) | P[Y > 2E[Y]] |

---

### 2. 무엇을 묻고 왜 이 도구인가

지수분포의 CCDF (Lecture05, p.13–14):

$$P(Y > t) = e^{-\lambda t}, \quad t \ge 0$$

E[Y] = 1/λ를 t에 대입하면 λ가 약분되어 사라진다.

---

### 3. 핵심 통찰

**지수분포에서 P[Y > n·E[Y]] = e^(-n) — λ값에 무관한 보편 상수다.**

---

### 4. 풀이

E[Y] = 1/λ (Lecture05, p.14)를 먼저 확정.

**(a) P[Y > E[Y]] = P[Y > 1/λ]**

$$P\!\left[Y > \frac{1}{\lambda}\right] = e^{-\lambda \cdot \frac{1}{\lambda}} = e^{-1} \approx \boxed{0.368}$$

**(b) P[Y > 2E[Y]] = P[Y > 2/λ]**

$$P\!\left[Y > \frac{2}{\lambda}\right] = e^{-\lambda \cdot \frac{2}{\lambda}} = e^{-2} \approx \boxed{0.135}$$

λ가 어떤 값이든 답이 고정된다.

---

### 5. 검산·직관

- P[Y > E[Y]] ≈ 0.368 > 0.5 — 지수분포는 오른쪽 꼬리가 두꺼워 평균 초과 확률이 1/2보다 크다. 균등분포(1/2)와 대조적. ✓
- **일반화**: P[Y > n·E[Y]] = e^(-n). n=1,2,3 → 0.368, 0.135, 0.050 순으로 감소 ✓

---

### 6. 한 줄 요약

> 지수분포에서 P[Y > n·E[Y]] = e^(-n) — 파라미터 λ가 약분되어 사라지므로, 평균의 n배를 초과할 확률은 λ와 무관한 보편 상수다.
