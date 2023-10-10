-- 테이블 생성
CREATE TABLE animals (
    animal_name TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    age INTEGER
);

-- meal 컬럼 생성
ALTER TABLE animalS ADD COLUMN meal TEXT;

-- animal_name TO name
ALTER TABLE animals RENAME COLUMN animal_name TO name;

-- 테이블 명 변경
ALTER TABLE animals RENAME TO zoo;

-- 테이블 삭제
DROP TABLE zoo;