#!/usr/bin/env bash

export CLOUD_SDK_VERSION=168.0.0

curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz

cd google-cloud-sdk/

#source /google-cloud-sdk/completion.bash.inc

#source /google-cloud-sdk/path.bash.inc

source completion.bash.inc

source path.bash.inc

