# git (오픈소스)
## 1. 분산 버전 관리 시스템 
- 파일 히스토리를 저장하는 도구
- 과거 특정 시점으로 되돌어가거나, 한번에 여러 버전으로 개발자들이 동시에 작업이 진행 가능하다! (브랜치 기능)

개발 현업에서 대항마가 없음 ex) Vue3 <-> React

### 특징 
---
- 코드의 히스토리(버전)을 관리하는 도구
- 개발되어온 과정 파악 가능
- 이전 버전과의 변경 사항 비교 및 분석

## 2. 성능
- Unix를 만든 GNU에서 git 개발 + 오픈소스(무료)로 배포하면서 독점! 
- 이전에 있었던 모든 버전관리 프로그램보다 선능이 월등이 빨랐음
- 대용량 프로젝트를 효율적으로 관리 가능
- Bit keeper : 라이센스 이슈

## 3. 커뮤니티
- 오픈소스 소프트웨어  
-> 커뮤니티 기반으로 개발이 누구나 참여 가능(활발한 의견 교류)

## 4. 공개 저장소 
- 사용자들이 공개 저장소(github)를 이용해서 프로젝트를 공유
- 프로젝트 관리/팀 개발 용이

# 버전관리
컴퓨터 소프트웨어의 특정 상태들을 관리하는 것
ex)  최종/최최종/진짜최종 st  
-> 파일에 날짜와 시간을 적어봐 !
-> 스냅샷 방식 : 원본 파일 + 수정사항을 저장하여 백업할 수 있도록 하는 것 -> 히스토리도 남길 수 있고 돌아갈 수 있음

**중앙집중식 버전 관리**  
---
원격 저장소에서 최신 파일만 다운 받아서 사용
1) 원격 서버에서 별도의 PC 에서 히스토리 가지지 않고 가볍게 사용할 수 있음
2) 관리자가 모든 히스토리를 쉽게 관리할 수 있음
but 원격서버에 사고 발생 -> 더 이상 사용할 수 없음

**분산 버전 관리** 
---
히스토리를 포함해서 모든 버전을 복제하는 것

**장점**
1) 각각의 PC에서 자유롭게 관리 가능함 
2) 원격 서버 다운되어도 사용 가능!
3) 다른 PC에 전달 가능  

**단점**
1) DB 용량 자체가 크다! (히스토리 용량부담)
-> 무거운 자료 올렸다가 삭제해도 히스토리에 남음
2) 나중에 하나로 합쳤을때(merge) 병합할 때 충돌 발생 가능
-> PC1, PC2에서 각각 같은 버전을 수정해서 병합할 때 충돌 발생

# github
웹 호스팅 서비스  
gitlab / github / bitbuket  
**git -> 분산버전관리시스템
-> 웹호스팅 서비스**  
git(시스템) : 커피  
github(버전관리웹호스팅서비스) : 커피숍

**버전관리한다는 점은 동일하다!**

github 사용이유
---
1) git을 이용한 버전 관리
2) github를 이용한 포트폴리오 - 잔디 심기/웹뷰 카드

## GUI와 CLI
**GUI (graphic user interface)** 
: 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식  
-> 사용하기 쉽지만 단계가 많고, 컴츄터의 성능을 더 많이 소모  
**CLI (command line interface)**
: 콘솔창에서 키보드로 명령어 입력해서 컴퓨터 조작하게 하는 인터페이스
명령어를 통해 사용자와 컴퓨터가 상호작용하는 방식  
-> 텍스트 형태의 현재 경로와 옮길 경로를 알아야한다!  
-> 수많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공 : 개발환경 충분히 구축할 줄 알아야 gka

### 절대 경로와 상대 경로
---
**절대 경로**
루트 디렉토리부터 모적 지점가지 거치는 모든 경로를 전부 작성한 것  
윈도우 바탕 화면의 절대 경로 : C:/Users/ssafy/Desktop

**상대 경로**
현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 저장한 것  
현재 작업하고 있는 디렉토리가  C:/Users일때
윈도우 바탕화명으로의 상대경로: ./ssafy/Desktop

**./ : 현재 작업하고 있는 폴더  
../ : 현재 작업하고 있는 폴더의 부모 폴더**

C:/Users/ssafy/Desktop == ./ssafy/Desktop
-> 지역번호와 유사.. 같은 지역은 지역번호 생략 가능!

## gitbash 명령어
```~ : 메인 홈 디렉토리 
pwd : 현재 경로 출력 (pirnt working directory)
ls : 현재 작업 중인 디렉토리의 폴터/파일 목록을 보여주는 명령어
ls -al : 파일 경로, 권한 등을 볼 수 있음
clear : 화면 지우기
cd : 현재 작업중인 디렉토리 변경(change directory)
touch : 파일 생성 -> 한번에 여러 파일 생성 가능 ! 띄어쓰기로 구분
Mkdir : Mkdir
pwd > temp.txt : pwd를 temp.txt 파일에 작성(이전 내용 초기화 된다.)
echo "빨강: >> temp.txt : 기존 내용에 추가
echo " " : 내용을 콘솔 출력으로 내보낼 수 있음
cat orange : 해당 파일 내용 확인할 수 있음
rm : 파일 삭제 (-r : 옵션 추가시 폴더 삭제 가능)
```

