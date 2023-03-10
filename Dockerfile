FROM python:3.10-slim-buster as base

FROM base AS python-deps

COPY . .

# Install pipenv and compilation dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends gcc


FROM base AS runtime

# Run the application
ENTRYPOINT ["python", "main.py"]
# CMD ["--config", "/config/config.yaml"]
