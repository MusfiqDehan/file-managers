FROM python:3.10.0-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "file_managers/__init__.py"]