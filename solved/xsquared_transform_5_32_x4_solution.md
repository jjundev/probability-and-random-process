# Y = X² 파생분포 (f_X = (5/32)x⁴, CDF·PDF·EY) 풀이

> 출처: 사용자 첨부 이미지 (Problem 5), 1순위 근거 Lecture07_Further_Topics_RV_Part_1, 풀이일 2026-06-17

## 문제 원문

Let X be a continuous random variable with PDF

f_X(x) = (5/32)x⁴  for 0 < x ≤ 2,  and 0 otherwise.

and let Y = X².

- a. Find the CDF of Y.
- b. Find the PDF of Y.
- c. Find EY.

---

### 1. 문제 정리 (Setup)

X는 연속확률변수, Y = X².

$$f_X(x) = \begin{cases} \dfrac{5}{32}x^4, & 0 < x \le 2 \\[4pt] 0, & \text{otherwise} \end{cases}$$

| 부분 | 구할 것 |
|---|---|
| a | Y의 CDF, F_Y(y) |
| b | Y의 PDF, f_Y(y) |
| c | 기댓값 E[Y] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

파생분포 문제. 정리노트 핵심 원칙: **무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; §2.1) 정리노트에 Y = X²의 예시가 직접 실려 있다 (Lecture07, p.10; §2.4).

다만 노트의 일반식 F_Y(y) = F_X(√y) − F_X(−√y)는 X가 음수도 가질 때의 **양쪽 가지** 공식이다. 여기서는 X ∈ (0,2]로 **양수만** 가지므로 음의 가지 F_X(−√y)는 0 — 한쪽 가지만 살아남는다. 이것이 이 문제의 포인트다.

치역: X ∈ (0,2] → Y = X² ∈ (0,4].

### 3. 핵심 통찰 (Aha)

X > 0이므로 "X² ≤ y" ⇔ "X ≤ √y" (음수 가지 소멸) → F_Y(y) = F_X(√y). 그러니 먼저 F_X를 구해 √y를 대입하면 끝.

### 4. 풀이 (Worked solution)

**준비 — F_X(x).** 0 < x ≤ 2에서:

$$F_X(x) = \int_0^x \frac{5}{32}t^4\,dt = \frac{5}{32}\cdot\frac{x^5}{5} = \frac{x^5}{32}$$

검: F_X(2) = 32/32 = 1 ✓ (정규화 성립).

**(a) CDF.** 0 < y ≤ 4에서 F_Y(y) = F_X(√y) = (√y)⁵/32 = y^(5/2)/32:

$$F_Y(y) = \begin{cases} 0, & y \le 0 \\[2pt] \dfrac{y^{5/2}}{32}, & 0 < y \le 4 \\[4pt] 1, & y > 4 \end{cases}$$

검: F_Y(4) = 4^(5/2)/32 = 32/32 = 1 ✓.

**(b) PDF.** CDF 미분 (Lecture07, p.10):

$$f_Y(y) = \frac{d}{dy}\frac{y^{5/2}}{32} = \frac{5}{2}\cdot\frac{y^{3/2}}{32} = \frac{5\,y^{3/2}}{64} \quad (0 < y \le 4), \qquad \text{otherwise } f_Y(y) = 0$$

**(c) E[Y].** f_Y 없이 원변수로 바로 적분(LOTUS):

$$E[Y] = E[X^2] = \int_0^2 x^2\cdot\frac{5}{32}x^4\,dx = \frac{5}{32}\int_0^2 x^6\,dx = \frac{5}{32}\cdot\frac{2^7}{7} = \frac{5}{32}\cdot\frac{128}{7} = \frac{20}{7} \approx 2.857$$

### 5. 검산·직관 (Sanity check)

- f_Y 정규화: ∫₀⁴ 5y^(3/2)/64 dy = (5/64)·(2/7)·4^(7/2) = (5/64)(2/7)(128) = 1 ✓.
- E[Y] 재확인 (f_Y로): ∫₀⁴ y·5y^(3/2)/64 dy = (5/64)(2/7)·4^(7/2) = 20/7 ✓ 두 경로 일치.
- 직관: f_X = (5/32)x⁴는 x=2 근처로 강하게 쏠린 분포 → X는 2에 가깝고 Y = X²은 4에 가깝다. E[Y] = 20/7 ≈ 2.86이 치역 (0,4]의 위쪽에 위치 — 일치.
- 차원/경계: F_Y가 0→1로 단조증가, y=4에서 1 도달 ✓.

### 6. 한 줄 요약

> Y = X²의 분포는 CDF부터: 정의역이 양수뿐이면 일반식 F_X(√y) − F_X(−√y)에서 음의 가지가 사라져 F_Y(y) = F_X(√y) 한쪽만 남는다.
