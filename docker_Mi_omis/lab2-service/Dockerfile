FROM python:3

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8001

CMD ["python", "service.py"]