
# 6주차 수업 과제
내 이미지 주소:ghcr.io/slskdu/guestbook:week06

<img width="958" height="488" alt="image" src="https://github.com/user-attachments/assets/595ab87d-5009-4312-8fb8-0fa70cfbbce3" />

Dockerfile
# ---------------------------------------------------------------
# 학생 과제: 아래 각 줄이 무엇을 하는지 주석으로 설명을 달아보세요.
# ---------------------------------------------------------------

FROM python:3.12-slim
# Python 3.12 기반 이미지를 사용

WORKDIR /app
# 컨테이너 내부의 작업 폴더를 지정


COPY requirements.txt .
# 의존성 목록을 이미지 안으로 복사

RUN pip install --no-cache-dir -r requirements.txt
# 필요한 Python 패키지를 설치

COPY . .
# 나머지 애플리케이션 파일을 컨테이너의 /app으로 복사

RUN useradd -m appuser
# 앱을 실행할 비루트 사용자 appuser를 만듬
USER appuser
# 이후 컨테이너 명령은 appuser 권한으로 실행

ENV APP_TITLE="InhaTC DevOps 방명록" \
    THEME_COLOR="#0054A6"
# 앱 제목과 테마 색상의 기본 환경 변수를 이미지에 설정

EXPOSE 5000
# 컨테이너 앱이 사용하는 포트가 5000임을 문서화

CMD ["python", "app.py"]
# 컨테이너 시작 시 Python으로 app.py를 실행

코드에 직접 설정하면 app.py에서 설정하고 코드를 수정 후 이미지를 다시빌드함 
env는 Dockerfile에서 설정되고 이미지에 기본값을 넣어 두고 별도 설정이 없으면 사용됨
-e는 실행할 때 docker run 명령으로 설정되고 이미지나 코드를 바꾸지 않고 컨테이너마다 값을 다르게 줄 수 있음

<img width="851" height="251" alt="image" src="https://github.com/user-attachments/assets/ad2abfca-223b-48c0-bf4b-7ad4148f336d" />
