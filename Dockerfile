FROM python:3.11-slim

WORKDIR /app/src/

ENV PYTHONWRITEBYCODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install --no-cache-dir poetry

COPY ./pyproject.toml ./poetry.lock /app

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

COPY src .

COPY entrypoint.sh /app

RUN sed -i 's/\r$//g' /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
