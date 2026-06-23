# -*- coding: utf-8 -*-
"""
기말 직전 최종복습 시험지 (solved 20選).
포맷: A4 가로 1p 표지(네이비 배너 + 떠올릴 개념/문항 목차) + 문제당 1p.
각 문제 페이지 = 상단 문제 PNG + 하단 '핵심/답' 풀이존(빈 공간 채움).
렌더: HTML + Playwright(system Chrome) — 브라우저 글리프 폴백으로 수식 유니코드 안 깨짐.
"""
import os, json, base64, html, pathlib, shutil
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\확랜"
PNG_MAP = json.load(open(os.path.join(ROOT, "tmp", "png_map.json"), encoding="utf-8"))
OUT_PDF = os.path.join(HERE, "최종복습_20選_solved.pdf")
WORK = r"C:\Users\Hyunjun\AppData\Local\Temp\final20pdf"   # ASCII workdir for file:// URI

TITLE = "기말 직전 최종복습 — solved 20選 (L05~L12 전범위 · 풀이/핵심 포함)"

CONCEPTS = [
    "연속RV: f(x)=dF/dx, F(x)=P[X≤x]; 모든 PMF/PDF는 구간 밖 = 0 (항상 명시)",
    "균등 U(a,b): f=1/(b−a), E=(a+b)/2, Var=(b−a)²/12 / 지수 Exp(λ): f=λe^(−λx)(x≥0), E=1/λ, Var=1/λ², 무기억성",
    "정규: Z=(X−μ)/σ 표준화 → P=Φ로; Φ(−z)=1−Φ(z)",
    "결합: 주변=합/적분, 조건부 f_{X|Y}=f_{X,Y}/f_Y, 의존영역은 적분한계 주의(삼각/원판)",
    "공분산 Cov=E[XY]−E[X]E[Y], ρ=Cov/(σ_X σ_Y)∈[−1,1], Var(X±Y)=VarX+VarY±2Cov",
    "반복기댓값 E[X]=E[E[X|Y]] (E[X|Y]는 RV!), 전분산 Var(X)=E[Var(X|Y)]+Var(E[X|Y])",
    "결합정규: 선형결합도 정규, ρ=0 ⟺ 독립(이 분포 한정), MMSE가 선형이 됨",
    "추정: MMSE=E[X|Y]; 선형추정 a*=Cov/Var(Y), b*=E[X]−a*E[Y], e*_L=VarX−Cov²/VarY, 직교원리 E[(X−X̂)Y]=0",
]

