FROM ubuntu:20.04

RUN apt-get update -y

# install libheif
RUN apt install -y heif-gdk-pixbuf
RUN apt install -y libheif-examples

# install python3
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get install -y python-dev

RUN apt-get update -y

WORKDIR /home/user/
COPY . .
CMD python3 convert2png.py HEIC