# 12.1.1 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture11 (LMS = 조건부 기댓값), 풀이일 2026-06-14

## 문제 원문

12.1.1 ● Generalizing the solution of Example 12.2, let the call duration T be an exponential (λ) random variable. For t₀ > 0, show that the minimum mean square error estimate of T, given that T > t₀ is

T̂ = t₀ + E[T].

---

### 1. 문제 정리 (Setup)

| 항목 | 내용 |
|---|---|
| 주어진 것 | T ~ Exponential(λ), 즉 통화시간이 지수분포 |
| 관측(조건) | T > t₀ (단, t₀ > 0) — "이미 t₀만큼 통화가 이어졌다" |
| 구할 것 | T > t₀ 조건에서 T의 MMSE 추정값이 T̂ = t₀ + E[T] 임을 보여라 |

지수분포 PDF:

```
f_T(t) = λe^(−λt),   t ≥ 0
       = 0,          otherwise        (otherwise = 0)
E[T] = 1/λ
```

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

MMSE(minimum mean square error) 추정 = LMS 추정 = 조건부 기댓값이다. (Lecture11, slide 6, "θ̂_LMS = E[Θ|X=x]") 제곱오차를 최소화하는 값은 조건부 분포의 평균.

여기서 "관측 데이터 x" 자리에 들어가는 건 숫자가 아니라 사건 {T > t₀}. 그래도 원리는 같다: 그 사건으로 조건을 건 뒤 T의 조건부 평균을 구하면 그게 MMSE 추정값.

```
T̂_MMSE = E[T | T > t₀]
```

### 3. 핵심 통찰 (Aha)

> 지수분포는 무기억(memoryless) — 이미 t₀만큼 기다렸어도 "앞으로 더 걸릴 시간"은 처음부터 새로 시작하는 지수분포와 통계적으로 똑같다. 그래서 남은 시간의 기대값은 그냥 E[T]이고, 거기에 이미 흐른 t₀만 더하면 끝.

### 4. 풀이 (Worked solution)

**방법 A — 조건부 PDF 직접 적분**

T > t₀ 조건에서의 조건부 PDF (사건 확률 P(T>t₀) = e^(−λt₀)로 정규화):

```
f_{T|T>t₀}(t) = f_T(t) / P(T>t₀) = λe^(−λt) / e^(−λt₀)
             = λe^(−λ(t−t₀)),   t > t₀
             = 0,               otherwise        (otherwise = 0)
```

조건부 기댓값을 적분. 치환 u = t − t₀ (du = dt):

```
E[T | T>t₀] = ∫_{t₀}^∞  t · λe^(−λ(t−t₀)) dt
            = ∫_0^∞ (u + t₀) · λe^(−λu) du
            = ∫_0^∞ u·λe^(−λu) du  +  t₀·∫_0^∞ λe^(−λu) du
            = (1/λ)               +  t₀·(1)
            = t₀ + 1/λ
```

```
∴  T̂ = E[T | T>t₀] = t₀ + 1/λ = t₀ + E[T]   ∎
```

**방법 B — 무기억성으로 한 줄에**

무기억성: P(T > t₀ + s | T > t₀) = P(T > s). 즉 조건부로 본 잔여시간 R = T − t₀ 는 다시 Exponential(λ). 따라서

```
E[T | T>t₀] = E[(T − t₀) | T>t₀] + t₀ = E[R] + t₀ = E[T] + t₀
```

(잔여시간 R ~ Exponential(λ)라 E[R] = E[T] = 1/λ.) 적분 없이 끝.

### 5. 검산·직관 (Sanity check)

- 정규화: ∫_{t₀}^∞ λe^(−λ(t−t₀)) dt = ∫_0^∞ λe^(−λu) du = 1 ✓ (조건부 PDF 합 = 1)
- t₀ → 0 극한: 아무 조건 없을 때 T̂ → E[T] = 1/λ. 무조건부 MMSE 추정값과 일치 ✓
- 단위·차원: t₀[초] + E[T][초] = [초], 시간 차원 일관 ✓
- 선형 이동 직관: t₀가 1초 늘면 추정값도 정확히 1초 늘어남. "이미 흐른 시간은 그대로 더하고, 앞으로의 기대만 E[T]로 고정" — 지수분포만의 특성.

### 6. 한 줄 요약

> 사건 조건에서의 MMSE 추정값은 조건부 기댓값 E[T|T>t₀]이고, 지수분포의 무기억성 덕에 잔여시간의 기대가 E[T] 그대로라 추정값은 단순히 t₀ + E[T]가 된다.
