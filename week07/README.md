#7주차 혼자 해보기

PS C:\Users\전제형\guestbook-week07\guestbook> docker compose ps
NAME                IMAGE            COMMAND                   SERVICE   CREATED         STATUS                   PORTS
guestbook-redis-1   redis:7-alpine   "docker-entrypoint.s…"   redis     2 minutes ago   Up 2 minutes (healthy)   6379/tcp
guestbook-web-1     guestbook-web    "python app.py"           web       2 minutes ago   Up 2 minutes (healthy)   5000/tcp


<img width="568" height="350" alt="image" src="https://github.com/user-attachments/assets/5591d964-fdec-4e7a-9f87-188ef20a87dc" />

<img width="590" height="380" alt="image" src="https://github.com/user-attachments/assets/85f6ec28-0b3c-4912-b72a-526629919652" />

`docker compose down` 후 `up -d`: Redis 볼륨이 유지되어 데이터가 남아있음
`docker compose down -v` 후 `up -d`: Redis 볼륨이 삭제되어 데이터가 사라짐

.env에는 Redis 비밀번호와 같은 민감한 환경 변수나 개인용 토큰을 넣기 때문에 남들에서 유출되면 내 계정을 마음대로 남용 당할 수 있으므로  
올리지 않고  .gitignore에 .env를 추가해 Git 추적에서 제외시킨다. 
