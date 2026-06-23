# Yates 6.4.1 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L07_PSP_6.4.1.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
확률변수 X와 Y는 다음 결합 PDF를 갖는다.

f_(X,Y)(x, y) = 6xy^2,   0 ≤ x, y ≤ 1
f_(X,Y)(x, y) = 0,   otherwise

V = max(X, Y) 라 하자. V의 CDF와 PDF를 구하라.

## 1. 문제 정리
- 주어진 것: 단위정사각형 [0,1]×[0,1] 위 결합 PDF f_XY = 6xy^2, 그 밖은 0.
- 구할 것: V = max(X, Y)의 CDF F_V(v)와 PDF f_V(v).

## 2. 무엇을 묻고 왜 이 도구인가
파생분포(derived distribution) — 원칙은 "무조건 CDF부터 구하고 미분" (Lecture07, p.10). max는 PDF를 직접 노리기 어렵지만 CDF는 사건을 교집합으로 바꿔 쉽다. 핵심 보조사실: 이 결합 PDF는 변수분리가 되어 X ⊥ Y 임을 먼저 확인하면 (Lecture06, p.18), max의 CDF가 두 주변 CDF의 곱으로 떨어진다 (Lecture07, p.11).

## 3. 핵심 통찰
"max(X,Y) ≤ v" ⇔ "X ≤ v 그리고 Y ≤ v" — 큰 놈이 v 이하면 작은 놈은 당연히 이하 (Lecture07, p.11). 독립이면 이 교집합 확률 = F_X(v)·F_Y(v).

## 4. 풀이

**Step 0 — 독립 확인 (주변 PDF):** (Lecture06, p.11)
f_X(x) = ∫_0^1 6xy^2 dy = 6x·[y^3/3]_0^1 = 6x·(1/3) = 2x,  0 ≤ x ≤ 1;  otherwise = 0.
f_Y(y) = ∫_0^1 6xy^2 dx = 6y^2·[x^2/2]_0^1 = 6y^2·(1/2) = 3y^2,  0 ≤ y ≤ 1;  otherwise = 0.
곱 검증: f_X(x)·f_Y(y) = 2x·3y^2 = 6xy^2 = f_XY(x,y) ✓ → X ⊥ Y (Lecture06, p.18).

**Step 1 — 주변 CDF:** (Lecture05, p.9)
F_X(x) = ∫_0^x 2t dt = x^2,  0 ≤ x ≤ 1.
F_Y(y) = ∫_0^y 3t^2 dt = y^3,  0 ≤ y ≤ 1.
(둘 다 v < 0이면 0, v > 1이면 1.)

**Step 2 — V의 CDF (max ⇔ 둘 다 이하 + 독립):** (Lecture07, p.11)
0 ≤ v ≤ 1 에서
F_V(v) = P(max(X,Y) ≤ v) = P(X ≤ v, Y ≤ v) = P(X ≤ v)·P(Y ≤ v) = F_X(v)·F_Y(v) = v^2 · v^3 = v^5.

경계 포함 정리:
F_V(v) = 0,    v < 0
F_V(v) = v^5,  0 ≤ v ≤ 1
F_V(v) = 1,    v > 1

**Step 3 — V의 PDF (CDF 미분):** (Lecture07, p.10)
f_V(v) = dF_V/dv = 5v^4,   0 ≤ v ≤ 1
f_V(v) = 0,   otherwise

## 5. 검산·직관
- 정규화: ∫_0^1 5v^4 dv = [v^5]_0^1 = 1 ✓ (Lecture05, p.6).
- F_V(0) = 0, F_V(1) = 1 ✓; F_V 단조증가 ✓.
- f_V(v) = 5v^4 는 v가 클수록 급격히 커짐 — max는 큰 값으로 쏠리니 직관 일치. 게다가 Y의 CDF가 y^3로 빠르게 커지므로(Y가 1쪽에 쏠림) max는 더더욱 오른쪽으로 몰림.

## 6. 한 줄 요약
> max의 분포는 "max ≤ v ⇔ 둘 다 ≤ v"로 CDF를 만들고(독립이면 두 주변 CDF의 곱) 미분한다 — 여기선 F_V = v^5, f_V = 5v^4.
