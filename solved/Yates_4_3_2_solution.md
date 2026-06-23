# Yates 4.3.2 풀이

> 출처: Yates & Goodman PSP, 사용자 첨부 이미지, 1순위 근거 Lecture05_Continuous_RV_Part_1, 풀이일 2026-06-07

## 문제 원문

The cumulative distribution function of random variable X is

F_X(x) = 0          for x < -1
F_X(x) = (x+1)/2   for -1 ≤ x < 1
F_X(x) = 1          for x ≥ 1

Find the PDF f_X(x) of X.

---

### 1. 문제 정리 (Setup)

$$F_X(x) = \begin{cases} 0, & x < -1 \\ \dfrac{x+1}{2}, & -1 \le x < 1 \\ 1, & x \ge 1 \end{cases}$$

구할 것: PDF f_X(x).

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

연속 RV에서 CDF와 PDF의 관계 (Lecture05, p.10):

$$f_X(x) = \frac{dF_X}{dx}(x)$$

구간마다 F_X(x)를 x로 미분하면 끝.

### 3. 핵심 통찰 (Aha)

F_X(x) = (x+1)/2 는 x에 대해 선형 — 기울기가 상수 1/2 이므로 PDF는 그 구간 전체에서 균일하다.

### 4. 풀이 (Worked solution)

구간별로 미분 (Lecture05, p.10):

- x < −1: F_X = 0 (상수) → f_X = 0
- −1 ≤ x < 1: F_X = (x+1)/2 → f_X = d/dx[(x+1)/2] = 1/2
- x ≥ 1: F_X = 1 (상수) → f_X = 0

$$\boxed{f_X(x) = \begin{cases} \dfrac{1}{2}, & -1 \le x < 1 \\ 0, & \text{otherwise} \end{cases}}$$

이는 X ~ Uniform(−1, 1) 의 PDF다.

### 5. 검산·직관 (Sanity check)

$$\int_{-1}^{1} \frac{1}{2}\,dx = \frac{1}{2}\cdot 2 = 1 \;\checkmark$$

F_X(x) = ∫_{−∞}^x f_X(t)dt = ∫_{−1}^x (1/2)dt = (x+1)/2 (−1≤x<1) → 원래 CDF 복원 ✓

### 6. 한 줄 요약

> CDF의 선형 구간은 기울기가 곧 PDF — 미분 한 번으로 균등분포임이 드러난다.
