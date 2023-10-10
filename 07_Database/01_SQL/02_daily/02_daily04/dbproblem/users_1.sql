-- 테이블 생성
CREATE TABLE users (
    first_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT ,
    balance INTEGER NOT NULL
);

-- 데이터 추가
INSERT INTO users
VALUES
    ('미현', '김', 19, '경기도', '011-211-8482', 300),
    (NULL, '최', 33, '제주특별자치도', NULL, 300),
    ('미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
    ('남석', '박', 18, '경기도', '011-484-8667', 260),
    ('철수', '박', 22, '경상남도', '016-295-8989', 500),
    (NULL, '박', 45, '전라남도', NULL, 320),
    ('민준', '이', 35, '전라남도', '019-965-8833', 350),
    (NULL, '남', 24, '충청남도', '010-5882-5969', 210),
    ('신', '유', 29, '경상북도', '010-4949-2848',290),
    (NULL, '김', 18, '대전광역시', NULL, 300);

-- 나이가 25 미만인 사람들의 ID AGE BALANCE를 AGE는 내림, BAL은 오름차순
SELECT rowid, age, balance
FROM users
WHERE age < 25
ORDER BY age DESC, balance;

-- first_name존재, BALANCE가 400보다 큰 사람의 FIRST_NAME과 BALANCE
SELECT first_name, balance
FROM users
WHERE first_name IS NOT NULL AND balance > 400;

-- phone null인 사람드의 정보를 알 수 없음으로 수정
UPDATE users
SET phone = '알 수 없음'
WHERE phone IS NULL;

SELECT *
FROM users;