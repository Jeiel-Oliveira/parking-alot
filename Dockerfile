FROM python:3.9

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./src/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /src/

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