# (file-key, lecture, bank, num, topic, difficulty, key, answer)
ITEMS = [
    ("Yates_4_3_2", "L05", "PSP", "4.3.2", "CDF→PDF 미분(균등)", "기본",
     "f_X(x)=dF_X/dx, 구간별 미분.\n선형 CDF → 기울기=일정한 PDF(균등).\n구간 밖 0 명시.",
     "f_X(x)=1/2 (−1≤x<1), 그 밖 0 (Uniform(−1,1))"),
    ("Yates_4_5_13", "L05", "PSP", "4.5.13", "지수분포 식별·CDF·E·Var", "기본",
     "λe^(−λx)에서 λ=1/2 식별. 구간 밖 0.\nCDF=1−e^(−λx), E=1/λ, Var=1/λ².\n지수분포: Var=(E[X])²",
     "P≈0.239, F=1−e^(−x/2), E[X]=2, Var=4"),
    ("Yates_4_5_10", "L05", "PSP", "4.5.10", "균등 E[g(X)]·홀함수=0", "기본",
     "f_X=1/(b−a), 구간 밖 0. E[X]=(a+b)/2.\nE[g(X)]=∫g f dx. 홀함수+원점대칭 → 0.\nE[eˣ]=(e⁵−e⁻⁵)/10≈14.84",
     "f=1/10 (−5≤x≤5), E[X]=0, E[X⁵]=0, E[eˣ]≈14.84"),
    ("Yates_4_4_6", "L05", "PSP", "4.4.6", "CDF→PDF·모멘트(치환)", "중",
     "미분: f_V=(v+5)/72, 구간 밖 0.\nu=v+5 치환 → E[Uᵏ]=12^(k+2)/(72(k+2)).\nV=U−5 선형변환으로 모멘트 환산.",
     "E[V]=3, Var[V]=8, E[V³]=431/5=86.2"),
    ("Yates_4_6_1", "L06", "PSP", "4.6.1", "정규 표준화 Φ 확률", "기본",
     "Yates는 N(μ,σ): σ=10. Z=(T−μ)/σ.\nP[Z>z]=1−Φ(z), Φ(−z)=1−Φ(z).\n경계를 σ단위로 환산이 핵심.",
     "0.0668, 0.0062, 0.8664"),
    ("Yates_5_2_1", "L06", "PSP", "5.2.1", "결합PMF 정규화·부등식확률", "기본",
     "가분형: ΣΣxy=(Σx)(Σy)=28 → c=1/28. 표 깔고 조건 칸만 합산. 구간 밖 0.\n주변 P_Y(y)=y/4로 검산.",
     "c=1/28; P[Y<X]=9/14; P[Y>X]=9/28; P[Y=X]=1/28; P[Y=3]=3/4"),
    ("Yates_5_5_1", "L06", "PSP", "5.5.1", "삼각영역 균등 결합PDF·주변", "중",
     "x 고정 → y는 x부터 1까지(의존 한계!). f_X(x)=½(1−x), −1≤x≤1 밖 0.\n균등=확률은 넓이비. E[X]=∫x·f_X dx.",
     "f_X(x)=½(1−x); P[X>0]=1/4; E[X]=−1/3"),
    ("Yates_4_4_1", "L07", "PSP", "4.4.1", "Y=X² 변환·E·Var·Jensen", "중",
     "E[g(X)]=∫g·f dx 직접적분(E[X],E[X²],E[X⁴]).\nVar[Y]=E[X⁴]−(E[X²])².\nJensen: 볼록 x² → h(E[X])≤E[h(X)].",
     "E[X]=1, Var[X]=4/3; h(E[X])=1, E[h(X)]=7/3; E[Y]=7/3, Var[Y]=304/45≈6.76"),
    ("Yates_5_7_5", "L07", "PSP", "5.7.5", "ρ로 Var(X+Y) 역산", "기본",
     "Cov=ρ·√(VarX·VarY)=½·2=1. Var[X+Y]=VarX+VarY+2Cov.\n평균0은 미끼(분산은 평행이동 불변).",
     "Var[X+Y]=1+4+2=7"),
    ("Yates_5_8_1", "L07", "PSP", "5.8.1", "Y=X+Z 상관계수·독립판정", "기본",
     "Cov(X,X+Z)=VarX+Cov(X,Z)=1+0=1. VarY=1+16=17.\nρ=Cov/√(VarX·VarY)=1/√17. ρ≠0 → 독립 아님.",
     "ρ=1/√17≈0.243; X,Y 독립 아님"),
    ("Yates_7_5_2", "L08", "PSP", "7.5.2", "결합PDF 조건부기댓값 E[Y|X]", "기본",
     "x 고정 → Y~U[0,x]. f_X(x)=2x(밖0), f_{Y|X}=1/x.\nE[Y|X=x]=x/2(구간 중점).",
     "f_X=2x, f_{Y|X}=1/x, E[Y|X=x]=x/2"),
    ("Yates_7_5_4", "L08", "PSP", "7.5.4", "반복기댓값 E[E[B|A]]", "중",
     "함정: E[B|A]는 숫자 아닌 RV g(A). U의 PMF는 A확률을 g(a)로 옮김.\nE[U]=E[E[B|A]]=E[B] (반복기댓값).",
     "P_U(1/2)=2/3, P_U(2/3)=1/3, E[U]=E[B]=5/9"),
    ("Yates_7_5_5", "L08", "PSP", "7.5.5", "포아송 결합·반복기댓값", "중",
     "결합이 k에 무관 ⇒ K|N~Uniform{0..n}, P_{K|N}=1/(n+1)(밖0).\nN~Poisson(100), E[K|N]=N/2, E[K]=E[N]/2.",
     "P_N~Poi(100), E[K|N=n]=n/2, E[K]=50"),
    ("Yates_7_6_3", "L08", "PSP", "7.6.3", "혼합집단 전분산·Simpson", "상",
     "전공분산: Cov=E[그룹내Cov]+그룹평균 간 Cov.\n전분산: Var=E[Var|M]+Var(E[·|M]).\n그룹내 음(−)이라도 평균차가 압도→전체 양(+), 성별 무시 금지.",
     "Cov=+14, Var(X)=8, Var(Y)=125, ρ≈+0.44"),
    ("Pishro_5_4_36", "L08", "IPSRP", "5.4.36", "결합정규 선형결합·공분산", "중",
     "결합정규 선형결합=정규 → 평균·분산만 구해 Φ.\nVar(aX+bY)=a²VarX+b²VarY+2ab·Cov, Cov=ρσ_Xσ_Y.\n공분산 쌍선형 전개.",
     "(a) Φ(1)≈0.8413   (b) 1"),
    ("Yates_12_1_1", "L11", "PSP", "12.1.1", "사건조건 MMSE·무기억성", "기본",
     "MMSE=조건부평균 E[T|T>t₀].\n지수 무기억성: 잔여시간~Exp(λ), E[R]=E[T]=1/λ.\nf는 t≥0 밖 0; 조건부 f는 t>t₀ 밖 0.",
     "T̂ = t₀ + E[T] = t₀ + 1/λ"),
    ("Yates_12_1_4", "L11", "PSP", "12.1.4", "MMSE=조건부평균 E[X|Y]", "중",
     "MMSE=조건부평균 E[X|Y]; 조건부밀도=결합÷주변(구간 밖 0).\nf_Y=3y², f_X=3(1−x)²; 선형삼각분포 평균은 긴 변 쪽 1/3 지점.",
     "x̂_M(y)=y/3, ŷ_M(x)=(x+2)/3; f_{X|Y}=2(y−x)/y²"),
    ("Yates_12_1_6", "L12", "PSP", "12.1.6", "결합가우시안 MMSE=선형", "중",
     "결합가우시안 → MMSE가 선형=LLMS: Ẑ=E[Z]+(Cov/VarY)(Y−E[Y]).\nCov(Z,Y)=VarZ=1, VarY=2; MSE=(1−ρ²)VarZ, ρ²=1/2.",
     "Ẑ(Y)=Y/2, e=1/2"),
    ("Yates_12_2_2", "L12", "PSP", "12.2.2", "신호+독립잡음 선형추정", "기본",
     "독립잡음: Var[R]=VarV+VarX, Cov[V,R]=VarV (잡음 소거).\na*=Cov/VarR<1 (수축), e*_L=VarV−Cov²/VarR; VarUnif=(β−α)²/12.",
     "E[R]=0, Var[R]=15, Cov=12, a*=4/5, b*=0, e*_L=12/5=2.4"),
    ("Yates_12_2_8", "L12", "PSP", "12.2.8", "원점통과 aY·직교원리", "중",
     "a*=E[XY]/E[Y²]; 오차 X−a*Y가 Y와 직교: E[(X−a*Y)Y]=0.\ne*=E[X²]−(E[XY])²/E[Y²].\naY가 LMSE ⇔ 아핀 상수항 b_L=0 (특히 E[X]=E[Y]=0).",
     "a*=E[XY]/E[Y²], e*=E[X²]−(E[XY])²/E[Y²]"),
]

