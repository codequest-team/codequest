FROM python

LABEL maintainer="peskovdev@proton.me"

WORKDIR /code

RUN pip install poetry

RUN apt-get update \
  && apt-get install -y netcat \
  && rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./poetry.lock /code/

RUN poetry config virtualenvs.create false \
  && poetry install --only main

COPY . /code/

ENTRYPOINT ["/code/boot.sh"]
