# Yates 2.2.1 풀이 — 다항계수: P[R₂Y₂G₂B₂]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture03 (Discrete RV Part 1) p.11 이항계수 → 다항계수로 확장 (⚠ 강의 범위 밖), 풀이일 2026-06-07

## 문제 원문

On each turn of the knob, a gumball machine is equally likely to dispense a red, yellow, green or blue gumball, independent from turn to turn. After eight turns, what is the probability P[R₂Y₂G₂B₂] that you have received 2 red, 2 yellow, 2 green and 2 blue gumballs?

---

### 1. 문제 정리

각 턴: R/Y/G/B 각 확률 1/4, 독립. 8턴 후 P[R₂Y₂G₂B₂] = ?

---

### 2. 무엇을 묻고 왜 이 도구인가

> ⚠ 다항계수는 강의 정리노트에 없어 Lecture03 이항계수 공식(p.11)을 4결과로 일반화해 유도합니다.

---

### 3. 핵심 통찰

**"특정 순서 하나의 확률 × 그 순서 가짓수" — 순서별 확률은 독립성으로, 가짓수는 자리 배분으로 센다.**

---

### 4. 풀이

**Step 1 — 특정 순서 하나의 확률**

$$\left(\frac{1}{4}\right)^8 = \frac{1}{65536}$$

**Step 2 — 가짓수 (다항계수)**

$$\binom{8}{2}\binom{6}{2}\binom{4}{2}\binom{2}{2} = 28 \times 15 \times 6 \times 1 = \frac{8!}{2!\,2!\,2!\,2!} = 2520$$

**Step 3 — 곱**

$$P[R_2 Y_2 G_2 B_2] = \frac{2520}{65536} = \boxed{\frac{315}{8192} \approx 0.0385}$$

---

### 5. 검산·직관

- 4^8 = 65536, 유리한 경우 2520 → 2520/65536 < 1 ✓
- 4색 균등 배분은 드문 사건 → 약 3.85% ✓

---

### 6. 한 줄 요약

> 다항계수 8!/(2!2!2!2!) = 2520이 "색깔 배분 방법 수"이고, 여기에 각 순서의 확률 (1/4)^8을 곱하면 끝이다.