DIFF_COLOR = {"기본": "#2e7d32", "중": "#b8860b", "상": "#c62828"}


def data_uri(path):
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    with open(path, "rb") as f:
        b = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/{ext};base64,{b}"


def esc(s):
    return html.escape(s).replace("\n", "<br>")


def cover_html(n):
    bullets = "\n".join(f"<li>{esc(b)}</li>" for b in CONCEPTS)
    toc = []
    for i, it in enumerate(ITEMS, 1):
        _, lec, bank, num, topic, diff = it[0], it[1], it[2], it[3], it[4], it[5]
        col = DIFF_COLOR.get(diff, "#555")
        toc.append(
            f'<div class="toc-row"><span class="idx">[{i}]</span> '
            f'{esc(lec)} · {esc(bank)} {esc(num)} — {esc(topic)} '
            f'<span class="diff" style="color:{col}">({esc(diff)})</span></div>'
        )
    toc_html = "\n".join(toc)
    return f"""
<section class="page cover">
  <div class="banner">확률·랜덤프로세스 기말대비 &nbsp;&nbsp; {esc(TITLE)}</div>
  <div class="instbar">①&nbsp; 한 문제당 1페이지 · 상단=문제, 하단=핵심/답 &nbsp;&nbsp;&nbsp; ②&nbsp; 1시간 전 회독용: 답 가리고 접근만 떠올려보기 &nbsp;&nbsp;&nbsp; ③&nbsp; (★주의) L09 CLT·표본평균은 solved에 없음 → 노트로 별도 점검</div>
  <div class="cols">
    <div class="col">
      <div class="colhead">떠올릴 개념</div>
      <ul class="concepts">{bullets}</ul>
    </div>
    <div class="col">
      <div class="colhead">문항 목차 (총 {n}문항)</div>
      {toc_html}
    </div>
  </div>
  <div class="foot">solved 62문제 중 전범위·기법 중복 최소화로 20選 · 가로모드 · 핵심/답 포함 &nbsp;|&nbsp; 난이도 색: <span style="color:#2e7d32">기본</span> · <span style="color:#b8860b">중</span> · <span style="color:#c62828">상</span></div>
</section>
"""


