# 통계적 추론 II: 점추정량 (MAP · LMS)

> 출처: notes/Lecture11_Statistical_Inference_Part_2.pdf, STT/260610_Lecture11_Statistical_Inference_Part_2.txt
> 베이지안 추론의 결론은 사후분포(PDF/PMF) 자체. 이번 강의는 그 사후분포에서 "값 하나"를 뽑는 두 점추정량 MAP·LMS를 다룸. (Lecture11, slide 5; STT 260610, "결론이 PDF")

## 1. 핵심 정의
- **점추정(Point estimate)**: 사후분포가 주어졌을 때 관측 x에 대해 단 하나의 값 θ를 추론 결과로 선택. (요약·단순 답을 요구받는 상황) (Lecture11, slide 5)
- **추정값(estimate) vs 추정량(estimator)**: estimate `θ̂ = g(x)`는 관측 인스턴스 x를 수로 보내는 사상; estimator `Θ̂ = g(X)`는 랜덤변수 X를 받으므로 그 자체가 랜덤변수. (Lecture11, slide 7; STT 260610, "에스티메이터는 함수다")
- **MAP 추정량 (Maximum A Posteriori)**: 사후 PMF/PDF를 최대로 만드는 θ = "가장 강한 믿음을 가진 값". (Lecture11, slide 6; STT 260610, "Largest PMF")
- **LMS 추정량 (Least Mean Squares)**: 사후분포의 조건부 평균. (Lecture11, slide 6; STT 260610, "모르겠고 그냥 평균")

## 2. 주요 공식 / 정리

**두 점추정량 정의** (Lecture11, slide 6)
```
θ̂_MAP = argmax_θ p_{Θ|X}(θ|x)   (이산)   /   argmax_θ f_{Θ|X}(θ|x)   (연속)
θ̂_LMS = E[Θ | X = x]            (조건부 기댓값)
```

**MAP 최적성** — 주어진 x에서 오결정 확률 `P(θ̂≠Θ|X=x)`를 최소화(Claim 1)하고, x에 대해 평균낸 전체 오결정 확률 `P(Θ̂≠Θ)`도 최소화(Claim 2). (Lecture11, slide 9–10; STT 260610, "틀릴 확률을 미니마이즈")
```
증명 골자: E[I|X=x] = P[g(X)=Θ|X=x] ≤ P[g_MAP(X)=Θ|X=x] = E[I_MAP|X=x]
          → 반복기대법칙(law of iterated expectations)으로 평균까지 확장
```
(I = 올바른 결정의 지시함수) (Lecture11, slide 10)

**LMS 최적성** — 조건부 MSE `E[(Θ-θ̂)²|X=x]`를 최소화하는 값은 `θ̂ = E[Θ|X=x]`. (Lecture11, slide 13–14)
```
E[(Θ-θ̂)²] = var(Θ) + (E[Θ] - θ̂)²    → 둘째 항을 0으로 만드는 θ̂ = E[Θ]에서 최소
```
- 분해 근거는 Law of Total Variance. LMS의 실제 MSE = `var(Θ|X=x)`, x에 대해 평균내면 `E[var(Θ|X)]`. (Lecture11, slide 13–14; STT 260610, "Law of Total Variance")

**명명 분포 / 켤레성** (모두 명시 구간 밖은 0)
- Beta prior: `f_Θ(θ) = θ^(α-1)(1-θ)^(β-1) / B(α,β)`, 0 ≤ θ ≤ 1; **otherwise = 0**. (Lecture11, slide 8; STT 260610, "베타 프라이어")
- Binomial 우도: `p_{X|Θ}(k|θ) = C(n,k) θ^k (1-θ)^(n-k)`, k = 0,1,…,n; **otherwise = 0**. (Lecture11, slide 8; STT 260610, "n번 던져 k번")
- **켤레성(conjugacy)**: `Θ ~ Beta(α,β)`이고 n번 중 k번 head면 `Θ|{X=k} ~ Beta(k+α, n-k+β)`. 사후분포도 Beta꼴:
  `f_{Θ|X}(θ|k) ∝ θ^(α+k-1)(1-θ)^(β+n-k-1)`, 0 ≤ θ ≤ 1; **otherwise = 0**. (Lecture11, slide 8; STT 260610, "포스테리어도 베타")

## 3. 핵심 예시 (1~2개)

**(1) Bent coin + Beta prior — MAP vs LMS** (Lecture11, slide 8, 15)
- 상황: n번 던져 k번 head, prior `Beta(α,β)`.
- MAP: 사후 PDF에 log 취해(단조증가라 argmax 불변) 미분=0 →
  `θ̂_MAP = (α+k-1)/(α+β-2+n)`. α=β=1(U[0,1] prior)이면 `k/n`. (STT 260610, "미분해서 0")
- LMS: `E[Θ|X=k] = (k+α)/(α+β+n)`. α=β=1이면 `(k+1)/(n+2)`.
- 둘은 다를 수 있음(분포의 peak ≠ mean). 단, 사후가 Gaussian이면 peak=mean이라 MAP=LMS로 일치. (STT 260610, "가우시안 케이스에서는 같아요")

**(2) 관측이 없는 경우 U[4,10]** (Lecture11, slide 13; STT 260610, "반띵")
- prior: `f_Θ(θ) = 1/6`, 4 ≤ θ ≤ 10; **otherwise = 0**. 관측 없으면 사후 = prior.
- MAP: 평평해서 [4,10] 아무 값이나 → 무용(not useful).
- LMS: `E[Θ] = 7` (유니폼은 중점이 평균). MSE 최소라는 의미에서 합리적.

## 4. 자주 헷갈리는 포인트
- **연속 RV에서 MAP의 "틀릴 확률"은 항상 1**: 한 점을 정확히 맞힐 확률 P(Θ=특정값)=0이기 때문. → 분류엔 MAP, 연속 추정엔 MSE 기반 LMS가 자연스러운 이유. (STT 260610, "틀릴 확률이 1이라고")
- **estimate vs estimator**: 소문자 x(손에 쥔 값) 기반이면 값, 대문자 X(랜덤변수) 기반이면 함수=랜덤변수. (Lecture11, slide 7; STT 260610, "어감 차이")
- 사후분포에서 분모 `f_X(x)`는 θ와 무관한 상수 → 분포의 "모양(shape)"엔 영향 없어 `∝`로 생략 가능. (STT 260610, "분모는 변치 않는 사실")

## 5. 시험 / 응용 관점
- **분류·가설검정 → MAP**(오결정확률 최소), **연속 파라미터 추정 → LMS**(MSE 최소). 문제 유형으로 추정량 선택. (STT 260610, "클래시피케이션에서는 맵 룰")
- 켤레 prior(Beta)는 **재귀적(recursive) 추론** 가능: 이번 사후가 다음 실험의 prior로 그대로 재사용 → 온라인/머신러닝 학습. (STT 260610, "리컬시브한 인퍼런스")
- **LMS의 한계**: 고차원 Θ(딥러닝 파라미터 수 AlexNet 60M ~ GPT-3 175B ~ DeepSeek-V3 671B)에서 사후분포의 적분 `f_X(x)=∫f_Θ(θ')f_{X|Θ}(x|θ')dθ'`이 사실상 불가능 → 대안이 다음 강의 LLMS(Linear LMS). (Lecture11, slide 16; STT 260610, "적분을 250번")

*roadmap의 (6) LLMS·(7) Classical ML estimator는 이번 강의(Part 2)에서 다루지 않고 다음 강의 예고로만 언급됨 — notes/STT에서 본문 내용은 확인되지 않음*
