# fetches Python image based on Slim
FROM python:3.8-slim

# setup working directory
WORKDIR /.

# copy folder into working directory
COPY ./ /src

# install requirements
RUN pip install -r ./src/requirements.txt
RUN python ./src/setup.py develop
RUN python -m spacy download en_core_web_lg

EXPOSE 5000

CMD ["python", "./src/SeemsPhishy/gui/run.py"]