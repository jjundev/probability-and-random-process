# uniform(0,1) → Y = e^(-X) 파생분포 풀이

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture07 (Derived Distributions), 풀이일 2026-06-08

## 문제 원문

Let X be a uniform(0,1) random variable, and let Y = e^(-X).

a. Find the CDF of Y.
b. Find the PDF of Y.
c. Find EY.

---

## 1. 문제 정리

| 주어진 것 | 구할 것 |
|---|---|
| X ~ Uniform(0,1) | (a) CDF F_Y(y) |
| Y = e^(-X) | (b) PDF f_Y(y) |
| | (c) E[Y] |

---

## 2. 무엇을 묻고 왜 이 도구인가

파생분포 문제 — Y = g(X)의 분포를 구한다. 원칙: **무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; STT 260518, "첫 번째 뭐부터 계산한다? cdf부터 계산한다")

PDF를 직접 도출하려면 복잡하지만, CDF는 단순히 확률 부등식 P(Y ≤ y)를 X의 사건으로 바꿔 쓰면 끝난다.

기댓값(c)는 LOTUS — E[g(X)] = ∫ g(x) · f_X(x) dx — 를 쓰면 Y의 PDF 없이도 직접 계산 가능. (Lecture05, p.7)

---

## 3. 핵심 통찰 (Aha)

Y = e^(-X)는 **단조감소** 함수이므로, {Y ≤ y}를 X의 사건으로 바꾸면 **부등호 방향이 반전**된다: {e^(-X) ≤ y} ⟺ {X ≥ -ln(y)}.

---

## 4. 풀이

**범위 확정:** X ∈ [0,1]이고 e^(-X)는 감소함수이므로 Y ∈ [e^(-1), 1] = [1/e, 1].

### (a) CDF

1/e ≤ y ≤ 1 일 때:

$$F_Y(y) = P(Y \le y) = P\!\left(e^{-X} \le y\right)$$

양변에 ln 적용(단조증가 → 부등호 유지), 이후 -1 곱(방향 역전):

$$e^{-X} \le y \;\Longleftrightarrow\; -X \le \ln y \;\Longleftrightarrow\; X \ge -\ln y$$

X ~ Uniform(0,1)이므로 F_X(x) = x:

$$F_Y(y) = P(X \ge -\ln y) = 1 - F_X(-\ln y) = 1 - (-\ln y) = 1 + \ln y$$

경계 확인: -ln y ∈ [0,1] iff y ∈ [1/e, 1] ✓

완전한 CDF:

$$\boxed{F_Y(y) = \begin{cases} 0 & y < 1/e \\ 1 + \ln y & 1/e \le y \le 1 \\ 1 & y > 1 \end{cases}}$$

### (b) PDF

F_Y(y)를 미분:

$$f_Y(y) = \frac{d}{dy}F_Y(y) = \frac{d}{dy}(1 + \ln y) = \frac{1}{y}$$

$$\boxed{f_Y(y) = \begin{cases} \dfrac{1}{y} & 1/e \le y \le 1 \\ 0 & \text{otherwise} \end{cases}}$$

### (c) E[Y]

**방법 1 — f_Y 직접 사용:**

$$E[Y] = \int_{1/e}^{1} y \cdot \frac{1}{y}\, dy = \int_{1/e}^{1} 1\, dy = 1 - \frac{1}{e}$$

**방법 2 — LOTUS (검증용):** (Lecture05, p.7)

$$E[Y] = E\!\left[e^{-X}\right] = \int_0^1 e^{-x} \cdot 1\, dx = \left[-e^{-x}\right]_0^1 = -e^{-1} + 1 = 1 - \frac{1}{e}$$

$$\boxed{E[Y] = 1 - \frac{1}{e} \approx 0.6321}$$

---

## 5. 검산·직관

- **정규화:** ∫_{1/e}^{1} (1/y) dy = [ln y]_{1/e}^{1} = 0 - (-1) = 1 ✓
- **CDF 경계:** F_Y(1/e) = 1 + ln(1/e) = 1 - 1 = 0 ✓, F_Y(1) = 1 + ln(1) = 1 ✓
- **단조감소 직관:** X가 0에 몰릴수록 Y = e^(-X) → 1 (큰 값); Y의 분포는 큰 값(1 근처)에서 밀도가 작고, 작은 값(1/e 근처)에서 높아야 함. f_Y(y) = 1/y는 y 작을수록 커짐 ✓
- **LOTUS 양 방법 일치** ✓ — f_Y를 경유한 계산과 f_X에서의 직접 적분이 같은 값 산출.

---

## 6. 한 줄 요약

> 단조감소 변환 Y = g(X)의 CDF는 {Y ≤ y} ⟺ {X ≥ g⁻¹(y)}로 부등호가 역전되며, 이 점만 잡으면 나머지는 기계적 미분이다.
