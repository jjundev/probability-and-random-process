# Yates 4.5.2 풀이 — Uniform(−10,10): P[|Y| < 3]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture05 (Continuous RV Part 1) p.7, 풀이일 2026-06-07

## 문제 원문

The current Y across a 1 kΩ resistor is a continuous uniform (−10, 10) random variable. Find P[|Y| < 3].

---

### 1. 문제 정리

Y ~ Uniform(−10, 10). 구할 것: P[|Y| < 3]

$$f_Y(y) = \frac{1}{20}, \quad -10 \le y \le 10, \qquad \text{otherwise } = 0$$

---

### 2. 무엇을 묻고 왜 이 도구인가

절댓값 부등식을 일반 부등식으로 풀고, 균등분포의 구간 길이 비율로 계산. (Lecture05, p.7)

---

### 3. 핵심 통찰

**|Y| < 3 ⟺ −3 < Y < 3** — 절댓값을 벗기면 대칭 구간이 되고, 균등분포에서 확률은 길이 비율.

---

### 4. 풀이

$$P[|Y| < 3] = P[-3 < Y < 3] = \frac{3-(-3)}{10-(-10)} = \frac{6}{20} = \boxed{\frac{3}{10}}$$

---

### 5. 검산·직관

[-10, 10] 전체 길이 20 중 [-3, 3] 구간 길이 6 → 비율 6/20 = 0.3 ✓  
대칭 분포에서 중앙 30% — 직관과 일치.

---

### 6. 한 줄 요약

> |Y| < c는 −c < Y < c로 벗기고, 균등분포 확률은 구간 길이 비율로 끝낸다.
