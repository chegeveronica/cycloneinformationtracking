FROM python:3.8-alpine
WORKDIR  /app
#python output is transmitted directly to the terminal without being buffered and that allows displaying the application’s output in real-time
ENV PYTHONUNBUFFERED = 1  

#postgres-client to help interact with postgres
RUN apk add --update --no-cache postgresql-client jpeg-dev
#temporary files to assist run requirements
RUN apk add --update --no-cache --virtual .tmp-build-deps  
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
#default directory
#RUN mkdir /app
#COPY ./app /app/
WORKDIR /app

COPY requirements.txt ./



#\ gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
