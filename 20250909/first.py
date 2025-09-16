# -*- coding: utf-8 -*-
import pandas as pd

# Excel 파일 읽기 (헤더가 1번째 행에 있음을 지정)
file_path = r"C:\kkw\ABCD-C\20250909\data.xlsx"
df = pd.read_excel(file_path, header=1)

# 불필요한 첫 번째 컬럼 제거 (Unnamed: 0)
df = df.drop(df.columns[0], axis=1)

# 컬럼명의 공백 제거
df.columns = df.columns.str.strip()

# 데이터 확인
print("데이터 형태:", df.shape)
print("\n컬럼명:", df.columns.tolist())
print("\n첫 5행:")
print(df.head())

# 각 과목별 평균 계산
print("\n=== 과목별 평균 성적 ===")
korean_avg = df['국어'].mean()
english_avg = df['영어'].mean()
math_avg = df['수학'].mean()

print(f"국어 평균: {korean_avg:.2f}점")
print(f"영어 평균: {english_avg:.2f}점")
print(f"수학 평균: {math_avg:.2f}점")

# 전체 평균도 계산
total_avg = df[['국어', '영어', '수학']].mean().mean()
print(f"\n전체 평균: {total_avg:.2f}점")

# 각 과목별 통계 요약
print("\n=== 과목별 상세 통계 ===")
print(df[['국어', '영어', '수학']].describe())