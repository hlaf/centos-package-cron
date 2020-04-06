FROM centos:7.7.1908

RUN useradd -m nonrootuser -G wheel \
  && echo "nonrootuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN yum -y install systemd-libs \
    yum clean all; \
    (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;\
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/*; \
    rm -f /etc/yum.repos.d/CentOS-Media.repo; \
    yum -y install epel-release ; \
    yum -y install rpm-build yum-utils sudo rpmlint rake python-pip; \
    yum clean all; \
    pip install --upgrade pip setuptools wheel; \

CMD ["/bin/bash"]
