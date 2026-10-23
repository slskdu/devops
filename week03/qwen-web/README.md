# 3주차 - 셸 스크립팅과 로컬 AI 서비스

## 수업 내용 요약
Ollama와 Qwen 모델을 실행해보고 이를 파이썬 웹 프로그램으로 실행라고 조건문을 만들어 봄 

## 실습 명령어

### Ollama와 Python 확인

`ollama --version`: Ollama 버전을 확인한다.  
`python3 --version`: Python 버전을 확인한다.  
`curl -fsS http://127.0.0.1:11434/api/tags`: Ollama 서버의 응답과 모델 목록을 확인한다.  
`ollama serve`: Ollama 서버가 실행 중이 아닐 때 서버를 시작한다.

### Qwen 모델 관리

`ollama pull qwen3:0.6b`: Qwen 모델을 내려받는다.  
`ollama list`: 내려받은 모델 목록을 확인한다.

### 셸 스크립트 실행

`chmod u+x start.sh`: 스크립트에 실행 권한을 추가한다.  
`./start.sh`: 현재 폴더의 스크립트를 실행한다.  
`cd "$(dirname "$0")"`: 스크립트 파일이 있는 폴더로 이동한다.  
`exec python3 chat.py`: 셸을 Python 프로그램으로 바꾸어 실행한다.

### 환경 변수로 실행 설정

`export MODEL="qwen3:0.6b"`: 실행할 모델을 환경 변수로 지정한다.  
`export WEB_PORT="8080"`: 웹앱의 포트를 8080으로 설정한다.  
`./start_with_export.sh`: 환경 변수를 설정한 뒤 웹앱을 실행한다.  
`./start_with_export_2.sh`: 8080 포트 설정으로 웹앱을 실행한다.


