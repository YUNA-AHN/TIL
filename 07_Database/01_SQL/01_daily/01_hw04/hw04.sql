-- 쿼리문 작성
CREATE TABLE users (
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber TEXT NOT NULL,
    gender INTEGER,
    address TEXT NOT NULL DEFAULT 'no address'
);

-- phoneNumer 컬럼 number로 변경
ALTER TABLE users RENAME COLUMN phoneNumber TO number;

-- user 제거하는 쿼리문
DROP TABLE users;