CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- SELECT
-- 이름과 나이 조회하기
SELECT first_name, age
FROM users;

-- 전체 데이터 조회하기
SELECT *
FROM users;

-- rowid와 이름 조회하기
SELECT rowid, first_name
FROM users;

-- ORDER BY
-- 이름과 나이를 나이가 어린 순서대로 조히하기
SELECT first_name, age
FROM users
ORDER BY age;

-- 이름과 나이를 나이가 많은 순으로 정렬
SELECT first_name, age
FROM users
ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 같은 나이라면 계좌 잔고가 많은 순으로 정렬
SELECT first_name, age, balance
FROM users
ORDER BY age, balance DESC;

-- DISTINCT 
-- 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country
FROM users
ORDER BY country;

-- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country
FROM users;

-- WHERE
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고
SELECT first_name, age, balance
FROM users
WHERE age >= 30;

-- 나이가 30살 이상 + 50만원 초과 사람들의 이름, 나이, 계좌 잔고
SELECT first_name, age, balance
FROM users
WHERE age >= 30 AND balance > 500000;

-- LIKE
-- 이름에 '호'가 들어가는 모든 사람들을 조회하기
SELECT first_name, last_name
FROM users
WHERE first_name LIKE '%호%';

-- 이룸이 '준'으로 끝나는 모든 사람 조회하기
SELECT first_name
FROM users
WHERE first_name LIKE '%준';

-- 핸드폰 번호가 010으로 시작하는 사람들의 이름, 핸드폰 번호 조회
-- 하이픈 체크!
SELECT first_name, phone
FROM users
WHERE phone LIKE '010-%';

-- 서을 지역 번호를 가진 사람 조회
SELECT first_name, phone
FROM users
WHERE phone LIKE '02-%';

-- 나이가 20대 인사라
SELECT first_name, age
FROM users
WHERE AGE LIKE '2_';
-- AGE/10 = 2
-- BETWRRN 20 AND 29 : 얘가 젤 빠름

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화 번호 조회하기
SELECT first_name, phone
FROM users
WHERE phone LIKE '%-51__-%';

-- IN
-- 경기도 강원도에 사는 사람들의 이름과 지역 조사하기
SELECT first_name, country
FROM users
WHERE country IN ("강원도", "경기도");

-- 경기도 강원도에 살지 않는 사람들의 이름과 지역 조사하기
SELECT first_name, country
FROM users
WHERE country NOT IN ("강원도", "경기도");

-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance
FROM users
ORDER BY balance DESC
LIMIT 10;

-- USERS 테이블의 행의 갯수 출력하기, 별칭 영어면 '', AS 생략 가능
SELECT COUNT(*) AS 'ROW_COUNT'
FROM users;

-- USERS 테이블 내에서 잔액의 평균을 출력
SELECT AVG(balance) AS avg_balance
FROM users;

-- 전라북도의 평균 BALANCE 출력
SELECT country, AVG(balance) AS avg_balance
FROM users
WHERE country = '전라북도';

-- 각 지역별 평균 BALANCE 출력
SELECT country, AVG(balance) AS avg_balance
FROM users
GROUP BY country;

-- 각 지역별 평균 내림차순 BALANCE 출력
SELECT country, AVG(balance) AS avg_balance
FROM users
GROUP BY country
ORDER BY avg_balance DESC;

-- 나이가 30살 이상인 사람들의 평균 나이를 계산하라
SELECT AVG(age)
FROM users
WHERE age >= 30;

-- 각 지역별로 몇 명 살고 있는지 조회
SELECT COUNT(*) AS PEOPLE
FROM users
GROUP BY country;

-- 성씨 별로 몇명 있는 지 조히
SELECT last_name, COUNT(*) AS PEOPLE
FROM users
GROUP BY last_name;

-- 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) AS PEOPLE
FROM users
GROUP BY last_name
ORDER BY PEOPLE DESC;

-- 각 지역별 평균 나이 조회
SELECT country, AVG(age) AS avg_age
FROM users
GROUP BY country;

-- Changing data
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

-- INSERT
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

-- 여러 행 삽입하기
INSERT INTO classmates
VALUES 
('김철수', 30, '경기'),
('이영미', 31, '강원'),
('박진성', 26, '전라'),
('최지수', 12, '충청'),
('정요한', 28, '경상');

-- UPDATE
-- 2번 데이터의 이름을 '김철수한무두루미' 주소를 '제주도'로 수정하기
UPDATE classmates
SET name = '김철수한무두루미',
    address = '제주도'
WHERE ROWID = 2 ;

-- DELETE
-- 5번 데이터 삭제하기
DELETE FROM classmates WHERE ROWID = 5;
SELECT ROWID, * FROM classmates;

-- 이름에 영이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;

-- JOIN
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    userid INTEGER NOT NULL
);

DROP TABLE users;
CREATE TABLE users(
    name TEXT NOT NULL,
    roleid  INTEGER PRIMARY KEY AUTOINCREMENT,
);

INSERT INTO articles (title, content, userid)
VALUES  ('제목1', '내용1', 1),
        ('제목2', '내용2', 2),
        ('제목3', '내용3', 3);


INSERT INTO users (name, roleid)
VALUES  ('adien', 1),
        ('ken', 2),
        ('lynda', 3);

-- 크로스 조인
SELECT * FROM articles, users;