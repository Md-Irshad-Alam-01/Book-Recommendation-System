# Book Recommender System

Production-ready changes and deployment instructions.

- Uses Flask + gunicorn for production.
- Model files are local pickles: `popular.pkl`, `pt.pkl`, `books.pkl`, `similarity_scores.pkl`.

Quick local run

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
python app.py
```

Run with gunicorn (recommended)

```bash
gunicorn -b 0.0.0.0:5000 app:app
```

Docker

```bash
docker build -t book-recommender .
docker run -p 5000:5000 book-recommender
```

Push to GitHub (example)

```bash
git init
git add .
git commit -m "Production: add Dockerfile, Procfile, README, app hardening"
# create a repo on GitHub, then:
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

Notes

- If your `.pkl` files are large, use Git LFS or store them in object storage (S3) and load at runtime.
- On platforms like Heroku, the `Procfile` is used; ensure `gunicorn` is in `requirements.txt`.
