# SMC — Frontend + Flask Backend Hosting Bundle

## Contents
- `frontend/` — static frontend (index.html + src/)
- `backend/` — Flask app (app.py) and requirements.txt
- `Dockerfile` (inside backend/) — builds a container serving both frontend and backend via gunicorn
- `docker-compose.yml` — local development: builds and runs container
- `Procfile` — for Heroku/Render-style deployments

## Quick local run (Docker)
1. From the root of this bundle (where `docker-compose.yml` is):
   ```
   docker compose up --build
   ```
2. Visit http://localhost:5000

## Deploy to Render (recommended simple option)
1. Create a new Web Service on Render.
2. Connect your GitHub repo (push this bundle to a repo first).
3. Set the build command: `docker build -t web .`
   (Render can detect Dockerfile automatically if present.)
4. Start command: use the default (Render will run the container).

## Deploy to Railway
1. Create a new project > Deploy from repo.
2. Railway will detect Dockerfile and build the container.

## GitHub Pages (frontend only)
- If you want only the frontend on GitHub Pages:
  1. Create branch `gh-pages`.
  2. Upload the *contents* of `frontend/` (index.html + src/) to the root of `gh-pages`.
  3. In repo Settings → Pages, choose branch `gh-pages` and folder `/ (root)`.

## API endpoints
- `GET /api/health` — health check
- `POST /api/predict` — accepts JSON, returns dummy prediction

## Notes
- Replace dummy predict function with real model loading/inference.
- For production, consider setting up HTTPS via your hosting provider.
