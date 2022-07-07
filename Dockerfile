# ===================== PYTHON-BASE =========================
FROM python:3.10-alpine as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR="/opt/poetry/cache"

ENV PATH="$POETRY_HOME/bin:$PATH"

# ===================== BUILDER-BASE =========================
FROM python-base as builder

RUN apk update \
    && apk add libffi-dev build-base curl gcc postgresql-dev python3-dev musl-dev

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry install --no-dev

# ===================== PRODUCTION-BASE =========================
FROM python-base as production

WORKDIR /app

RUN apk update \
    && apk add postgresql-dev

COPY --from=builder $POETRY_HOME $POETRY_HOME

COPY . /app

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
