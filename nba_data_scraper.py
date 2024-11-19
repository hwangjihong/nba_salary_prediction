from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# Selenium을 사용하여 NBA 선수들의 개인 지표 크롤링
# 매개변수 seasons: 리스트 형태 예시 ['2024-25', '2023-24']
def get_player_stats(seasons):
    # Selenium WebDriver 초기화
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # 웹 페이지 로딩 대기 시간 설정
    
    perMode = "Totals"  # 게임 전체 지표
    statCategory = "PTS"  # PTS 순으로 정렬 (득점)
    seasonType = "Regular+Season"  # 정규 시즌
    
    # 주어진 시즌에 대해 반복
    for season_data in seasons:
        season = season_data  # 시즌 변수 설정
        
        # URL 생성 (선수 지표 조회 페이지)
        url = "https://www.nba.com/stats/leaders?"
        url += "PerMode=" + perMode
        url += "&StatCategory=" + statCategory
        url += "&Season=" + season
        url += "&SeasonType=" + seasonType
        
        # 페이지 로딩
        driver.get(url)

        # 드롭다운 메뉴에서 'All Players' 선택
        select_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select')
        select = Select(select_element)
        select.select_by_value("-1")  # 'All Players'를 선택
        
        # 테이블 HTML 추출
        table_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        table_html = table_element.get_attribute('outerHTML')
        
        # BeautifulSoup을 사용하여 HTML을 읽고 pandas로 변환
        df = pd.read_html(StringIO(table_html))[0]
    
    # WebDriver 종료
    driver.quit()

# BeautifulSoup을 사용하여 NBA 선수들의 급여 크롤링
# 매개변수 seasons: 리스트 형태 예시 ['2024', '2023']
def get_player_salary(seasons):
    # 주어진 시즌에 대해 반복
    for season in seasons:
        all_data = []  # 모든 데이터를 저장할 리스트
        
        # 기본 URL 설정 (시즌별 급여 정보)
        base_url = "https://www.espn.com/nba/salaries/"
        base_url += "_/year/" + season
        
        # 첫 페이지 요청 및 HTML 파싱
        response = requests.get(base_url, headers={'User-Agent':'Chrome'})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 페이지 수 계산 (전체 페이지가 몇 페이지인지)
        end_page = (soup.select_one('#my-players-table > div > div.mod-content > div > div.controls > div.page-numbers').text).split("of")[1]
        
        # 각 페이지에 대해 반복
        for i in range(1, int(end_page) + 1):
            # 각 페이지 URL 설정
            url = base_url + "/page/" + str(i)
            
            # 페이지 요청 및 HTML 파싱
            response = requests.get(url, headers={'User-Agent':'Chrome'})
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 테이블 추출
            table = soup.select_one('#my-players-table > div > div.mod-content > table')
            
            # 테이블을 pandas 데이터프레임으로 변환
            df = pd.read_html(StringIO(str(table)))[0]
            
            # 데이터프레임을 리스트에 추가
            all_data.append(df)
        
        # 모든 페이지에서 수집한 데이터프레임을 하나로 합침
        final_df = pd.concat(all_data, ignore_index=True)
        
        # 중복된 행 제거
        # 'RK', 'NAME', 'TEAM', 'SALARY' 컬럼을 기준으로 중복된 데이터를 제거하고, 첫 번째 항목만 남깁니다.
        final_df = final_df.drop_duplicates(subset=[0, 1, 2, 3], keep=False, ignore_index=True)
        
        # 불필요한 첫 번째 열(0) 삭제
        final_df = final_df.drop(0, axis=1)
        
        # 컬럼 이름 변경
        final_df.columns = ['NAME', 'TEAM', 'SALARY']
