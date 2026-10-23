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