CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 데이터 입력 순서가 올바르지 않음  : 입력하고자 하는 순서대로 컬럼명 지정
INSERT INTO zoo (age, height, weight, name, eat) VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) rowid는 암시적 자동 증가 컬럼으로 동일한 값 입력 불가능
-- 지금까지 생성된 데이터의 rowid 값보다 크게 입력하면 실행은 되나, 지정한 값으로 입력되지는 않음...
INSERT INTO zoo (name, eat, weight, age) VALUES
('dolphin', 'carnivore', 210, 3),
('alligator', 'carnivore', 250, 50);

-- 3) weight에 null 값을 허용하지 않으므로 입력해주어야 하다. 
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 105);
