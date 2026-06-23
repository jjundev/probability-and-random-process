# 12.1.5 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture11 (LMS=조건부 평균 slide 6; 잔여오차=조건부 분산 slide 13–14) + MMSE_조건부평균_유도.md, 풀이일 2026-06-16

## 문제 원문

X, Y have the joint PDF

f_{X,Y}(x,y) = 2 for 0 ≤ x ≤ y ≤ 1, and 0 otherwise.

(a) What is f_{X|Y}(x|y)?
(b) What is x̂_M(y), the MMSE estimate of X given Y = y?
(c) What is e*(0.5) = E[(X − x̂_M(0.5))² | Y = 0.5], the minimum mean square error of the estimate of X given Y = 0.5?

---

### 1. 문제 정리 (Setup)

결합 PDF (12.1.3과 동일):

$$f_{X,Y}(x,y) = \begin{cases} 2, & 0 \le x \le y \le 1,\\[2pt] 0, & \text{otherwise.}\end{cases}$$

| 소문제 | 구할 것 | 정체 |
|---|---|---|
| (a) | f_{X|Y}(x|y) | Y=y 관측 후 X의 조건부 분포 |
| (b) | x̂_M(y) = E[X | Y=y] | LMS(=MMSE) 추정량 |
| (c) | e*(0.5) = E[(X − x̂_M(0.5))² | Y=0.5] | 그 추정의 잔여 MSE = Var(X | Y=0.5) |

여기서 추정 대상 X는 강의노트의 Θ, 관측 Y는 강의노트의 X 역할이다.

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

정리노트 직접 인용:

- (b) "θ̂_LMS = E[Θ | X = x]" — 조건부 MSE를 최소화하는 점추정량은 사후분포의 조건부 평균. (Lecture11, slide 6, 13–14) 그래서 x̂_M(y) = E[X|Y=y].
- (c) "LMS의 실제 MSE = var(Θ|X=x)" — 추정값을 조건부 평균으로 잡았으니 남는 제곱오차는 그 조건부 분포의 분산 그 자체. (Lecture11, slide 13–14) MMSE 유도 노트도 같은 결론: "E[(X−c)²|조건] = Var(X|조건) + (E[X|조건]−c)² → c=조건부평균에서 최소" (MMSE_조건부평균_유도.md, §3).

따라서 (a)에서 조건부 분포만 확정하면 (b)=그 평균, (c)=그 분산.

### 3. 핵심 통찰 (Aha)

> 결합이 상수(균등)면 Y=y로 자른 단면도 균등 → X | Y=y ~ Uniform[0,y]. 그러면 LMS 추정은 중점 y/2, 잔여 MSE는 균등분포 분산 y²/12로 적분 없이 끝.

### 4. 풀이 (Worked solution)

주변밀도:

$$f_Y(y) = \int_0^y 2\,dx = 2y,\quad 0\le y\le 1,\qquad \text{otherwise } f_Y(y)=0.$$

(a) 조건부 PDF = 결합 / 주변 (조건부 밀도 정의):

$$f_{X\mid Y}(x\mid y) = \frac{2}{2y} = \frac{1}{y},\quad 0\le x\le y,\qquad \text{otherwise } 0.$$

x에 무관한 상수 1/y → X | Y=y ~ Uniform[0, y].

(b) LMS 추정량 = 조건부 평균 (Lecture11, slide 6). Uniform[0,y]의 평균 = 중점:

$$\hat{x}_M(y) = E[X\mid Y=y] = \frac{y}{2}.$$

(c) 잔여 MSE = 조건부 분산 (Lecture11, slide 13–14). Uniform[0,a]의 분산 = a²/12, a=0.5:

$$e^*(0.5) = \mathrm{Var}(X\mid Y=0.5) = \frac{(0.5)^2}{12} = \frac{1/4}{12} = \boxed{\frac{1}{48}} \approx 0.0208.$$

### 5. 검산·직관 (Sanity check)

- 조건부 PDF 정규화: ∫₀ʸ (1/y) dx = 1 ✓.
- 추정값 범위: x̂_M(y) = y/2 ∈ [0, y] — 지지구간 중점, 합리적 ✓.
- (c) 직접적분 교차검산: ∫₀^{0.5}(x−0.25)²·(1/0.5)dx = 2·[(x−0.25)³/3]₀^{0.5} = 1/48 ✓.
- 전분산법칙 일관성: E[Var(X|Y)] = ∫₀¹ (y²/12)·2y dy = 1/24 < Var(X) — 관측 Y가 불확실성을 줄였다는 뜻 (Lecture11, "Law of Total Variance") ✓.

### 6. 한 줄 요약

> LMS(=MMSE) 추정은 조건부 평균, 그 잔여오차 e*는 곧 조건부 분산 — 균등 결합에서 X|Y=y ~ Uniform[0,y]라 x̂_M(y)=y/2, e*(0.5)=1/48. (Lecture11, slide 6·13–14)
