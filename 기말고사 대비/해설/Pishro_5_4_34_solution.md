# Pishro 5.4.34 풀이
> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), L07_IPSRP_5.4.34.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X ~ Uniform(1, 3) 이고 Y | X ~ Exponential(X) 이다. Cov(X, Y)를 구하라.

## 1. 문제 정리
- 주어진 것: X ~ Uniform(1, 3); 그리고 X = x 가 주어지면 Y는 rate λ = x 인 지수분포.
  - X의 PDF: f_X(x) = 1/2,  1 ≤ x ≤ 3;  f_X(x) = 0, otherwise. (Lecture05, p.7)
  - 조건부: f_(Y|X)(y|x) = x·e^(−xy),  y ≥ 0;  = 0, otherwise. (Lecture05, p.13)
- 구할 것: Cov(X, Y).

## 2. 무엇을 묻고 왜 이 도구인가
Cov(X,Y) = E[XY] − E[X]E[Y] (Lecture07, p.23). 여기서 Y의 정보는 "X가 주어졌을 때"만 깔끔하므로, 반복기댓값(law of iterated expectations) E[·] = E[E[·|X]] (Lecture08, p.17)으로 조건부 안쪽을 먼저 처리한다. 핵심 사실: rate λ인 지수분포의 평균은 1/λ (Lecture05, p.13)이므로 E[Y|X] = 1/X.

## 3. 핵심 통찰
E[XY|X] = X·E[Y|X] = X·(1/X) = 1 — X가 깔끔히 약분되어 E[XY] = E[1] = 1 이 즉시 나온다. 남는 일은 E[X]E[Y]뿐.

## 4. 풀이

**(준비) 조건부 평균:** rate가 X인 지수분포이므로 (Lecture05, p.13)
E[Y | X] = 1/X.

**(1) E[XY] — 반복기댓값:** (Lecture08, p.17)
E[XY] = E[ E[XY | X] ] = E[ X · E[Y|X] ] = E[ X · (1/X) ] = E[1] = 1.

**(2) E[X] — Uniform(1,3):** (Lecture05, p.7: E[X] = (a+b)/2)
E[X] = (1 + 3)/2 = 2.

**(3) E[Y] — 반복기댓값:** (Lecture08, p.17)
E[Y] = E[ E[Y|X] ] = E[ 1/X ] = ∫_1^3 (1/x) · (1/2) dx
= (1/2)·[ ln x ]_1^3 = (1/2)·(ln 3 − ln 1) = (1/2) ln 3 ≈ 0.5493.

**(4) Cov(X, Y):** (Lecture07, p.23)
Cov(X, Y) = E[XY] − E[X]·E[Y] = 1 − 2 · (1/2) ln 3 = 1 − ln 3 ≈ 1 − 1.0986 = −0.0986.

## 5. 검산·직관
- 부호가 음수(−0.0986): X(=지수의 rate)가 커지면 Y의 평균 1/X는 작아진다 → X와 Y는 음의 관계. 직관 일치 (Lecture07, p.23: 부호가 방향성 표시).
- |Cov|가 작은 것도 타당 — X의 범위가 [1,3]로 좁아 1/X 변동이 크지 않다.
- E[XY] = 1 이 깔끔히 떨어지는 건 조건부 구조 Y|X ~ Exp(X)의 의도된 약분 (E[Y|X]·X = 1).

## 6. 한 줄 요약
> 조건부로만 주어진 RV의 Cov는 반복기댓값으로 E[XY]=E[X·E[Y|X]]를 먼저 약분(=1)하고 E[X]E[Y]를 빼면 된다 — 여기선 1 − ln3 ≈ −0.099.
