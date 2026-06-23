# 12.1.6 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), 사용자 첨부 이미지, 1순위 근거 Lecture12 (LLMS 공식 p.7, MSE=(1−ρ²)var p.8). ⚠ "결합 가우시안 ⇒ LLMS=전역 MMSE"는 강의 밖(일반 교과서 사실) — 강의의 가우시안 언급은 MAP=LMS(Lecture11)로 별개. 풀이일 2026-06-16

## 문제 원문

A signal X and noise Z are independent Gaussian (0,1) random variables, and Y = X + Z is a noisy observation of the signal X. Usually, we want to use Y to estimate X; however, in this problem we will use Y to estimate the noise Z.

(a) Find Ẑ(Y), the MMSE estimator of Z given Y.
(b) Find the mean squared error e = E[(Z − Ẑ(Y))²].

---

### 1. 문제 정리 (Setup)

신호 X ~ N(0,1), 잡음 Z ~ N(0,1), 둘은 독립. 관측 Y = X + Z. 보통은 Y로 X를 추정하지만, 이 문제는 Y로 잡음 Z를 추정한다.

| 소문제 | 구할 것 |
|---|---|
| (a) | Ẑ(Y) = Z의 MMSE 추정량 (관측 Y) |
| (b) | MSE e = E[(Z − Ẑ(Y))²] |

추정 대상 Z는 강의노트의 Θ, 관측 Y는 강의노트의 X 역할이다.

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

원칙적으로 MMSE 추정량은 조건부 평균 E[Z|Y]인데, 일반적으로 이건 적분이 필요해 어렵다. 그런데 여기엔 결합 가우시안이라는 결정적 구조가 있다:

- X, Z가 독립 가우시안이고 Y = X + Z는 그 선형결합 → (Z, Y)는 결합 가우시안.
- ⚠ 강의 밖(일반 교과서 사실, Yates Ch.12): 결합 가우시안이면 E[Z|Y]가 Y의 1차식이 된다 → 즉 일반 MMSE 추정량(LMS)이 선형 추정량(LLMS)과 정확히 일치한다. **주의**: 이건 강의에서 명시되지 않았다. 강의의 가우시안 언급은 "포스테리어가 가우시안이면 MAP=LMS(피크=평균)"(Lecture11, STT 260610)로, 이 "MMSE가 선형"과는 별개의 명제다.

따라서 강의 범위로 엄밀히 보증되는 것은 "최적 선형(LLMS) 추정량 = Y/2, MSE = 1/2"이고, 거기에 위 가우시안 사실을 더하면 그게 곧 전역 MMSE 답이 된다. LLMS 공식은 적분 없이 "외워 쓰는" 형태. (Lecture12, p.7, "기말고사 볼 때는 그냥 저거 써놓으세요")

### 3. 핵심 통찰 (Aha)

> 결합 가우시안에서는 최적 추정량이 선형이라, LLMS 공식 Ẑ = E[Z] + (cov(Z,Y)/var(Y))(Y − E[Y]) 가 곧 MMSE 추정량 — 분포 적분 없이 평균·분산·공분산 세 개만으로 끝난다.

### 4. 풀이 (Worked solution)

필요한 모멘트만 모은다(LLMS는 분포 불필요, 모멘트만). (Lecture12, p.7)

평균: E[Z] = 0, E[Y] = E[X] + E[Z] = 0.

공분산 (Z ⊥ X 사용):

$$\mathrm{cov}(Z,Y) = \mathrm{cov}(Z,\,X+Z) = \underbrace{\mathrm{cov}(Z,X)}_{0} + \mathrm{var}(Z) = 1.$$

분산:

$$\mathrm{var}(Y) = \mathrm{var}(X) + \mathrm{var}(Z) = 1 + 1 = 2.$$

(a) LLMS 공식 (Lecture12, p.7) — 결합 가우시안이라 이게 MMSE 추정량:

$$\hat{Z}(Y) = E[Z] + \frac{\mathrm{cov}(Z,Y)}{\mathrm{var}(Y)}\big(Y - E[Y]\big) = 0 + \frac{1}{2}(Y - 0) = \boxed{\frac{Y}{2}}.$$

(b) 상관계수 ρ = cov(Z,Y)/(σ_Z σ_Y) = 1/(1·√2) = 1/√2, 즉 ρ² = 1/2. MSE 공식 (Lecture12, p.8):

$$e = (1-\rho^2)\,\mathrm{var}(Z) = \Big(1 - \tfrac12\Big)\cdot 1 = \boxed{\tfrac12}.$$

### 5. 검산·직관 (Sanity check)

- 대칭성: X와 Z는 통계적으로 완전 대칭(둘 다 N(0,1), 독립)이라 Y로 X를 추정해도 X̂(Y) = Y/2, MSE = 1/2 — Z 추정과 같아야 하고, 실제로 X̂ + Ẑ = Y/2 + Y/2 = Y로 관측과 정합 ✓.
- 직교성(무상관 오차): 추정오차 Z − Y/2 = Z − (X+Z)/2 = (Z−X)/2. 이게 Y = X+Z와 무상관인지 확인 — cov((Z−X)/2, X+Z) = ½(cov(Z,X)+var(Z)−var(X)−cov(X,Z)) = ½(0+1−1−0) = 0 ✓ (MMSE 추정의 필수 성질).
- 크기 감각: 관측 전 var(Z)=1 → 관측 후 1/2로 절반 감소. ρ²=1/2만큼 정보를 얻음, 0<e<var(Z) 합리적 ✓.
- 모멘트만 직접 검산: e = E[((Z−X)/2)²] = ¼(var(Z)+var(X)) = ¼·2 = 1/2 ✓ (공식과 일치).

### 6. 한 줄 요약

> 결합 가우시안이면 MMSE 추정량이 선형이라 LLMS 공식이 곧 정답 — Y=X+Z에서 잡음 추정은 Ẑ(Y)=Y/2, 그 오차는 (1−ρ²)var(Z)=1/2다. (Lecture12, p.7–8)
