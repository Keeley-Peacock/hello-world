FROM python:3.8-slim as base

FROM base as build
RUN python -m pip install poetry  && poetry config virtualenvs.create false
WORKDIR /wheels
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install --no-root

FROM build as test
COPY . . 
RUN tox -e py38,flake8,pylint,mypy,coverage -p all && tox -e build

FROM base as prod
COPY --from=test /wheels/dist/ .
RUN pip install --no-cache --find-links=. hello_world*.whl

CMD ["gunicorn", "-w 1", "--bind", "0.0.0.0:8000", "hello_world.serve:app"]
