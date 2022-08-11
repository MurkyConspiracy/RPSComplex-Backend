FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install tomli
WORKDIR /app
COPY /src /app
COPY /config /app/config
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python3","-u", "backend-engine.py"]