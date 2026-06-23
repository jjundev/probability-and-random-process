# Uniform(0,1), Y = e^(−X) 파생분포 (CDF·PDF·EY) 풀이

> 출처: 사용자 첨부 이미지 (Problem 4), 1순위 근거 Lecture07_Further_Topics_RV_Part_1, 풀이일 2026-06-17

## 문제 원문

Let X be a uniform(0,1) random variable, and let Y = e^(−X).

- a. Find the CDF of Y.
- b. Find the PDF of Y.
- c. Find EY.

---

### 1. 문제 정리 (Setup)

X ~ Uniform(0,1), 그리고 Y = e^(−X).

| 부분 | 구할 것 |
|---|---|
| a | Y의 CDF, F_Y(y) |
| b | Y의 PDF, f_Y(y) |
| c | 기댓값 E[Y] |

주어진 분포:

$$f_X(x) = 1 \ \ (0\le x\le 1), \qquad \text{otherwise } f_X(x)=0, \qquad F_X(x)=x \ \ (0\le x\le 1)$$

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

파생분포(derived distribution) 문제다. 정리노트의 핵심 원칙: **PDF를 직접 노리지 말고 무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; §2.1) Y = e^(−X)는 비선형 변환이지만 단조(monotone)이므로, "Y ≤ y" 사건을 X에 대한 사건으로 그대로 번역할 수 있어 CDF 경로가 깔끔하다.

먼저 **치역**부터 잡는 게 함정 방지의 핵심이다. X ∈ (0,1)이고 e^(−X)는 감소함수 → Y ∈ (e⁻¹, 1) = (1/e, 1). 이 바깥에서 모든 밀도·확률은 0이다.

### 3. 핵심 통찰 (Aha)

e^(−X)는 **감소함수**이므로 "Y ≤ y" ⇔ "e^(−X) ≤ y" ⇔ "X ≥ −ln y" — 부등호가 뒤집힌다. 그래서 F_Y(y) = P(X ≥ −ln y) = 1 − F_X(−ln y).

### 4. 풀이 (Worked solution)

**(a) CDF.** 1/e ≤ y ≤ 1에서 (이때 −ln y ∈ [0,1]):

$$F_Y(y) = \mathbb{P}(e^{-X}\le y) = \mathbb{P}(X \ge -\ln y) = 1 - F_X(-\ln y) = 1-(-\ln y) = 1 + \ln y$$

치역 밖은 상수로 이어 붙인다:

$$F_Y(y) = \begin{cases} 0, & y < 1/e \\ 1 + \ln y, & 1/e \le y \le 1 \\ 1, & y > 1 \end{cases}$$

**(b) PDF.** CDF를 미분 (Lecture07, p.10):

$$f_Y(y) = \frac{d}{dy}\bigl(1+\ln y\bigr) = \frac{1}{y} \quad \left(\tfrac{1}{e} \le y \le 1\right), \qquad \text{otherwise } f_Y(y) = 0$$

**(c) E[Y].** 변환 RV의 기댓값은 굳이 f_Y를 안 거치고 원변수로 바로 적분하는 게 빠르다 (LOTUS):

$$E[Y] = E[e^{-X}] = \int_0^1 e^{-x}\cdot 1\,dx = \bigl[-e^{-x}\bigr]_0^1 = 1 - \frac{1}{e} \approx 0.632$$

### 5. 검산·직관 (Sanity check)

- 경계: F_Y(1) = 1 + ln 1 = 1 ✓, F_Y(1/e) = 1 + ln(1/e) = 1 − 1 = 0 ✓ — 치역 양끝에서 0과 1로 정확히 맞물림.
- 정규화: ∫_{1/e}^{1} (1/y) dy = [ln y]_{1/e}^{1} = 0 − (−1) = 1 ✓.
- E[Y] 재확인 (f_Y로): ∫_{1/e}^{1} y·(1/y) dy = ∫_{1/e}^{1} 1\,dy = 1 − 1/e ✓ 두 경로 일치.
- 직관: E[Y] = 1 − 1/e ≈ 0.632가 치역 (0.368, 1)의 가운데보다 약간 아래 — f_Y = 1/y가 작은 y 쪽에서 더 크니(밀도가 1/e 근처로 쏠림) 평균이 아래로 당겨지는 것과 일치.

### 6. 한 줄 요약

> 단조 변환의 분포는 "Y ≤ y"를 X의 사건으로 번역(감소함수면 부등호 뒤집힘)해 CDF부터 세우고 미분하며, 기댓값은 f_Y 없이 E[g(X)]로 바로 적분한다.
