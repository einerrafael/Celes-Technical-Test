FROM python:3.9

WORKDIR /code

# Instala las dependencias de Java necesarias para PySpark
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean

#ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64
#ENV PATH $JAVA_HOME/bin:$PATH

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env

COPY ./main.py /code/main.py
COPY ./app /code/app
COPY ./assets /code/assets

CMD ["fastapi", "run", "main.py", "--port", "80"]
