# 5주차 실습: Docker

- [v] `docker --version` 정상 출력
- [v] `docker run hello-world` 실행
- [v] `web`이라는 이름으로 nginx 컨테이너 실행
- [v] 브라우저 또는 `curl`로 `http://localhost:8080` 응답 확인
- [v] `docker ps`에서 실행 상태 확인
- [v] 실습 결과를 `week05/README.md`에 기록
- [v] 수업에서 만든 컨테이너 정리
- [v] 혼자서 해보기 완료

## 5주차 수업 내용

프로그램 개발중 개인이나 회사컴에선 정상 작동하지만 환경이 달라지만 바로 작동이 안된다는 문제가 발생 이를 해결하기위한 방법으로 앱만 보내는 것이 아니라 운영체제 까지 통째로 보내는 법이 VM
앱만 보내지 말고 앱과 실행에 필요한 라이브러리 , 설정 , 파일을 함께 묶어서 보내는 법이 컨테이너

이를 실습에서 직접하는 건 컨테이너로 docker를 사용했음 

### docker 명령문

docker --version: 설치된 Docker 버전을 확인한다.
docker run hello-world: 이미지가 없으면 내려받아 컨테이너로 실행한다.

docker run: 이미지로 컨테이너를 실행한다.
-d: 백그라운드에서 실행한다.
-p 8080:80: PC의 8080 포트를 컨테이너의 80 포트에 연결한다.
--name web: 컨테이너 이름을 web으로 지정한다.
docker ps: 실행 중인 컨테이너를 확인한다.
docker ps -a: 정지된 컨테이너까지 확인한다.

curl -I: 웹 서버의 HTTP 응답 헤더를 확인한다.
docker logs web: 컨테이너 로그를 확인한다.
docker logs -f web: 로그를 실시간으로 확인한다. 종료할 때는 Ctrl+C를 누른다.

docker stop: 컨테이너를 정지한다.
docker start: 정지한 컨테이너를 시작한다.
docker restart: 컨테이너를 재시작한다.
docker rm -f: 실행 중인 컨테이너도 강제로 삭제한다.
docker images: 내려받은 이미지 목록을 확인한다.