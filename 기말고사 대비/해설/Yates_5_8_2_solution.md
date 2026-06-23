# Yates 5.8.2 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L07_PSP_5.8.2.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
Problem 5.2.1 의 확률변수 X 와 Y 에 대해 다음을 구하라.
(a) W = Y/X 의 기댓값 E[W].
(b) 상관(correlation) r_(X,Y) = E[XY].
(c) 공분산(covariance) Cov[X, Y].
(d) 상관계수(correlation coefficient) ρ_(X,Y).
(e) X + Y 의 분산 Var[X + Y].
(Problem 5.3.1 의 결과를 참고해도 좋다.)

(Problem 5.2.1 의 결합 PMF:
 p_(X,Y)(x,y) = c·x·y,  x = 1, 2, 4;  y = 1, 3
 p_(X,Y)(x,y) = 0,      otherwise. )

## 1. 문제 정리
주어진 것: 결합 PMF p_(X,Y)(x,y) = c·xy on x∈{1,2,4}, y∈{1,3}, otherwise = 0.
먼저 c 와 주변 PMF·모멘트가 필요(Problem 5.2.1/5.3.1 의 선행 결과). 구할 것: (a)~(e).

선행 계산 (Lecture03, p.20 marginal; p.18 var):
- 정규화: Σ_x Σ_y c·xy = c·(Σ_x x)(Σ_y y) = c·(1+2+4)(1+3) = c·7·4 = 28c = 1 → c = 1/28.
- PMF 가 x-함수 × y-함수 (cxy) 로 분리되고 지지가 곱집합 {1,2,4}×{1,3} → **X ⊥ Y 독립** (Lecture07, p.63 독립판정과 동형: p_(X,Y)=p_X p_Y).
- 주변 p_X(x) = x/7 (x=1,2,4), otherwise 0;  p_Y(y) = y/4 (y=1,3), otherwise 0.
- E[X] = Σ x·(x/7) = (1+4+16)/7 = 21/7 = 3.   E[X²] = (1+8+64)/7 = 73/7.  Var(X) = 73/7 − 9 = 10/7.
- E[Y] = Σ y·(y/4) = (1+9)/4 = 10/4 = 5/2.    E[Y²] = (1+27)/4 = 28/4 = 7.   Var(Y) = 7 − 25/4 = 3/4.

## 2. 무엇을 묻고 왜 이 도구인가
공분산·상관·상관계수 묶음 문제. 핵심은 X ⊥ Y 를 알아채는 것 — 독립이면 E[XY]=E[X]E[Y], Cov=0, ρ=0 가 즉시 따라온다 (Lecture07, p.23, p.63). E[W]=E[Y/X] 는 Y 와 1/X 가 독립이라 E[Y]·E[1/X] 로 분해. Var[X+Y]=Var(X)+Var(Y)+2Cov 인데 Cov=0 (Lecture07, p.68).

## 3. 핵심 통찰
"cxy 로 분리 + 곱집합 지지 ⇒ 독립" 한 방에 (b)(c)(d) 가 풀린다 — Cov=0, ρ=0, 상관은 단지 평균의 곱. (a)(e)만 약간의 모멘트 계산.

## 4. 풀이

(a) E[W] = E[Y/X]
Y 와 1/X 는 (X⊥Y 이므로) 독립 → E[Y/X] = E[Y]·E[1/X] (Lecture03, p.21 함수 기댓값 + 독립 분해).
E[1/X] = Σ (1/x)·p_X(x) = (1/1)(1/7) + (1/2)(2/7) + (1/4)(4/7) = 1/7 + 1/7 + 1/7 = 3/7.
E[W] = (5/2)·(3/7) = 15/14 ≈ 1.071.

(b) 상관 r_(X,Y) = E[XY]
독립이므로 E[XY] = E[X]·E[Y] (Lecture07, p.63).
r_(X,Y) = 3·(5/2) = 15/2 = 7.5.

(c) 공분산 Cov[X,Y]
Cov(X,Y) = E[XY] − E[X]E[Y] = 15/2 − 3·(5/2) = 15/2 − 15/2 = 0 (Lecture07, p.62).
(독립 ⇒ uncorrelated 와 일치, Lecture07, p.63.)

(d) 상관계수 ρ_(X,Y)
ρ_(X,Y) = Cov(X,Y) / (σ_X σ_Y) = 0 / (σ_X σ_Y) = 0.
(분모 σ_X σ_Y = √(10/7)·√(3/4) > 0 이므로 정의됨; 분자 0 → ρ = 0.)

(e) Var[X + Y]
Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y) (Lecture07, p.68). Cov = 0 이므로
Var(X+Y) = Var(X) + Var(Y) = 10/7 + 3/4 = 40/28 + 21/28 = 61/28 ≈ 2.179.

## 5. 검산·직관
- 독립의 일관성: Cov=0 ⇒ ρ=0 ⇒ Var(X+Y)=Var(X)+Var(Y) — 세 결과가 서로 모순 없이 맞물림 ✓.
- r_(X,Y)=E[X]E[Y]=7.5 는 양수지만 이는 X,Y 가 둘 다 양의 평균을 가져서일 뿐, "상관"(선형 종속)과는 무관 — ρ=0 이 진짜 의존도(없음)를 말한다 (Lecture07, p.74 의 dimensionless 유계 지표 R3).
- E[1/X]=3/7 ≠ 1/E[X]=1/3: Jensen 류 비선형성으로 E[1/X] ≥ 1/E[X] (3/7 ≈ 0.429 > 0.333) ✓ — 1/X 평균을 1/평균으로 착각하지 말 것.

## 6. 한 줄 요약
> 결합 PMF 가 cxy 로 분리되면 X⊥Y 이라 Cov=ρ=0, 상관 r=E[X]E[Y]=7.5, Var(X+Y)=Var(X)+Var(Y)=61/28, 그리고 E[Y/X]=E[Y]E[1/X]=15/14 로 모두 곱으로 분해된다.
