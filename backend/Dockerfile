# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy backend and frontend into the image
COPY ./frontend /app/frontend
COPY ./backend /app/backend

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt

# Expose port
EXPOSE 5000

# Use gunicorn to serve the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "backend.app:app"]
