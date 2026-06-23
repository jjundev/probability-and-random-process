# Pishro 4.4.4 풀이
> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), L07_IPSRP_4.4.4.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X ~ Uniform(0,1) 이고 Y = e^(−X) 라 하자.
a. Y의 CDF를 구하라.
b. Y의 PDF를 구하라.
c. E[Y] 를 구하라.

## 1. 문제 정리
- 주어진 것: X ~ Uniform(0,1), 즉 f_X(x) = 1 (0 < x < 1), f_X(x) = 0 otherwise. Y = e^(−X).
- 구할 것: F_Y(y), f_Y(y), E[Y].
- 먼저 Y의 치역(support)을 잡는다. x ∈ (0,1) 이면 −x ∈ (−1,0) 이고 e^(−x) 는 감소함수이므로 Y = e^(−X) ∈ (e^(−1), 1) = (1/e, 1).

## 2. 무엇을 묻고 왜 이 도구인가
파생분포(derived distribution) 문제다. 원칙은 단 하나 — **무조건 CDF부터 구하고 미분한다.** (Lecture07, p.10; STT 260518, "첫 번째 뭐부터 계산한다? cdf부터 계산한다") g(x) = e^(−x) 가 단조(순감소)이므로 사건 {Y ≤ y} 를 X에 대한 부등식으로 깔끔히 뒤집을 수 있어 이 방법이 자연스럽다.

## 3. 핵심 통찰
Y = e^(−X) 는 X에 대해 순감소(strictly decreasing)다. 따라서 "Y ≤ y" ⇔ "e^(−X) ≤ y" ⇔ "−X ≤ ln y" ⇔ "X ≥ −ln y" — 감소함수라 부등호가 뒤집힌다는 점이 결정적 한 수.

## 4. 풀이

(a) CDF. 1/e < y < 1 범위에서:

F_Y(y) = P(Y ≤ y) = P(e^(−X) ≤ y) = P(X ≥ −ln y) = 1 − P(X < −ln y) = 1 − F_X(−ln y).

X ~ Uniform(0,1) 이므로 0 < −ln y < 1 일 때 F_X(−ln y) = −ln y. 따라서

F_Y(y) = 0,   y ≤ 1/e
F_Y(y) = 1 + ln y,   1/e < y < 1
F_Y(y) = 1,   y ≥ 1

(경계 확인: y = 1/e 에서 1 + ln(1/e) = 1 − 1 = 0 ✓, y = 1 에서 1 + ln 1 = 1 ✓.)

(b) PDF. 위 CDF를 y로 미분한다. d/dy [1 + ln y] = 1/y 이므로

f_Y(y) = 1/y,   1/e < y < 1
f_Y(y) = 0,   otherwise

(c) E[Y]. 정의대로 PDF로 적분해도 되고, LOTUS(무의식적 통계학자의 법칙)로 X에 대해 적분해도 된다. 후자가 더 간단하다:

E[Y] = E[e^(−X)] = ∫_0^1 e^(−x) · 1 dx = [−e^(−x)]_0^1 = −e^(−1) − (−e^0) = 1 − 1/e.

수치로 약 1 − 0.3679 = 0.6321.

(검산용으로 PDF 적분: E[Y] = ∫_(1/e)^1 y · (1/y) dy = ∫_(1/e)^1 1 dy = 1 − 1/e ✓ 동일.)

## 5. 검산·직관
- 정규화: ∫_(1/e)^1 (1/y) dy = [ln y]_(1/e)^1 = 0 − (−1) = 1 ✓.
- support 점검: Y ∈ (1/e, 1) ≈ (0.368, 1). E[Y] ≈ 0.632 가 이 구간 안에 들어옴 ✓.
- 직관: f_Y(y) = 1/y 는 y가 작을수록(1/e 근처) 밀도가 큼. X가 1 근처일 때 Y가 1/e 근처로 모이고, e^(−x) 의 기울기가 그쪽에서 완만해 확률이 더 쌓이는 것과 일치.

## 6. 한 줄 요약
> 단조감소 변환은 "Y ≤ y ⇔ X ≥ g⁻¹(y)"로 부등호를 뒤집어 CDF를 만든 뒤 미분하고, 기댓값은 LOTUS로 원변수 X에 대해 적분하면 빠르다.
