import os
import pandas as pd
import lxml
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

# streamlit 페이지 생성
st.set_page_config(
    page_title='5문항 설문 결과 시각화',		# 브라우저 탭 제목
    page_icon = ":bar_chart:",				# 브라우저 파비콘
    layout = "wide"							# 레이아웃
    )

# 파일 읽어오기
def read_csv_files():
	path = "./data"
	file_list = os.listdir(path)
	lst_csv = [file for file in file_list if file.endswith(".csv")]	# 폴더내 확장자가 엑셀파일 인것을 리스트에 담기
	# '_'로 구분했을 때 마지막
	return lst_csv

# 마지막 파일 선택하기
def get_lastest_file():
    lst_csv = read_csv_files()
    lst_csv.sort()
    return lst_csv, lst_csv[-1]

lst_csv, default_ix = get_lastest_file()	# 파일 목록과 최신 파일 선택하기

# 데이터 파일 불러오기
def get_csvfile(p_file):
	df = pd.read_csv(f'./data/{p_file}', index_col=None)
	return df

# --- 사이드바 생성하기 ---
st.sidebar.header("Please Fliter Here:")	# 사이드바 헤더

# 파일 선택하기
file_csvs = st.sidebar.selectbox(
	"Select data file:",
	lst_csv,
	index=lst_csv.index(default_ix)
)

# 데이터프레임 생성
df = get_csvfile(file_csvs)
st.dataframe(df)