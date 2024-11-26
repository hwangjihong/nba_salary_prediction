# NBA 선수들 급여 예측 프로젝트

## 데이터 수집 방법

이 프로젝트에서는 **Selenium**과 **BeautifulSoup**을 사용하여 웹 크롤링을 통해 데이터를 수집합니다. Selenium은 동적인 웹 페이지에서 데이터를 수집하는 데 사용되며, BeautifulSoup은 정적인 HTML을 파싱하는 데 사용됩니다. 수집된 데이터들은 nba_stats_yyyy-yy.csv, nba_salary_yyyy-yy.csv 형식으로 저장합니다.

### 사용된 웹 크롤링 기술

- **Selenium**: 동적인 웹 페이지에서 데이터를 자동으로 탐색하고 추출
- **BeautifulSoup**: HTML을 파싱하고 데이터를 정리하여 추출

---

## 데이터 크롤링 사이트

### 2. [NBA 선수 개인 지표](https://www.nba.com/stats/leaders)

- **URL**: [https://www.nba.com/stats/leaders](https://www.nba.com/stats/leaders)
- **정보**: 이 사이트는 NBA 선수들의 개인 지표를 제공합니다. 득점(PTS), 리바운드, 어시스트 등 다양한 통계를 확인할 수 있습니다.
- **데이터 수집 방법**:
    - `Selenium`을 사용하여 동적 페이지에서 데이터를 자동으로 로드합니다.
    - 페이지 내 드롭다운 메뉴에서 필요한 옵션을 선택한 후, 선수들의 지표를 포함한 테이블을 추출합니다.
    - `pandas`를 사용하여 테이블을 데이터프레임 형식으로 변환합니다.

### 1. [NBA 선수 개인 급여](https://www.espn.com/nba/salaries)

- **URL**: [https://www.espn.com/nba/salaries](https://www.espn.com/nba/salaries)
- **정보**: 이 사이트는 NBA 선수들의 급여 정보를 제공합니다. 각 시즌별로 선수들의 급여 순위를 확인할 수 있습니다.
- **데이터 수집 방법**:
    - `requests`와 `BeautifulSoup`을 사용하여 HTML 페이지를 가져옵니다.
    - 선수들의 급여 데이터를 포함한 테이블을 추출합니다.
    - 페이지네이션을 처리하여 모든 페이지에서 데이터를 수집합니다.
    - `pandas`를 사용하여 테이블을 데이터프레임 형식으로 변환합니다.
---

### 전체 프로세스 흐름

1. **데이터 수집**: Selenium과 BeautifulSoup을 활용하여 필요한 데이터를 웹에서 크롤링합니다.
2. **데이터 정리**: 크롤링한 데이터를 `pandas` 데이터프레임으로 정리하고, 불필요한 데이터를 제거하거나 변환합니다.
3. **급여 예측 모델**: 수집한 데이터를 기반으로 예측 모델을 학습시켜 NBA 선수들의 급여를 예측합니다.
