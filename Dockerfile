FROM ubuntu:latest
RUN apt-get update
WORKDIR /

RUN apt-get install wget -y

RUN mkdir 3rdparty

# Installing Eigen
RUN cd 3rdparty && wget http://bitbucket.org/eigen/eigen/get/3.3.7.tar.gz
RUN cd 3rdparty && mkdir -p eigen && tar xvf 3.3.7.tar.gz -C eigen --strip-components=1


RUN apt-get install make -y
RUN apt-get install cmake -y
RUN apt-get install build-essential -y #C/C++ compiler

# Installing ITK
RUN cd 3rdparty && wget https://sourceforge.net/projects/itk/files/itk/4.13/InsightToolkit-4.13.2.tar.gz
RUN cd 3rdparty && tar xvf InsightToolkit-4.13.2.tar.gz
RUN mkdir 3rdparty/InsightToolkit-4.13.2/build
RUN cd 3rdparty/InsightToolkit-4.13.2/build && cmake -DCMAKE_INSTALL_PREFIX=../../itk ..
RUN cd 3rdparty/InsightToolkit-4.13.2/build && make -j4
RUN cd 3rdparty/InsightToolkit-4.13.2/build && make install

# Installing BOOST and TBB
RUN apt-get install libboost-all-dev -y
RUN apt-get install libtbb-dev -y

# Make alias for dropreg
RUN echo "alias dropreg=/home/build/drop/apps/dropreg/dropreg" >> ~/.bashrc

# install python
RUN apt-get update && apt-get install -y python python-dev python3.7 python3.7-dev python3-pip \
    virtualenv libssl-dev libpq-dev git build-essential libfontconfig1 libfontconfig1-dev
RUN pip3 install setuptools pip --upgrade --force-reinstall

# Copying files
COPY drop /home/drop
COPY itkio /home/itkio
COPY mia /home/mia
COPY mrfopt /home/mrfopt
COPY .travis.yml /home/.travis.yml
COPY build.sh /home/build.sh
COPY CMakeLists.txt /home/CMakeLists.txt

# Build code
RUN mkdir /home/build
RUN cd /home/build && THIRD_PARTY_DIR=/3rdparty cmake ..
RUN cd /home/build && THIRD_PARTY_DIR=/3rdparty make -j4

COPY start.py /home/