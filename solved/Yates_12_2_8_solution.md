# 12.2.8 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 없음(⚠ 강의 밖 — Ch.12 추정/LMSE는 L01–L09 범위 밖), 풀이일 2026-06-16

## 문제 원문

For random variables X and Y, we wish to use Y to estimate X. However, our estimate must be of the form X̂ = aY.

(a) Find a*, the value of a that minimizes the mean square error e = E[(X − aY)²].
(b) For a = a*, what is the minimum mean square error e*?
(c) Under what conditions is X̂ the LMSE estimate of X?

---

> ⚠ 이 문제는 아직 강의 범위 밖 (Ch.12 추정이론, LMSE) — 정리노트(L01–L09: 표본평균·WLLN·CLT까지)에 근거가 없어 일반 교과서 지식으로 풉니다.

### 1. 문제 정리 (Setup)

확률변수 X, Y가 있고, Y로 X를 추정하되 **추정량의 형태가 X̂ = aY로 제한**(상수항 없는 1차, 원점 통과)된다.

| 소문제 | 구할 것 |
|---|---|
| (a) | MSE e = E[(X − aY)²]를 최소화하는 a* |
| (b) | a = a*일 때 최소 MSE e* |
| (c) | X̂ = aY가 LMSE(최적 선형) 추정량이 되는 조건 |

### 2. 무엇을 묻고 왜 이 도구인가

핵심은 **MSE가 a에 대한 2차식**이라는 점이다. e(a)를 전개하면 a에 대해 위로 볼록한 포물선이 되므로, 미분해서 0으로 놓는 한 번의 계산으로 전역 최소가 잡힌다. (a)는 사실상 "포물선 꼭짓점 찾기"다. (c)는 이 제한된 추정량(상수항=0)이 언제 **일반 LMSE 추정량** X̂_L = aY + b와 일치하는지를 묻는다.

### 3. 핵심 통찰 (Aha)

> e(a)는 a의 2차식이므로 de/da = 0이 유일한 최소. 그리고 최적해에서 **추정오차 (X − a*Y)는 Y와 직교**한다 — E[(X − a*Y)Y] = 0 (직교 원리). 이 직교성이 (a)·(b)·(c)를 한 줄로 꿴다.

### 4. 풀이 (Worked solution)

**(a)** MSE를 전개:

$$e(a) = \mathbb{E}[(X-aY)^2] = \mathbb{E}[X^2] - 2a\,\mathbb{E}[XY] + a^2\,\mathbb{E}[Y^2]$$

a에 대해 미분 후 0으로:

$$\frac{de}{da} = -2\,\mathbb{E}[XY] + 2a\,\mathbb{E}[Y^2] = 0 \;\Longrightarrow\; \boxed{a^* = \frac{\mathbb{E}[XY]}{\mathbb{E}[Y^2]}}$$

(d²e/da² = 2E[Y²] ≥ 0 이므로 최소. 이는 곧 직교 조건 E[(X − a*Y)Y] = 0 과 동치.)

**(b)** a*를 대입. 직교성 덕분에 깔끔하게 정리된다:

$$e^* = \mathbb{E}[X^2] - 2a^*\mathbb{E}[XY] + (a^*)^2\mathbb{E}[Y^2] = \mathbb{E}[X^2] - 2\frac{(\mathbb{E}[XY])^2}{\mathbb{E}[Y^2]} + \frac{(\mathbb{E}[XY])^2}{\mathbb{E}[Y^2]}$$

$$\boxed{e^* = \mathbb{E}[X^2] - \frac{(\mathbb{E}[XY])^2}{\mathbb{E}[Y^2]}}$$

**(c)** 일반(아핀) LMSE 추정량은

$$\hat{X}_L = \mu_X + \frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)}\,(Y-\mu_Y) = a_L Y + b_L,\quad a_L=\frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)},\; b_L=\mu_X - a_L\mu_Y$$

X̂ = aY (상수항 b = 0)가 LMSE가 되려면 **최적 아핀 추정량의 상수항이 0**, 즉 b_L = 0이어야 한다:

$$\mu_X = \frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)}\,\mu_Y$$

이때 b_L = 0이면 E[XY] = a_L·E[Y²]가 따라 나와 a* = a_L 도 자동 성립한다. 가장 흔하고 깔끔한 충분조건은 **E[X] = 0 이고 E[Y] = 0** (둘 다 영평균) — 그러면 Cov(X,Y) = E[XY], Var(Y) = E[Y²]가 되어 a* = a_L, b_L = 0 이 모두 만족된다.

$$\boxed{\hat{X}=aY \text{ 가 LMSE } \iff \mu_X = \frac{\mathrm{Cov}(X,Y)}{\mathrm{Var}(Y)}\mu_Y \;\;(\text{특히 } \mathbb{E}[X]=\mathbb{E}[Y]=0 \text{ 이면 항상 성립})}$$

### 5. 검산·직관 (Sanity check)

- **단위/극단**: Y와 X가 무관해 E[XY] = 0이면 a* = 0 → X̂ = 0, e* = E[X²] = X의 평균제곱. Y가 아무 정보를 못 주니 "추정 안 함"이 최선. ✓
- **e* ≥ 0**: 코시–슈바르츠 (E[XY])² ≤ E[X²]E[Y²]에서 e* = E[X²] − (E[XY])²/E[Y²] ≥ 0. 분산은 음수 불가 — 일관됨. ✓
- **직교 확인**: E[(X − a*Y)Y] = E[XY] − a*E[Y²] = E[XY] − E[XY] = 0. ✓ 추정오차가 데이터 Y와 직교 → 더 짜낼 정보 없음.

### 6. 한 줄 요약

> 원점 통과 선형추정 X̂=aY의 최적은 "오차가 Y와 직교"하는 a*=E[XY]/E[Y²]이고, 이것이 곧 LMSE가 되는 건 최적 아핀의 상수항이 사라질 때 — 즉 X·Y가 영평균일 때다.
