-- 계약 Contracts 테이블을 생성
-- 테이블 생성 CREATE TABLE
CREATE TABLE contacts (
    -- 컬럼명 자료형 제약조건
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    EMAIL TEXT NOT NULL UNIQUE
);

-- Alter
-- 1. 테이블 이름 변경
ALTER TABLE contacts
RENAME TO new_contacts;

-- 2. 컬럼 이름 변경
ALTER TABLE new_contacts
RENAME COLUMN name TO last_name;

-- 3-1. 컬럼 추가 address
-- 기존 데이터가 NULL로 입력되므로 NOT NULL 조건 불가능
-- DEFAULT 값을 추가해줌으로써 생성 가능
ALTER TABLE new_contacts
ADD COLUMN address TEXT NOT NULL DEFAULT "Unknown";

-- 3-2. 컬럼 삭제 address
ALTER TABLE new_contacts
DROP COLUMN address;