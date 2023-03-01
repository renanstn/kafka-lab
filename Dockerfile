FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip && pip install poetry
WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false && poetry install --no-root

FROM base AS producer
COPY producer.py /code/
CMD [ "python", "producer.py" ]

FROM base AS consumer
COPY consumer.py /code/
CMD [ "python", "consumer.py" ]
