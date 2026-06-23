# Pishro 5.4.33 풀이
> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), L07_IPSRP_5.4.33.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X와 Y는 두 확률변수이다. σ²_X = 4, σ²_Y = 9 라 하자.
두 확률변수 Z = 2X − Y 와 W = X + Y 가 독립임을 알 때, Cov(X,Y)와 ρ(X,Y)를 구하라.

## 1. 문제 정리
- 주어진 것: Var(X) = 4, Var(Y) = 9, 그리고 Z = 2X − Y 와 W = X + Y 가 독립.
- 구할 것: Cov(X,Y), ρ(X,Y).

## 2. 무엇을 묻고 왜 이 도구인가
독립 ⇒ uncorrelated, 즉 Cov(Z,W) = 0 이다 (Lecture07, p.23). 우리는 Cov(X,Y)를 모르므로, "Z와 W가 독립"이라는 조건을 Cov(Z,W) = 0 이라는 **방정식 한 개**로 바꿔 미지수 Cov(X,Y)를 푼다. 이때 공분산의 쌍선형성(bilinearity) 항등식이 핵심 도구다 (Lecture07, p.25).

## 3. 핵심 통찰
Cov는 양쪽 인수에 대해 선형이고 Cov(X,X)=Var(X)이므로, Cov(2X−Y, X+Y)를 전개하면 Var(X), Var(Y), Cov(X,Y)만 남는다. 독립이 주는 "= 0"이 Cov(X,Y)를 유일하게 결정한다.

## 4. 풀이

공분산 항등식 (Lecture07, p.25):
Cov(X,X) = Var(X),   Cov(aX, Y) = a·Cov(X,Y),   Cov(X, Y+Z) = Cov(X,Y) + Cov(X,Z),   Cov(X,Y) = Cov(Y,X)

쌍선형 전개:
Cov(2X − Y, X + Y)
 = Cov(2X, X) + Cov(2X, Y) + Cov(−Y, X) + Cov(−Y, Y)
 = 2·Cov(X,X) + 2·Cov(X,Y) − Cov(Y,X) − Cov(Y,Y)
 = 2·Var(X) + 2·Cov(X,Y) − Cov(X,Y) − Var(Y)
 = 2·Var(X) + Cov(X,Y) − Var(Y)

Z ⊥ W ⇒ Cov(Z,W) = 0 (Lecture07, p.23):
2·Var(X) + Cov(X,Y) − Var(Y) = 0
2·(4) + Cov(X,Y) − 9 = 0
8 + Cov(X,Y) − 9 = 0
Cov(X,Y) = 1

상관계수 (Lecture08, p.6):
ρ(X,Y) = Cov(X,Y) / √(Var(X)·Var(Y)) = 1 / √(4·9) = 1/6 ≈ 0.1667

## 5. 검산·직관
- |ρ| = 1/6 ≤ 1 유계 만족 ✓ (Lecture08, p.6).
- 부호 점검: Cov(X,Y) = 1 > 0 이면 Z, W를 독립으로 만들려면 2Var(X) − Var(Y) = 8 − 9 = −1 을 +Cov로 상쇄해야 한다 → Cov = 1. 일관됨 ✓.
- 주의: "Z ⊥ W ⇒ Cov(Z,W)=0"은 한 방향만 쓴다(독립 ⇒ uncorrelated). 역은 일반적으로 거짓이지만 여기서는 정방향만 필요 (Lecture07, p.23).

## 6. 한 줄 요약
> "독립 ⇒ Cov = 0"을 쌍선형 전개 Cov(2X−Y, X+Y) = 2Var(X) + Cov(X,Y) − Var(Y) = 0 에 대입하면 Cov(X,Y)가 곧장 결정된다.
