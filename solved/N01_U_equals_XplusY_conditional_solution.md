# Problem 28 풀이 — 독립 N(0,1), U=X+Y 조건부 분포

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture06 (조건부 PDF·Bayes)·Lecture07 (Normal+Normal=Normal)·Lecture08 (조건부 기댓값·분산), 풀이일 2026-06-09

## 문제 원문

Let X and Y be two independent N(0,1) random variables, and U = X + Y.

a. Find the conditional PDF of U given X = x, f_{U|X}(u|x).
b. Find the PDF of U, f_U(u).
c. Find the conditional PDF of X given U = u, f_{X|U}(x|u).
d. Find E[X|U = u], and Var(X|U = u).

---

### 1. 문제 정리 (Setup)

X, Y ~ N(0,1) 독립, U = X + Y.

| 파트 | 구할 것 |
|------|---------|
| (a) | f_{U|X}(u|x) |
| (b) | f_U(u) |
| (c) | f_{X|U}(x|u) |
| (d) | E[X|U=u], Var(X|U=u) |

---

### 2. 무엇을 묻고 왜 이 도구인가

(a)→(b)→(c)→(d) 순서가 핵심 체계다.

- **(a)**: X=x 고정 → U = x+Y, Y의 단순 이동. (Lecture06, p.18)
- **(b)**: 독립 정규합 → Normal+Normal=Normal 직접 적용. (Lecture07, p.18)
- **(c)**: f_{U|X}와 f_X를 알았으니 **연속형 Bayes 정리**로 역추론. (Lecture06, p.22)
- **(d)**: (c)가 Gaussian이면 파라미터에서 바로 읽힌다. (Lecture08, p.16, p.21)

---

### 3. 핵심 통찰 (Aha)

X=x를 고정하면 U는 N(x, 1)이고, 역방향 f_{X|U}는 Bayes 공식 후 지수부를 x에 대해 **완전제곱** 한 번으로 N(u/2, 1/2)이 나온다 — 조건부도 Gaussian.

---

### 4. 풀이 (Worked solution)

**[a] f_{U|X}(u|x)**

X = x로 고정되면 U = x + Y이고 Y ~ N(0,1)이므로 U|X=x 는 Y를 x만큼 이동:

$$f_{U|X}(u \mid x) = \frac{1}{\sqrt{2\pi}}\,e^{-(u-x)^2/2}, \quad u \in \mathbb{R}$$

(Gaussian은 전 실수에서 양수 — otherwise 없음.) (Lecture06, p.5, p.18)

---

**[b] f_U(u)**

X ~ N(0,1), Y ~ N(0,1) 독립이므로 Normal+Normal 정리 적용: (Lecture07, p.18)

$$U = X+Y \;\sim\; \mathcal{N}(0+0,\;1+1) = \mathcal{N}(0,\,2)$$

$$f_U(u) = \frac{1}{\sqrt{4\pi}}\,e^{-u^2/4},\quad u \in \mathbb{R}$$

---

**[c] f_{X|U}(x|u)**

연속형 Bayes 정리 (Lecture06, p.22):

$$f_{X|U}(x \mid u) = \frac{f_{U|X}(u \mid x)\cdot f_X(x)}{f_U(u)}$$

**분자** 계산:

$$f_{U|X}(u|x)\cdot f_X(x) = \frac{1}{\sqrt{2\pi}}e^{-(u-x)^2/2}\cdot\frac{1}{\sqrt{2\pi}}e^{-x^2/2} = \frac{1}{2\pi}\,e^{-\frac{(u-x)^2+x^2}{2}}$$

지수부 전개:

$$-\frac{(u-x)^2+x^2}{2} = -\frac{u^2-2ux+2x^2}{2} = -\frac{u^2}{2}+ux-x^2$$

분모 f_U(u) = (1/(2√π)) e^(-u²/4)로 나누면:

$$f_{X|U}(x \mid u) = \frac{1/(2\pi)}{1/(2\sqrt\pi)}\cdot e^{\left(-\frac{u^2}{2}+ux-x^2\right)+\frac{u^2}{4}} = \frac{1}{\sqrt\pi}\cdot e^{-x^2+ux-\frac{u^2}{4}}$$

지수부를 x에 대해 **완전제곱**:

$$-x^2+ux-\frac{u^2}{4} = -\!\left(x-\frac{u}{2}\right)^2$$

따라서:

$$f_{X|U}(x \mid u) = \frac{1}{\sqrt{\pi}}\,e^{-(x-u/2)^2},\quad x \in \mathbb{R}$$

이는 N(u/2, 1/2)의 PDF이다 (σ² = 1/2이면 1/(σ√(2π)) = 1/((1/√2)·√(2π)) = 1/√π ✓).

---

**[d] E[X|U=u], Var(X|U=u)**

(c)에서 X|U=u ~ N(u/2, 1/2)이므로: (Lecture08, p.16, p.21)

$$E[X \mid U = u] = \frac{u}{2}$$

$$\text{Var}(X \mid U = u) = \frac{1}{2}$$

---

### 5. 검산·직관 (Sanity check)

1. **적분 = 1**: ∫ (1/√π) e^(-(x-u/2)²) dx = (1/√π)·√π = 1 ✓ (Gaussian 적분 ∫ e^(-t²) dt = √π)
2. **대칭성 논증**: X와 Y는 동일분포 독립 → E[X|U=u] = E[Y|U=u]. 두 값의 합 = E[U|U=u] = u이므로 E[X|U=u] = u/2 ✓
3. **분산 감소**: Var(X) = 1 → Var(X|U=u) = 1/2 — U 관측이 불확실성을 절반으로 줄임 ✓
4. **특수값** u=0: E[X|U=0] = 0 = E[X] — U=0은 대칭 조건이므로 X의 사전 평균과 동일 ✓
5. **Gaussian 폐쇄성**: (X,Y) 독립 정규 → (X, U=X+Y) 공동 정규 → 조건부도 정규. (Lecture07, p.18)

---

### 6. 한 줄 요약

> X|U=u는 N(u/2, 1/2) — "독립 N(0,1)의 합을 알면 각 성분의 조건부 분포는 Bayes 완전제곱 한 번으로 자동으로 Gaussian이 된다."
