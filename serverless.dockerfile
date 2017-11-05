FROM lambci/lambda:build-python2.7

RUN yum clean all && \
    yum -y install python27-devel python27-virtualenv nano gcc lapack-devel blas-devel atlas libyaml-devel && \
    yum -y install tcl tcl-devel tk tk-devel agg agg-devel libpng-devel && \
    yum --enablerepo=epel -y install hdf5-devel

RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash - && \
    yum install -y nodejs && \
    npm install -g serverless

WORKDIR /var/task

RUN virtualenv /var/env -p python2.7 && \
    source /var/env/bin/activate && \
    deactivate

RUN echo "source /var/env/bin/activate" >> ${HOME}/.bashrc

CMD ["serverless"]
