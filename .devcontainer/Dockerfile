FROM python:3.9.11-slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=user

ENV container docker

USER root

# Create non-root user
RUN groupadd $USER && useradd --gid $USER --shell /bin/bash --create-home $USER

RUN apt-get update &&\
 apt-get install --assume-yes --no-install-recommends -y\
 build-essential\
 ca-certificates\
 curl\
 git-all\
 less\
 nano\
 rsync\
 gnupg\
 gnupg2\
 gnupg1\
 sqlite3\
 jq\
 vim\
 nano\
 htop\
 procps\
 wget\
 zsh\
 git-lfs

 # Install basic packages
RUN curl -k https://packages.microsoft.com/keys/microsoft.asc | apt-key add -\
 && curl -k https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list\
 && apt-get update\
 && ACCEPT_EULA=Y apt-get install --assume-yes --no-install-recommends -y\
 msodbcsql17\
 mssql-tools\
 unixodbc-dev\
 libgssapi-krb5-2\
 python3-tk\
 && apt-get clean\
 && rm -rf /var/lib/apt/lists/*

 # Add mssq application to .bashrc
RUN echo "export PATH='$PATH:/opt/mssql-tools/bin'" >> /home/$USER/.bash_profile\
 && echo "export PATH='$PATH:/opt/mssql-tools/bin'" >> /home/$USER/.bashrc

# RUN echo "Install Conda..."\
#  && cd /tmp\
#  && curl https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh --progress-bar -o installer.sh\
#  && bash installer.sh -b -p $HOME/anaconda3\
#  && rm installer.sh\
#  && conda install -c conda-forge mamba

# Upgrade pip then install poetry and wheel
RUN pip3 install --no-cache-dir --upgrade pip \
 && pip3 install --no-cache-dir wheel poetry

# Install oh-my-zsh
RUN yes Y | sh -c "$(curl -k -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

COPY .devcontainer/config_devcontainer.sh /tmp
COPY --chown=$USER:$USER . /home/$USER/python_learning
WORKDIR /home/$USER/python_learning
USER $USER

ARG DEBIAN_FRONTEND=noninteractive