def problem_html(i, n, it):
    key_file, lec, bank, num, topic, diff, key, ans = it
    info = PNG_MAP[key_file]
    uri = data_uri(info["path"])
    col = DIFF_COLOR.get(diff, "#555")
    return f"""
<section class="page">
  <div class="phead">
    <div class="pleft">[{i}/{n}] &nbsp; <b>{esc(lec)} · {esc(bank)} {esc(num)}</b> &nbsp;—&nbsp; {esc(topic)}
      <span class="diff" style="color:{col}">· {esc(diff)}</span></div>
    <div class="pright">{i} / {n}</div>
  </div>
  <div class="imgbox"><img src="{uri}"></div>
  <div class="soln">
    <div class="slabel">■ 핵심 / 접근</div>
    <div class="skey">{esc(key)}</div>
    <div class="sans"><span class="atag">답</span> {esc(ans)}</div>
  </div>
</section>
"""


CSS = """
@page { size: A4 landscape; margin: 11mm 12mm; }
* { box-sizing: border-box; }
html,body { margin:0; padding:0; }
body { font-family:'Malgun Gothic','Segoe UI','Segoe UI Symbol','Segoe UI Emoji','DejaVu Sans',sans-serif;
       color:#111; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

/* cover */
.banner { background:#22335a; color:#fff; font-weight:700; font-size:14pt;
          padding:10pt 12pt; border-radius:3pt; }
.instbar { background:#f4f2e2; color:#222; font-size:9pt; padding:7pt 10pt; margin-top:8pt; border-radius:3pt; }
.cols { display:flex; gap:20pt; margin-top:14pt; }
.col { flex:1; }
.colhead { font-weight:700; font-size:12pt; margin-bottom:6pt; border-bottom:1.4pt solid #22335a; padding-bottom:3pt; }
ul.concepts { margin:0; padding-left:15pt; }
ul.concepts li { font-size:9.3pt; line-height:1.5; margin-bottom:4pt; }
.toc-row { font-size:9.3pt; line-height:1.62; }
.toc-row .idx { color:#22335a; font-weight:700; }
.toc-row .diff { font-size:8.5pt; }
.foot { margin-top:16pt; font-size:8.3pt; color:#555;
        border-top:0.6pt solid #ccc; padding-top:5pt; }

/* problem pages */
.phead { display:flex; justify-content:space-between; align-items:baseline;
         font-size:11pt; border-bottom:1.2pt solid #333; padding-bottom:4pt; }
.phead .pright { color:#888; font-size:10pt; }
.phead .diff { font-size:9pt; }
.imgbox { text-align:left; margin-top:9pt; }
.imgbox img { max-width:100%; max-height:88mm; }
.soln { margin-top:10pt; border:1pt solid #d9d2b8; background:#fbfaf3; border-radius:4pt;
        padding:8pt 11pt; }
.slabel { font-weight:700; font-size:10pt; color:#22335a; margin-bottom:4pt; }
.skey { font-size:10.5pt; line-height:1.62; }
.sans { margin-top:6pt; font-size:10.5pt; font-weight:700; color:#10371a; }
.sans .atag { background:#2e7d32; color:#fff; font-size:8.5pt; padding:1pt 6pt; border-radius:3pt; margin-right:5pt; font-weight:700; }
"""

HEAD = ('<!doctype html><html lang="ko"><head><meta charset="utf-8">'
        f"<style>{CSS}</style></head><body>")


def main():
    n = len(ITEMS)
    parts = [HEAD, cover_html(n)]
    for i, it in enumerate(ITEMS, 1):
        parts.append(problem_html(i, n, it))
    parts.append("</body></html>")
    html_doc = "\n".join(parts)

    os.makedirs(WORK, exist_ok=True)
    html_path = os.path.join(WORK, "exam.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print("HTML written:", html_path, "items:", n, "bytes:", len(html_doc))

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        page.goto(pathlib.Path(html_path).as_uri(), wait_until="load")
        page.wait_for_timeout(500)
        page.pdf(path=OUT_PDF, print_background=True, prefer_css_page_size=True)
        browser.close()
    print("PDF written:", OUT_PDF)
    print("size bytes:", os.path.getsize(OUT_PDF))


if __name__ == "__main__":
    main()
