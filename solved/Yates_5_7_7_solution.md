# 5.7.7 풀이

> 출처: Yates (Probability and Stochastic Processes), 사용자 첨부 이미지, 1순위 근거 Lecture06_Continuous_RV_Part_2 (조건부 PDF·marginal)·Lecture08_Further_Topics_RV_Part_2 (조건부 기댓값), 풀이일 2026-06-15

## 문제 원문

5.7.7 — Over the circle X² + Y² ≤ r², random variables X and Y have the uniform PDF

```
f_{X,Y}(x,y) = 1/(πr²)   for x² + y² ≤ r²,
             = 0          otherwise.
```

- (a) What is f_{Y|X}(y|x)?
- (b) What is E[Y|X = x]?

---

### 1. 문제 정리 (Setup)

반지름 r인 원판 위 균등분포 (otherwise = 0):

$$f_{X,Y}(x,y) = \begin{cases} \dfrac{1}{\pi r^2} & x^2+y^2 \le r^2 \\[4pt] 0 & \text{otherwise} \end{cases}$$

| 부분 | 구할 것 |
|---|---|
| a | 조건부 PDF f_{Y\|X}(y\|x) |
| b | 조건부 기댓값 E[Y \| X = x] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

조건부 PDF 정의는 f_{Y|X}(y|x) = f_{X,Y}(x,y)/f_X(x) (Lecture06, p.18)이므로 **먼저 marginal f_X(x)를 적분으로 구해야** 한다. X=x로 자른 단면에서 y가 어디까지 가능한지(원의 현 길이)가 핵심. b는 그 조건부 분포의 중심이라 대칭성으로 즉답된다 (Lecture08, p.16의 E[Y|X=x]는 숫자).

### 3. 핵심 통찰 (Aha)

> X=x로 원판을 수직 절단하면 단면은 **길이 2√(r²−x²)인 선분 위 균등분포** — 조건부는 그 선분 길이의 역수, 조건부 평균은 선분의 중점 0.

### 4. 풀이 (Worked solution)

**marginal f_X(x).** X=x 고정 시 y는 −√(r²−x²) ≤ y ≤ √(r²−x²) (원 방정식). 그 구간을 적분 (Lecture06, p.31의 marginal):

$$f_X(x) = \int_{-\sqrt{r^2-x^2}}^{\sqrt{r^2-x^2}} \frac{1}{\pi r^2}\,dy = \frac{2\sqrt{r^2-x^2}}{\pi r^2},\quad -r\le x\le r,\qquad \text{otherwise } = 0$$

**(a) 조건부 PDF** (Lecture06, p.18, f_X(x)>0인 |x|<r에서):

$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)} = \frac{1/(\pi r^2)}{2\sqrt{r^2-x^2}/(\pi r^2)} = \frac{1}{2\sqrt{r^2-x^2}}$$

$$f_{Y|X}(y|x) = \begin{cases} \dfrac{1}{2\sqrt{r^2-x^2}} & -\sqrt{r^2-x^2}\le y\le \sqrt{r^2-x^2} \\[4pt] 0 & \text{otherwise} \end{cases}$$

즉 Y | X=x ~ Uniform[−√(r²−x²), √(r²−x²)].

**(b) 조건부 기댓값.** 조건부 분포가 0을 중심으로 대칭인 균등분포이므로:

$$\mathbb{E}[Y\mid X=x] = \int_{-\sqrt{r^2-x^2}}^{\sqrt{r^2-x^2}} y\cdot\frac{1}{2\sqrt{r^2-x^2}}\,dy = 0,\qquad -r<x<r$$

### 5. 검산·직관 (Sanity check)

- 조건부 정규화: 길이 2√(r²−x²) × 높이 1/(2√(r²−x²)) = 1 ✓ (적분=1).
- x→±r 극단: 단면 길이 → 0, 조건부 밀도 → ∞ — 원 가장자리에서 단면이 한 점으로 수렴하니 타당.
- E[Y|X=x]=0: x가 무엇이든 단면이 y=0 대칭(원은 x축 대칭) → 조건부 평균 0, 직관 일치 ✓.

### 6. 한 줄 요약

> 원판 균등분포에서 X=x 단면은 **길이 2√(r²−x²) 선분 위 균등** — 조건부 PDF는 그 길이의 역수 1/(2√(r²−x²)), 조건부 평균은 대칭으로 0이다.
