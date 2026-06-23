# Joint PMF 공분산·상관계수 (Problem 31) 풀이

> 출처: 사용자 첨부 이미지 (Problem 31, Table 5.6), 1순위 근거 Lecture07_Further_Topics_RV_Part_1 (Covariance)·Lecture08_Further_Topics_RV_Part_2 (Correlation), 풀이일 2026-06-15

## 문제 원문

Consider two random variables X and Y with joint PMF given in Table 5.6:

```
            Y=0     Y=1     Y=2
X=0         1/6     1/4     1/8
X=1         1/8     1/6     1/6
```

Find Cov(X, Y) and ρ(X, Y).

---

### 1. 문제 정리 (Setup)

결합 PMF p_{X,Y}(x,y) (otherwise = 0):

$$\begin{array}{c|ccc} p_{X,Y} & Y=0 & Y=1 & Y=2 \\ \hline X=0 & 1/6 & 1/4 & 1/8 \\ X=1 & 1/8 & 1/6 & 1/6 \end{array}$$

구할 것: **Cov(X,Y)** 와 **ρ(X,Y)**. (전체합 검산, /24로: 4+6+3+3+4+4 = 24 → 합 1 ✓)

### 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

공분산은 정의식 E[(X−μ_X)(Y−μ_Y)]보다 **계산식 Cov = E[XY] − E[X]E[Y]** 가 표 계산에 훨씬 편하다 (Lecture07, p.23). 그래서 필요한 재료는 딱 셋: E[X], E[Y], E[XY] — 모두 marginal과 표에서 바로 나온다. 상관계수는 그 Cov를 각 σ로 정규화한 무차원 양 (Lecture08, p.6).

### 3. 핵심 통찰 (Aha)

> Cov는 **E[XY] − E[X]E[Y]** 한 줄로 끝나고, ρ는 그걸 **√(Var X · Var Y)로 나눠 [−1,1]에 가두는** 정규화일 뿐이다 (Lecture08, p.22의 bound).

### 4. 풀이 (Worked solution)

**marginal & 평균.** 행 합 → P_X, 열 합 → P_Y (otherwise = 0):

$$p_X(0)=\tfrac16+\tfrac14+\tfrac18=\tfrac{13}{24},\quad p_X(1)=\tfrac18+\tfrac16+\tfrac16=\tfrac{11}{24}$$

$$p_Y(0)=\tfrac16+\tfrac18=\tfrac{7}{24},\quad p_Y(1)=\tfrac14+\tfrac16=\tfrac{10}{24},\quad p_Y(2)=\tfrac18+\tfrac16=\tfrac{7}{24}$$

$$\mathbb{E}[X]=0\cdot\tfrac{13}{24}+1\cdot\tfrac{11}{24}=\tfrac{11}{24},\qquad \mathbb{E}[Y]=0\cdot\tfrac{7}{24}+1\cdot\tfrac{10}{24}+2\cdot\tfrac{7}{24}=\tfrac{24}{24}=1$$

**E[XY].** X=0인 칸은 곱이 0이라 무시, X=1 행에서 Y≥1만 기여:

$$\mathbb{E}[XY]=\sum_{x,y}xy\,p_{X,Y}(x,y)=1\cdot1\cdot\tfrac16+1\cdot2\cdot\tfrac16=\tfrac16+\tfrac26=\tfrac12$$

**Cov(X,Y)** (Lecture07, p.23):

$$\mathrm{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]=\tfrac12-\tfrac{11}{24}\cdot1=\tfrac{12}{24}-\tfrac{11}{24}=\boxed{\tfrac{1}{24}}$$

**분산.** X는 값 {0,1}이라 X²=X ⇒ E[X²]=E[X]=11/24:

$$\mathrm{Var}(X)=\tfrac{11}{24}-\left(\tfrac{11}{24}\right)^2=\tfrac{11}{24}\cdot\tfrac{13}{24}=\tfrac{143}{576}$$

$$\mathbb{E}[Y^2]=0+1\cdot\tfrac{10}{24}+4\cdot\tfrac{7}{24}=\tfrac{38}{24}=\tfrac{19}{12},\qquad \mathrm{Var}(Y)=\tfrac{19}{12}-1^2=\tfrac{7}{12}$$

**ρ(X,Y)** (Lecture08, p.6):

$$\rho(X,Y)=\frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)\,\mathrm{Var}(Y)}}=\frac{1/24}{\sqrt{\tfrac{143}{576}\cdot\tfrac{7}{12}}}=\frac{1/24}{\sqrt{1001/6912}}=\sqrt{\tfrac{12}{1001}}\approx \boxed{0.1095}$$

(1001 = 7·11·13. 정확형 ρ = 2√3 / √1001 = √(12/1001).)

### 5. 검산·직관 (Sanity check)

- marginal 두 줄 합 모두 1 ✓ (13+11=24; 7+10+7=24).
- **−1 ≤ ρ ≤ 1** 만족 (0.11) ✓ (Lecture08, p.22).
- Cov > 0 → X와 Y는 **약한 양의** 선형 관계. 직관: X=1일 때 큰 Y(=2) 확률(1/6)이 X=0일 때(1/8)보다 커서 같이 커지는 경향 — 부호 일치 ✓.
- ρ가 0.11로 작음 → 선형 의존이 약함. Cov 자체는 단위에 의존해 크기 판단이 어렵지만, ρ는 정규화돼 "약한 상관"임을 바로 읽게 해줌.

### 6. 한 줄 요약

> 공분산은 **E[XY] − E[X]E[Y]** 한 줄, 상관계수는 그것을 **√(VarX·VarY)로 나눠 [−1,1]로 정규화**한 선형 의존 지표다 — 여기선 Cov=1/24, ρ≈0.11(약한 양의 상관).
