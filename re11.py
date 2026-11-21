import re
"""


1. 유효한 이메일 추출: 문서 전체에서 올바른 형식의 이메일 주소만 모두 추출하시오. (단, 도메인 형식이 손상된 hyunwoo@.ac.kr은 제외)

2. 휴대폰 번호 추출: 010으로 시작하고 중간 4자리, 끝 4자리로 구성된 휴대폰 번호만 모두 추출하시오. (구분자는 -, ., 공백 모두 허용하며 지역번호 02 및 자릿수 부족 번호 제외)

3. 본교 재학생 학번과 학과 분리 추출: 대괄호([학번 / 학과]) 표기 중 202로 시작하는 9자리 학번과 학과명을 튜플 (학번, 학과) 형태로 추출하시오.

4. GitHub 저장소 및 유효 쿠폰 추출: gitlab.com을 제외한 github.com 저장소 URL만 추출하시오. 2026년도에 발급된 유효 쿠폰 코드(FEST-2026-XXXX)만 추출하시오.

5. 부스별 총 매출액 추출 및 합산: 정산 내역에서 카드/현금 세부 내역이나 쿠폰 금액(5,000원)을 제외하고, 각 부스의 총 매출액(매출:  뒤에 오는 금액)만 추출하여 전체 매출 합계를 구하시오.



"""


with open("./07_02jj.txt", encoding="utf-8") as f:
    data = f.read()

    email = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\.\w+)+', data)

    phone = re.findall(r'010[- ,.]+\d{4}[- ,.]+\d{4}', data)

    students = re.findall(r'(202\d+)\s*/\s*([가-힣]+과)', data)

    github_urls = re.findall(
        r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?', data)

    coupons = re.findall(r'FEST-2026-[A-Z0-9]{4}', data)

    # 발급 쿠폰: FEST-2026-BH99

    print(f"email:{email}")
    print(f"phone:{phone}")
    print(f"students:{students}")
    print(f"github_urls:{github_urls}")
    print(f"coupons:{coupons}")

    sales = re.findall(r'매출:\s*([\d,]+)원', data)

    total = sum(int(s.replace(',', '')) for s in sales)

    print("추출된 매출:", sales)
    print("총합:", format(total, ',d'), "원")
