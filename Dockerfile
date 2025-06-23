FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --locked --no-install-project
RUN uv sync --locked

COPY app.py ./

CMD ["uv", "run","streamlit", "run", "app.py"]
