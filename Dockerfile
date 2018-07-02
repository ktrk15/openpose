FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends \
    build-essential cmake libatlas-base-dev git vim wget \
    python-dev python-pip python-setuptools python-numpy \
    libopencv-dev libgoogle-glog-dev protobuf-compiler libprotobuf-dev \
    libboost-all-dev libhdf5-dev

RUN pip install -q --upgrade pip
RUN pip install jupyter opencv-python

WORKDIR /root
RUN git clone https://github.com/ktrk15/openpose.git

WORKDIR /root/openpose/build
RUN cmake ..
RUN make
RUN make install

WORKDIR /root/openpose
