## building jenkins image including docker-cli and git 
FROM jenkins/jenkins:lts

## switching to user root to install packages
USER root

RUN apt-get update && \
    apt-get install -y git docker.io && \
    rm -rf /var/lib/apt/lists/*

## switching back to jenkins user
USER jenkins

