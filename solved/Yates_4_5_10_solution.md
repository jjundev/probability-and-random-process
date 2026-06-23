# Yates 4.5.10 풀이 — Uniform(−5,5): PDF·CDF·E[X]·E[X^5]·E[e^X]

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture05 (Continuous RV Part 1) p.7, 풀이일 2026-06-07

## 문제 원문

X is a continuous uniform (−5, 5) random variable.

(a) What is the PDF f_X(x)?  
(b) What is the CDF F_X(x)?  
(c) What is E[X]?  
(d) What is E[X^5]?  
(e) What is E[e^X]?

---

### 1. 문제 정리

X ~ Uniform(−5, 5), a = −5, b = 5, b−a = 10

| | 구할 것 |
|---|---|
| (a) | PDF f_X(x) |
| (b) | CDF F_X(x) |
| (c) | E[X] |
| (d) | E[X^5] |
| (e) | E[e^X] |

---

### 2. 무엇을 묻고 왜 이 도구인가

(a)·(b)·(c)는 균등분포 공식 직접 적용 (Lecture05, p.7).  
(d)·(e)는 기댓값 법칙 E[g(X)] = ∫ g(x) f_X(x) dx (Lecture05, p.7). (d)는 홀함수 대칭 논리로 적분 없이, (e)는 e^x 적분.

---

### 3. 핵심 통찰

**X^5는 홀함수(odd function), [−5,5]는 원점 대칭 구간 → 적분이 0. e^X는 짝함수가 아니어서 직접 적분해야 한다.**

---

### 4. 풀이

#### (a) PDF

$$\boxed{f_X(x) = \frac{1}{10}, \quad -5 \le x \le 5, \qquad \text{otherwise } = 0}$$

#### (b) CDF

$$F_X(x) = \begin{cases} 0 & x < -5 \\ \dfrac{x+5}{10} & -5 \le x \le 5 \\ 1 & x > 5 \end{cases}$$

#### (c) E[X]

$$E[X] = \frac{a+b}{2} = \frac{-5+5}{2} = \boxed{0}$$

#### (d) E[X^5]

x^5는 홀함수, [−5,5]는 원점 대칭 → ∫_{-5}^{5} x^5 dx = 0

$$\boxed{E[X^5] = 0}$$

(원점 대칭 균등분포에서 모든 홀수 차수 모멘트 = 0)

#### (e) E[e^X]

$$E[e^X] = \frac{1}{10}\int_{-5}^{5} e^x\,dx = \frac{1}{10}\left[e^x\right]_{-5}^{5} = \frac{e^5 - e^{-5}}{10} = \frac{\sinh 5}{5} \approx \boxed{14.84}$$

---

### 5. 검산·직관

- F_X(−5) = 0, F_X(5) = 1 ✓
- 홀함수 논리: 모든 홀수 차수 모멘트 E[X^(2k+1)] = 0 (원점 대칭 균등분포 공통) ✓
- e^(−5) ≈ 0.007로 거의 0 → E[e^X] ≈ e^5/10 ≈ 14.84 ✓

---

### 6. 한 줄 요약

> 균등분포 기댓값은 E[g(X)] = (1/(b−a)) ∫_a^b g(x) dx — g가 홀함수이고 구간이 원점 대칭이면 적분 없이 0, 그 외에는 직접 계산한다.
