# 12.1.2 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture11 (LMS/MMSE = 조건부 기댓값), 풀이일 2026-06-14

## 문제 원문

12.1.2 ● X and Y have the joint PDF

f_{X,Y}(x,y) = 6(y − x),  0 ≤ x ≤ y ≤ 1
             = 0,          otherwise.

(a) What is f_X(x)?
(b) What is the blind estimate x̂_B?
(c) What is the minimum mean square error estimate of X given X < 0.5?
(d) What is f_Y(y)?
(e) What is the blind estimate ŷ_B?
(f) What is the minimum mean square error estimate of Y given Y > 0.5?

---

### 1. 문제 정리 (Setup)

결합 PDF:

```
f_{X,Y}(x,y) = 6(y−x),   0 ≤ x ≤ y ≤ 1
             = 0,         otherwise        (otherwise = 0)
```

지지영역은 대각선 위 삼각형(0 ≤ x ≤ y ≤ 1). 구할 것:

| 부분 | 묻는 것 | 정체 |
|---|---|---|
| (a) | f_X(x) | X 주변 PDF |
| (b) | x̂_B (blind) | 관측 없는 MMSE = E[X] |
| (c) | MMSE of X given X<0.5 | E[X | X<0.5] |
| (d) | f_Y(y) | Y 주변 PDF |
| (e) | ŷ_B (blind) | E[Y] |
| (f) | MMSE of Y given Y>0.5 | E[Y | Y>0.5] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

- Blind estimate: 관측이 하나도 없을 때의 MMSE 추정값. 제곱오차 E[(X−x̂)²]를 최소화하는 상수는 분포의 평균 → x̂_B = E[X] (무조건부 평균). (Lecture11, slide 6·13)
- MMSE given 사건: 사건(X<0.5 등)으로 조건 건 뒤의 MMSE = 조건부 평균 E[X | 사건]. (Lecture11, slide 6, "θ̂_LMS = E[Θ|X=x]")

둘 다 평균인데, 어느 분포의 평균이냐만 다름 — 그래서 주변/조건부 분포를 먼저 만드는 게 자연스러운 첫 수.

### 3. 핵심 통찰 (Aha)

> blind = "주변분포의 평균", 사건조건 MMSE = "그 사건으로 자른 뒤 재정규화한 분포의 평균" — 둘 다 똑같이 평균을 구하는 일이고, 차이는 적분 범위와 정규화 상수뿐.

### 4. 풀이 (Worked solution)

**(a) f_X(x)** — y를 x부터 1까지 적분:

```
f_X(x) = ∫_{x}^{1} 6(y−x) dy = 6·[(y−x)²/2]_{x}^{1} = 3(1−x)²,   0 ≤ x ≤ 1
       = 0,   otherwise        (otherwise = 0)
```

**(b) x̂_B = E[X]**:

```
E[X] = ∫_0^1 x·3(1−x)² dx = ∫_0^1 (3x − 6x² + 3x³) dx
     = 3/2 − 2 + 3/4 = 1/4
```
```
x̂_B = 1/4
```

**(c) E[X | X<0.5]** — X<0.5로 자르고 재정규화:

```
P(X<0.5) = ∫_0^{1/2} 3(1−x)² dx = [−(1−x)³]_0^{1/2} = 1 − 1/8 = 7/8

∫_0^{1/2} x·3(1−x)² dx = [3x²/2 − 2x³ + 3x⁴/4]_0^{1/2}
                       = 3/8 − 1/4 + 3/64 = 11/64

E[X | X<0.5] = (11/64) / (7/8) = 11/56 ≈ 0.196
```

**(d) f_Y(y)** — x를 0부터 y까지 적분:

```
f_Y(y) = ∫_0^{y} 6(y−x) dx = 6·[yx − x²/2]_0^{y} = 6·(y²/2) = 3y²,   0 ≤ y ≤ 1
       = 0,   otherwise        (otherwise = 0)
```

**(e) ŷ_B = E[Y]**:

```
E[Y] = ∫_0^1 y·3y² dy = ∫_0^1 3y³ dy = 3/4
```
```
ŷ_B = 3/4
```

**(f) E[Y | Y>0.5]** — Y>0.5로 자르고 재정규화:

```
P(Y>0.5) = ∫_{1/2}^1 3y² dy = [y³]_{1/2}^1 = 1 − 1/8 = 7/8

∫_{1/2}^1 y·3y² dy = [3y⁴/4]_{1/2}^1 = 3/4 − 3/64 = 45/64

E[Y | Y>0.5] = (45/64) / (7/8) = 45/56 ≈ 0.804
```

### 5. 검산·직관 (Sanity check)

- 주변 PDF 정규화: ∫_0^1 3(1−x)² dx = 1 ✓, ∫_0^1 3y² dy = 1 ✓
- 조건이 평균을 옮기는 방향:
  - (c) X<0.5로 자르면 윗꼬리가 잘려 평균이 내려가야 함 → 11/56 ≈ 0.196 < 1/4 = 0.25 ✓
  - (f) Y>0.5로 자르면 아랫부분이 잘려 평균이 올라가야 함 → 45/56 ≈ 0.804 > 3/4 = 0.75 ✓
- X와 Y의 비대칭: f_X는 작은 x로(3(1−x)², 감소), f_Y는 큰 y로(3y², 증가) 쏠림. x ≤ y 제약상 X는 아래쪽, Y는 위쪽에 몰리는 게 당연 → E[X]=1/4 < E[Y]=3/4 ✓
- 공통 분모 7/8: P(X<0.5)=P(Y>0.5)=7/8 — 둘 다 (0.5)³=1/8을 잘라낸 꼴이라 대칭적으로 들어맞음 ✓

### 6. 한 줄 요약

> blind estimate는 주변분포의 평균 E[·], 사건조건 MMSE는 그 사건으로 자른 분포의 조건부 평균 — 둘 다 "적절한 분포의 평균"이며, 결합 PDF에서 주변분포부터 뽑는 게 출발점이다.
