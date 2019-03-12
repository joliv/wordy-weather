FROM python:3.7-alpine3.9

LABEL Name=wordy-weather Version=0.0.1
ENV PORT 80
EXPOSE 80

WORKDIR /app
ADD . /app

# Using pip:
RUN python3 -m pip install -r requirements.txt
CMD ["gunicorn", "main:app"]
