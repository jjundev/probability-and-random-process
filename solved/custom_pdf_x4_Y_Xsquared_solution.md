# f_X = (5/32)x⁴, Y = X² 파생분포 풀이

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture07 (Derived Distributions), 풀이일 2026-06-08

## 문제 원문

Let X be a continuous random variable with PDF

f_X(x) = (5/32)x^4,  0 < x ≤ 2
        = 0,          otherwise

and let Y = X².

a. Find the CDF of Y.
b. Find the PDF of Y.
c. Find EY.

---

## 1. 문제 정리

| 주어진 것 | 구할 것 |
|---|---|
| f_X(x) = (5/32)x⁴, 0 < x ≤ 2 (otherwise 0) | (a) CDF F_Y(y) |
| Y = X² | (b) PDF f_Y(y) |
| | (c) E[Y] |

---

## 2. 무엇을 묻고 왜 이 도구인가

파생분포 — **무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; STT 260518, "cdf부터 계산한다")

Y = X²는 X > 0 구간에서 단조증가이므로, F_Y(y)를 F_X(√y)로 표현하는 것이 자연스럽다.

---

## 3. 핵심 통찰 (Aha)

X는 (0, 2]에만 있어서 **X > 0 보장** — 따라서 {X² ≤ y} ⟺ {X ≤ √y}로 부등호 방향이 유지된다(음수 쪽 분기 없음). F_Y(y) = F_X(√y) 단 한 항으로 끝.

---

## 4. 풀이

**범위 확정:** X ∈ (0, 2], Y = X² ∈ (0, 4].

**F_X(x) 먼저 계산 (0 < x ≤ 2):**

$$F_X(x) = \int_0^x \frac{5}{32}t^4\,dt = \frac{5}{32}\cdot\frac{x^5}{5} = \frac{x^5}{32}$$

### (a) CDF

0 < y ≤ 4 일 때, X > 0이므로:

$$F_Y(y) = P(Y \le y) = P(X^2 \le y) = P(X \le \sqrt{y}) = F_X(\sqrt{y})$$

$$= \frac{(\sqrt{y})^5}{32} = \frac{y^{5/2}}{32}$$

경계: F_Y(4) = 4^(5/2)/32 = 2⁵/32 = 1 ✓

$$\boxed{F_Y(y) = \begin{cases} 0 & y \le 0 \\ \dfrac{y^{5/2}}{32} & 0 < y \le 4 \\ 1 & y > 4 \end{cases}}$$

### (b) PDF

CDF 미분:

$$f_Y(y) = \frac{d}{dy}\frac{y^{5/2}}{32} = \frac{1}{32}\cdot\frac{5}{2}\,y^{3/2} = \frac{5}{64}\,y^{3/2}$$

$$\boxed{f_Y(y) = \begin{cases} \dfrac{5}{64}\,y^{3/2} & 0 < y \le 4 \\ 0 & \text{otherwise} \end{cases}}$$

### (c) E[Y]

**방법 1 — f_Y 직접:**

$$E[Y] = \int_0^4 y\cdot\frac{5}{64}\,y^{3/2}\,dy = \frac{5}{64}\int_0^4 y^{5/2}\,dy = \frac{5}{64}\cdot\frac{y^{7/2}}{7/2}\Bigg|_0^4 = \frac{5}{64}\cdot\frac{2}{7}\cdot 128 = \frac{20}{7}$$

**방법 2 — LOTUS 검증:** (Lecture05, p.7)

$$E[Y] = E[X^2] = \int_0^2 x^2\cdot\frac{5}{32}x^4\,dx = \frac{5}{32}\int_0^2 x^6\,dx = \frac{5}{32}\cdot\frac{128}{7} = \frac{20}{7}$$

$$\boxed{E[Y] = \frac{20}{7} \approx 2.857}$$

---

## 5. 검산·직관

- **f_X 정규화:** ∫₀² (5/32)x⁴ dx = (5/32)·(32/5) = 1 ✓
- **f_Y 정규화:** ∫₀⁴ (5/64)y^(3/2) dy = (5/64)·(2/5)·4^(5/2) = (1/32)·32 = 1 ✓
- **음수 분기 미존재:** 일반 공식 f_Y(y) = [f_X(√y)+f_X(-√y)]/(2√y)에서 f_X(-√y) = 0 (X > 0이므로), 결국 (5/32)(√y)⁴/(2√y) = 5y^(3/2)/64 ✓ 일치
- **LOTUS 양 방법 일치** ✓

---

## 6. 한 줄 요약

> X > 0이 보장된 경우 Y = X²의 CDF는 음수 분기 없이 F_Y(y) = F_X(√y) 한 줄로 끝나고, 미분하면 PDF가 나온다.
