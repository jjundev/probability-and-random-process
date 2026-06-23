# Binomial, Geometric, Negative Binomial 정리

## 1. 핵심 비교표

| 분포 | 고정된 것 | 랜덤인 것 | 확률변수의 의미 | PMF | 핵심 질문 |
|---|---|---|---|---|---|
| Binomial | 시행 횟수 `n` | 성공 횟수 `X` | `n`번 시행 중 성공이 몇 번 나오는가 | \(\displaystyle P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}\) | "정해진 횟수 안에 성공이 몇 번?" |
| Geometric | 첫 성공 1번 | 첫 성공까지의 시행 횟수 `X` | 처음 성공이 몇 번째 시행에서 나오는가 | \(\displaystyle P(X=x)=(1-p)^{x-1}p,\; x=1,2,3,\dots\) | "처음 성공까지 몇 번?" |
| Negative Binomial | 성공 횟수 `r` | `r`번째 성공까지의 시행 횟수 `X` | `r`번째 성공이 몇 번째 시행에서 나오는가 | \(\displaystyle P(X=x)=\binom{x-1}{r-1}p^r(1-p)^{x-r},\; x=r,r+1,\dots\) | "`r`번째 성공까지 몇 번?" |

---

## 2. 한눈에 구별하는 법

### Binomial

- 시행 횟수 `n`이 처음부터 정해져 있다.
- 그 안에서 성공이 몇 번 나오는지를 센다.

예:

- 동전을 10번 던져 앞면이 몇 번 나오는가
- 20명의 학생 중 시험 합격자가 몇 명인가

---

### Geometric

- 성공이 처음 나올 때까지 계속한다.
- 처음 성공까지 몇 번 걸리는지를 센다.

예:

- 처음 앞면이 나올 때까지 동전을 몇 번 던지는가
- 첫 번째 불량품이 나올 때까지 몇 개를 검사하는가

---

### Negative Binomial

- 성공이 `r`번 나올 때까지 계속한다.
- `r`번째 성공까지 몇 번 걸리는지를 센다.

예:

- 6번째 정답자가 나올 때까지 몇 명에게 질문하는가
- 5번째 승리가 나올 때까지 몇 경기를 하는가

---

## 3. Geometric은 Negative Binomial의 특수한 경우

Geometric distribution은 성공 횟수 `r=1`인 negative binomial이라고 볼 수 있다.

즉,

- Geometric: 첫 성공까지
- Negative Binomial: `r`번째 성공까지

이다.

---

## 4. 문제를 보면 무엇을 먼저 확인해야 하는가

문제를 보면 아래 순서로 확인하면 된다.

1. 시행 횟수가 미리 정해져 있는가?
2. 아니면 성공이 나올 때까지 계속하는가?
3. 성공이 1번 나올 때까지인가, `r`번 나올 때까지인가?

이 질문에 따라 분포가 정해진다.

---

## 5. 빠른 판별 규칙

- "총 10번 중 몇 번 성공?" -> Binomial
- "처음 성공까지 몇 번?" -> Geometric
- "6번째 성공까지 몇 번?" -> Negative Binomial

---

## 6. 3.3.14에 적용

문제 `3.3.14`에서는

- 각 전화가 성공할 확률 `p=0.75`
- `L` = 6번째로 생일을 아는 사람이 나올 때까지 필요한 총 전화 수

이므로 `L`은

\[
L \sim \text{Negative Binomial}(r=6,\; p=0.75)
\]

이다.

즉, 이 문제는 Binomial 문제가 아니라 Negative Binomial 문제이다.

다만 (c)에서

"처음 8번 전화 안에 성공이 몇 번 나왔는가?"

를 따로 보면, 그 횟수는

\[
X \sim \text{Binomial}(8,0.75)
\]

로 볼 수 있다.

그래서 `3.3.14`는 본질적으로는 negative binomial 문제이고, 일부 계산에서만 binomial을 보조적으로 사용할 수 있다.

---

## 7. 시험장에서 헷갈릴 때 쓰는 한 줄 요약

- Binomial: 횟수 고정, 성공 개수 셈
- Geometric: 첫 성공까지의 횟수
- Negative Binomial: `r`번째 성공까지의 횟수

---

## 8. 자주 하는 실수

### 실수 1. 성공 확률 `p`만 보고 바로 Binomial이라고 생각하기

성공/실패 구조가 있다고 해서 항상 binomial은 아니다.  
무엇이 고정되어 있는지를 먼저 봐야 한다.

### 실수 2. "몇 번째 성공" 문제를 Binomial로 처리하기

"몇 번째 성공"은 보통 geometric 또는 negative binomial이다.

### 실수 3. Negative Binomial과 Geometric을 완전히 다른 분포로 외우기

Geometric은 negative binomial의 `r=1`인 특별한 경우로 보면 훨씬 기억하기 쉽다.
