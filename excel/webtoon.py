import tablib

rows = [
    ['월요웹툰', '화요웹툰', '수요웹툰', '목요웹툰', '금요웹툰', '토요웹툰', '일요웹툰'],
    ['신의 탑', '마음의소리', '고수', '기기괴괴', '덴마', '호랑이형님', '열럽전사'],
    ['귀전구담', '노블레스', '퍼미스미션', '하루 3컷', '테러맨', '부활남', '다이스'],
    ['히어로메이커', '하이브', 'DEY 호러채널', '마술사', '오즈랜드', '유미의세포들', '조선왕조실톡'],
]

data = tablib.Dataset()
data.headers = rows[0]
for row in rows[1:]:
    data.append(row)

with open('webtoon.xlsx', 'wb') as f:
    f.write(data.xlsx)
