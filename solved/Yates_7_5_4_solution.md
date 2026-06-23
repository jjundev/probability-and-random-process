# 7.5.4 풀이

> 출처: Probability and Stochastic Processes (Yates & Goodman), Probability_and_Stochastic_Processes_Problems/problems_png/7.5.4.png (및 데이터 출처 7.5.3.png), 1순위 근거 Lecture08, 풀이일 2026-06-12

## 문제 원문

**7.5.4** For random variables A and B given in Problem 7.5.3, let U = E[B|A]. Find the PMF P_U(u). What is E[U] = E[E[B|A]]?

**참조 — 7.5.3에서 주어진 모델:**

$$P_A(a) = \begin{cases} 1/3 & a = -1,\\ 2/3 & a = 1,\\ 0 & \text{otherwise.}\end{cases}$$

$$P_{B\mid A}(b\mid -1) = \begin{cases} 1/3 & b = 0,\\ 2/3 & b = 1,\\ 0 & \text{otherwise,}\end{cases} \qquad P_{B\mid A}(b\mid 1) = \begin{cases} 1/2 & b = 0,\\ 1/2 & b = 1,\\ 0 & \text{otherwise.}\end{cases}$$

---

## 1. 문제 정리 (Setup)

**주어진 것**: 위 7.5.3의 P_A(a)와 두 조건부 PMF P_{B|A}(b|−1), P_{B|A}(b|1).

**구할 것**: U = E[B|A]로 정의된 확률변수 U의 PMF P_U(u), 그리고 E[U] = E[E[B|A]].

## 2. 무엇을 묻고 왜 이 도구인가 (개념 동기)

핵심은 표기 함정 하나다 — **E[B|A]는 숫자가 아니라 확률변수다.**

> "E[X|Y]는 RV Y의 함수로 정의되는 랜덤 베리어블 g(Y)로서, Y=y일 때 값 g(y) = E[X|Y=y]를 가짐." (Lecture08, p.16)

각 a에 대해 E[B|A=a]는 **숫자**(함수값)지만, 이것을 A의 함수로 보면 U = g(A)라는 **새 확률변수**가 된다 (Lecture08, p.16; "자주 헷갈리는 포인트"). PMF 구하기는 자동이다: U = g(A)는 A의 변환 RV이므로 **A의 확률을 그대로 물려받는다.** A가 값 a를 가질 확률 P_A(a)가 곧 U가 값 g(a)를 가질 확률이다.

E[U]는 문제가 E[U] = E[E[B|A]]로 적어준 게 힌트 — **반복기댓값 법칙**:

$$\mathbb{E}\!\left[\mathbb{E}[B\mid A]\right] = \mathbb{E}[B] \qquad \text{(Lecture08, p.17)}$$

## 3. 핵심 통찰 (Aha)

> U = E[B|A]는 A의 함수이므로, **"A = a일 확률"이 곧 "U = E[B|A=a]일 확률"** 이다 — U의 PMF는 A의 PMF를 g로 옮긴 것뿐.

## 4. 풀이 (Worked solution)

**(1단계) 각 a에서 조건부 기댓값 g(a) = E[B|A=a] 계산.** B는 {0,1} 값만 가지므로 E[B|A=a] = P(B=1|A=a):

$$g(-1) = \mathbb{E}[B\mid A=-1] = 0\cdot\tfrac13 + 1\cdot\tfrac23 = \tfrac23$$

$$g(1) = \mathbb{E}[B\mid A=1] = 0\cdot\tfrac12 + 1\cdot\tfrac12 = \tfrac12$$

두 값이 **서로 다르므로**(2/3 ≠ 1/2) U는 질량점 두 개를 갖는다.

**(2단계) U = g(A)에 A의 확률을 옮겨 PMF 구성.** A = −1 (확률 1/3)이면 U = 2/3, A = 1 (확률 2/3)이면 U = 1/2:

$$P_U(u) = \begin{cases} 2/3 & u = 1/2,\\[2pt] 1/3 & u = 2/3,\\[2pt] 0 & \text{otherwise.}\end{cases}$$

**(3단계) E[U] — 두 방법으로.**

방법 A (P_U에서 직접):

$$\mathbb{E}[U] = \tfrac12\cdot\tfrac23 + \tfrac23\cdot\tfrac13 = \tfrac13 + \tfrac29 = \tfrac39 + \tfrac29 = \frac{5}{9}$$

방법 B (반복기댓값): E[U] = E[E[B|A]] = E[B]. 결합 PMF P_{A,B}(a,b) = P_A(a)·P_{B|A}(b|a)에서 P_B(1) = (1/3)(2/3) + (2/3)(1/2) = 2/9 + 1/3 = 5/9이므로

$$\mathbb{E}[B] = 1\cdot P_B(1) = \frac{5}{9}$$

$$\boxed{\;P_U(2/3)=\tfrac13,\quad P_U(1/2)=\tfrac23,\qquad \mathbb{E}[U]=\mathbb{E}[\mathbb{E}[B\mid A]]=\mathbb{E}[B]=\tfrac59\;}$$

두 방법이 일치한다 — 이것이 반복기댓값 법칙의 내용이다.

## 5. 검산·직관 (Sanity check)

- **PMF 합 = 1**: 2/3 + 1/3 = 1 ✓.
- **범위 점검**: B ∈ {0,1}이므로 어떤 조건부 평균도 [0,1] 안. U 값 2/3, 1/2 모두 [0,1] ✓, E[U] = 5/9 ≈ 0.556도 [0,1] 안 ✓.
- **결합 PMF로 교차검증**: P_{A,B}는 1/9, 2/9, 3/9, 3/9 (합 = 9/9 = 1 ✓). P_B(1) = 2/9+3/9 = 5/9, 위 결과와 일치 ✓.
- **직관**: U는 A를 본 뒤 갱신된 B의 예측치. A를 보기 전(E[B]=5/9)이든 본 뒤 평균을 내든(E[U]=5/9) 같다 — "갱신된 예측의 평균은 원래 평균과 같다" (Lecture08, p.18).

## 6. 한 줄 요약

> E[B|A]는 A의 함수인 **확률변수**라서 PMF는 A의 확률을 g(a)=E[B|A=a]로 옮긴 것이고, 그 평균은 반복기댓값 법칙에 의해 그냥 E[B]로 되돌아온다.
