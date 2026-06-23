# 통계적 추론 입문 Part 1 — 베이지안 vs 클래시컬 (Lecture 10)

> 출처: notes/Lecture10_Statistical_Inference_Part_1.pdf, STT/260608_Lecture10_Statistical_Inference.txt
> (PDF는 15페이지까지만 존재. 베타분포·recursive inference는 STT에만 등장 → Part 2 예고분으로 §5에 분리.)

## 1. 핵심 정의
- **Statistical Inference (SI)**: 노이즈가 낀 가용 데이터로부터 *unknown variable* 또는 *unknown model*에 대한 정보를 추출하는 과정. (Lecture10, p.5)
- **Unknown model vs unknown variable**: 같은 관측식 X=aS+W에서, 모델 파라미터 a를 추론(=model building)하느냐 원신호 S를 추론(=variable estimation)하느냐의 차이. 모델의 파라미터가 곧 변수인 경우가 많아 **수학적 구조는 동일**. (Lecture10, p.8; STT 260608, "바이스 벌사한 같은 문제")
- **Hypothesis testing**: unknown이 *몇 개의 가능한 값(유한·countable)* 중 하나. 목표 = 오결정(incorrect decision) 확률 최소화. (Lecture10, p.9)
- **Estimation**: unknown이 *무한·연속 집합*의 한 값. 목표 = 참값에 가까운 값 찾기. (Lecture10, p.9; STT 260608, "컨티뉴스 셋에서 어떤 값을 추론")
- **Likelihood**: 모델값 θ를 가정했을 때 관측 데이터가 나올 조건부 확률 `p(x; θ)` = `P(data | θ)`. (Lecture10, p.10-11)
- **Prior**: unknown Θ를 *랜덤 베리어블*로 보고 부여하는 사전 분포 p_Θ / f_Θ. (Lecture10, p.11, 14)
- **Posterior**: 데이터 x 관측 *후* Θ의 분포 `p_Θ|X(θ|x)`. 베이지안 추론의 **complete answer**(완전한 답). (Lecture10, p.11, 14; STT 260608, "컴플리트한 완벽한 앤서")

## 2. 주요 공식 / 정리
- **Wi-Fi 관측 모델**: `X = aS + W`, 0<a<1, W ~ N(0,1) (표준정규; 지지집합이 ℝ 전체라 otherwise=0 영역 없음). (Lecture10, p.5, 8)
- **동전 1회 PMF (Bernoulli)**: `P(H)=θ`, `P(T)=1−θ`, **otherwise = 0**. (Lecture10, p.9-10; STT 260608, "앞면이 나올 확률 세타")
- **Classical (ML detection)** — likelihood가 큰 쪽 선택:
  `P(HHH|θ=3/4)=(3/4)³=27/64`, `P(HHH|θ=1/4)=(1/4)³=1/64` (27배) → **θ=3/4**. (Lecture10, p.10; STT 260608, "라이클리 후드 디텍션")
- **Bayesian** — posterior가 큰 쪽 선택. prior `P(θ=3/4)=P(θ=1/4)=1/2`일 때:
  분모(evidence) `P(HHH)=(27/64)(1/2)+(1/64)(1/2)=7/32` (전확률 정리),
  `P(θ=3/4|HHH)=27/28`, `P(θ=1/4|HHH)=1/28`, **otherwise = 0** (두 값 합=1) → **θ=3/4**. (Lecture10, p.10; STT 260608, "포스테리어 확률이 큰 쪽")
- **베이즈 룰 4가지 버전** (Θ·X 각각 이산/연속):

