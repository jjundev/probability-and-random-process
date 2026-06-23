# 5.7.5 풀이

> 출처: Yates (Probability and Stochastic Processes), 사용자 첨부 이미지, 1순위 근거 Lecture07_Further_Topics_RV_Part_1 (var 합 공식)·Lecture08_Further_Topics_RV_Part_2 (ρ 정의), 풀이일 2026-06-15

## 문제 원문

5.7.5 — X and Y are random variables with E[X] = E[Y] = 0 and Var[X] = 1, Var[Y] = 4 and correlation coefficient ρ = 1/2. Find Var[X + Y].

---

### 1. 문제 정리 (Setup)

| 주어진 것 | 값 |
|---|---|
| E[X] = E[Y] | 0 |
| Var[X] | 1 |
| Var[Y] | 4 |
| 상관계수 ρ(X,Y) | 1/2 |

구할 것: **Var[X + Y]**.

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

합의 분산은 두 분산의 단순 합이 **아니라** 공분산 항이 붙는다 (Lecture07, p.23). 여기선 ρ가 주어졌으니 Cov를 ρ로부터 역산하면 끝 — ρ = Cov/√(VarX·VarY) (Lecture08, p.6)를 Cov에 대해 풀면 된다. 평균 0은 미끼: 분산은 평균 위치에 무관.

### 3. 핵심 통찰 (Aha)

> Var[X+Y] = Var X + Var Y + **2·ρ·σ_X·σ_Y** — ρ를 σ 두 개와 곱하면 곧바로 Cov가 되어 합의 분산에 들어간다.

### 4. 풀이 (Worked solution)

**Cov 역산** (Lecture08, p.6의 ρ = Cov/√(VarX·VarY)):

$$\mathrm{Cov}(X,Y)=\rho\,\sqrt{\mathrm{Var}[X]\,\mathrm{Var}[Y]}=\tfrac12\cdot\sqrt{1\cdot 4}=\tfrac12\cdot 2=1$$

**합의 분산** (Lecture07, p.23의 var(X+Y) = var X + var Y + 2cov):

$$\mathrm{Var}[X+Y]=\mathrm{Var}[X]+\mathrm{Var}[Y]+2\,\mathrm{Cov}(X,Y)=1+4+2\cdot 1=\boxed{7}$$

### 5. 검산·직관 (Sanity check)

- 극단값 점검: ρ=1(완전 양의 선형)이면 Cov=2, Var=1+4+4=9 = (σ_X+σ_Y)²=(1+2)²=9 ✓ 상한. ρ=−1이면 1+4−4=1=(σ_Y−σ_X)²=1 ✓ 하한. ρ=1/2는 그 사이값 7 → 타당.
- 평균 0을 쓰지 않았음 — 분산은 평행이동 불변이므로 정상 (미끼 정보).

### 6. 한 줄 요약

> 합의 분산은 Var X + Var Y에 **2ρσ_Xσ_Y(=2Cov)** 를 더한 것 — 상관이 양이면 분산이 부풀고, 여기선 1+4+2 = 7.
