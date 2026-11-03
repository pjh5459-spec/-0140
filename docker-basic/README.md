# Git / Docker 개발환경 실습 기록

## 1. 프로젝트 개요
이 저장소는 Windows 환경에서 VSCode, Git, GitHub, Docker Desktop을 이용해
기본 개발환경을 구성하고, 실습 내용을 문서화한 기록이다.

이번 미션의 목표는 다음과 같다.

- VSCode에서 터미널을 사용해 Git 명령어를 실행할 수 있다.
- 로컬 저장소를 생성하고 GitHub 원격 저장소와 연결할 수 있다.
- 파일 수정 → add → commit → push 흐름을 반복 수행할 수 있다.
- Docker Desktop을 설치하고 기본 명령어를 확인할 수 있다.
- README 문서만 읽어도 수행 내용과 현재 상태를 파악할 수 있도록 정리한다.

---

## 2. 실행 환경
- OS: Windows
- Shell: Git Bash
- Editor / Terminal: VSCode Integrated Terminal
- Docker: Docker Desktop
- Docker version: `(docker --version 결과 입력)`
- Git version: `(git --version 결과 입력)`

---

## 3. 수행 항목 체크리스트

### Git / GitHub
- [x] Git 설치 및 사용자 정보 설정
- [x] 로컬 저장소 초기화 (`git init`)
- [x] 첫 커밋 생성
- [x] 기본 브랜치명을 `main`으로 변경
- [x] GitHub 원격 저장소 연결
- [x] `push`를 통해 GitHub 업로드
- [x] 파일 수정 후 `add → commit → push` 반복 실습
- [x] `status / diff / add / commit` 차이 실습
- [x] merge 충돌 해결 후 push 성공

### 터미널 / 편집 환경
- [x] VSCode에서 Git Bash 터미널 사용
- [x] 파일 저장과 터미널 명령 실행의 차이 이해

### Docker
- [x] Docker Desktop 설치
- [x] Docker 기본 실행 환경 준비
- [ ] Dockerfile 작성
- [ ] 포트 매핑 실습
- [ ] 볼륨 마운트 실습
- [ ] 권한 관련 이슈 정리

> 체크리스트는 현재까지 확인된 작업 기준이며,
> 미수행 항목은 이후 실습 후 업데이트할 예정이다.

---

## 4. 검증 방법

### 4-1. Git 상태 확인
```bash
git status
