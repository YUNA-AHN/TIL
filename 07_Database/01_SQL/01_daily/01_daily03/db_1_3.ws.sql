-- 1번 이름이 건우이고, 지역정보가 경기도
SELECT first_name, country
FROM users
WHERE first_name = '건우' AND country = '경기도';

-- 2번 경기도 혹은 강원도에 살지 않고 나이가 20살 이상, 30살 이하 나이 오름차순
SELECT age, country
FROM users
WHERE country NOT IN ('강원도', '경기도') AND age BETWEEN 20 AND 30
ORDER BY age;