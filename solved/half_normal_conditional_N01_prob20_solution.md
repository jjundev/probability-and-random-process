# Problem 20 풀이 — N(0,1) 조건부 분포 (X > 0)

> 출처: 사용자 첨부 이미지, 1순위 근거 Lecture06 (Continuous RV Part 2), 풀이일 2026-06-07

## 문제 원문

Let X ~ N(0,1).

a. Find the conditional PDF and CDF of X given X > 0.  
b. Find E[X | X > 0].  
c. Find Var(X | X > 0).

---

### 1. 문제 정리

X ~ N(0,1). 표준정규 PDF: φ(x) = (1/√(2π))e^(-x²/2), CDF: Φ(x) = ∫₋∞^x φ(t) dt. (Lecture06, p.5)

| | 구할 것 |
|---|---|
| (a) | 조건부 PDF f_{X|X>0}(x) 및 CDF F_{X|X>0}(x) |
| (b) | E[X | X > 0] |
| (c) | Var(X | X > 0) |

---

### 2. 무엇을 묻고 왜 이 도구인가

사건 A = {X > 0}에 조건화된 연속 RV의 분포 문제. 핵심 공식 (Lecture06, p.13):

$$f_{X|\{X\in C\}}(x) = \frac{f_X(x)}{P(X \in C)}, \quad x \in C, \qquad \text{otherwise } = 0$$

분모 P(X > 0)만 계산하면 조건부 PDF가 즉시 나온다. 조건부 기댓값·분산은 이 PDF로 적분.

---

### 3. 핵심 통찰

**X > 0으로 자르면 N(0,1)의 오른쪽 절반만 남는다 — 밀도를 2배 스케일해 면적을 다시 1로 만든 것이 조건부 PDF다.**

---

### 4. 풀이

#### (a) 조건부 PDF와 CDF

N(0,1)의 대칭성에 의해:

$$P(X > 0) = \frac{1}{2}$$

공식 대입 (C = (0, ∞)):

$$f_{X|X>0}(x) = \frac{\varphi(x)}{1/2} = 2\varphi(x) = \frac{2}{\sqrt{2\pi}}\,e^{-x^2/2}, \quad x > 0, \qquad \text{otherwise } = 0$$

조건부 CDF — x > 0에서:

$$F_{X|X>0}(x) = P(X \le x \mid X > 0) = \frac{P(0 < X \le x)}{P(X > 0)} = \frac{\Phi(x) - \Phi(0)}{1/2} = 2\Phi(x) - 1$$

$$F_{X|X>0}(x) = \begin{cases} 2\Phi(x) - 1 & x > 0 \\ 0 & x \le 0 \end{cases}$$

---

#### (b) E[X | X > 0]

$$E[X \mid X>0] = \int_0^{\infty} x \cdot 2\varphi(x)\,dx = \frac{2}{\sqrt{2\pi}}\int_0^{\infty} x\,e^{-x^2/2}\,dx$$

치환: u = x²/2, du = x dx:

$$= \frac{2}{\sqrt{2\pi}}\int_0^{\infty} e^{-u}\,du = \frac{2}{\sqrt{2\pi}} \cdot 1$$

$$\boxed{E[X \mid X>0] = \sqrt{\frac{2}{\pi}} \approx 0.7979}$$

---

#### (c) Var(X | X > 0)

Var = E[X² | X>0] − (E[X | X>0])². 먼저 E[X² | X>0]:

$$E[X^2 \mid X>0] = \int_0^{\infty} x^2 \cdot 2\varphi(x)\,dx = 2\int_0^{\infty} x^2\,\varphi(x)\,dx$$

N(0,1)에서 E[X²] = Var(X) = 1이고, x²φ(x)는 우함수이므로:

$$\int_0^{\infty} x^2\,\varphi(x)\,dx = \frac{1}{2}$$

따라서 E[X² | X>0] = 2 · (1/2) = 1.

$$\text{Var}(X \mid X>0) = 1 - \left(\sqrt{\frac{2}{\pi}}\right)^2 = 1 - \frac{2}{\pi}$$

$$\boxed{\text{Var}(X \mid X>0) = 1 - \frac{2}{\pi} \approx 0.3634}$$

---

### 5. 검산·직관

- **CDF 경계**: F_{X|X>0}(0) = 2·(1/2)−1 = 0 ✓, x→∞이면 2·1−1 = 1 ✓
- **조건부 PDF 정규화**: ∫₀^∞ 2φ(x)dx = 2·(1/2) = 1 ✓
- **분산 감소 직관**: X > 0으로 자르면 분포가 [0,∞)에 집중되어 퍼짐이 줄어든다. Var = 1−2/π ≈ 0.36 < Var(X) = 1 ✓
- **기댓값 직관**: E[X] = 0이지만 X > 0 조건이면 양수쪽에 쏠리니 E[X|X>0] ≈ 0.8 > 0 ✓

---

### 6. 한 줄 요약

> 사건 A에 조건화된 PDF는 f_X를 P(A)로 나눠 재정규화한 것 — N(0,1)을 X>0으로 자르면 밀도가 2배, 분산은 1에서 1−2/π로 줄어든다.
