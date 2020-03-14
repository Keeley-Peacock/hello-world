FROM python:3.8-alpine as base

FROM base as build
RUN apk add --no-cache py-cryptography gcc musl-dev libffi-dev libressl-dev git
RUN python -m pip install poetry && poetry config virtualenvs.create false
WORKDIR /wheels
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install --no-root

FROM build as test
COPY . . 
RUN poetry run nox

FROM base as prod
COPY --from=test /wheels/dist/ .
RUN pip install --no-cache --find-links=. hello_world*.whl

CMD ["waitress-serve", "--listen=*:8000", "hello_world.serve:app"]
