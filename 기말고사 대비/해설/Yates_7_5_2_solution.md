# Yates 7.5.2 풀이
> 출처: Probability and Stochastic Processes (Yates & Goodman), L08_PSP_7.5.2.png, 1순위 근거 Lecture08, 풀이일 2026-06-08
> 수식 표기: PDF용 유니코드 평문 (solve-problem 기본 $$ 대비 의도적 평문화)

## 문제
확률변수 X와 Y가 Problem 7.5.1과 같은 결합 PDF
f_X,Y(x,y) = 2,   0 ≤ y ≤ x ≤ 1
f_X,Y(x,y) = 0,   otherwise
를 가진다.
주변 PDF f_X(x), 조건부 PDF f_Y|X(y|x), 조건부 기댓값 E[Y|X=x] 를 구하라.

## 1. 문제 정리
주어진 것:
- f_X,Y(x,y) = 2 (영역 0 ≤ y ≤ x ≤ 1), 그 외 0. (7.5.1과 동일)

구할 것:
- 주변 PDF f_X(x)
- 조건부 PDF f_Y|X(y|x)
- 조건부 기댓값 E[Y|X=x]

## 2. 무엇을 묻고 왜 이 도구인가
7.5.1의 거울 문제 — 이번엔 X를 고정하고 Y를 적분/조건화한다. 조건부 PDF는 f_Y|X(y|x) = f_X,Y(x,y)/f_X(x) (Lecture04, slide 8의 연속 대응). 적분 한계가 7.5.1과 반대: 영역 0 ≤ y ≤ x 에서 x를 고정하면 y ∈ [0, x].

## 3. 핵심 통찰
x를 고정하면 y ∈ [0, x]. 그래서 f_X(x) = 2x, 조건부는 [0,x] 위 균등분포 1/x — E[Y|X=x]는 [0,x]의 중점 x/2.

## 4. 풀이

### 주변 PDF f_X(x)
x 고정 시 y ∈ [0, x] (영역 0 ≤ y ≤ x):
f_X(x) = ∫_0^x f_X,Y(x,y) dy = ∫_0^x 2 dy = 2x,   0 ≤ x ≤ 1.
f_X(x) = 0,   otherwise.

### 조건부 PDF f_Y|X(y|x)
0 < x ≤ 1 (f_X(x) > 0) 인 x에 대해:
f_Y|X(y|x) = f_X,Y(x,y) / f_X(x) = 2 / (2x) = 1/x,   0 ≤ y ≤ x.
f_Y|X(y|x) = 0,   otherwise.

즉 X=x가 주어지면 Y는 구간 [0, x] 위의 균등분포 Uniform(0, x) 이다.

### 조건부 기댓값 E[Y|X=x]
균등분포 Uniform(0,x)의 평균은 중점:
E[Y|X=x] = ∫_0^x y · 1/x dy = 1/x · [y^2/2]_0^x = 1/x · x^2/2 = x/2,   0 < x ≤ 1.

## 5. 검산·직관
- f_X 정상성: ∫_0^1 2x dx = [x^2]_0^1 = 1 ✓.
- 조건부 정상성: ∫_0^x 1/x dy = x/x = 1 ✓.
- E[Y|X=x] = x/2 는 [0,x] 중점 ✓. Y ≤ X 제약상 E[Y|X=x] ≤ x 여야 하는데 x/2 ≤ x ✓.
- 교차검산(예시 1과의 일관성): 두 주변을 곱하면 f_X(x)f_Y(y) = 2x·2(1−y) ≠ 2 = f_X,Y → X와 Y는 독립이 아님 ✓ (삼각형 영역이라 당연).

## 6. 한 줄 요약
> 7.5.1을 X↔Y로 뒤집은 거울 문제 — x 고정 시 y∈[0,x]라 조건부는 [0,x] 균등분포, E[Y|X=x]는 중점 x/2.
