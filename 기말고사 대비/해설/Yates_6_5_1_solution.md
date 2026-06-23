# Yates 6.5.1 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L07_PSP_6.5.1.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X와 Y가 독립인 이산 확률변수로, 모든 비정수 k에 대해 P_X(k) = P_Y(k) = 0 이라 하자. W = X + Y 의 PMF가 다음을 만족함을 보여라.

P_W(w) = Σ_(k=−∞)^∞ P_X(k) · P_Y(w − k).

## 1. 문제 정리
- 주어진 것: X, Y 독립인 정수값 이산 RV (비정수에서 PMF = 0). W = X + Y.
- 구할 것(증명): 이산 convolution 공식 P_W(w) = Σ_k P_X(k) P_Y(w − k).

## 2. 무엇을 묻고 왜 이 도구인가
독립 두 RV의 합 W = X + Y의 분포는 convolution으로 주어진다 (Lecture07, p.14). 이 문제는 그 공식을 "유도"하라는 것이다. 출발점은 PMF의 정의 P_W(w) = P(W = w) = P(X + Y = w) (Lecture03, p.6)와, 한 사건을 서로소 경우들의 합집합으로 쪼개는 전체확률정리 (Lecture02, p.12), 그리고 독립의 곱 분해 p_(X,Y) = p_X·p_Y (Lecture04, slide 19).

## 3. 핵심 통찰
사건 {X + Y = w}를 "X가 어떤 정수 k인가"로 분해하면, 각 가지는 서로소인 {X = k, Y = w − k}이고 이들의 합집합이 전체다.

## 4. 풀이

**Step 1 — PMF 정의:** (Lecture03, p.6)
P_W(w) = P(W = w) = P(X + Y = w).

**Step 2 — X의 값으로 사건 분해 (전체확률정리):** (Lecture02, p.12; Lecture03, p.21의 Z=g(X,Y) PMF)
X는 정수값만 가지므로, 사건 {X + Y = w}는 서로소인 사건들
  {X = k 그리고 Y = w − k},  k = …, −1, 0, 1, …
의 합집합이다 (X = k가 정해지면 X + Y = w이려면 반드시 Y = w − k). 서로 다른 k는 X 값이 달라 서로소이므로, 확률은 단순 합:
P_W(w) = Σ_(k=−∞)^∞ P(X = k, Y = w − k)
     = Σ_(k=−∞)^∞ p_(X,Y)(k, w − k).

**Step 3 — 독립으로 곱 분해:** (Lecture04, slide 19: X ⊥ Y ⇔ p_(X,Y)(x,y) = p_X(x) p_Y(y))
P_W(w) = Σ_(k=−∞)^∞ P_X(k) · P_Y(w − k). ∎

이로써 이산 convolution 공식이 유도되었다 (Lecture07, p.14).

**보충 (비정수 PMF = 0의 역할):** P_X(k), P_Y(w − k)가 정수 k에서만 0이 아니므로 합에 실제로 기여하는 항은 X, Y가 모두 정수가 되는 k뿐이다. w가 정수가 아니면 모든 항이 0 → P_W(w) = 0 (W도 정수값 RV)와 일관.

## 5. 검산·직관
- 대칭성: k 대신 j = w − k로 치환하면 P_W(w) = Σ_j P_X(w − j) P_Y(j) — X, Y 역할 대칭 ✓ (덧셈이라 당연).
- 정규화: Σ_w P_W(w) = Σ_w Σ_k P_X(k) P_Y(w−k) = Σ_k P_X(k) Σ_w P_Y(w−k) = Σ_k P_X(k)·1 = 1 ✓.
- 직관: "합이 w가 되는 모든 (X, Y) 쌍"을 X = k로 가지치기해 확률을 더한 것 — convolution = 한쪽을 뒤집어 밀며 곱해 더하기 (Lecture07, p.15).

## 6. 한 줄 요약
> 독립 합 W=X+Y의 PMF는 {X+Y=w}를 X=k로 서로소 분해(전체확률)하고 독립으로 곱 분해하면 곧바로 convolution Σ_k P_X(k)P_Y(w−k)가 된다.
