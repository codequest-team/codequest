FROM python

LABEL maintainer="peskovdev@proton.me"

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry config virtualenvs.create false \
  && poetry install --only main

COPY . /code/
