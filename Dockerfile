FROM python:3.5.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN \
  apt-get update -qq -y && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    git \
    make \
    curl \
    xz-utils \
    file

RUN \
  git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && mkdir -p /usr/lib/mecab/dic \
  && ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y \
  && rm -r mecab-ipadic-neologd

RUN pip install mecab-python3 bottle gunicorn
COPY main.py /usr/src/app/

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:3000", "-w", "2", "main:app"]
