# Yates 4.5.7 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L05_PSP_4.5.7.png, 1순위 근거 Lecture05, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
Y 는 Erlang (n = 2, λ = 2) 확률변수다.
(a) E[Y] 는?
(b) Var[Y] 는?
(c) P[0.5 ≤ Y < 1.5] 는?

## 1. 문제 정리
- 주어진 것: Y ~ Erlang(n = 2, λ = 2).
- 구할 것: (a) E[Y], (b) Var[Y], (c) P[0.5 ≤ Y < 1.5].
- Erlang(n, λ) 은 **독립인 n 개 Exponential(λ) 의 합**이다 (n 번째 도착까지의 대기시간). n = 1 이면 Exponential(λ) 그 자체.

## 2. 무엇을 묻고 왜 이 도구인가
정리노트 L05 는 Exponential(λ) 의 PDF·CDF·모멘트를 다룬다 (Lecture05, p.13–14): f(x) = λe^(−λx) (x ≥ 0, otherwise = 0), E = 1/λ, Var = 1/λ². Erlang 은 그 n 합이라 모멘트가 단순 n 배가 되고, 확률 (c) 는 "무조건 CDF 부터" 원칙으로 CDF 차로 계산한다 (Lecture05, p.9). ⚠ Erlang 자체(합·convolution)는 L07 주제라 정리노트 L05 에 PDF/CDF 공식이 직접은 없어 일반 교과서의 Erlang 공식을 쓰되, 적분·모멘트·CDF 차 계산 방법론은 L05 를 따른다.

## 3. 핵심 통찰
Erlang(n, λ) = 독립 Exponential(λ) n 개의 합 ⇒ 평균·분산은 그냥 **각각의 n 배**(E[Y] = n/λ, Var[Y] = n/λ²). 확률은 PDF 적분 대신 닫힌형 CDF F_Y(y) = 1 − e^(−λy)(1 + λy) (n = 2 전용)의 차로 잡는다.

## 4. 풀이

Erlang(n, λ) 의 PDF (일반 교과서 표준형, n = 2 대입):

f_Y(y) = λ^n y^(n−1) e^(−λy) / (n−1)! = λ² y e^(−λy) = 4y e^(−2y),   y ≥ 0
f_Y(y) = 0,                                                            otherwise

### (a) E[Y]
독립 Exponential(λ) 의 합이므로 기댓값의 선형성:
E[Y] = n · (1/λ) = 2 · (1/2) = 1.

### (b) Var[Y]
독립합이라 분산도 단순 합 (Lecture05 의 Var[Exp] = 1/λ² 를 n 번):
Var[Y] = n · (1/λ²) = 2 · (1/4) = 1/2.

### (c) P[0.5 ≤ Y < 1.5]
n = 2 Erlang 의 CDF (부분적분 1 회로 얻어지는 표준 결과):
F_Y(y) = 1 − e^(−λy)(1 + λy),   y ≥ 0,   otherwise = 0.
λ = 2 → F_Y(y) = 1 − e^(−2y)(1 + 2y).

P[0.5 ≤ Y < 1.5] = F_Y(1.5) − F_Y(0.5)
  = [1 − e^(−3)(1 + 3)] − [1 − e^(−1)(1 + 1)]
  = 2e^(−1) − 4e^(−3).

수치: 2e^(−1) = 0.73576, 4e^(−3) = 0.19915 →
P[0.5 ≤ Y < 1.5] = 0.73576 − 0.19915 ≈ 0.5366.

(연속 RV 라 P(Y = 0.5) = 0 이므로 ≤ 와 < 의 경계 차이는 무관 — Lecture05, p.6.)

## 5. 검산·직관
- 단위·부호: E[Y] = 1, Var[Y] = 0.5 모두 양수, 평균 1 근처에 퍼짐 √0.5 ≈ 0.71. 구간 [0.5, 1.5] 은 평균 ±0.5 라 분포의 중심 덩어리를 덮으므로 확률이 0.5 정도 나오는 것이 타당.
- CDF 극한: F_Y(0) = 1 − 1·1 = 0 ✓, F_Y(∞) = 1 ✓.
- Erlang↔Exp 일관성: n = 1 넣으면 F = 1 − e^(−λy) 로 Exponential CDF (Lecture05, p.13) 와 일치 → 공식 형태 신뢰.

## 6. 한 줄 요약
> Erlang(n, λ) 은 Exponential(λ) n 개의 합이라 평균·분산은 각각의 n 배(n/λ, n/λ²)이고, 구간확률은 닫힌형 CDF F = 1 − e^(−λy)(1 + λy) 의 차로 구한다.
