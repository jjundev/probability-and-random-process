# Discrete Random Variables Part 2: 조건부 PMF · 기억 없는 성질 · 독립

> 출처: notes/Lecture04_Discrete_RV_Part_2.pdf, STT/260406_Lecture04_Discrete_RV_Part_2.txt, STT/260408_Lecture04_Discrete_RV_Part_3.txt

---

## 1. 핵심 정의

- **조건부 PMF (이벤트 A 조건)**:
  ```
  p_{X|A}(x) = P(X = x | A)
  ```
  (Lecture04, slide 5)

- **조건부 PMF (RV Y 조건)**:
  ```
  p_{X|Y}(x|y)  =  P(X = x | Y = y)  =  p_{X,Y}(x,y) / p_Y(y),   p_Y(y) > 0인 y에 대해
  sum_x p_{X|Y}(x|y) = 1  (정규화)
  ```
  (Lecture04, slide 8)

- **조건부 기댓값 · 분산**:
  ```
  E[X|A]      = sum_x  x * p_{X|A}(x)
  E[g(X)|A]   = sum_x  g(x) * p_{X|A}(x)
  var[X|A]    = E[X^2|A] - (E[X|A])^2
  ```
  A 자리에 {Y=y}를 넣으면 → E[X|Y=y], var[X|Y=y]로 확장 (Lecture04, slides 5,7)

- **Memoryless Property**:
  ```
  X가 memoryless  ⟺  P(X > n+m | X > m) = P(X > n),  for any n, m >= 0
  ```
  등가 표현: P(X-m > n | X > m) = P(X > n)  
  직관: "과거(X > m)를 잊어버리고 0에서 다시 시작한 것과 동일"  
  (Lecture04, slide 15; STT 260406, "이거는 데피니션이니까 외워도 돼요")

- **두 RV의 독립**:
  ```
  X ⊥ Y  ⟺  p_{X,Y}(x,y) = p_X(x) · p_Y(y),  for ALL x, y
  ```
  조건부 독립 (Z=z 조건):
  ```
  p_{X,Y|Z}(x,y|z) = p_{X|Z}(x|z) · p_{Y|Z}(y|z),  for ALL x, y
  ```
  (Lecture04, slide 19; STT 260406, "모든 x, 모든 y에 대해서")

---

## 2. 주요 공식 · 정리

- **Multiplication Rule**:
  ```
  p_{X,Y}(x,y)   = p_Y(y) · p_{X|Y}(x|y)  =  p_X(x) · p_{Y|X}(y|x)
  p_{X,Y,Z}(x,y,z) = p_X(x) · p_{Y|X}(y|x) · p_{Z|X,Y}(z|x,y)
  ```
  (Lecture04, slide 8)

- **Total Expectation Theorem (TET)**:
  ```
  {A_i}가 Omega를 partition할 때:  E[X] = sum_i P(A_i) · E[X|A_i]
  RV Y로 partition:                 E[X] = sum_y p_Y(y) · E[X|Y=y]
  ```
  직관: 각 그룹의 조건부 평균을 그룹 확률로 가중평균 (Lecture04, slides 11-12; STT 260406, "1학년 평균, 2학년 평균 … weighted sum")

- **Geometric RV PMF 및 평균**:
  ```
  P(X = k) = (1-p)^(k-1) · p,   k = 1, 2, 3, ...
  P(X = k) = 0,                  otherwise
  P(X > k) = (1-p)^k
  E[X] = 1/p
  ```
  (Lecture04, slides 16-17)

- **독립 RV의 기댓값 · 분산**:
  ```
  항상 성립:   E[X+Y] = E[X] + E[Y]
  항상 성립:   var[aX] = a^2·var[X],   var[X+a] = var[X]
  X ⊥ Y 일 때만:  E[XY] = E[X]·E[Y]
  X ⊥ Y 일 때만:  E[g(X)h(Y)] = E[g(X)]·E[h(Y)]
  X ⊥ Y 일 때만:  var[X+Y] = var[X] + var[Y]
  ```
  증명 핵심:
  ```
  var[X+Y] = var[X] + var[Y] + 2(E[XY] - E[X]E[Y])
  ```
  X ⊥ Y이면 마지막 항 = 0 (Lecture04, slides 21-22; STT 260406, "통계적으로 독립일 때는 이게 성립해요")

