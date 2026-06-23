# Yates 5.1.2 풀이 — 결합 CDF 경계값과 주변 CDF

> 출처: Yates & Goodman (PSP), 사용자 첨부 이미지, 1순위 근거 Lecture06 (Continuous RV Part 2) p.12, 풀이일 2026-06-07

## 문제 원문

Express the following extreme values of F_{X,Y}(x,y) in terms of the marginal cumulative distribution functions F_X(x) and F_Y(y).

(a) F_{X,Y}(x, −∞)  
(b) F_{X,Y}(x, +∞)  
(c) F_{X,Y}(−∞, +∞)  
(d) F_{X,Y}(−∞, y)  
(e) F_{X,Y}(+∞, y)

---

### 핵심 통찰

**한 변수를 ±∞로 보내면 그 사건이 "전체(Ω)" 또는 "공집합(∅)"이 된다.**

- +∞: {Y ≤ ∞} = Ω → 제약 소멸 → 상대방의 주변 CDF
- −∞: {Y ≤ −∞} = ∅ → 확률 0

---

### 풀이

| 경계값 | 결과 | 이유 |
|---|---|---|
| F_{X,Y}(x, −∞) | 0 | {Y ≤ −∞} = ∅ |
| F_{X,Y}(x, +∞) | **F_X(x)** | {Y ≤ ∞} = Ω, Y 제약 소멸 |
| F_{X,Y}(−∞, +∞) | 0 | F_X(−∞) = 0 |
| F_{X,Y}(−∞, y) | 0 | {X ≤ −∞} = ∅ |
| F_{X,Y}(+∞, y) | **F_Y(y)** | {X ≤ ∞} = Ω, X 제약 소멸 |

---

### 한 줄 요약

> 결합 CDF의 경계: 한 변수를 +∞로 보내면 상대방의 주변 CDF, −∞로 보내면 0.
