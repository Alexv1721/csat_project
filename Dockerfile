FROM python:3.11

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY csat_project/ /app/

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
