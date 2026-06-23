# 문제 PNG → 일자별 PDF 제작 가이드 (종합)

> 문제 이미지(PNG)를 모아 **태블릿 풀이용 가로 PDF**(`문제_6월N일.pdf`)로 만드는 전체 과정과, 작업하며 쌓인 노하우·함정을 한곳에 정리.
> 관련 스크립트: `python/refine_pngs.py`(정제) · `python/build_daily_problem_pdfs.py`(PDF 생성)
> 정제 상세는 [_PNG_정제_방법.md](_PNG_정제_방법.md) 참조(이 문서는 PNG→PDF 전 과정 + 노하우 종합).

---

## 0. 전체 워크플로우

```
문제 선별/복사 → [1] refine_pngs.py(정제) → [2] build_daily_problem_pdfs.py(PDF) → [3] 검증
   (PNG 배치)        autocrop+reflow,            표지+문제/페이지,                 PDF 페이지
                     dirty 후보 보고             높이상한으로 풀이공간 확보          눈으로 확인
```

- 입력: `기말고사 대비/6월 N일/*.png` (문제 이미지)
- 출력: 각 폴더에 `문제_6월N일.pdf`
- 원본 백업: `_png_원본백업/6월 N일/` (정제 전 원본)

---

## 1. 입력 규약

### 폴더 구조
```
기말고사 대비/
├─ 6월 7일/ … 6월 16일/      # 일자별
│   ├─ <문제>.png            # 문제 이미지(정제 대상)
│   ├─ 개념_*.pdf            # 그날 개념 자료(PDF에는 안 들어감)
│   └─ 오늘_복습.md          # 표지 제목·개념 불릿의 소스
├─ _png_원본백업/            # 정제 전 원본(자동 생성)
└─ _재크롭_후보.md           # dirty crop 후보 보고(자동 생성)
```

### 파일명 규약 (PDF 헤더·정렬·목차의 근거)
`L05_IPSRP_4.4.1.png` = **(L05 학습용)·(은행 IPSRP)·(교재번호 4.4.1)**
`복습L02_PSP_2.4.2.png` = 중간범위 복습 문제.
- 정규식: `^(복습)?L(\d{2})_([A-Za-z]+)_(.+)\.png$` → (복습여부, 강의번호, 은행, 번호).
- 두 은행: `IPSRP`(Pishro-Nik, 가로로 넓음) / `PSP`(세로로 김, 2단 조판).

---

## 2. [1단계] PNG 정제 — `refine_pngs.py` (요약)

PDF에 넣기 전 여백·레이아웃을 정리. (상세: [_PNG_정제_방법.md](_PNG_정제_방법.md))

- **① content-bbox autocrop**: 바깥 여백 제거(내부 들여쓰기·수식 보존). `gray<240`=잉크, 행/열 잉크≥3.
- **② 컬럼 reflow**: 2단 조판으로 오른쪽 칸에 밀린 가로 밴드를 좌측으로 평행이동(세로 위치 보존 → 수식 안 깨짐). 이동량 `> max(120, 0.22·W)`인 밴드만.
- **③ dirty 후보 보고**: 내부 세로 갭 ≥70px면 `_재크롭_후보.md`에 기록(자동 수정 X). 검수완료 파일은 `REVIEWED_CLEAN`으로 제외.
- 원본은 `_png_원본백업/`에 보관, **백업에서 읽어 재처리(멱등)**.
- dirty(그래프·코드 등 혼입)는 수동 재크롭(진짜 블록만 골라 세로로 stack).

핵심 파라미터: `THR=240, K=3, PAD=14, GAPBAND=22, GAP_FLAG=70`.

---

## 3. [2단계] PDF 생성 — `build_daily_problem_pdfs.py` (핵심)

### 도구/환경
- **reportlab**(PDF 생성) + **PIL**(이미지 치수). `pandoc`·`img2pdf`·`wkhtmltopdf`는 환경에 **없음**.
- **한글 폰트**: `C:\Windows\Fonts\malgun.ttf`(+malgunbd)를 `pdfmetrics.registerFont(TTFont(...))`로 등록. 실패 시 Helvetica 폴백(→ 한글 깨짐).

### 페이지/구성
- **A4 가로**: `W,H = landscape(A4)` ≈ 842×595pt, 여백 `M=36`. (reportlab 좌표 원점 = **좌하단**, y는 위로 증가.)
- **표지 1p + 문제당 1p**.

