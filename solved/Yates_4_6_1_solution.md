# Yates 4.6.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 1순위 근거 Lecture06, 풀이일 2026-06-09

## 문제 원문

The peak temperature T, as measured in degrees Fahrenheit, on a July day in New Jersey is the Gaussian (85, 10) random variable. What is P[T > 100], P[T < 60], and P[70 ≤ T ≤ 100]?

---

### 1. 문제 정리 (Setup)

T ~ Gaussian(85, 10) — Yates 표기법에서 Gaussian(μ, σ)이므로 μ=85, σ=10 (σ²=100).

| 구할 것 | 식 |
|---------|-----|
| P[T > 100] | ? |
| P[T < 60] | ? |
| P[70 ≤ T ≤ 100] | ? |

---

### 2. 무엇을 묻고 왜 이 도구인가

임의 Gaussian 확률 → **표준화(standardization)**: Z = (T - μ)/σ ~ N(0,1)으로 변환 후 Φ 표 하나로 처리. (Lecture06, p.7)

$$\Phi(z) = P[Z \le z] = \int_{-\infty}^{z} \frac{1}{\sqrt{2\pi}} e^{-t^2/2}\,dt$$

---

### 3. 핵심 통찰 (Aha)

Z = (T - 85)/10 으로 표준화하면 모든 확률이 Φ값 뺄셈으로 환원된다.

---

### 4. 풀이 (Worked solution)

**P[T > 100]**

$$P[T > 100] = P\!\left[Z > \frac{100-85}{10}\right] = P[Z > 1.5] = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668$$

**P[T < 60]**

$$P[T < 60] = P\!\left[Z < \frac{60-85}{10}\right] = P[Z < -2.5] = 1 - \Phi(2.5) = 1 - 0.9938 = 0.0062$$

**P[70 ≤ T ≤ 100]**

$$P[70 \le T \le 100] = P[-1.5 \le Z \le 1.5] = \Phi(1.5) - \Phi(-1.5) = 2\Phi(1.5) - 1 = 2(0.9332) - 1 = 0.8664$$

---

### 5. 검산·직관 (Sanity check)

- P[70 ≤ T ≤ 100] + P[T > 100] = 0.8664 + 0.0668 = 0.9332 = Φ(1.5) = P[T ≤ 100] ✓
- P[T < 60]은 μ에서 2.5σ 아래 → 꼬리가 매우 얇음(0.62%) ✓
- P[70 ≤ T ≤ 100]은 ±1.5σ 구간 → 86.6% ✓

---

### 6. 한 줄 요약

> Gaussian 확률은 Z = (X−μ)/σ 표준화 한 번으로 Φ 표에 완전히 넘어간다 — 핵심은 경계값을 σ 단위로 환산하는 것.
