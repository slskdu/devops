# 4주차 - 자동차와 협업

## 수업 내용 요약

이번 주에는 로그 파일에서 필요한 내용을 검색하고, 실행 중인 프로세스를 확인·관리하는 방법을 실습했다. 
또한 파일과 디렉터리를 압축해 백업하고 복원한 뒤 원본과 비교해 결과를 확인하는 법도 배우고 
Pull Request 검토와 충돌 해결 흐름을 배워서 협업 방법을 배우고 

IP 주소로 네트워크 장치를 찾고, 포트 번호로 해당 장치에서 제공하는 서비스를 구분하는 방법을 배우고 DNS로 도메인 이름의 IP 주소를 조회,명령어로 연결 상태와 서버 응답을 확인했다. Python 간이 웹 서버를 직접 실행해 브라우저와 `curl`로 접속 및 관리법을 배움.

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


### 네트워크 실습 명령어
`python3 -m http.server 8080`: 현재 폴더를 웹 서버로 제공한다.  
`curl http://localhost:8080`: 웹 서버의 응답 내용을 확인한다.  
`curl -I http://localhost:8080`: HTTP 상태 코드와 응답 헤더를 확인한다.  
`ss -tlnp | grep 8080`: 8080 포트가 사용 중인지 확인한다.  
`python3 -m http.server 8000`: 포트 충돌이 발생하면 다른 포트로 서버를 실행한다.  
`kill PID`: 지정한 프로세스를 종료해 사용 중인 포트를 비운다.
