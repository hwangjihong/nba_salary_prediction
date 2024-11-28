# NBA 선수 연봉 예측

NBA 선수의 경기 퍼포먼스 데이터를 기반으로 연봉을 예측하는 머신러닝 프로젝트입니다.

---

## 프로젝트 개요

이 프로젝트는 NBA 선수들의 경기 통계(득점, 어시스트, 리바운드, 슈팅 성공률 등)를 활용하여 연봉을 예측하는 것을 목표로 합니다. 회귀 모델과 고급 특징 엔지니어링 기법을 활용하여 선수 연봉에 영향을 미치는 주요 요인을 분석하고 예측합니다.

---

## 데이터 수집 방법

이 프로젝트에서는 **Selenium**과 **BeautifulSoup**을 사용하여 웹 크롤링을 통해 데이터를 수집하였습니다.

### **사용된 크롤링 기술**
- **Selenium**: 동적인 웹 페이지에서 데이터를 탐색하고 추출.
- **BeautifulSoup**: 정적인 HTML 페이지를 파싱하여 데이터를 정리 및 추출.
- 수집된 데이터는 `nba_stats_yyyy-yy.csv`, `nba_salary_yyyy-yy.csv` 형식으로 저장됩니다.

---

## 데이터 크롤링 사이트

### 1. [NBA 선수 개인 급여](https://www.espn.com/nba/salaries)
- **URL**: [https://www.espn.com/nba/salaries](https://www.espn.com/nba/salaries)
- **정보**: 
  - 각 시즌별 NBA 선수들의 급여 정보를 제공합니다.
  - 선수 이름, 순위, 급여 정보를 포함.
- **데이터 수집 방법**:
  - `requests`와 `BeautifulSoup`을 사용하여 HTML 페이지를 가져옵니다.
  - 테이블 데이터를 파싱하고 `pandas`를 사용하여 데이터프레임 형식으로 저장합니다.
  - 페이지네이션 처리로 모든 급여 데이터를 수집합니다.

### 2. [NBA 선수 개인 지표](https://www.nba.com/stats/players/traditional)
- **URL**: [https://www.nba.com/stats/players/traditional](https://www.nba.com/stats/players/traditional)
- **정보**:
  - NBA 선수들의 경기 통계를 제공합니다.
  - 주요 지표: 득점(PTS), 리바운드(REB), 어시스트(AST), 필드골 성공률(FG%), 3점 성공률(3P%) 등.
- **데이터 수집 방법**:
  - `Selenium`을 사용하여 동적 웹 페이지에서 데이터를 자동으로 로드합니다.
  - 드롭다운 메뉴를 조작하여 시즌 및 필터 조건을 설정.
  - 데이터를 추출한 뒤, `pandas`를 사용하여 데이터프레임 형식으로 변환합니다.

---

## 주요 기능

- **데이터 전처리**:
  - 결측값 처리 및 이상치 제거.
  - 변수 스케일링(정규화/표준화).
- **변수**:
  - 경기 지표(`PTS`, `REB`, `AST`, `FG%`...)등 활용하여 모델링.
  - 불필요한 변수 (`Unnamed: 0`, `W`, `L`, `PF`...)등 제거
- **모델 개발**:
  - 선형 회귀, 랜덤 포레스트 등 다양한 회귀 모델을 사용하여 연봉 예측.
- **결과 분석**:
  - 변수 중요도 분석 및 시각화.
  - 모델 성능 평가

---

## 모델링

### **사용된 모델**
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor
- Gradient Boosting Regressor
- K-Nearest Neighbors Regressor
- XGBoost Regressor

### **평가 지표**
- **RMSE** (Root Mean Squared Error): 평균 제곱근 오차.
- **R²** (R-Squared): 결정계수.

---
## 결과

### **모델 성능**
- **랜덤 포레스트 기준**:
  - **R²**: 0.711817
  - **RMSE**: $6,234,440
