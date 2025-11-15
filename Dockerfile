FROM python:3.11-slim
WORKDIR /app
COPY ./frontend /app/frontend
COPY ./backend /app/backend
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "backend.app:app"]
