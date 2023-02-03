FROM amazonlinux
RUN ulimit -n 1024 && yum -y update && yum -y install \
    python3 \
    python3-pip \
    python3-devel \
    zip \
    && yum clean all
# ADD lambda_function.py /
# RUN python3 -m pip install pip=21
RUN pip3 install virtualenv