**git bash 실습 예제**
---
```
1. 현재 디렉토리 출력 : pwd 
2. sample 디렉토리 생성 : Mkdir sample
3. sample 로 작업디렉토리 이동: cd sample
4. 현재 디렉토리 출력 : /c/Users/SSAFY/> sample
5. red, orange, white 파일 추가 : touch red orange white
6. red 파일에 "빨강" 내용 추가 : echo "빨강" > red
7. orange 파일에 "주황" 내용 추가 : echo "주황" >> orange
8. 현재 디렉토리 출력 :  pwd
9. white 파일 삭제 : rm white
10. 현재 디렉토리 출력 : pwd
11. sample : 디렉토리 삭제  
-> 부모 디렉토리로 이동 cd ../  
-> sample 삭제 : rm -r sample
12. 패턴이 동일한 파일 삭제 (1.txt 2.txt 3.txt) : rm *.txt
```
## 마크다운
- 텍스트 기반의 가벼운 마크업 언어  
	-> 태그를 이용하여 문서의 구조를 나타내는 것
- 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
- 깃허브 문서의 시작과 끝!  
    - README.md 파일을 통해 오픈 소스의 공식 문서 작성  
    - 개인 프로젝트의 소개 문서 작성
    - 매일 학습한 내용 정리  
    - 마크다운을 이용한 블로그 운영

- github 관련 사이트 https://soo-vely-dev.tistory.com/159#--%C-%A-shiedls-io
- 아이콘 https://simpleicons.org/?q=python

## Repository
- 특정 디렉토리를 버전 관리하는 저장소  
- 히스토리, 태그, 브랜치(버전에서 뻗어나는)
- git init 명령어로 로컬 저장소를 생성
- .git 디렉토리에 버전 관리에 필요한 모든 것이 들어 있음 << 숨김 폴더로 생성된다!

새 폴더에서 README.md 파일 생성하기  
cd /c/SSAFY/TestRepo/ : 디렉토리 변경  
git init : 레파지토리 생성  
(master) 이 브랜치 내에서 작업을 할   것이다...?  
깃 만들어서 VScode로 가서 문서 작성 가능함

터미널>뉴터미널>아래버튼>select default terminal profile  
ctrl+j : 터미널 on/off

이 파일을 버전을 관리하여 git 사용해보기!
-> 특정 버전으로 남긴다 = 커밋(commit)한다! : 3가지 영역을 바탕으로 동작!

**3가지 영역**
Woking Directory : 내가 작업하고 있는 실제 디렉토리
Staging Area : 커밋으로 남기고 싶은 특정 버전으로 관리하고 싶은 파일이 있는 곳
히스토리(커밋)를 기록하기전 대기 stage : 완충지대
-> 우리가 생성한 readme 파일이 커밋하기 전 상태
Repository : 커밋들이 저당되는 곳
이전 단계에서 커밋을 하면 버전 관리가 되는 저장소...!

Git Staging Area가 있는 이유
---
1. 일부분만 커밋하고 싶을 때
: 워킹 디렉토리 골라서 커밋하고 싶을 때 -> 완충지대에서 선택하여 하나의 커밋으로 해결할 수 있음!

2. 충돌을 해결할 때
: 협업 과정에서 여러 사람이 파일 작업 중 수정사항이 겹치는 영역에 대해서 Staging Area를 통해 충돌을 해소

3. 커밋을 다시 고치고 싶을 때
로그 메시지만 고치는게 아니라, 파일을 수정해서 다시 커밋(버전을 수정)하고 싶다면 'commit --amend'

Woking Directory - untracked된 파일을 git add README.md
Staging Area - tracked git(추적되고 있는 상태) git commit -m "메세지"
-> 올릴 때 누구인지?! Gmail/username
Repository



로컬 레파지토리 명령어
---
```
git config --global user.email "yunanash1234@gmail.com"
git config --global user.name "yuna-ahn"
git add . : 해당 폴더의 모든 파일을 스테이지에 올리는 것
git commit -m "첫번째 커밋"
git log : 로그 보여준다.
git status : 현재 상황 - 수정하고 스테이지 안올렸으면 빨간불 떠있음 !!
Q키 누르면 에디터 상황에서 빠져 나올 수 있음
```

git commit 실습
```1. 바탕화면에 edu_git_commit 폴더를 만들고 git 저장소를 생성해주세요
- 워킹디렉토리 변경
cd C:/Users/SSAFY/Desktop/edu_git_commit/
git 저장소 생성
git init

2. 해당 폴더 안에 a.txt 라는 텍스트 파일을 만들고 "add a.txt"라는 커밋 메세지로 커밋을 만들어주세요.
> a.txt 생성
touch a.txt
> 스테이지에 올리기
git add a.txt
> 커밋
git commit a.txt -m 'add a.txt'

3. 해당 폴더 안에 b.txt 라는 텍스트 파일을 만들고 "add b.txt"라는 커밋 메세지로 커밋을 만들어주세요.
> b.txt 생성
touch b.txt
> 스테이지에 올리기
git add b.txt
> 커밋
git commit b.txt -m 'add b.txt'

4. a.txt 파일을 수정하고, "update a.txt"라는 커밋메세지로 커밋을 만들어주세요
> a.txt 수정
pwd >>  a.txt
> 스테이지에 올리기
git add a.txt
> 커밋
git commit a.txt -m "update a.txt'

```

## source tree 
활용하면 더 간편하게 사용 가능!  
우클릭 > 브랜치가지 초기화 (soft/mix/hard)
깃허브 레포지토리 가져오려면 클론에서 해당 래포지토리 주소 가져오기!

github - local
깃허브와 로컬이 동기화되어있는 상태는 X
깃허브(원격)를 업데이트 시켜줘야한다!

git remote add origin {remote_repo}
git pusg -u origin master

로컬 ->원격  : push
원격 -> 로컬 : pull

TIL : Today I Learned
매일 내가 배운 것을 마크다운으로 정리해 문선화 하는 것
신입 개발자에게 요구되는 가장 큰 능력!
