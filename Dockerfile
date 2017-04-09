FROM gcr.io/tensorflow/tensorflow

RUN mkdir /metabrain
WORKDIR /metabrain

ADD . /metabrain

RUN pip install --upgrade Flask

EXPOSE 3000

CMD ["python", "./app.py"]