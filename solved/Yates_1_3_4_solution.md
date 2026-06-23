# Yates 1.3.4 풀이

> 출처: Yates & Goodman PSP, 사용자 첨부 이미지, 1순위 근거 notes/Lecture01_Probabilistic_Model.pdf, 풀이일 2026-06-07

## 문제 원문

Indicate whether each statement is true or false.

(a) If P[A] = 2P[A^c], then P[A] = 1/2.
(b) For all A and B, P[AB] ≤ P[A]P[B].
(c) If P[A] < P[B], then P[AB] < P[B].
(d) If P[A∩B] = P[A], then P[A] ≥ P[B].

---

### 1. 문제 정리 (Setup)

각 명제가 **항상** 성립하는지 판단. 사용할 핵심 도구 (Lecture01, p.13–14):

| 공리/유도 성질 | 출처 |
|---|---|
| A1. P(A) ≥ 0, A2. P(Ω)=1, A3. 서로소면 P(A∪B)=P(A)+P(B) | Lecture01, p.13 |
| 여사건: P(A) = 1 − P(A^c) | Lecture01, p.14 proof 1 |
| 단조성: A⊆B ⟹ P(A) ≤ P(B) | Lecture01, p.14 proof 3 |
| P(∅) = 0 | Lecture01, p.14 proof 2 |

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

네 명제 모두 "공리 3개로부터 유도되는 부등식·등식이 특정 방향으로 강화되는가"를 묻는다. 핵심 전략은 **반례 한 개** 또는 **공리 chain 증명** 중 적합한 것을 고르는 것.

### 3. 핵심 통찰 (Aha)

A∩B ⊆ A ⊆ B 포함관계와 단조성 P(A∩B) ≤ P(A) ≤ P(B) — 이 두 부등식이 (c)·(d) 판단의 전부다.

### 4. 풀이 (Worked solution)

---

**(a) FALSE** — P[A] = 2P[A^c] 이면 P[A] = 2/3, NOT 1/2

여사건 공식 (Lecture01, p.14): P[A^c] = 1 − P[A]:

$$P[A] = 2P[A^c] = 2(1-P[A]) \;\Rightarrow\; 3P[A]=2 \;\Rightarrow\; P[A]=\frac{2}{3}$$

---

**(b) FALSE** — P[AB] ≤ P[A]P[B]는 일반적으로 성립하지 않음

반례: A = B이고 0 < P[A] < 1인 임의의 사건.

P[AB] = P[A∩A] = P[A], P[A]P[B] = P[A]² < P[A] (since P[A] < 1).

따라서 P[AB] = P[A] > P[A]² = P[A]P[B]. 부등호 방향이 반대.

---

**(c) TRUE** — P[A] < P[B] ⟹ P[AB] < P[B]

A∩B ⊆ A 이므로 단조성 (Lecture01, p.14) 적용:

$$P[AB] = P[A\cap B] \le P[A] < P[B]$$

따라서 P[AB] < P[B]. ∎

---

**(d) FALSE** — P[A∩B] = P[A] 이면 P[A] ≤ P[B] (반대 방향)

A∩B ⊆ B 이므로 단조성 (Lecture01, p.14):

$$P[A] = P[A\cap B] \le P[B]$$

즉 옳은 결론은 P[A] ≤ P[B]지, P[A] ≥ P[B]가 아님.

반례: Ω={1,2,3}, 균등확률. A={1}, B={1,2}.
P[A∩B]=P[A]=1/3, P[B]=2/3 → P[A] < P[B].

---

### 5. 검산·직관 (Sanity check)

| 소문항 | 판정 | 핵심 근거 |
|---|---|---|
| (a) | FALSE | 여사건 식 풀면 2/3 나옴 |
| (b) | FALSE | A=B 반례 — 양의 상관이면 곱보다 크다 |
| (c) | TRUE | 단조성: P[AB] ≤ P[A] < P[B] |
| (d) | FALSE | 단조성: A∩B⊆B → P[A]≤P[B], 방향이 반대 |

### 6. 한 줄 요약

> 확률 부등식 문제는 공리 3개(비음·정규화·가산가법)에서 유도된 단조성·여사건 공식으로 chain을 만들거나, 반례 한 개로 끊으면 끝난다.
