정규표현식을 활용한 대동제로그 데이터 분석
프로젝트 소개

이 프로젝트는 Python의 re 모듈(정규표현식)을 사용하여 대동제 및 해커톤 운영 로그 데이터에서 필요한 정보를 추출하는 프로그램입니다.

로그 데이터에서 GitHub 저장소 주소, 유효 쿠폰 코드, 부스별 매출액을 추출하고 전체 매출을 계산합니다.

개발 환경
Python 3.x
re (Regular Expression)
구현 기능
1. GitHub 저장소 URL 추출

GitLab 주소를 제외하고 GitHub 저장소 주소만 추출합니다.

정규식

Python
r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?'

결과

https://github.com/dawn-coders/campus-mate
https://github.com/bug-hunters-kr/smart-timetable
http://github.com/gpa-guardian/lecture-summary.git
2. 2026년도 유효 쿠폰 코드 추출

정규식

Python
r'FEST-2026-[A-Z0-9]{4}'

결과

FEST-2026-DC01
FEST-2026-BH99
FEST-2026-GP77
3. 부스별 매출액 추출

정규식

Python
r'매출:\s*([\d,]+)원'
 

결과

1,350,000
2,180,500
840,000
1,920,000
4. 전체 매출 합계 계산

사용 코드

Python
total = sum(int(s.replace(',', '')) for s in sales)

결과

6,290,500원

실행 방법
Shell
python main.py
학습 내용
정규표현식 기본 문법 학습
re.findall() 활용
캡처 그룹 () 사용
문자열 데이터 추출 및 가공
replace()를 이용한 문자열 처리
숫자 데이터 합산 처리


작성자 
Lee
