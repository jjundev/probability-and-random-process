# Yates 4.4.1 풀이

> 출처: Yates & Goodman PSP, 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

Random variable X has PDF

f_X(x) = 1/4  for -1 ≤ x ≤ 3,  0 otherwise.

Define the random variable Y by Y = h(X) = X².

(a) Find E[X] and Var[X].
(b) Find h(E[X]) and E[h(X)].
(c) Find E[Y] and Var[Y].

---

### 1. 문제 정리 (Setup)

$$f_X(x) = \begin{cases} 1/4, & -1 \le x \le 3 \\ 0, & \text{otherwise} \end{cases}$$

Y = h(X) = X².

| 소문항 | 구할 것 |
|---|---|
| a | E[X], Var[X] |
| b | h(E[X]) 와 E[h(X)] |
| c | E[Y], Var[Y] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

- **(a)**: 기댓값 규칙 직접 적분 (Lecture05, p.7). E[X²]도 같은 방식.
- **(b)**: h(E[X])는 그냥 숫자 대입. E[h(X)]는 기댓값 규칙 E[g(X)] = ∫g(x)f_X(x)dx. **둘이 다름**을 보여주는 게 핵심 — 비선형 g에선 E[g(X)] ≠ g(E[X]) (Jensen).
- **(c)**: Var[Y] = E[Y²] − (E[Y])² 이므로 E[X⁴]까지 필요.

### 3. 핵심 통찰 (Aha)

h(x) = x²는 볼록(convex)이라 h(E[X]) ≤ E[h(X)] — 평균을 먼저 제곱하는 것과, 제곱한 뒤 평균 내는 것은 다르다 (Jensen 부등식).

### 4. 풀이 (Worked solution)

**먼저 공통으로 쓸 적분값들** (Lecture05, p.7):

$$\mathbb{E}[X] = \int_{-1}^{3} x\cdot\frac{1}{4}\,dx = \frac{1}{4}\left[\frac{x^2}{2}\right]_{-1}^{3} = \frac{1}{4}\cdot\frac{9-1}{2} = \frac{1}{4}\cdot 4 = 1$$

$$\mathbb{E}[X^2] = \int_{-1}^{3} x^2\cdot\frac{1}{4}\,dx = \frac{1}{4}\left[\frac{x^3}{3}\right]_{-1}^{3} = \frac{1}{4}\cdot\frac{27-(-1)}{3} = \frac{1}{4}\cdot\frac{28}{3} = \frac{7}{3}$$

$$\mathbb{E}[X^4] = \int_{-1}^{3} x^4\cdot\frac{1}{4}\,dx = \frac{1}{4}\left[\frac{x^5}{5}\right]_{-1}^{3} = \frac{1}{4}\cdot\frac{243-(-1)}{5} = \frac{1}{4}\cdot\frac{244}{5} = \frac{61}{5}$$

---

**(a) E[X] and Var[X]**

$$\mathbb{E}[X] = 1, \qquad \text{Var}[X] = \mathbb{E}[X^2]-(\mathbb{E}[X])^2 = \frac{7}{3}-1 = \boxed{\frac{4}{3}}$$

---

**(b) h(E[X]) vs E[h(X)]**

$$h(\mathbb{E}[X]) = h(1) = 1^2 = \boxed{1}$$

$$\mathbb{E}[h(X)] = \mathbb{E}[X^2] = \boxed{\frac{7}{3} \approx 2.33}$$

h(E[X]) = 1 < 7/3 = E[h(X)] — h(x)=x²가 볼록이므로 Jensen 부등식 방향 ✓.

---

**(c) E[Y] and Var[Y]**

$$\mathbb{E}[Y] = \mathbb{E}[X^2] = \frac{7}{3}$$

$$\mathbb{E}[Y^2] = \mathbb{E}[X^4] = \frac{61}{5}$$

$$\text{Var}[Y] = \mathbb{E}[Y^2]-(\mathbb{E}[Y])^2 = \frac{61}{5}-\left(\frac{7}{3}\right)^2 = \frac{61}{5}-\frac{49}{9}$$

$$= \frac{549}{45}-\frac{245}{45} = \boxed{\frac{304}{45} \approx 6.76}$$

### 5. 검산·직관 (Sanity check)

- f_X 적분: ∫_{−1}^{3} (1/4)dx = (1/4)·4 = 1 ✓
- E[X] = 1: 균등분포 중점 = (−1+3)/2 = 1 ✓
- Var[X] = 4/3: U(a,b) 공식 (b−a)²/12 = 16/12 = 4/3 ✓
- Y = X²는 [0,9] 범위 (x∈[−1,3]), E[Y]=7/3≈2.33, Var[Y]≈6.76 — Y의 범위가 넓어 분산이 큰 게 직관과 일치 ✓

### 6. 한 줄 요약

> E[h(X)]와 h(E[X])는 다르다 — 비선형 h에서 기댓값은 함수 안으로 들어갈 수 없고, 반드시 E[g(X)] = ∫g(x)f_X(x)dx 를 직접 적분해야 한다.
