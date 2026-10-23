# 4주차 - 자동차와 협업

## 수업 내용 요약

이번 주에는 로그 파일에서 필요한 내용을 검색하고, 실행 중인 프로세스를 확인·관리하는 방법을 실습했다. 
또한 파일과 디렉터리를 압축해 백업하고 복원한 뒤 원본과 비교해 결과를 확인하는 법도 배우고 
Pull Request 검토와 충돌 해결 흐름을 배워서 협업 방법을 배웠다.

## 실습 명령어

### 로그 검색

grep "ERROR" server.log: 로그에서 `ERROR`가 포함된 줄을 검색
grep -i "error" server.log: 대소문자를 무시하고 검색
grep -c "ERROR" server.log: `ERROR`가 포함된 줄의 개수를 센다.
grep -n "ERROR" server.log: 검색 결과와 함께 줄 번호를 표시한다.  
grep -v "INFO" server.log: `INFO`가 없는 줄만 출력

find . name "*.txt":txt 파일 찾기
find . type d :디렉터리만 찾기
find / name "start.sh" 2>/dev/null :시스템 전체에서 찾기 오래 걸릴 수 있음
find / name "start.sh" sh" :2>/dev/null 빼고 실행해보기

### 프로세스 확인 및 관리

ps aux: 실행 중인 프로세스 목록을 확인한다.  
jobs: 현재 터미널에서 실행한 작업을 확인한다.  
kill PID: 지정한 프로세스에 종료 신호를 보낸다.

### 백업과 복원

tar -czf: 파일이나 디렉터리를 `.tar.gz` 형식으로 압축한다.  
tar -tzf: 압축 파일 안에 들어 있는 파일 목록을 확인한다.  
tar -xzf: `.tar.gz` 압축 파일을 해제한다.  
diff -rq: 원본과 복원한 디렉터리의 차이를 비교한다.  
du -sh: 파일이나 디렉터리의 크기를 확인한다.
