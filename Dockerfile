FROM python:3.9.16-alpine
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
#COPY ./requirements.txt .
RUN POETRY_VIRTUALENVS_CREATE=false poetry install
# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]