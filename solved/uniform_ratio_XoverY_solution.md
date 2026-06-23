# Uniform(0,1) 비율 Z = X/Y 풀이

> 출처: 수업 숙제 Problem 27, 사용자 첨부 이미지, 1순위 근거 Lecture07 (p.12), 풀이일 2026-06-08

## 문제 원문

Let X and Y be two independent Uniform(0,1) random variables, and Z = X/Y. Find the CDF and PDF of Z.

---

### 1. 문제 정리

| 주어진 것 | 구할 것 |
|---|---|
| X, Y ~ Uniform(0,1), 독립 | Z = X/Y의 CDF F_Z(z) |
| f_X(x) = 1 (0 ≤ x ≤ 1), otherwise = 0 | Z의 PDF f_Z(z) |
| f_Y(y) = 1 (0 ≤ y ≤ 1), otherwise = 0 | |

---

### 2. 무엇을 묻고 왜 이 도구인가

Z = g(X,Y) = X/Y 파생분포 문제. 원칙: **무조건 CDF부터 계산하고 미분한다.** (Lecture07, p.10; STT 260518, "첫 번째 뭐부터 계산한다? cdf부터 계산한다")

"X/Y ≤ z"를 단위 정사각형 [0,1]² 위의 기하학적 영역으로 바꾸면 joint density가 1이므로 넓이 계산으로 귀결된다. (Lecture07, p.12)

**범위 먼저:** X ≥ 0, Y > 0이므로 Z ≥ 0. X ≤ 1, Y는 0에 가까워질 수 있으므로 Z는 ∞까지 갈 수 있다. → Z의 지지(support)는 (0, ∞).

---

### 3. 핵심 통찰

P(X/Y ≤ z) = P(X ≤ zY) — 분모 Y > 0이므로 부등호 방향 유지. 이 조건을 단위 정사각형에 그리면 직선 x = zy 아래 영역이고, **z ≤ 1이면 직선이 정사각형 안에 완전히 들어오지만, z > 1이면 직선이 윗변(x=1)을 뚫고 나가므로 구간을 두 조각으로 나눠야 한다.**

---

### 4. 풀이

**z ≤ 0:** F_Z(z) = 0.

---

**0 < z ≤ 1 — 직선 x = zy가 정사각형 안에 완전히 포함**

y ∈ [0,1]에서 x는 0부터 zy까지 (zy ≤ z ≤ 1이므로 상한이 항상 1 이하).

$$F_Z(z) = \int_0^1 \int_0^{zy} 1\,dx\,dy = \int_0^1 zy\,dy = z\cdot\frac{1}{2} = \frac{z}{2}$$

---

**z > 1 — 직선 x = zy가 y = 1/z 이상에서 x = 1을 초과**

y ∈ [0, 1/z)이면 x의 상한 = zy < 1;  
y ∈ [1/z, 1]이면 x의 상한 = 1 (잘림).

$$F_Z(z) = \int_0^{1/z} zy\,dy + \int_{1/z}^{1} 1\,dy$$

$$= z\cdot\frac{1}{2z^2} + \left(1 - \frac{1}{z}\right) = \frac{1}{2z} + 1 - \frac{1}{z} = 1 - \frac{1}{2z}$$

---

**CDF 최종:**

$$F_Z(z) = \begin{cases} \dfrac{z}{2}, & 0 \le z \le 1 \\[6pt] 1 - \dfrac{1}{2z}, & z > 1 \\[4pt] 0, & \text{otherwise} \end{cases}$$

---

**PDF — CDF를 z로 미분:**

$$f_Z(z) = \begin{cases} \dfrac{1}{2}, & 0 \le z \le 1 \\[6pt] \dfrac{1}{2z^2}, & z > 1 \\[4pt] 0, & \text{otherwise} \end{cases}$$

(Lecture07, p.12의 Z = Y/X 예시와 동일 — X, Y가 i.i.d.이므로 대칭)

---

### 5. 검산·직관

**연속성 (z = 1에서 맞닿는지):**
- 좌: F_Z(1) = 1/2, f_Z(1⁻) = 1/2
- 우: F_Z(1) = 1 - 1/2 = 1/2, f_Z(1⁺) = 1/2 ✓

**적분 = 1:**

$$\int_0^1 \frac{1}{2}\,dz + \int_1^\infty \frac{1}{2z^2}\,dz = \frac{1}{2} + \left[-\frac{1}{2z}\right]_1^\infty = \frac{1}{2} + \frac{1}{2} = 1 \checkmark$$

**기대값 주의:** E[Z] = ∫₁^∞ z · 1/(2z²) dz = ∫₁^∞ 1/(2z) dz → **발산(∞)**. Y가 0에 가까울 때 X/Y가 무한히 커지므로 직관과 일치.

---

### 6. 한 줄 요약

> X/Y의 CDF는 "X ≤ zY" 영역을 단위 정사각형에서 적분한 것인데, z ≤ 1과 z > 1 두 케이스로 나눠야 직선 x = zy가 정사각형을 벗어나는 부분을 올바르게 처리할 수 있다.
