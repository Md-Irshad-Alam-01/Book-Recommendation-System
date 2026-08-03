FROM python:3.11-slim

# set workdir
WORKDIR /app

# install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . /app

# recommended non-root user (optional)
# RUN adduser --disabled-password appuser && chown -R appuser /app
# USER appuser

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "2", "--threads", "4"]
