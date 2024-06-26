FROM python:3.9

WORKDIR /parking

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . ./parking/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /parking/

EXPOSE 8000

CMD ["uvicorn", "parking.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
