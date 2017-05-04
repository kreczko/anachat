FROM continuumio/miniconda

#RUN /opt/conda/bin/conda update conda -y && \
RUN	/opt/conda/bin/pip install -U pip && \
	/opt/conda/bin/pip install slackbot slackweb && \
	/opt/conda/bin/conda clean -t

ENV PYTHONPATH=/opt/hepbot:/opt/hepbot/hepbot
RUN mkdir /opt/hepbot
COPY hepbot /opt/hepbot/hepbot

WORKDIR /opt/hepbot
CMD ["/opt/conda/bin/python", "/opt/hepbot/hepbot/run.py"]
