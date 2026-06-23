# 확률론적 모델 (Probabilistic Model)

> 출처: notes/Lecture01_Probabilistic_Model.pdf

## 1. 핵심 정의

- **확률론적 모델 (Probabilistic Model)**: 불확실한 상황을 수학적으로 기술하는 모델. 두 요소(표본 공간 + 확률 법칙)로 구성됨. (Lecture01, p.6)
- **표본 공간 (Sample Space, Omega)**: 관심 있는 모든 결과의 집합. 세 조건 필수. (Lecture01, p.8)
  - (1) 상호 배타적 (Mutually exclusive)
  - (2) 전체 망라 (Collectively exhaustive)
  - (3) 적절한 세분도 (Right granularity) — 너무 구체적이지도, 너무 추상적이지도 않게
- **사건 (Event)**: 표본 공간 Omega의 부분집합. 확률은 개별 원소가 아닌 사건에 부여됨. (Lecture01, p.10)
- **확률 법칙 (Probability Law) P(·)**: 각 사건(Omega의 부분집합)에 숫자를 할당하는 함수. (Lecture01, p.6, p.10)

## 2. 주요 공식 / 정리

**확률 공리 Version 1 — 유한 가산** (Lecture01, p.13)

```
A1. 비음성 (Nonnegativity):     P(A) >= 0,  모든 사건 A에 대해
A2. 정규화 (Normalization):     P(Omega) = 1
A3. 유한 가산성 (Finite add.):  A, B 서로소 => P(A U B) = P(A) + P(B)
```

**확률 공리 Version 2 — 가산 가산** (Lecture01, p.18)

```
A1, A2 동일
A3. 가산 가산성 (Countable add.):
    A1, A2, A3, ... 가 서로소인 무한 사건 수열이면,
    P(A1 U A2 U ...) = P(A1) + P(A2) + ...
```

**공리로부터 유도되는 성질** (Lecture01, p.14)

```
(i)  P(A) <= 1
     증명: 1 = P(Omega) = P(A U A^c) = P(A) + P(A^c) >= P(A)  [A1]

(ii) P(empty) = 0
     증명: P(Omega U empty) = P(Omega) + P(empty) = 1 + P(empty)
           => P(empty) = 0  [(i)와 A2]

(iii) A subset B => P(A) <= P(B)
     증명: P(B) = P(A) + P(B\A) >= P(A)  [A3, A1]
```

## 3. 핵심 예시

**예시 1: 세분도에 따른 표본 공간 설계** (Lecture01, p.8)

- 동전 던지기에서 H/T 확률만 알고 싶다면:
  `Omega = {H, T}`
- 날씨(비/맑음)가 동전에 미치는 영향까지 분석하고 싶다면:
  `Omega = {(H,R), (T,R), (H,NR), (T,NR)}`
- 핵심: 답하고 싶은 질문에 맞는 세분도로 Omega를 설계해야 함.

**예시 2: 유한 가산성의 한계 — 무한 표본 공간** (Lecture01, p.16)

- `Omega = {1,2,3,...}`, `P({n}) = 1/2^n`
- P(짝수) = P({2,4,6,...}) = 1/4 + 1/16 + ... = 1/3 을 구하고 싶지만,
  유한 가산 공리(Version 1)는 무한합을 허용하지 않으므로 이 계산은 부당함.
- 따라서 무한/연속 표본 공간에는 **가산 가산성(Version 2)**이 반드시 필요.

## 4. 자주 헷갈리는 포인트

- `Omega = {H, T, HT}`는 상호 배타성 위반 — "HT"는 동시에 H이자 T이므로 불가. (Lecture01, p.8)
- `Omega = {H}`는 전체 망라성 위반 — T가 빠져 있음. (Lecture01, p.8)
- 확률 법칙은 **개별 결과(outcome)가 아닌 사건(부분집합)**에 부여된다. 연속 표본 공간에서 특정 점 하나의 확률은 0일 수 있음. (Lecture01, p.10)
- Version 1(유한 가산)으로는 무한 개 사건의 합산 불가 → 무한/연속 표본 공간에서는 Version 2 사용. (Lecture01, p.16~18)

## 5. 시험 / 응용 관점

- **확률 계산 4단계**: ① 표본 공간 설정 → ② 확률 법칙 지정 → ③ 관심 사건 식별 → ④ 계산. (Lecture01, p.15)
- 3개 공리만으로 `P(A)<=1`, `P(empty)=0`, 단조성 등 모든 성질을 증명하는 문제 출제 가능. 각 등호/부등호에 어떤 공리(A1/A2/A3)를 사용했는지 명시하는 것이 핵심. (Lecture01, p.14)
- 가산 가산성이 왜 필요한지 (무한 표본 공간 예시와 함께) 설명할 수 있어야 함. (Lecture01, p.16~18)
