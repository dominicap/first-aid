FROM python:3.6.1

MAINTAINER Dominic Philip <domi.a.philip@gmail.com>

RUN apt-get -y update
RUN pip3 install flask

CMD ["/bin/bash"]