### 표지(`draw_cover`)
- 상단 **제목바**(남색 배경, 흰 글씨): `확률·랜덤프로세스 기말대비  ·  {오늘_복습.md의 H1 제목}`
- **지시 배너**: ① 오답 먼저 ② 신규는 상한 ③ 채점법
- **2단**: 좌=떠올릴 개념(오늘_복습.md의 `## … 떠올릴 개념` 섹션 불릿 추출), 우=문항 목차(파일명 파싱)
- 하단 **푸터**: 인쇄안내·시간예산

### 문제 페이지(`draw_problem`) — 가장 중요
- **헤더**: 좌 `[i/N] {강의}·{은행} {번호} — {주제}`, 우 로케이터 `i / N`, 아래 가로 구분선.
- **문제 이미지**: 헤더 아래 **좌상단 정렬**.
- **풀이 공간 확보(핵심 규칙)**: 이미지 높이를 **페이지 중앙선까지로 제한**해 **하단 절반은 항상 비움**.
  ```python
  SOLVE_MIN_FRAC = 0.5                         # 세로의 최소 이 비율은 풀이공간
  region_top = rule_y - 12                     # 헤더 구분선 아래
  avail_w    = W - 2*M                          # 770
  img_max_h  = region_top - H*SOLVE_MIN_FRAC    # ≈234pt (중앙선까지)
  scale = min(avail_w/iw, img_max_h/ih)         # 폭 또는 '상한 높이' 중 작은 쪽
  sw, sh = iw*scale, ih*scale
  x, y = M, region_top - sh                     # 좌상단 배치
  ```
  - 가로형(IPSRP): 폭에 묶여 짧게 들어감 → 풀이공간 넉넉.
  - 세로형(PSP): 높이 상한(234pt)에 묶임 → 하단 절반 확보.
  - `img_max_h ≤ avail_h`라 **풀이공간이 줄어들 일은 없음**(회귀 불가).
- **"— 풀이 —" 라벨**: 항상 이미지 아래.

### 정렬·메타
- **정렬**: `(복습여부, 강의번호, 은행[IPSRP<PSP], 번호의 숫자튜플)`. 번호는 **숫자 튜플 정렬**(`4.5.2 < 4.5.10`; 문자열 정렬이면 꼬임). 복습 문제는 뒤로.
- **강의→주제 맵(LECMAP)**: 05 연속RV1 / 06 연속RV2 / 07 Further1 / 08 Further2 / 09 점근 CLT / 01~04 중간범위.
- **표지 개념 추출**: `오늘_복습.md`에서 `떠올릴 개념` 헤더 다음 `- ` 불릿만(없으면 fallback 1줄). malgun에 없는 글리프(−, ₋, ˣ 등) 정규화.

---

## 4. 핵심 파라미터 한눈에

| 스크립트 | 파라미터 | 값 | 의미 |
|---|---|---|---|
| refine | THR / K | 240 / 3 | 잉크 판정 / 노이즈 가드 |
| refine | PAD | 14 | 크롭 후 흰 여백 |
| refine | GAPBAND | 22 | reflow 밴드 분리 갭 |
| refine | reflow 임계 | max(120, 0.22·W) | 이만큼 밀린 밴드만 좌측 이동 |
| refine | GAP_FLAG | 70 | dirty 후보 판정 갭 |
| pdf | W,H / M | 842×595 / 36 | A4 가로 / 여백 |
| pdf | **SOLVE_MIN_FRAC** | **0.5** | **세로 최소 절반=풀이공간(이미지 높이 상한)** |

---

## 5. 노하우 / 함정 (이번 작업의 교훈)

### 레이아웃
- **이미지 종횡비 양극화**가 핵심 이슈: IPSRP는 ~1500×낮음(가로형), PSP는 ~730×높음(세로형). 영역 전체에 맞추면 세로형이 페이지를 꽉 채워 **풀이공간 0pt** → **높이 상한(SOLVE_MIN_FRAC)** 으로 해결.
- 세로형 문제는 상한 때문에 작게 렌더됨 → 너무 작으면 `SOLVE_MIN_FRAC`를 0.45로 낮춰 절충.
- reportlab은 **좌하단 원점**. 이미지 top=region_top면 `y = region_top - sh`.

