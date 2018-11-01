FROM ubuntu:16.04
FROM python:2.7
LABEL maintainer="nate@cybersixgill.com"

#Set working directory inside container
WORKDIR /app

#Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

#Fix (java) certificate issues
RUN apt-get update && \
    apt-get install -y ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

#Install Firefox 46.0.1
RUN apt-get install -y wget tar
RUN wget -qO- https://ftp.mozilla.org/pub/firefox/releases/46.0.1/firefox-46.0.1.linux-x86_64.sdk.tar.bz2 | tar xvj

#Install assorted packages
RUN apt-get update && apt-get install -y \
    python-pip \
    polipo \
    tor \
    unzip \
    vim

#Move polipo config file to correct dir
COPY config /etc/polipo/
RUN service polipo start

#Install phantomJS
COPY phantom_install.sh /app
RUN ./phantom_install.sh

#Install chrome
COPY install_chrome.sh /app
RUN ./install_chrome.sh

#Install and configure google cloud sdk
COPY install_google_cloud_sdk.sh /app
COPY gcloud_credentials.json /app
RUN /app/install_google_cloud_sdk.sh && \
    bash /app/google-cloud-sdk/install.sh -q --usage-reporting false --path-update true
ENV GOOGLE_APPLICATION_CREDENTIALS "/app/gcloud_credentials.json"

#Set python path
ENV PYTHONPATH "/app/sixgill:/app/sixgill/crawler:/app/sixgill/crawler/sixgill:$PYTHONPATH"
RUN echo "export PYTHONPATH='$PYTHONPATH'" >> /root/.bashrc

ENV TMPDIR "/tmp/dev_doc_tmp"
RUN echo "export TMPDIR='$TMPDIR'" >> /root/.bashrc

#Install libraries from .txt file
COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD ["exec scraper.py"]