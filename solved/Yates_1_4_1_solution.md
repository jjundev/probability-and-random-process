# Yates 1.4.1 풀이 — 결합 확률표에서 조건부 확률

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture02 (Conditioning, Bayes Rule, Independence) p.7, 풀이일 2026-06-07

## 문제 원문

Mobile telephones perform handoffs as they move from cell to cell. During a call, a telephone either performs zero handoffs (H0), one handoff (H1), or more than one handoff (H2). In addition, each call is either long (L), if it lasts more than three minutes, or brief (B). The following table describes the probabilities of the possible types of calls.

|   | H0  | H1  | H2  |
|---|-----|-----|-----|
| L | 0.1 | 0.1 | 0.2 |
| B | 0.4 | 0.1 | 0.1 |

(a) What is the probability that a brief call will have no handoffs?  
(b) What is the probability that a call with one handoff will be long?  
(c) What is the probability that a long call will have one or more handoffs?

---

### 1. 문제 정리

결합 확률표 (행·열 합 추가):

|   | H0 | H1 | H2 | 행 합 |
|---|---|---|---|---|
| L | 0.1 | 0.1 | 0.2 | 0.4 |
| B | 0.4 | 0.1 | 0.1 | 0.6 |
| 열 합 | 0.5 | 0.2 | 0.3 | 1.0 |

---

### 2. 무엇을 묻고 왜 이 도구인가

조건부 확률 (Lecture02, p.7):

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

분모 = 행·열 합(주변 확률), 분자 = 셀 값.

---

### 3. 핵심 통찰

**조건부 확률 = 해당 행(또는 열)으로 세계를 좁힌 뒤 비율을 재계산 — 분모는 행·열 합, 분자는 셀 값.**

---

### 4. 풀이

#### (a) P(H0 | B)

$$P(H_0 \mid B) = \frac{P(H_0 \cap B)}{P(B)} = \frac{0.4}{0.6} = \boxed{\frac{2}{3} \approx 0.667}$$

#### (b) P(L | H1)

$$P(L \mid H_1) = \frac{P(L \cap H_1)}{P(H_1)} = \frac{0.1}{0.2} = \boxed{\frac{1}{2} = 0.5}$$

#### (c) P(H1 ∪ H2 | L)

H1, H2는 서로소이므로:

$$P(H_1 \cup H_2 \mid L) = \frac{P(L \cap H_1) + P(L \cap H_2)}{P(L)} = \frac{0.1 + 0.2}{0.4} = \boxed{\frac{3}{4} = 0.75}$$

---

### 5. 검산·직관

- P(H0|L) + P(H1∪H2|L) = 0.25 + 0.75 = 1 ✓
- (a): B 행 중 H0가 압도적(0.4/0.6) ✓

---

### 6. 한 줄 요약

> 조건부 확률은 표의 해당 행·열로 세계를 좁힌 뒤 비율을 재계산 — 분모는 행·열 합, 분자는 셀 값.
