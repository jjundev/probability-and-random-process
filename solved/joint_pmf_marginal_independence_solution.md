# Joint PMF marginal·조건부·독립 (Problem 1) 풀이

> 출처: 사용자 첨부 이미지 (Problem 1, Table 5.4), 1순위 근거 Lecture04_Discrete_RV_Part_2, 풀이일 2026-06-15

## 문제 원문

Consider two random variables X and Y with joint PMF given in Table 5.4:

```
            Y=1     Y=2
X=1         1/3     1/12
X=2         1/6     0
X=4         1/12    1/3
```

- a. Find P(X ≤ 2, Y > 1).
- b. Find the marginal PMFs of X and Y.
- c. Find P(Y = 2 | X = 1).
- d. Are X and Y independent?

---

### 1. 문제 정리 (Setup)

결합 PMF p_{X,Y}(x,y) (otherwise = 0):

$$\begin{array}{c|cc} p_{X,Y} & Y=1 & Y=2 \\ \hline X=1 & 1/3 & 1/12 \\ X=2 & 1/6 & 0 \\ X=4 & 1/12 & 1/3 \end{array}$$

| 부분 | 구할 것 |
|---|---|
| a | P(X ≤ 2, Y > 1) |
| b | X, Y의 marginal PMF |
| c | P(Y = 2 \| X = 1) |
| d | X, Y 독립 여부 |

(검산용 전체합: 4/12+1/12+2/12+0+1/12+4/12 = 12/12 = 1 ✓ — 유효한 결합 PMF)

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

결합 PMF 표 한 장에서 네 가지 핵심 연산이 모두 나온다 (Lecture04):
- **결합확률(a)**: 사건 영역에 해당하는 칸들을 그냥 더한다.
- **marginal(b)**: 한 변수를 "지워" 다른 변수로 합산 — 표의 행 합/열 합.
- **조건부(c)**: p_{X|Y} = p_{X,Y}/p_Y, "한 줄로 좁힌 뒤 그 줄 안에서 재정규화" (Lecture04, slide 8).
- **독립(d)**: 모든 칸이 marginal 곱과 일치해야 함 (Lecture04, slide 19).

### 3. 핵심 통찰 (Aha)

> 결합 PMF 표에서 **marginal = 가장자리(margin) 합**, **조건부 = 한 줄만 떼어 그 줄 합으로 나눔**, **독립 = 모든 칸이 (행합)×(열합)인지 검사 — 단 한 칸이라도 어긋나면 종속** (Lecture04, slide 124의 "하나만 달라도 다른 거야").

### 4. 풀이 (Worked solution)

**a. P(X ≤ 2, Y > 1).** 조건 = X∈{1,2} 그리고 Y=2. 해당 칸은 (X=1,Y=2)와 (X=2,Y=2):

$$P(X\le 2, Y>1) = p_{X,Y}(1,2) + p_{X,Y}(2,2) = \tfrac{1}{12} + 0 = \tfrac{1}{12}$$

**b. Marginal PMF.** 행으로 합 → P_X, 열로 합 → P_Y.

$$p_X(x) = \sum_y p_{X,Y}(x,y):\quad p_X(1)=\tfrac13+\tfrac{1}{12}=\tfrac{5}{12},\ \ p_X(2)=\tfrac16+0=\tfrac16,\ \ p_X(4)=\tfrac{1}{12}+\tfrac13=\tfrac{5}{12}$$

$$p_Y(y) = \sum_x p_{X,Y}(x,y):\quad p_Y(1)=\tfrac13+\tfrac16+\tfrac{1}{12}=\tfrac{7}{12},\ \ p_Y(2)=\tfrac{1}{12}+0+\tfrac13=\tfrac{5}{12}$$

둘 다 otherwise = 0. (검산: 5/12+2/12+5/12=1 ✓, 7/12+5/12=1 ✓)

**c. P(Y = 2 | X = 1).** 조건부 PMF 정의 (Lecture04, slide 8):

$$P(Y=2\mid X=1) = \frac{p_{X,Y}(1,2)}{p_X(1)} = \frac{1/12}{5/12} = \tfrac{1}{5}$$

**d. 독립 여부.** X⊥Y ⟺ 모든 (x,y)에서 p_{X,Y}=p_X·p_Y (Lecture04, slide 19). 반례 한 칸만 찾으면 충분 — (X=2, Y=2):

$$p_{X,Y}(2,2)=0 \quad\text{vs}\quad p_X(2)\,p_Y(2)=\tfrac16\cdot\tfrac{5}{12}=\tfrac{5}{72}\neq 0$$

한 칸이 어긋나므로 **X와 Y는 독립이 아니다 (종속).**

### 5. 검산·직관 (Sanity check)

- marginal 두 줄 모두 합 1 ✓, 모든 칸 ≥ 0 ✓.
- 조건부 c: X=1 줄(1/3, 1/12)을 그 합 5/12로 나누면 (4/5, 1/5) → P(Y=2|X=1)=1/5, 둘 합 1 ✓.
- 독립 직관: p_{X,Y}(2,2)=0인데 X=2도 Y=2도 각각 가능 — "둘 다 가능한데 동시엔 절대 불가" = 강한 의존. 한 칸의 0만으로도 종속 확정.

### 6. 한 줄 요약

> 결합 PMF 표는 **행·열 합 = marginal, 한 줄 떼어 재정규화 = 조건부, 모든 칸 = 곱인지 검사 = 독립**이며, 독립은 단 한 칸의 불일치(여기선 (2,2)의 0)로 무너진다.
