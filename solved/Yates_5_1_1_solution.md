# Yates 5.1.1 풀이 — 결합 CDF → 확률·주변 CDF·독립성

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture06 (Continuous RV Part 2) p.12, 풀이일 2026-06-07

## 문제 원문

Random variables X and Y have the joint CDF

$$F_{X,Y}(x,y) = \begin{cases}(1-e^{-x})(1-e^{-y}) & x \ge 0,\ y \ge 0 \\ 0 & \text{otherwise}\end{cases}$$

(a) What is P[X ≤ 2, Y ≤ 3]?  
(b) What is the marginal CDF, F_X(x)?  
(c) What is the marginal CDF, F_Y(y)?

---

### 1. 문제 정리

| | 구할 것 |
|---|---|
| (a) | P[X ≤ 2, Y ≤ 3] |
| (b) | 주변 CDF F_X(x) |
| (c) | 주변 CDF F_Y(y) |

---

### 2. 무엇을 묻고 왜 이 도구인가

결합 CDF F_{X,Y}(x,y) = P(X ≤ x, Y ≤ y) (Lecture06, p.12).

- (a): 좌표 대입 → 바로 확률
- (b)·(c): F_X(x) = lim_{y→∞} F_{X,Y}(x,y), F_Y(y) = lim_{x→∞} F_{X,Y}(x,y)

---

### 3. 핵심 통찰

**결합 CDF에서 한 변수를 ∞로 보내면 그 인수가 1이 되어 소거된다 — 나머지가 주변 CDF.**

---

### 4. 풀이

#### (a) P[X ≤ 2, Y ≤ 3]

$$P[X\le 2,\, Y\le 3] = F_{X,Y}(2,3) = (1-e^{-2})(1-e^{-3}) \approx \boxed{0.821}$$

#### (b) 주변 CDF F_X(x)

$$F_X(x) = \lim_{y\to\infty}(1-e^{-x})(1-e^{-y}) = (1-e^{-x})\cdot 1$$

$$F_X(x) = \begin{cases}1 - e^{-x} & x \ge 0 \\ 0 & \text{otherwise}\end{cases}$$

→ X ~ Exponential(λ = 1)

#### (c) 주변 CDF F_Y(y)

$$F_Y(y) = \lim_{x\to\infty}(1-e^{-x})(1-e^{-y}) = 1\cdot(1-e^{-y})$$

$$F_Y(y) = \begin{cases}1 - e^{-y} & y \ge 0 \\ 0 & \text{otherwise}\end{cases}$$

→ Y ~ Exponential(λ = 1)

#### 보너스: 독립성

F_{X,Y}(x,y) = F_X(x)·F_Y(y) → **X와 Y는 독립**

---

### 5. 검산·직관

- F_X(0)=0, F_X(∞)=1 ✓
- P[X≤2,Y≤3] = P[X≤2]·P[Y≤3] (독립) = (1-e^(-2))(1-e^(-3)) ✓

---

### 6. 한 줄 요약

> 결합 CDF에서 주변 CDF는 한 변수를 ∞로 보내 얻고, 결합 CDF = F_X · F_Y이면 두 RV는 독립이다.