---

## 3. 핵심 예시

### 예시 1 — Geometric RV 평균 (TET + Memorylessness)
- 상황: 확률 p로 성공. X = 성공까지의 시도 횟수. E[X]=?
- A_1 = {X=1} (첫 번째 성공), A_2 = {X>1} (첫 번째 실패)
  ```
  E[X] = 1 + E[X-1]
       = 1 + P(A_1)·E[X-1|X=1] + P(A_2)·E[X-1|X>1]   [TET]
       = 1 + p·0               + (1-p)·E[X]            [memorylessness]
  => p·E[X] = 1  =>  E[X] = 1/p
  ```
  (Lecture04, slide 17; STT 260406, "토탈 익스펙테이션 띄어람을 쓸 건데")

### 예시 2 — Hat Problem
- 상황: n명이 모자를 넣고 눈 감고 뽑기. X = 자기 모자 뽑은 사람 수.
- 분해: X_i = 1 (i번째 사람이 자기 모자 뽑음), 0 (아니면) → X = sum_{i=1}^{n} X_i
- {X_i}: identically distributed (대칭), **but NOT independent** (2명일 때 X_1=1 ⟹ X_2=1)
  ```
  E[X]   = n · E[X_1] = n · (1/n) = 1   (n에 무관)
  E[X_i^2] = 1/n
  E[X_i·X_j] = P(X_i=1)·P(X_j=1|X_i=1) = (1/n)·(1/(n-1))
  E[X^2] = n·E[X_1^2] + n(n-1)·E[X_1·X_2]
          = n·(1/n)   + n(n-1)·1/(n(n-1))  = 1 + 1 = 2
  var[X] = E[X^2] - (E[X])^2 = 2 - 1 = 1   (n에 무관)
  ```
  (Lecture04, slides 23-24; STT 260408, "배리언스 계산하면 2에서 1 뺀 1")

---

## 4. 자주 헷갈리는 포인트

- **var[X+Y] = var[X]+var[Y]는 X ⊥ Y일 때만**: X=Y이면 var[X+Y]=var[2X]=4var[X]이므로 틀림. X=-Y이면 var[X+Y]=0. (Lecture04, slide 22)
- **Hat problem: X_i들은 identical하지만 NOT independent**: n=2이면 X_1=1 → X_2=1로 완전 의존. var[X]를 구할 때 독립 가정을 쓰면 틀림. (Lecture04, slide 24; STT 260408, "통계적으로 독립이 아니야")
- **독립 체크**: 모든 (x,y)에 대해 joint=marginal 곱이어야 함. 하나라도 다르면 not independent. (Lecture04, slide 20; STT 260406, "하나만 달라도 다른 거야")
- **E[XY]=E[X]E[Y]는 독립의 필요조건이 아님**: 이 등식이 성립해도 독립이 아닐 수 있음 (covariance=0 ≠ 독립). (Lecture04, slide 22)

---

## 5. 시험·응용 관점

- **TET + Memorylessness 콤보**: 직접 계산이 복잡한 RV 평균은, 첫 번째 시도를 {성공}/{실패}로 파티션 → TET 적용 → memoryless 성질로 재귀 방정식 수립 → 풀기. Geometric RV 평균이 대표 사례. (STT 260406, "메모리 리스 프로퍼티를 갖고 있다라는 걸 써먹으면 돼요")
- **Indicator RV 분해**: 카운팅 문제는 X = sum X_i로 분해하고 E의 선형성으로 평균 계산. X_i가 identical하면 대표 하나만 계산하면 됨 (hat problem 기법). var 계산 시에는 독립 여부 반드시 확인 후 진행.
