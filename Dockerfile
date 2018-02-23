FROM python:2.7

COPY ./app /app
RUN pip install --no-cache-dir -r /app/requirements.txt

#CMD ["gunicorn", "--bind", "0.0.0.0", "wsgi:app"]

CMD "gunicorn --bind 0.0.0.0 wsgi:app"
