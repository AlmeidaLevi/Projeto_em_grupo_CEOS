FROM python:3.13

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install django


EXPOSE 8000

COPY ./entrypoint.sh /usr/local/src/entrypoint.sh

ENTRYPOINT [ "bash", "-x", "/usr/local/src/entrypoint.sh" ]

CMD ["start"]
