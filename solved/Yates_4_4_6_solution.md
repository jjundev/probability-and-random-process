# Yates 4.4.6 풀이

> 출처: Yates & Goodman PSP, 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

The cumulative distribution function of random variable V is

F_V(v) = 0               for v < -5
F_V(v) = (v+5)²/144     for -5 ≤ v < 7
F_V(v) = 1               for v ≥ 7

(a) What are E[V] and Var[V]?
(b) What is E[V³]?

---

### 1. 문제 정리 (Setup)

$$F_V(v) = \begin{cases} 0, & v < -5 \\ \dfrac{(v+5)^2}{144}, & -5 \le v < 7 \\ 1, & v \ge 7 \end{cases}$$

| 소문항 | 구할 것 |
|---|---|
| a | E[V], Var[V] |
| b | E[V³] |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

CDF가 주어졌으니 **먼저 미분해 PDF를 얻고**, 그다음 기댓값 규칙 E[g(V)] = ∫g(v)f_V(v)dv 를 쓴다 (Lecture05, p.10, p.7). 치환 u = v+5 로 적분 범위를 [0,12]로 바꾸면 계산이 훨씬 깔끔해진다.

### 3. 핵심 통찰 (Aha)

(v+5)²/144 를 미분하면 f_V(v) = (v+5)/72 — 구간 [−5,7]에서 단조 증가하는 삼각형 PDF이므로 u=v+5 치환 하나로 모든 적분이 ∫₀¹² u^k/72 du 꼴로 통일된다.

### 4. 풀이 (Worked solution)

**Step 0 — PDF 도출** (Lecture05, p.10)

$$f_V(v) = \frac{dF_V}{dv} = \begin{cases} \dfrac{v+5}{72}, & -5 \le v < 7 \\ 0, & \text{otherwise} \end{cases}$$

검증: ∫_{−5}^{7} (v+5)/72 dv = [(v+5)²/144]_{−5}^{7} = 144/144 = 1 ✓

---

**u = v+5 치환** (u ∈ [0,12], v = u−5):

$$\mathbb{E}[U^k] = \int_0^{12} u^k \cdot \frac{u}{72}\,du = \frac{1}{72}\cdot\frac{u^{k+2}}{k+2}\Bigg|_0^{12} = \frac{12^{k+2}}{72(k+2)}$$

| k | E[U^k] | 값 |
|---|---|---|
| 1 | 12³/(72·3) | 1728/216 = 8 |
| 2 | 12⁴/(72·4) | 20736/288 = 72 |
| 3 | 12⁵/(72·5) | 248832/360 = 3456/5 |

---

**(a) E[V] and Var[V]**

V = U − 5 이므로 선형 변환 공식 (Lecture05, p.7):

$$\mathbb{E}[V] = \mathbb{E}[U] - 5 = 8 - 5 = \boxed{3}$$

$$\mathbb{E}[V^2] = \mathbb{E}[(U-5)^2] = \mathbb{E}[U^2] - 10\mathbb{E}[U] + 25 = 72 - 80 + 25 = 17$$

$$\text{Var}[V] = \mathbb{E}[V^2] - (\mathbb{E}[V])^2 = 17 - 9 = \boxed{8}$$

---

**(b) E[V³]**

$$\mathbb{E}[V^3] = \mathbb{E}[(U-5)^3] = \mathbb{E}[U^3] - 15\mathbb{E}[U^2] + 75\mathbb{E}[U] - 125$$

$$= \frac{3456}{5} - 15\cdot72 + 75\cdot8 - 125 = \frac{3456}{5} - 1080 + 600 - 125$$

$$= \frac{3456}{5} - 605 = \frac{3456 - 3025}{5} = \boxed{\frac{431}{5} = 86.2}$$

### 5. 검산·직관 (Sanity check)

- E[V]=3: PDF가 단조 증가라 질량이 오른쪽으로 쏠림 → 중점 (−5+7)/2=1 보다 오른쪽인 3이 맞다 ✓
- Var[V]=8: 범위 12, 균등분포라면 Var=144/12=12 — 삼각 PDF는 중심부 밀도가 낮아 분산이 더 작은 게 직관과 일치 ✓
- E[V³]=86.2 > (E[V])³=27: 분포가 양수 방향으로 치우쳐 있어 양수값이 나오는 것이 자연스럽다 ✓

### 6. 한 줄 요약

> CDF를 미분해 PDF를 얻은 뒤 u=v+5 치환으로 적분 범위를 [0,12]로 통일하면, 모든 모멘트가 u^k 거듭제곱 공식 하나로 해결된다.
