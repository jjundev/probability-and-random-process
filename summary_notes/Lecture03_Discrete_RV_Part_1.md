# 이산 확률변수 Part I (Discrete Random Variables Part I)

> 출처: notes/Lecture03_Discrete_RV_Part_1.pdf, STT/260325_Lecture03_Discrete_RV_Part_1.txt, STT/260330_Lecture03_Discrete_RV_Part_1.txt

## 1. 핵심 정의

- **확률변수 (RV) X**: 샘플 스페이스 Omega의 원소를 실수 R로 매핑하는 함수. (Lecture03, p.6)
  - 표기: 대문자 X = RV 자체, 소문자 x = 구체적 숫자 값
  - 같은 샘플 스페이스에서 여러 RV를 자유롭게 정의할 수 있음
- **이산 확률변수 (Discrete RV)**: 취할 수 있는 값이 유한 또는 가산 무한개인 RV. (Lecture03, p.6)
- **PMF (확률 질량 함수)**:
  `pX(x) = P(X=x) = P({ omega in Omega | X(omega) = x })` (Lecture03, p.6)
  - pX(x)는 RV X의 "정체(statistical behavior)"를 완전히 기술함 (STT 260330, "PMF를 알면 RV의 정체를 다 안다")
- **Indicator RV**: 이벤트 A에 대해
  `1_A = 1 (A 발생), 0 (otherwise = 0)` (Lecture03, p.9)

## 2. 주요 공식 / 정리

### 유명한 이산 RV PMF (모두 otherwise = 0)

- **Bernoulli(p)**, p in [0,1]:
  ```
  pX(0) = 1-p
  pX(1) = p
  otherwise = 0
  ```
  이진 결과 모델링 (성공/실패, head/tail). (Lecture03, p.9)

- **Uniform(a, b)**, integers a <= b:
  ```
  pX(i) = 1/(b-a+1),  i in {a, a+1, ..., b}
  otherwise = 0
  ```
  완전한 무지(complete ignorance) 상황 모델링. (Lecture03, p.10)

- **Binomial(n, p)**: n번 독립 Bernoulli 시행에서 성공 횟수
  ```
  pX(k) = C(n,k) * p^k * (1-p)^(n-k),  k = 0, 1, ..., n
  otherwise = 0
  ```
  C(n,k) = n! / (k!(n-k)!). (Lecture03, p.11)

- **Geometric(p)**: 첫 번째 성공까지의 시행 횟수
  ```
  pX(k) = (1-p)^(k-1) * p,  k = 1, 2, 3, ...
  otherwise = 0
  ```
  대기 시간(waiting time) 모델링. (Lecture03, p.12)

### 기댓값 (Expectation / Mean)

- **정의**: `E[X] = sum_x  x * pX(x)` (Lecture03, p.14)
- **기본 성질**: (Lecture03, p.15)
  - X >= 0  =>  E[X] >= 0
  - a <= X <= b  =>  a <= E[X] <= b
  - E[c] = c (상수의 기댓값은 자기 자신)

### 함수의 기댓값 & 선형성

- Y = g(X)도 RV이고: `E[g(X)] = sum_x  g(x) * pX(x)` (Lecture03, p.16)
- **선형성**: `E[aX + b] = a*E[X] + b` (Lecture03, p.16)
  (증명: Expectation은 linear operator이므로 상수 분리 가능)

### 분산 (Variance) & 표준편차

- **정의**: `var[X] = E[(X - mu)^2]`,  mu = E[X] (Lecture03, p.17)
- **표준편차**: `sigma_X = sqrt(var[X])`
- **계산 공식**: `var[X] = E[X^2] - (E[X])^2`  (제곱의 평균 빼기 평균의 제곱) (Lecture03, p.18; STT 260330, "제곱의 평균 빼기 평균의 제곱")
- **이동 불변**: Y = X + b  =>  `var[Y] = var[X]`  (평균만 이동, 퍼짐 불변) (Lecture03, p.18)
- **스케일**: Y = aX  =>  `var[Y] = a^2 * var[X]` (Lecture03, p.18)

### Joint PMF & 다중 RV

- **Joint PMF**: `pX,Y(x,y) = P({X=x} ∩ {Y=y})`;  sum_x sum_y pX,Y(x,y) = 1 (Lecture03, p.20)
- **Marginal PMF**:
  - `pX(x) = sum_y  pX,Y(x,y)` (y를 marginalize)
  - `pY(y) = sum_x  pX,Y(x,y)` (Lecture03, p.20)
- **Z = g(X,Y)의 PMF**: `pZ(z) = sum_{(x,y): g(x,y)=z}  pX,Y(x,y)` (Lecture03, p.21)
- **E[g(X,Y)]**: `= sum_x sum_y  g(x,y) * pX,Y(x,y)` (Lecture03, p.21)
- **다중 RV 선형성**: `E[X+Y] = E[X] + E[Y]`  (독립 여부 무관) (Lecture03, p.22)
  - 일반화: `E[X1 + ... + Xn] = E[X1] + ... + E[Xn]`

## 3. 핵심 예시

### 예시 1: Binomial 평균을 선형성으로 유도
- Binomial(n,p)를 따르는 Y = X1 + ... + Xn, 각 Xi는 Bernoulli(p)
- `E[Y] = n * E[Xi] = n * p = np` (Lecture03, p.22; STT 260325, "바이노미얼 랜덤 베리어블의 평균")
- 핵심: 복잡한 RV를 단순한 Bernoulli 합으로 분해하는 trick

### 예시 2: Bernoulli(p) 분산 계산
- mu = E[X] = p  (X in {0,1}이므로 0*pX(0) + 1*pX(1) = p)
- E[X^2] = 0^2*(1-p) + 1^2*p = p  (X^2 = X for X in {0,1})
- `var[X] = E[X^2] - mu^2 = p - p^2 = p(1-p)` (Lecture03, p.18)

## 4. 자주 헷갈리는 포인트

- **PMF는 반드시 otherwise = 0**: Bernoulli/Uniform/Binomial/Geometric 모두 범위 밖에서는 pX(x) = 0. 이를 명시하지 않으면 정의 불완전.
- **음수사원 원칙**: P(X=x)를 계산할 때 항상 "X(omega)=x가 되려면 원래 omega는 무엇이었어야 하나"로 거슬러 올라갈 것. (STT 260325, "음수사원해야 돼")
- **var[X+b] = var[X]**: 상수를 더해도 분산은 변하지 않음 (PMF가 단순 이동). 평균만 b만큼 이동.
- **E[X+Y] = E[X]+E[Y]**는 독립 여부와 무관하게 항상 성립; 반면 var[X+Y] = var[X]+var[Y]는 독립 조건이 필요.

## 5. 시험 / 응용 관점

- PMF 4종(Bernoulli, Uniform, Binomial, Geometric)의 공식과 적용 상황을 구분하여 암기 필요.
  - Bernoulli: 1회 이진 시행; Binomial: n회 반복; Geometric: 첫 성공까지 대기.
- 기댓값 선형성(E[X+Y]=E[X]+E[Y])은 복잡한 RV를 Bernoulli 합으로 분해하는 핵심 도구 — Binomial 평균 np 유도가 대표적.
- Joint PMF → Marginal PMF 변환(marginalization)은 다중 RV 문제의 기본 연산.