```
[Θ 이산, X 이산]  p(θ|x) = p_Θ(θ)·p_X|Θ(x|θ) / p_X(x) ,  p_X(x) = Σ_θ' p_Θ(θ')·p_X|Θ(x|θ')
[Θ 이산, X 연속]  p(θ|x) = p_Θ(θ)·f_X|Θ(x|θ) / f_X(x) ,  f_X(x) = Σ_θ' p_Θ(θ')·f_X|Θ(x|θ')
[Θ 연속, X 연속]  f(θ|x) = f_Θ(θ)·f_X|Θ(x|θ) / f_X(x) ,  f_X(x) = ∫  f_Θ(θ')·f_X|Θ(x|θ') dθ'
[Θ 연속, X 이산]  f(θ|x) = f_Θ(θ)·p_X|Θ(x|θ) / p_X(x) ,  p_X(x) = ∫  f_Θ(θ')·p_X|Θ(x|θ') dθ'
```
규칙: Θ가 이산이면 p_Θ·(분모는 Σ), 연속이면 f_Θ·(분모는 ∫). X도 이산→p, 연속→f. (Lecture10, p.15; STT 260608, "어떤 거는 서메이션하고 어떤 거는 인테그레이션")

## 3. 핵심 예시 (1~2개)
- **편향 동전 HHH (오늘의 가장 중요한 페이지)**: θ∈{1/4, 3/4}, 3번 던져 HHH. ① Classical = likelihood (3/4)³ vs (1/4)³ 비교(27배) → 3/4. ② Bayesian = prior 1/2씩 주고 posterior 27/28 vs 1/28 → 3/4. **prior가 uniform이면 두 결론이 일치**. (Lecture10, p.10; STT 260608, "이 페이지 하나만 이해하면 끝")
- **레이더 — 새 vs 비행기**: 탐지 물체가 새인지 비행기인지(2지선다) → hypothesis testing, 오분류 확률 최소화 문제. (Lecture10, p.9; STT 260608, "버드라고 착각할 확률")

## 4. 자주 헷갈리는 포인트
- **Likelihood ≠ 확률**: θ를 바꿔가며 계산한 값들의 합이 1이 아님(27/64+1/64≠1). 조건 자체가 바뀌므로 정규화가 안 됨 → "maximum probability"가 아니라 "maximum **likelihood**". (STT 260608, "확률자를 붙일 수가 없는")
- **Bayesian의 답은 분포 전체**(posterior PMF/PDF, 합/적분=1). 숫자 하나가 필요할 때만 *point estimation* 수행(다음 강의: MAP, LMS). (STT 260608, "포인트 에스티메이션")
- **Bayesian ⊃ Classical**: prior를 uniform으로 주면 Bayesian이 Classical과 같아짐. uniform이 아니면(전문가 지식·선험 선호) 결과가 달라질 수 있음. 베이지안이 더 광범위하나 계산이 까다로움(다차원 적분). (Lecture10, p.11-12; STT 260608, "유니폼할 때는 같아요")
- **같은 문제, 다른 풀이**: 후보가 유한(객관식)이면 hypothesis testing, 연속이면 estimation — 설계자가 선택. (Lecture10, p.9; STT 260608, "3지선다로 정답은")

## 5. 시험 / 응용 관점
- **용어 대응**(본질 동일): (통계) hypothesis testing/estimation = (ML) classification/regression = (신호처리) detection/estimation. (STT 260608, "본질상 같은 거예요")
- **응용 연결**: 디지털 통신의 bit error 확률 최소화, ML의 cross-entropy 최소화가 모두 "오결정 확률 최소화"의 사례. (STT 260608, "비트 에러 확률을 미니마이즈")
- **Bayesian 프레임워크 흐름**: prior p_Θ + 관측모델 p_X|Θ → (관측) x → posterior 계산 → point estimate / error analysis. (Lecture10, p.14)
- **(Part 2 예고 — STT only, PDF 15p엔 없음)** 확률(0~1 값)을 추론할 땐 prior로 **베타 분포**를 자주 씀: `f_Θ(θ) = θ^(α−1)(1−θ)^(β−1) / B(α,β)` (0≤θ≤1), **otherwise = 0**. 동전 m회 중 앞면 k회 관측 시 posterior = Beta(α+k, β+(m−k)) → **conjugate prior**(사전·사후 동형)라 recursive inference(칼만 필터 등)에 유리. Beta(1,1)=uniform, 평균=α/(α+β). (STT 260608, "베타 디스트리뷰션", "리컬시브하게")
- **다음 시간 예고**: MAP(maximum a posteriori) rule, LMS/LLMS(MMSE 기반 point estimation). (STT 260608, "다음 시간에 맵에 대해서")
