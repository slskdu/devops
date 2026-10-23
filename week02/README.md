# 2주차 - 실습 환경 구축과 버전 관리 기초

## 2주차 수업 정리

이번 주에는 Windows에서 WSL2와 Ubuntu를 이용해 리눅스 실습 환경을 만들고, 기본적인 파일·디렉터리 명령어를 익히고 Git으로 파일 변경 이력을 기록하는 법을 배움

## 실습 명령어

wsl -l -v: 설치된 Linux 배포판과 WSL 버전을 확인한다.
wsl --install: WSL 기능과 기본 Ubuntu 환경을 설치한다.

mkdir: 디렉터리를 만든다.
cd: 디렉터리를 이동한다.
pwd: 현재 위치를 확인한다.
ls: 현재 디렉터리의 파일과 폴더를 확인한다.

touch: 빈 파일을 만든다.
echo "내용" > 파일: 파일에 내용을 새로 기록한다.
cat: 파일 내용을 출력한다.

cp: 파일을 복사한다.
mv: 파일을 이동하거나 이름을 바꾼다.
rm: 파일을 삭제한다.

git --version: Git 설치 버전을 확인한다.
git config: 커밋 작성자 정보와 기본 브랜치를 설정한다.

git init: 현재 디렉터리를 Git 저장소로 초기화한다.
git status: 파일의 변경 및 추적 상태를 확인한다.

git add: 변경한 파일을 다음 커밋에 포함하도록 준비한다.
git commit -m: 준비된 변경 사항을 메시지와 함께 기록한다.
git log --oneline: 커밋 기록을 한 줄씩 확인한다.

git switch -c: 새 브랜치를 만들고 이동한다.
git branch: 브랜치 목록을 확인한다.
git diff: 두 브랜치 또는 버전 사이의 변경 내용을 비교한다.
git log --all --graph: 모든 브랜치의 커밋 흐름을 그래프로 확인한다.

gh auth login: GitHub 계정에 로그인한다.
gh repo create: 현재 로컬 저장소를 바탕으로 GitHub 저장소를 만들고 원격 저장소를 연결한다.
--push: 로컬 커밋을 GitHub에 올린다.

git clone: GitHub 저장소와 커밋 이력을 로컬로 복제한다.
