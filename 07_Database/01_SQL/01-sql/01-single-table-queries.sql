-- 01. Querying data
-- 단일 필드 조회
SELECT LastName 
FROM employees;

-- 다중 필드 조회
SELECT LastName, FirstName 
FROM employees;

-- 전체 필드 조회
SELECT * 
FROM employees;

-- 별칭으로 조회
SELECT FirstName AS '이름' 
FROM employees;

-- NAME과 MILLESECONDS 분단위로
SELECT Name, Milliseconds / 60000 AS '재생시간(분)' 
FROM tracks;

-- 02. Sorting data
-- firstname 오름차순 정렬
SELECT FirstName
FROM employees
ORDER BY FirstName;

-- firstname 내림차순 정렬
SELECT FirstName
FROM employees
ORDER BY FirstName DESC;

-- customers에서 COUNTRY 기준 내림차순 정렬 후 CITY 필드 기준으로 오름차순 정렬
SELECT Country, City
FROM customers
ORDER BY Country DESC, City;

-- MILLESECONDS기준으로 내림차순 NAME과 MILLESECONDS 분단위로 조회
SELECT Name, Milliseconds / 60000 AS '재생시간(분)' 
FROM tracks
ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
SELECT ReportsTo
FROM employees
ORDER BY ReportsTo;

-- 03. Filtering data
-- DISTICT
-- CUSTOMERS에서 COUNTRY
SELECT Country
FROM customers
ORDER BY Country;

-- CUSTOMERS에서 COUNTRY 중복없이
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

-- WHERE
-- CITY값이 Prague인 LastName, FirstName, City 조회
SELECT LastName, FirstName, City
FROM customers
WHERE City = 'Prague';

-- CITY값이 Prague이 아닌 LastName, FirstName, City 조회
SELECT LastName, FirstName, City
FROM customers
WHERE City != 'Prague';

-- customers에서 Company가 NULL, Country가 ‘USA’인 데이터 LastName, FirstName, Company, Country 조회
SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NULL AND Country = 'USA';

-- customers에서 Company가 NULL이거나 Country가 ‘USA’인 데이터 LastName, FirstName, Company, Country 조회
SELECT LastName, FirstName, Company, Country
FROM customers
WHERE Company IS NULL OR Country = 'USA';

-- 테이블 tracks에서 Bytes 필드 값이 100000 이상 500000 이하인 데이터의 Name, Bytes 조회
SELECT NAME, Bytes
FROM tracks
WHERE BYTES BETWEEN 100000 AND 500000;

-- 테이블 tracks에서 Bytes 필드 값이 100000 이상 500000 이하인 데이터의 Name, Bytes 조회 (BYTES 오름차순)
SELECT NAME, Bytes
FROM tracks
WHERE BYTES BETWEEN 100000 AND 500000
ORDER BY Bytes;

-- 테이블 customers에서 Country 필드 값이 ‘Canada’ 또는 ‘Germany’ 또는 ‘France’인
-- 데이터의 LastName, FirstName, Country 조회
SELECT LastName, FirstName, Country
FROM customers
WHERE Country IN ('Canada', 'Germany', 'France');

-- 테이블 customers에서 Country 필드 값이 ‘Canada’ 또는 ‘Germany’ 또는 ‘France’가 아닌
-- 데이터의 LastName, FirstName, Country 조회
SELECT LastName, FirstName, Country
FROM customers
WHERE Country NOT IN ('Canada', 'Germany', 'France');

-- 테이블 customers에서 LastName 필드 값이 son으로 끝나는 데이터의 LastName, FirstName 조회
SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son';

-- 테이블 customers 에서 FirstName 필드 값이 4자리면서 ‘a’로 끝나는 데이터의 LastName, FirstName 조회
SELECT LastName, FirstName
FROM customers
WHERE FirstName LIKE '___a';

-- LIMIT
-- 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개만 조회
SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

-- 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 4번째부터 7번째 데이터만 조회
SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data
-- 예시
SELECT Country, COUNT(*)
FROM customers
GROUP BY Country;

-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
SELECT Composer, AVG(Bytes) AS avgOfBytes
FROM tracks
GROUP BY Composer
ORDER BY avgOfBytes DESC;

-- 에러
-- 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10 미만인 데이터 조회
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
WHERE avgOfMinute < 10
GROUP BY Composer;

-- 에러 해결
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
GROUP BY Composer
HAVING avgOfMinute < 10;