# Git / Docker 개발환경 구축 및 데이터 영속성 검증 실습 기록

## 1. 프로젝트 개요
본 저장소는 Windows 환경에서 VSCode, Git, GitHub, Docker Desktop을 이용하여 개발 워크스테이션 환경을 구성하고, 커스텀 웹 서버 컨테이너 빌드, 포트 매핑 접속 검증 및 Docker Volume을 이용한 데이터 영속성 검증 과정을 문서화한 기술 문서이다.

### 핵심 목표
- VSCode 통합 터미널(Git Bash)을 활용한 Git/GitHub 버전관리 및 원격 저장소 연동
- Dockerfile을 통한 Nginx 커스텀 웹 서버 이미지 빌드 및 실행
- 호스트-컨테이너 간 포트 매핑(`-p 8080:80`) 접속 검증
- Docker Volume을 활용한 컨테이너 생명주기 독립적 데이터 영속성 검증

---

## 2. 실행 환경
- **OS:** Windows
- **Shell:** Git Bash
- **Editor / Terminal:** VSCode Integrated Terminal
- **Docker Version:** Docker version 29.9.2, build a82e528
- **Git Version:** git version 2.56.0.windows.4

---

## 3. 수행 항목 체크리스트

### 3-1. Git / GitHub
- [x] Git 설치 및 사용자 정보 설정 (`git config`)
- [x] 로컬 저장소 초기화 (`git init`) 및 기본 브랜치명 `main` 설정
- [x] GitHub 원격 저장소 연동 및 첫 커밋 Push
- [x] 파일 수정 후 `add` -> `commit` -> `push` 반복 실습
- [x] Merge 충돌 해결 및 재업로드 확인

### 3-2. 터미널 조작 및 기초 실습
- [x] VSCode 내 Git Bash 터미널 환경 구성
- [x] `hello-world` 컨테이너 실행 및 도커 데몬 정상 동작 확인
- [x] `ubuntu` 컨테이너 진입 (`-it`) 및 기본 CLI 명령어 (`ls`, `echo`) 수행

### 3-3. Docker 커스텀 이미지 및 서버 구축
- [x] Nginx 베이스의 커스텀 `Dockerfile` 작성
- [x] 커스텀 이미지 빌드 (`docker build -t my-web:1.0 .`)
- [x] 포트 매핑 옵션(`-p 8080:80`)을 이용한 웹 서버 실행
- [x] 웹 브라우저 접속(`http://localhost:8080`) 검증

### 3-4. Docker Volume 데이터 영속성 검증
- [x] Docker Volume 생성 (`docker volume create mydata`)
- [x] 1호 컨테이너(`vol-test`)에 볼륨 마운트 후 데이터 작성 (`hello.txt`)
- [x] 1호 컨테이너 강제 삭제 (`docker rm -f vol-test`)
- [x] 2호 컨테이너(`vol-test2`)에 동일 볼륨 마운트 후 데이터 유지 확인

---

## 4. 수행 과정 및 검증 로그

### 4-1. Dockerfile 작성 및 커스텀 이미지 빌드
`docker-basic/Dockerfile` 경로에 아래와 같이 커스텀 웹 서버 설계도를 작성함.

```dockerfile
FROM nginx:alpine
RUN echo "<h1>Hello, Codyssey Docker Web Server!</h1>" > /usr/share/nginx/html/index.html
EXPOSE 80
