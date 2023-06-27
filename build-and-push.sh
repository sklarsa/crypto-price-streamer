#! /bin/bash

set -euxo pipefail

TAG=$1
if [ -z $TAG ] ; then
    echo "ERROR: usage: ./build-and-push.sh TAG"
    exit 1
fi

REPO=sklarsa/crypto-price-streamer

docker buildx build --platform linux/arm64/v8,linux/amd64 --push -t ${REPO}:${TAG} .
