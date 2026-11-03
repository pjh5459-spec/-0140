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
- Docker version: `(Docker version 29.9.2, build a82e528)`
- Git version: `(git version 2.56.0.windows.4)`

---

## 3. 수행 항목 체크리스트

### 3-1. Git / GitHub
- [x] Git 설치 및 사용자 정보 설정
- [x] 로컬 저장소 초기화 (`git init`)
- [x] 첫 커밋 생성
- [x] 기본 브랜치명을 `main`으로 변경
- [x] GitHub 원격 저장소 연결
- [x] `push`를 통해 GitHub 업로드
- [x] 파일 수정 후 `add → commit → push` 반복 실습
- [x] `status / diff / add / commit` 차이 실습
- [x] merge 충돌 해결 후 push 성공

### 3-2. 터미널 / 편집 환경
- [x] VSCode에서 Git Bash 터미널 사용
- [x] 파일 저장과 터미널 명령 실행의 차이 이해
- [x] 기본 Git 명령어 실행 확인

### 3-3. Docker
- [x] Docker Desktop 설치
- [x] Docker 기본 실행 환경 준비
- [ ] Dockerfile 작성
- [ ] 포트 매핑 실습
- [ ] 볼륨 마운트 실습
- [ ] 권한 관련 이슈 정리

> 위 체크리스트는 현재까지 실제로 확인된 작업 기준이다.  
> 아직 수행하지 않은 항목은 이후 실습 후 업데이트한다.

---

## 4. 검증 방법

### 4-1. Git 상태 확인
명령어:
    git status

확인 목적:
- 현재 브랜치 확인
- 수정된 파일 존재 여부 확인
- 커밋 전/후 작업 트리 상태 확인

정상 예시:
    On branch main
    nothing to commit, working tree clean

---

### 4-2. Git 버전 확인
명령어:
    git --version

확인 목적:
- Git 설치 여부 및 버전 확인

기록 위치:
- 본 README의 `실행 환경` 항목

---

### 4-3. Docker 버전 확인
명령어:
    docker --version

확인 목적:
- Docker 설치 여부 및 버전 확인

기록 위치:
- 본 README의 `실행 환경` 항목

---

### 4-4. 원격 저장소 연결 확인
명령어:
    git remote -v

확인 목적:
- 현재 로컬 저장소가 어떤 GitHub 원격 저장소와 연결되어 있는지 확인

기록 위치:
- GitHub 저장소 페이지
- 본 README의 `결과 위치` 항목

---

### 4-5. 최근 커밋 확인
명령어:
    git log --oneline

확인 목적:
- 최근 커밋이 정상적으로 생성되었는지 확인
- README 수정 이력이 반영되었는지 확인

---

## 5. 결과 위치
- GitHub 저장소: `https://github.com/pjh5459-spec/-0140`
- 기술 문서 위치: `README.md`

> 위 GitHub 저장소 주소는 실제 본인 저장소 링크로 수정해야 한다.

---

## 6. 트러블슈팅

### 6-1. 문제: merge 충돌 또는 push 충돌 발생
문제 상황:
- 로컬 작업과 원격 저장소 내용이 달라 바로 `push`가 되지 않거나 충돌이 발생했다.

원인 가설:
- 원격 저장소에도 수정 내용이 있었고, 로컬 변경과 겹쳐 자동 병합이 어려운 상태였을 가능성이 있다.

확인:
- `git status` 확인
- 병합 과정에서 충돌 표시가 있는 파일 확인

해결 / 대안:
- 충돌이 난 파일을 열어 내용을 직접 정리했다.
- 이후 `git add` → `git commit` → `git push` 순서로 다시 반영했다.

---

### 6-2. 문제: 파일 편집과 터미널 입력 방식이 혼동됨
문제 상황:
- README 내용을 작성할 때 파일 편집과 터미널 명령 입력이 섞여 혼동되었다.

원인 가설:
- 터미널은 명령 실행용이고, 문서 작성은 에디터에서 해야 하는데 두 작업의 역할이 명확히 구분되지 않았기 때문이다.

확인:
- VSCode 편집기에서 `README.md`를 직접 수정하는 방식과
- 터미널에서 `git status`, `git add`, `git commit`, `git push`를 입력하는 방식을 다시 구분해서 확인했다.

해결 / 대안:
- 문서 내용은 VSCode 편집기에서 수정하고 저장한다.
- Git 명령은 터미널에서만 실행한다.
- 작업 순서를 고정해서 실수를 줄인다.

---

### 6-3. 문제: Git 상태 표시와 작업 흐름이 헷갈림
문제 상황:
- `status`, `add`, `commit`, `push`가 각각 어떤 역할인지 처음에는 혼동되었다.

원인 가설:
- Git은 단순 저장이 아니라 단계별 기록 방식이라, 각 명령어의 역할을 구분해서 이해해야 하기 때문이다.

확인:
- 파일 수정 후 `git status`로 상태를 보고,
- `git add` 후 다시 상태를 확인하고,
- `git commit`, `git push` 후 GitHub 반영 여부를 비교했다.

해결 / 대안:
- 아래 흐름으로 정리해서 이해했다.

작업 흐름:
1. 파일 수정
2. `git add` : 커밋할 변경사항 올리기
3. `git commit` : 로컬 저장소에 기록 남기기
4. `git push` : GitHub에 업로드하기

---

## 7. 현재까지 정리
현재까지 Git과 GitHub의 기본 흐름은 직접 수행했다.

- 저장소 생성
- 파일 수정
- `add`
- `commit`
- `push`
- GitHub 반영 확인
- 브랜치명 `main` 사용
- 충돌 해결 및 재업로드 확인

또한 Docker Desktop 설치까지 완료했으며,  
이후에는 Dockerfile, 포트 매핑, 볼륨 마운트 등  
컨테이너 활용 실습을 추가로 진행할 예정이다.

---

## 8. 향후 보완 예정 항목
- Dockerfile 작성 및 실행
- 포트 매핑 실습 결과 기록
- 볼륨 마운트 실습 결과 기록
- 필요 시 스크린샷 또는 실행 결과 추가
- README에 실제 버전 정보와 저장소 링크 반영