# Yates 5.8.5 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L07_PSP_5.8.5.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X와 Y는 독립인 확률변수이고 PDF는 다음과 같다.

f_X(x) = (1/3)e^(−x/3),   x ≥ 0
f_X(x) = 0,   otherwise

f_Y(y) = (1/2)e^(−y/2),   y ≥ 0
f_Y(y) = 0,   otherwise

(a) 상관 r_{X,Y}를 구하라.
(b) 공분산 Cov[X, Y]를 구하라.

## 1. 문제 정리
주어진 것: X ~ Exponential(λ_X = 1/3) (평균 3), Y ~ Exponential(λ_Y = 1/2) (평균 2), X ⊥ Y.
구할 것: (a) 상관(correlation) r_{X,Y} = E[XY], (b) Cov[X,Y].

(주의: Yates에서 "correlation" r_{X,Y}는 곱의 기댓값 E[XY]를 뜻하며, 상관"계수" ρ와 다른 양이다.)

## 2. 무엇을 묻고 왜 이 도구인가
- 상관 r_{X,Y} = E[XY]. 독립이면 곱의 기댓값이 기댓값의 곱으로 분리된다: X ⊥ Y ⇒ E[XY] = E[X]E[Y]. (Lecture07, p.23 / Lecture04, slide 21)
- Cov 계산식: Cov(X,Y) = E[XY] − E[X]E[Y]. (Lecture07, p.23)
지수분포 평균은 1/λ (= 평균 파라미터)이므로 적분 없이 바로 대입 가능하다.

## 3. 핵심 통찰
"독립 ⇒ uncorrelated"가 결정타다. (Lecture07, p.23) 독립이 주어졌으니 E[XY]=E[X]E[Y]이고, 따라서 Cov는 자동으로 0 — 적분을 풀 필요조차 없다.

## 4. 풀이

지수분포의 평균:
E[X] = 1/λ_X = 1/(1/3) = 3
E[Y] = 1/λ_Y = 1/(1/2) = 2

**(a) 상관 r_{X,Y}** — 독립이므로 분리:

r_{X,Y} = E[XY] = E[X]·E[Y] = 3·2 = 6

**(b) 공분산 Cov[X,Y]**:

Cov[X,Y] = E[XY] − E[X]E[Y] = 6 − 3·2 = 0

(독립 ⇒ uncorrelated이므로 Cov = 0임이 정의상 보장된다.)

## 5. 검산·직관
- E[X]=3, E[Y]=2는 각 PDF가 평균 1/λ를 갖는 표준 지수분포 사실과 일치 ✓ (예: ∫_0^∞ x·(1/3)e^(−x/3) dx = 3).
- 독립이면 한 변수가 다른 변수에 대해 정보를 주지 않으므로 선형 연관(공분산)이 0인 게 당연 ✓.
- 역방향 주의: Cov=0이라고 항상 독립인 건 아니지만(Lecture07 예시 2), 여기선 독립이 전제로 주어져 한 방향만 쓰면 됨.

## 6. 한 줄 요약
> 독립이면 E[XY]=E[X]E[Y]이라 상관 r_{X,Y}=6, 공분산 Cov=0 — 적분 없이 "독립 ⇒ uncorrelated"로 끝난다.
