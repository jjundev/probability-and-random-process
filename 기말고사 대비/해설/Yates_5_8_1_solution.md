# Yates 5.8.1 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L07_PSP_5.8.1.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X와 Z는 독립인 확률변수로 E[X] = E[Z] = 0, Var[X] = 1, Var[Z] = 16 이다. Y = X + Z 라 하자. X와 Y의 상관계수 ρ를 구하라. X와 Y는 독립인가?

## 1. 문제 정리
- 주어진 것: X ⊥ Z, E[X] = E[Z] = 0, Var[X] = 1, Var[Z] = 16, Y = X + Z.
- 구할 것: ρ_(X,Y) (X와 Y의 상관계수), 그리고 X와 Y의 독립 여부.

## 2. 무엇을 묻고 왜 이 도구인가
공분산·상관계수 문제. 도구:
- 상관계수 정의 ρ_(X,Y) = cov(X,Y) / (σ_X · σ_Y) — 공분산을 [−1,1]로 정규화한 무차원 의존도 지표 (Lecture07, p.21의 R3 요건; correlation coefficient는 다음 강에서 정식 도입되나 정의는 cov/표준편차곱).
- 공분산 쌍선형성: cov(X, X+Z) = cov(X,X) + cov(X,Z) (Lecture07, p.25).
- 독립 ⇒ uncorrelated이지만 그 역은 거짓 (Lecture07, p.23) — 이 비대칭이 마지막 질문의 핵심.

## 3. 핵심 통찰
Y = X + Z 에서 X와 Y는 둘 다 X를 공유한다. cov(X,Y) = cov(X, X+Z) = var(X) + cov(X,Z), 그런데 X ⊥ Z 라 cov(X,Z) = 0. 결국 cov(X,Y) = var(X) = 1. "공유된 X 성분"이 상관의 원천이다.

## 4. 풀이

(전부 평균 0이라 cov(A,B) = E[AB], 단 정의·항등식으로 진행.)

공분산:
cov(X,Y) = cov(X, X+Z) = cov(X,X) + cov(X,Z)   (쌍선형성, Lecture07 p.25)
        = var(X) + cov(X,Z).
X ⊥ Z ⇒ cov(X,Z) = 0 (독립 ⇒ uncorrelated, Lecture07 p.23). 따라서
cov(X,Y) = var(X) = 1.

분산들:
var(X) = 1, 그러므로 σ_X = 1.
var(Y) = var(X + Z) = var(X) + var(Z) + 2cov(X,Z) = 1 + 16 + 0 = 17. (Lecture07 p.25)
σ_Y = √17.

상관계수:
ρ_(X,Y) = cov(X,Y) / (σ_X · σ_Y) = 1 / (1 · √17) = 1/√17 ≈ 0.2425.

독립 여부:
ρ ≠ 0 (= 1/√17 > 0) 이므로 X와 Y는 **상관(correlated)** 되어 있다. 상관이 있으면 결코 독립일 수 없다(독립 ⇒ uncorrelated의 대우). 따라서 **X와 Y는 독립이 아니다.** (Lecture07 p.23)
직관적으로도 Y = X + Z 가 X를 직접 포함하므로 X를 알면 Y에 대한 정보가 생겨 종속이다.

## 5. 검산·직관
- 부호·크기: cov = var(X) = 1 > 0 이라 양의 상관 ✓. Z의 분산 16이 커서 Y의 변동을 지배 → X가 설명하는 비율이 작아 ρ가 작음(0.24). 만약 var(Z)=0이면 Y=X로 ρ=1; var(Z)→∞면 ρ→0 (Z 잡음에 X가 묻힘) — 1/√17 은 그 사이의 합리적 값.
- 범위: ρ ∈ [−1,1] 안의 0.2425 ✓ (Lecture07 p.21, R3 유계성).
- 일관성: var(Y) = 1+16 = 17 은 독립합 분산가법성 ✓ (cov(X,Z)=0).

## 6. 한 줄 요약
> Y=X+Z가 X를 공유하므로 cov(X,Y)=var(X)=1, ρ = 1/√17 ≈ 0.24 ≠ 0 — 상관이 있으니 X와 Y는 독립이 아니다(상관 잡음 Z가 클수록 ρ는 작아진다).
