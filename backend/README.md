# InstaDL - Backend API

This is the FastAPI backend for InstaDL. It exposes REST APIs for media processing and proxying.

## Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Deployment

The backend is fully ready for deployment on AWS EC2 or Render.

### Render
You can connect this repository to Render and use the provided `render.yaml` as the blueprint, or set the start command manually:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### AWS EC2
You can deploy using Docker:
```bash
docker build -t instadl-api .
docker run -d -p 80:8000 instadl-api
```
Or use the provided `nginx.conf` to set up a reverse proxy with Nginx.

## Configuration

Make sure to set `CORS_ORIGINS` environment variable in production if it differs from the default `https://instadl.vercel.app`.
