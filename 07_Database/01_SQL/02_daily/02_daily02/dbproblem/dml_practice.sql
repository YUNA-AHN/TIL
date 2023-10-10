-- 테이블 생성
CREATE TABLE zoo (
    name TEXT NOT NULL,
    eat TEXT NOT NULL,
    weight INTEGER NOT NULL,
    height INTEGER,
    age INTEGER
);

-- 데이터 추가
INSERT INTO zoo
VALUES
    ('gorilla', 'omnivore', 215, 180, 5),
    ('tiger', 'carnivore', 220, 115, 3),
    ('rabbit', 'herbivore', 3, 150, NULL),
    ('elephant', 'herbivore', 3800, 280, 10),
    ('dog', 'omnivore', 8, 20, 1),
    ('eagle', 'carnivore', 8, 75, NULL),
    ('dolphin', 'carnivore', 210, NULL, 3),
    ('alligator', 'carnivore', 250, 50, NULL),
    ('panda', 'herbivore', 80, 90, 2),
    ('pig', 'omnivore', 70, 45, 5);

--  모든 동물의 이름과 키를 조회
SELECT name, height
FROM zoo;

-- 토끼 키를 15로 수정, 토끼 조회
UPDATE zoo
SET height = 15
WHERE name = 'rabbit';

-- 잡식 동물 데이터 삭제
DELETE FROM zoo WHERE eat = 'omnivore';