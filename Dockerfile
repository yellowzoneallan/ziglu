FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN pip3 install kubernetes
RUN pip3 install slackclient
COPY . /app
WORKDIR /app
EXPOSE 5555
CMD /usr/bin/python3 ./ziglu.py
