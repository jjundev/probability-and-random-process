# Pishro 4.4.6 풀이
> 출처: Introduction to Probability, Statistics, and Random Processes (Pishro-Nik), L07_IPSRP_4.4.6.png, 1순위 근거 Lecture07, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
X ~ Exponential(λ) 이고 Y = aX (a는 양의 실수)라 하자. Y ~ Exponential(λ/a) 임을 보여라.

## 1. 문제 정리
- 주어진 것: X ~ Exponential(λ), 즉 f_X(x) = λe^(−λx) (x ≥ 0), f_X(x) = 0 otherwise. Y = aX, a > 0.
- 보일 것: Y ~ Exponential(λ/a). 즉 f_Y(y) = (λ/a)·e^(−(λ/a)y) (y ≥ 0), 0 otherwise.

## 2. 무엇을 묻고 왜 이 도구인가
선형변환 Y = aX (b = 0, a > 0)의 파생분포다. 정리노트에 결론이 직접 적혀 있다 — **b = 0, a > 0 이면 Y ~ Exp(λ/a)** (Lecture07, p.8). 또한 선형 PDF 공식 f_Y(y) = (1/|a|)·f_X((y−b)/a) (Lecture07, p.7)을 그대로 쓰면 한 줄로 증명되지만, 정의에 충실하게 **CDF부터** 유도해 보인다. (Lecture07, p.10)

## 3. 핵심 통찰
a > 0 이므로 "aX ≤ y" ⇔ "X ≤ y/a" — 양수 스케일은 부등호를 보존한다. 그러면 F_Y(y) = F_X(y/a) 이고, 지수분포 CDF 안에 y/a 를 대입하면 지수의 계수가 λ → λ/a 로 바뀐다.

## 4. 풀이

지수분포의 CDF: x ≥ 0 에서 F_X(x) = 1 − e^(−λx), 0 otherwise. (Exponential(λ) 표준 결과)

y ≥ 0 일 때 (a > 0 이므로 y = aX ≥ 0):

F_Y(y) = P(Y ≤ y) = P(aX ≤ y) = P(X ≤ y/a) = F_X(y/a) = 1 − e^(−λ·(y/a)) = 1 − e^(−(λ/a)y).

이는 정확히 모수 λ/a 인 지수분포의 CDF다. 미분하여 PDF를 얻으면

f_Y(y) = d/dy [1 − e^(−(λ/a)y)] = (λ/a)·e^(−(λ/a)y),   y ≥ 0
f_Y(y) = 0,   otherwise

이는 Exponential(λ/a)의 PDF이므로 Y ~ Exponential(λ/a). ∎

(대안 — 선형 PDF 공식 직접 적용: f_Y(y) = (1/|a|) f_X(y/a) = (1/a)·λ e^(−λ(y/a)) = (λ/a) e^(−(λ/a)y) for y ≥ 0, otherwise = 0. (Lecture07, p.7) 동일한 결과.)

## 5. 검산·직관
- 정규화: ∫_0^∞ (λ/a) e^(−(λ/a)y) dy = 1 ✓ (지수분포 PDF 형태이므로 자동).
- 평균 점검: E[X] = 1/λ 이고 E[Y] = E[aX] = a·E[X] = a/λ. 한편 Exponential(λ/a)의 평균은 1/(λ/a) = a/λ ✓ 일치.
- 직관: a > 1 이면 시간축을 늘리는 것 → 사건이 더 늦게 발생 → 평균 a/λ 증가, rate(모수)는 λ/a 로 감소. 메모리리스 성질도 스케일 후 그대로 보존.
- 함정 주의: b ≠ 0 (예 Y = aX + b)이면 지수보존이 깨진다 (support가 b로 평행이동, 일반적으로 지수 아님). (Lecture07, p.8)

## 6. 한 줄 요약
> 지수분포에 양수 스케일 Y = aX 를 가하면 rate가 λ → λ/a 로 바뀐 지수분포가 되며(평균은 a배), 이는 F_Y(y) = F_X(y/a) 한 줄에서 곧장 나온다 — 단 상수항 b가 붙으면 보존되지 않는다.
