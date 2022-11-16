# BASE docker image for TrendsSetter 
# Unified Docker template for NeuroImaging
# From alpine:3.16 # This doesn't work for installations that require miniconda
FROM continuumio/miniconda3:4.10.3p0-alpine

ARG CONDA_VERSION="py39_4.12.0"
ARG CONDA_MD5="81c773ff87af5cfac79ab862942ab6b3"
ARG CONDA_DIR="/opt/conda"

# **************************** DEPENDENCIES ************************
RUN apk update 
# Application Dependencies
RUN apk add --no-cache \
                curl \
                wget \
                vim \
                nano \
                bash \
                screen \
                tmux \
                emacs \
                vim \
                gcc \
                nodejs \
                npm \ 
                ca-certificates
# Library Dependencies
RUN apk add --no-cache \ 
                libx11 \
                libxcomposite \
                libxcursor \
                libxdamage \
                libxext \
                libxfixes \
                libxext \
                libxtst \
                libxxf86vm 
                #alsa-lib-dev \
                #libatk1.0 \
                #cairo-dev \
                #libsndfile \
                #libxcb \
                #libxslt
RUN bash
# **************************** MINICONDA ***************************
# We need to downgrade to python3.7 
#RUN conda install -y python=3.6.6

# **************************** PYTHON LIBRARIES ********************
# Pybids and Bids Validator installation is mandatory
#RUN conda install -y -c aramislab pybids
RUN conda install -y pip
RUN pip install pybids
RUN pip install bids-validator
RUN npm install -g bids-validator

# Pep 8 installation is included for style warnings
RUN conda install -c anaconda pep8

# These are common, but optional python dependencies for neuroimaging
RUN conda install -y -c conda-forge \
    nilearn \
    nipype \
    nibabel
# And additional common dependences for plotting/reading in variables
RUN conda install -y -c conda-forge \
        pandas \
        matplotlib \
        seaborn 

# **************************** IO **********************************
RUN mkdir -p /input
RUN mkdir -p /output

# **************************** APP *********************************
WORKDIR /app
ENV HOME /app
ADD . /app

# **************************** PEP8 COMPLIANCE *********************
# Run Pep8 on the /app directory to show any style issues in 
# python files (including any wrappers)
# This can be removed if images contain no python code in the app
# or in the wrapper
RUN pep8 -v /app

# ***************************** RUN CMD ****************************
# The run command should reference your bash run script or python 
# wrapper, which the user references as an entrypoint into the image
CMD /app/run.sh