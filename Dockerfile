FROM python:3.12-slim

RUN useradd -m -u 1000 appuser
USER appuser
WORKDIR /home/appuser/appuser

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY --chown=appuser:appuser . .

CMD ["python","server.py"]