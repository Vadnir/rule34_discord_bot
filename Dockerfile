FROM python:3.10

RUN useradd -ms /bin/bash user
USER user

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY main.py .
COPY Rule.py .
COPY .env .

ENTRYPOINT [ "python", "main.py"]

