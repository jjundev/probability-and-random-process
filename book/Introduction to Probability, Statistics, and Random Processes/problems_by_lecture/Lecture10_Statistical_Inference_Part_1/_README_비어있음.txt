Lecture 10 — Introduction to Statistical Inference: Part 1
============================================================

이 폴더는 의도적으로 비어 있습니다 (문제 없음).

[이유]
Lecture 10 주제 = 통계적 추론 (MAP / LMS(MMSE) / LLMS(선형MMSE) / ML 추정,
베이지안 추론 framework). Pishro-Nik 교재에서는 8장(Classical) · 9장(Bayesian)에 해당.

그런데 이 IPSRP 은행에는 추론 문제 원본이 없습니다:
  - origin/ 에는 3~7장 PDF만 있음 (8장·9장 없음)
  - problems_png/ 에는 3.3.x ~ 7.3.x 만 추출되어 있음 (8.x·9.x 없음)

[채우려면]
1) Pishro-Nik 8장(Statistical Inference I) · 9장(Bayesian Inference) PDF를
   origin/ 에 추가
2) python/extract_pishro_nik_problems.py 로 8.x·9.x 문제 이미지 추출
3) python/extract_problem_texts.py 로 텍스트 추출
4) classification.json 에 해당 문제 → 10 으로 분류 후 이 폴더로 이동

[참고] 다른 은행(Probability_and_Stochastic_Processes_Problems)에는
Lecture 10 문제가 있습니다 → 12장(Estimation of a Random Variable) 전체 35문제가
Lecture10_Statistical_Inference_Part_1/ 에 분류되어 있음.
