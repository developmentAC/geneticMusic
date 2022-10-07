FROM ubuntu:20.04

RUN apt-get update && apt-get -y install git htop vim python3.10 python3-pip curl clustalw


RUN \
pip3 install --upgrade pip \
pip install bioPython

# RUN curl -sSL https://install.python-poetry.org | python3 - 

#export PATH="/root/.local/bin:$PATH"
#ENV PATH="${PATH}:/root/.local/bin:$PATH"

WORKDIR /root

CMD ["bash"]