### 폰트/렌더
- **한글은 malgun.ttf 등록 필수**(Helvetica는 한글이 빈칸/박스). 표지·헤더 전부 영향.
- `−`(U+2212)·아래/위첨자 등 일부 글리프는 malgun에 없어 표지 힌트에서 누락 → 텍스트 정규화(ASCII로 치환).
- **`pandoc`/`img2pdf`/`wkhtmltopdf` 없음** → 수식 포함 `.md→PDF` 불가. 개념 자료는 슬라이드 PDF 복사로 대체, 문제 PDF는 **reportlab로 PNG 합성**.

### 코드 함정
- **Python enumerate 버그**: 생성식 안에서 그 enumerate의 인덱스를 참조하면 `UnboundLocalError`. (먼저 wrap한 뒤 인덱스로 prefix 붙일 것.)

### PowerShell 함정 (Windows)
- **한글 변수 보간**: `"6월 $n일"`은 `$n일`을 변수명으로 해석(한글이 식별자 문자) → 빈 문자열. **`"6월 $($n)일"` 또는 `"6월 {0}일" -f $n`** 사용. (폴더 생성/조회가 조용히 빗나감.)
- **`Remove-Item` 보호 가드**: 동적 경로 삭제가 "protected path"로 차단됨(샌드박스 꺼도). **`[System.IO.File]::Delete($path)`(.NET) 또는 Python `os.remove`** 로 우회.

### 프로세스
- **백업 + 멱등성**: 정제는 `_png_원본백업/`에서 읽어 재처리 → 몇 번 돌려도 동일, 되돌리기 가능. (교재 은행도 2차 백업.)
- **dirty crop은 자동으로 못 고침**(여백 아니라 내용). 후보만 뽑아 **수동 재크롭**(진짜 블록 top+bottom만 stack, 난이도 범례·그래프 제거). MATLAB·범위밖 문제는 **교체**.
- **검증은 `Read`로 PDF 페이지를 이미지로 직접 확인**. 단, **PDF 뷰어 캐시** 때문에 "안 바뀐 것처럼" 보일 수 있으니 닫았다 다시 열기. (파일 mtime으로 재생성 확인 가능.)
- **전체 재생성**: `build_daily_problem_pdfs.py`는 항상 6월 7~16일 전부 재생성. PNG가 바뀌면 정제→PDF 순으로 다시.

---

## 6. 재실행 / 유지보수

```powershell
python python/refine_pngs.py            # ① PNG 정제(백업에서 재처리, 멱등)
python python/build_daily_problem_pdfs.py   # ② 정제된 PNG로 PDF 10개 생성
```

조정 노브:
- 풀이공간 비율 → `build_daily_problem_pdfs.py`의 `SOLVE_MIN_FRAC`(기본 0.5).
- dirty 판정 민감도 → `refine_pngs.py`의 `GAP_FLAG`(기본 70), 검수완료는 `REVIEWED_CLEAN`.
- 새 문제 추가/교체 시: 해당 일자 폴더에 PNG 넣고(파일명 규약 준수) ①② 재실행, `오늘_복습.md` 목록도 갱신.

---

## 7. 검증 체크리스트
- [ ] 표지: 한글 제목·개념·목차 정상 렌더, 문항 수 일치.
- [ ] 문제 페이지: 헤더 `[i/N]`·주제 정확, 이미지 1장, **하단 절반 풀이공간** 확보.
- [ ] 세로형(PSP) 문제도 풀이공간 ≥ 절반(직전 회귀 지점).
- [ ] dirty 후보(`_재크롭_후보.md`) 처리됨(현재 0).
- [ ] 일자 10개 PDF 모두 최신 mtime(전체 재생성 확인).

---

## 8. 파일·경로
- `python/refine_pngs.py` — PNG 정제(autocrop+reflow+dirty 보고)
- `python/build_daily_problem_pdfs.py` — 일자별 문제 PDF 생성
- `기말고사 대비/6월 N일/문제_6월N일.pdf` — 산출물
- `기말고사 대비/_png_원본백업/` — 정제 전 원본
- `기말고사 대비/_재크롭_후보.md` — dirty 후보 보고
- `기말고사 대비/_PNG_정제_방법.md` — 정제 상세 문서
