FROM lambci/lambda:build-python2.7


RUN yum clean all && \
    yum -y install python27-devel python27-virtualenv nano gcc lapack-devel blas-devel atlas libyaml-devel && \
    yum -y tcl tcl-devel tk tk-devel agg agg-devel libpng-devel && \
    yum --enablerepo=epel -y install hdf5-devel

WORKDIR /var/task

RUN virtualenv /var/env -p python2.7 && \
    source /var/env/bin/activate && \
    source install -U pip && \
    deactivate

RUN echo "source /var/env/bin/activate" >> .bashrc

CMD ["zappa"]
