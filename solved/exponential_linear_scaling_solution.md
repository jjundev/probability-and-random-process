# Exponential 선형 스케일링 풀이

> 출처: 수업 숙제 Problem 6, 사용자 첨부 이미지, 1순위 근거 Lecture07 + Lecture05, 풀이일 2026-06-08

## 문제 원문

Let X ~ Exponential(λ), and Y = aX, where a is a positive real number. Show that

$$Y \sim \mathrm{Exponential}\!\left(\frac{\lambda}{a}\right)$$

---

### 1. 문제 정리

| 주어진 것 | 구할 것 |
|---|---|
| X ~ Exponential(λ), 즉 f_X(x) = λe^(-λx), x ≥ 0; otherwise = 0 | Y = aX가 Exponential(λ/a)임을 증명 |
| a > 0 (양의 실수) | |

---

### 2. 무엇을 묻고 왜 이 도구인가

파생분포(derived distribution) 문제 — Y = g(X) = aX의 분포를 구하는 것.

강의 원칙: **무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; STT 260518, "첫 번째 뭐부터 계산한다? cdf부터 계산한다")

왜 CDF인가: Y의 PDF를 직접 쓰기 어렵지만, "Y ≤ y"라는 사건을 X에 대한 부등식으로 변환하면 이미 알고 있는 F_X를 바로 쓸 수 있기 때문이다.

---

### 3. 핵심 통찰

"P(aX ≤ y) = P(X ≤ y/a)" — a > 0이므로 나누기 방향이 바뀌지 않고, y/a를 X의 CDF에 그대로 꽂으면 끝이다. (Lecture07, p.7)

---

### 4. 풀이

**Step 0 — Y의 범위 확인**

X ≥ 0이고 a > 0이므로 Y = aX ≥ 0. 따라서 y < 0이면 F_Y(y) = 0.

**Step 1 — CDF 계산 (y ≥ 0)**

$$
F_Y(y) = \mathbb{P}(Y \le y) = \mathbb{P}(aX \le y) = \mathbb{P}\!\left(X \le \frac{y}{a}\right) = F_X\!\left(\frac{y}{a}\right)
$$

Exponential CDF(Lecture05, p.13-14): F_X(x) = 1 - e^{-λx} for x ≥ 0를 대입:

$$
F_Y(y) = 1 - e^{-\lambda \cdot \frac{y}{a}} = 1 - e^{-\frac{\lambda}{a}\,y}, \quad y \ge 0
$$

**Step 2 — PDF 도출 (미분)**

$$
f_Y(y) = \frac{d}{dy}F_Y(y) = \frac{\lambda}{a}\,e^{-\frac{\lambda}{a}\,y}, \quad y \ge 0, \qquad \text{otherwise } f_Y(y) = 0
$$

**Step 3 — 분포 식별**

Exponential(μ)의 PDF 형태: μe^{-μy}, y ≥ 0. (Lecture05, p.13)

위 f_Y(y)에서 μ = λ/a로 놓으면 정확히 일치한다. 따라서:

$$
\boxed{Y \sim \mathrm{Exponential}\!\left(\frac{\lambda}{a}\right)}
$$

(Lecture07, p.8: "b=0, a>0이면 Y ~ Exp(λ/a)")

---

### 5. 검산·직관

**적분 = 1 확인:**

$$
\int_0^{\infty} \frac{\lambda}{a}\,e^{-\frac{\lambda}{a}\,y}\,dy = \frac{\lambda}{a}\cdot \frac{a}{\lambda} = 1 \checkmark
$$

**기대값 직관:** E[Y] = a·E[X] = a·(1/λ) = a/λ. Exponential(λ/a)의 기대값은 a/λ ✓

**물리적 직관:** X가 "평균 1/λ 시간마다 발생"하는 사건의 대기시간이라면, Y = aX는 시간 축을 a배 늘린 것 — 당연히 도착률(rate)은 1/a배로 줄어 λ/a가 된다.

---

### 6. 한 줄 요약

> Y = aX (a > 0)로 지수분포를 선형 스케일하면 CDF에 y/a를 대입하는 것만으로 충분하고, rate는 λ에서 λ/a로 정확히 a분의 1이 된다.
