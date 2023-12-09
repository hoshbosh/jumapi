from python:3-alpine3.15
# FROM alpine:3.14 AS app 
# RUN apk upgrade --no-cache
RUN apk add --no-cache libstdc++ ncurses-libs
# RUN apk add --no-cache libstdc++=3.4.26 ncurses-libs
workdir /app
copy . /app
run pip install --upgrade pip
run pip install -r requirements.txt
# run apt-get install -y ffmpeg
# run pip --version
# run python --version
# run pip -v install vosk-api
run pip -v install https://github.com/alphacep/vosk-api/releases/download/v0.3.45/vosk-0.3.45-py3-none-linux_x86_64.whl 
run uvicorn main:app --host 0.0.0.0 --port 8080