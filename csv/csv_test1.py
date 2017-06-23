lines = """월요웹툰,화요웹툰,수요웹툰,목요웹툰,금요웹툰,토요웹툰,일요웹툰
신의 탑,마음의소리,고수,기기괴괴,덴마,호랑이형님,열럽전사
귀전구담,노블레스,퍼미스미션,하루 3컷,테러맨,부활남,다이스
히어로메이커,하이브,DEY 호러채널,마술사,오즈랜드,유미의세포들,조선왕조실톡"""

# UTF8로 인코딩했을 때 Excel2010에서 한글이 제대로 열리지 않는다.
# Excel -> 데이터 -> 외부 데이터 가져오기 -> 텍스트 
# 위와 같은 방식을 파일을 열어야 한다.
# 의외로 메모장으로 파일을 열면 잘 보인다
with open('webtoon_utf8.csv', 'wt', encoding='utf8') as fo:
    fo.write(lines)

"""
인코딩 옵션을 입력하지 않으면 windows에서는 자동으로 cp949로 인코딩 된다.
cp949로 인코딩된 csv파일은 엑셀과 메모장으로 확인하는데 불편함이 없다.
"""
with open('webtoon_cp949.csv', 'wt') as fo:
    fo.write(lines)
