FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y procps
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8199
CMD ["uvicorn", "service1:app", "--host", "0.0.0.0", "--port", "8199"]