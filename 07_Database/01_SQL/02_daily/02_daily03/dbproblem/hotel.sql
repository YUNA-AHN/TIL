-- 테이블 생성
CREATE TABLE hotel (
    room_num TEXT NOT NULL,
    check_in TEXT NOT NULL,
    check_out TEXT NOT NULL,
    grade  TEXT NOT NULL
);

-- 컬럼 추가
ALTER TABLE hotel ADD COLUMN price INTEGER NOT NULL DEFAULT 0;

-- 데이터 추가
INSERT INTO hotel
VALUES
    ('B203', date('2021-12-31'), date('2022-01-03'), 'suite', 900),
    ('1102', date('2022-01-04'), date('2022-01-08'), 'suite', 850),
    ('303', date('2022-01-01'), date('2022-01-03'), 'deluxe', 500),
    ('807', date('2021-01-04'), date('2022-01-07'), 'superior', 300),
    ('B205', date('2022-01-04'), date('2022-01-07'), 'deluxe', 550);


-- 방번호 807호인 경우 체크인 날짜 수정
UPDATE hotel
SET check_in = '2022-01-04'
WHERE room_num = 807;

-- 객실의 위치가 지하 혹은 등급이 DULUXE인 객실의 모든 정보
SELECT *
FROM hotel
WHERE room_num LIKE 'B%' OR grade = 'deluxe';