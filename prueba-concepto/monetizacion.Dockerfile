FROM python:3.10

EXPOSE 5002/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "app.infrastructure.Monetización.api:app", "--host", "0.0.0.0", "--port", "5002", "--reload"]