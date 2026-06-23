# Lecture 12 — 통계적 추론 Part 3 (LLMS · ML Estimator)

> 출처: notes/Lecture12_Statistical_Inference_Part_3_rev.pdf, STT/260615_Lecture12_Statistical_Inference_Part_3.txt

## 1. 핵심 정의

- **LMS estimator (복습)**: 미지수 Θ를 prior f_Θ(·)로 모델링, 관측 X=x이고 모델 f_{X|Θ}(x|θ)일 때, 조건부 MSE `E[(Θ−θ̂)²|X=x]`를 최소화하는 추정량. (Lecture12, p.5)
- **LLMS (Linear LMS) estimator**: 일반 추정량 g(X) 대신 **g(X)=aX+b 형태(선형)**로만 제약한 LMS 추정량. 최적성을 일부 포기하는 대신 단순·실용적 설계를 택함. (Lecture12, p.6; STT 260615, "리니어하게만 추론해봐")
- **Classical(고전적) inference**: 미지수 θ를 **deterministic(랜덤 아님) 상수**로 봄 → prior·posterior 확률이 없음. 관측 X의 분포는 θ에만 의존하며 `p_X(x;θ)`, `f_X(x;θ)`로 표기. (Lecture12, p.12; STT 260615, "디터미니스틱한 어떤 퀀터티")
- **Likelihood**: 파라미터가 θ일 때 관측값 x가 나타날 확률 `p_X(x₁,…,xₙ;θ)`. (Lecture12, p.14)
- **ML (Maximum Likelihood) estimator**: likelihood를 최대화하는 θ. 즉 `θ̂_ML = argmax_θ p_X(x₁,…,xₙ;θ)`. (Lecture12, p.14; STT 260615, "데이터만 믿어")

## 2. 주요 공식 / 정리

- **LMS 최적해**: `θ̂ = E[Θ|X=x]`, 추정량 `Θ̂ = E[Θ|X]`. 관측이 없으면 `θ̂=E[Θ]`이고, 이때 달성 가능한 최소 MSE = var(Θ). (Lecture12, p.5; STT 260615, "평균으로 퉁치는 게 가장 지혜로운")
- **LLMS 해 (★시험 암기)**: (Lecture12, p.7; STT 260615, "그냥 외우세요 … 기말고사 볼 때는 그냥 저거 써놓으세요")
  ```
  Θ̂_L = E(Θ) + [cov(Θ,X)/var(X)] · (X − E(X))
       = E(Θ) + ρ·(σ_Θ/σ_X) · (X − E(X)),   ρ = cov(Θ,X)/(σ_Θ σ_X)
  ```
  여기서 a = cov(Θ,X)/var(X), b = E(Θ) − a·E(X) 역할.
- **분포 불필요**: Θ, X의 평균·분산·공분산만 알면 LLMS 설계 가능 (전체 분포 불필요). (Lecture12, p.7)
- **LLMS의 MSE**: `E[(Θ̂_L − Θ)²] = (1 − ρ²)·var[Θ]`. ρ²∈[0,1]이므로 관측 후 불확실성은 항상 (1−ρ²)배로 **감소**. (Lecture12, p.8; STT 260615, "데이터를 받으면 받을수록 줄어드는")
- **ML 로그우도**: Xᵢ가 독립이면 `argmax_θ Σ_{i=1}^n log p_{Xᵢ}(xᵢ;θ)` 최대화와 동치 (곱→합으로 단순화). (Lecture12, p.14; STT 260615, "익스포넌트를 떼 버리려고 log")
- **ML ↔ MAP 관계**: `θ̂_MAP = argmax_θ [p_{X|Θ}(x|θ)·p_Θ(θ)/p_X(x)]`. **Θ가 uniform(완전 무지)이면 MAP == ML**. 즉 Bayesian이 classical ML을 포함. (Lecture12, p.15; STT 260615, "베이지안이 ML을 다 포함")

## 3. 핵심 예시 (2개)

- **예1) 편향 동전 + Uniform prior**: Θ~U[0,1] (E[Θ]=1/2, var[Θ]=1/12), n번 던져 앞면 X회, `p_{X|Θ}(k|θ)~Binomial(n,θ)` (그 외 k에서 = 0). LTV·반복기대값으로 E[X]=n/2, var(X)=n(n+2)/12, cov(Θ,X)=n/12 계산 → `Θ̂_L = (X+1)/(n+2)`. 이는 LMS 결과와 **동일**(Θ̂_LMS도 (X+1)/(n+2)) — LMS 해가 원래 선형 꼴이었기 때문. (참고: Θ̂_MAP = X/n.) (Lecture12, p.10; STT 260615, "동일할 수밖에 없는")
- **예2) 지수분포 파라미터 ML 추정**: 독립·동일 X₁,…,Xₙ ~ exp(θ), `f_X(x;θ)=θe^{−θx}` (x≥0), `=0` (x<0, otherwise). 로그우도 `n log θ − θΣxᵢ`를 θ로 미분=0 → `θ̂_ML = n / Σ_{i=1}^n xᵢ`. (Lecture12, p.16; STT 260615, "데이터만 보고")

## 4. 자주 헷갈리는 포인트

- **ρ>0 vs ρ=0**: ρ>0이면 baseline E[Θ] + 보정항(X>E[X]→Θ̂_L>E[Θ]). ρ=0(무상관)이면 데이터 무용, Θ̂_L=E[Θ]뿐. (Lecture12, p.7)
- **|ρ|=1**: MSE=0 (완벽 추정). X와 Θ가 상수배 관계라 X 관측 시 Θ를 정확히 앎. (Lecture12, p.8; STT 260615, "완벽한 추정")
- **LMS vs LLMS 혼동 주의**: LMS는 일반 함수 E[Θ|X](적분 필요), LLMS는 aX+b로 제약. 예1처럼 LMS 해가 우연히 선형이면 둘이 같아짐 — 항상 같은 건 아님. (STT 260615, "리니어 꼬라지였기 때문에")
- **classical에서 ; 표기**: `p_X(x;θ)`의 세미콜론은 θ가 파라미터(상수)임을 뜻하나, Bayesian의 조건부 `p_{X|Θ}(x|θ)`와 값은 대응됨. (Lecture12, p.15; STT 260615, "찰떡같이 그냥 기본 컨디션")

## 5. 시험 / 응용 관점

- **출제 1순위**: LLMS 공식 `Θ̂_L = E(Θ)+ρ(σ_Θ/σ_X)(X−E(X))`와 MSE `(1−ρ²)var[Θ]` — 교수가 "외워서 써놓으라"고 명시. (STT 260615)
- 편향 동전(Uniform prior) 예제 흐름(LTV로 var(X)·cov 계산 → Θ̂_L 도출)과 지수분포 ML 도출(로그우도 미분)은 전형적 계산 문항. (Lecture12, p.10, p.16)
- 공분산은 estimation theory에서 핵심: X가 Θ와 얼마나 상관있느냐가 관측으로 줄일 수 있는 불확실성의 양을 결정. (STT 260615, "코베리언스가 굉장히 중요한 역할")
