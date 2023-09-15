# ORM 문법 활용 전체 쿼리셋 id에 대해 내림차순 조회
Movie.objects.order_by("-id")

'''Out[9]: <QuerySet [<Movie: 4번째 영화 - Dune(adventure)>, <Movie: 3번째 영화 - 007 No Time To Die(action)>, <Movie: 2번째 영화 - Rons Gone Wrong(animation)>, <Movie: 1번째 영화 - Venom: Let There Be Carnage(action)>]>'''


# 내림차순+ genre가 action만 조회
Movie.objects.order_by("-id").filter(genre="action")

'''<QuerySet [<Movie: 3번째 영화 - 007 No Time To Die(action)>, <Movie: 1번째 영화 - Venom: Let There Be Carnage(action)>]>'''

# ORM 문법 활용 전체 쿼리셋 중 genre가 action만 조회
Movie.objects.filter(genre="action")
'''<QuerySet [<Movie: 1번째 영화 - Venom: Let There Be Carnage(action)>, <Movie: 3번째 영화 - 007 No Time To Die(action)>]>'''

# title이 e로 긑나는 것만 ㅈ회
Movie.objects.filter(title__endswith="e")
'''<QuerySet [<Movie: 1번째 영화 - Venom: Let There Be Carnage(action)>, <Movie: 3번째 영화 - 007 No Time To Die(action)>, <Movie: 4번째 영화 - Dune(adventure)>]>'''