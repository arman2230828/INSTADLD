# InstaDL

Fast, Clean & Secure Media Tool. Built with FastAPI (Python) and Vanilla JS + CSS3.

## Features
- **Async API**: FastAPI backend providing an async REST API.
- **Premium UI**: Dark mode + Neon Orange glassmorphism layout, fully responsive.
- **SEO Optimized**: Dynamic Meta tags, Open Graph, Twitter Cards, robots.txt, sitemap.xml.
- **Production Ready**: Contains configurations for Docker, Render, Nginx, and Heroku (Procfile). Includes Security Headers, CORS, and Rate Limiting.

## Project Structure

```
instadl/
├── app/
│   ├── main.py                # FastAPI initialization
│   ├── routers/               # API and Page routes
│   ├── services/              # Business logic (Media processing abstraction)
│   ├── models/                # Pydantic schemas
│   ├── utils/                 # Helper functions
│   ├── templates/             # HTML Jinja2 Templates
│   └── static/                # CSS, JS, Robots, Sitemap
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── render.yaml                # Render Blueprint
├── Procfile                   # Heroku/Render process file
├── .env.example               # Environment variables
├── nginx.conf                 # Nginx reverse proxy configuration
└── README.md                  # Project documentation
```

## Running Locally

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
   The app will be available at `http://localhost:8000`.

## Deployment

### Deploy to Render

**Using Blueprint (render.yaml):**
1. Push this repository to GitHub/GitLab.
2. Go to [Render Dashboard](https://dashboard.render.com).
3. Click **New** -> **Blueprint**.
4. Connect your repository. Render will automatically detect the `render.yaml` file and create the web service.

**Manual Web Service Deployment:**
1. Click **New** -> **Web Service**.
2. Connect your repository.
3. Language: Python 3.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Deploy with Docker
```bash
docker build -t instadl .
docker run -p 8000:8000 instadl
```
