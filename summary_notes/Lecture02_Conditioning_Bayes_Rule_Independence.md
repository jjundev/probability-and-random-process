# 조건부 확률 · 베이즈 룰 · 독립

> 출처: notes/Lecture02_Conditioning_Bayes_Rule_Independence.pdf, STT/260311_Lecture02_Conditioning.txt, STT/260316_Lecture02_Bayes_Rule_Independence.txt, STT/260318_Lecture02_Conditioning_Bayes_Rule_Independence.txt

---

## 1. 핵심 정의

- **조건부 확률 (Conditional Probability)**: P(A|B) = P(A∩B) / P(B),  단 P(B) > 0.
  이것은 theorem이 아닌 **definition**이다. 단순히 P(A∩B)로 정의하면 P(Ω|B) = P(B) ≠ 1이 되어 Axiom 2를 위반하므로, P(B)로 나누어 정규화한다. (Lecture02, p.7; STT 260311, "컨디셔널 프로배빌리티는 정의되는 개념")

- **통계적 독립 (Statistical Independence)**: A ⊥ B  iff  P(A∩B) = P(A) × P(B).
  동치 조건: P(B|A) = P(B). 대칭 관계이다. (Lecture02, p.19; STT 260318, "인디펜던스")

- **조건부 독립 (Conditional Independence)**: A ⊥ B | C  iff  P(A∩B|C) = P(A|C) × P(B|C).
  C가 주어진 세계 안에서의 독립이다. (Lecture02, p.20; STT 260318, "컨디셔널 인디펜던스")

---

## 2. 주요 공식 / 정리

**곱셈 법칙 (Multiplication Rule)**
```
P(A∩B) = P(A) · P(B|A) = P(B) · P(A|B)
```
일반화 (n개):
```
P(A1∩A2∩...∩An) = P(A1) · P(A2|A1) · P(A3|A1,A2) · ... · P(An|A1,...,An-1)
```
(Lecture02, p.11; STT 260311, "멀티플리케이션 룰")

**전체 확률 정리 (Total Probability Theorem)**

{A1, A2, ..., An}이 Ω의 partition일 때:
```
P(B) = Σ_i  P(Ai) · P(B|Ai)
```
P(B)를 각 원인 Ai에 대한 가중 평균으로 분해한다. (Lecture02, p.12; STT 260311, "토탈 프로배빌리티")

**베이즈 룰 (Bayes' Rule)**
```
P(Ai|B) = P(Ai) · P(B|Ai)  /  Σ_j P(Aj) · P(B|Aj)
```
- 분자 = prior × forward probability (likelihood)
- 분모 = P(B) (total probability로 계산)
- 목적: **역방향 확률** P(Ai|B)를 **순방향 확률** P(B|Ai)로 표현. (Lecture02, p.13; STT 260316, "리버스 프로배빌리티를 포워드로")

**다중 사건의 독립 (Independence of n Events)**

A1, ..., An이 독립  iff  모든 부분집합 S ⊆ {1,...,n}에 대해:
```
P( ∩_{i∈S} Ai ) = Π_{i∈S} P(Ai)
```
쌍별 독립(pairwise independence)만으로는 충분하지 않다. (Lecture02, p.23; STT 260318, "모든 서브셋")

---

## 3. 핵심 예시

**예시 1: Airplane-Radar** (Lecture02, p.14; STT 260316, "비행기 레이더")

- Prior: P(A) = 0.05  (비행기 있을 사전 확률)
- Forward: P(B|A) = 0.99,  P(B|Aᶜ) = 0.10
- P(B) = P(A)·P(B|A) + P(Aᶜ)·P(B|Aᶜ) = 0.05×0.99 + 0.95×0.10 = 0.0495 + 0.095 = **0.1445**
- P(A|B) = 0.0495 / 0.1445 ≈ **0.34**

해석: 레이더가 반응해도 실제 비행기일 확률은 34%뿐. 사전 확률이 낮으면 posterior도 낮다.

**예시 2: Happy/Sad-Shout** (Lecture02, p.15; STT 260316, "해피 쌔드")

- P(A1=Happy) = 0.7,  P(B=Shout|Happy) = 0.3
- P(A2=Sad) = 0.3,    P(B=Shout|Sad)   = 0.5
- P(B) = 0.7×0.3 + 0.3×0.5 = 0.21 + 0.15 = **0.36**
- P(A1|B) = 0.21/0.36 ≈ **0.583**,   P(A2|B) = 0.15/0.36 ≈ **0.417**

해석: 소리를 질렀을 때 행복할 확률이 사전(0.7)보다 낮아졌다 (0.583). 슬픔이 소리 지르는 원인으로 더 가능성 있다는 정보가 반영된 것.

---

## 4. 자주 헷갈리는 포인트

- **Disjoint ≠ Independent**: A∩B = ∅이면 P(A∩B) = 0이지만 P(A)·P(B) > 0이므로 독립이 아니다.
  오히려 반대—A가 일어났다는 정보가 B의 발생을 완전히 배제한다. (Lecture02, p.19; STT 260318)

- **A ⊥ B  →  A ⊥ B|C? NO**: 반례: H1, H2 = 공정한 동전의 두 번 던지기. C = "두 결과가 다름".
  P(H1∩H2|C) = 0  ≠  P(H1|C)·P(H2|C) = (1/2)·(1/2). 조건화가 독립을 깰 수 있다. (Lecture02, p.21; STT 260318, "Q1 카운터이그잼플")

- **A ⊥ B|C  →  A ⊥ B? NO**: 반례: Blue coin (P(H)=0.9), Red coin (P(H)=0.1)을 균등 선택.
  동전 종류 C가 주어지면 H1 ⊥ H2|C이지만, C를 모를 때 P(H1∩H2) = 0.41 ≠ 0.25. (Lecture02, p.22; STT 260318, "Q2 카운터이그잼플")

- **P(B|A) ≠ P(A|B) 일반적으로**: 베이즈 룰의 존재 이유가 바로 이 비대칭성을 역산하기 위함이다. (STT 260316, "리버스")

---

## 5. 시험 / 응용 관점

- **Bayesian Inference 계산 순서**: ① Prior P(Ai) 설정 → ② Forward P(B|Ai) 모델링 → ③ Total Probability로 P(B) 계산 → ④ Bayes' Rule로 Posterior P(Ai|B) 산출. (Lecture02, p.10; STT 260316)

- **조건부 독립의 실용**: Markov 성질, 통신 채널 모델, Naive Bayes 분류기 등에서 핵심 가정. A ⊥ B|C와 A ⊥ B의 방향 혼동에 주의. (Lecture02, p.20–22; STT 260318)
