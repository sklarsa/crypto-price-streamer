FROM python:3.10

# Install poetry
RUN pip install poetry

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

# Copy the app
COPY main.py ./

ENTRYPOINT [ "poetry", "run", "python" ]
CMD ["main.py"]
