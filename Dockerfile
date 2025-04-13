# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install Rust and C build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
 && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Add Rust binaries to PATH
ENV PATH="/root/.cargo/bin:$PATH"

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Force copying instead of symlinking from mounted volumes
ENV UV_LINK_MODE=copy

# Sync dependencies using the lockfile and cache
RUN --mount=type=cache,target=/root/.cache/uv,id=uv-cache \
    --mount=type=bind,source=uv.lock,target=/app/uv.lock \
    --mount=type=bind,source=pyproject.toml,target=/app/pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Add the rest of the project files and install the project itself
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv,id=uv-cache \
    uv sync --frozen --no-dev

# Make virtualenv available in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Prevent `uv` from being used as default entrypoint
ENTRYPOINT []

# Default: run FastAPI app with hot-reloading enabled
CMD ["fastapi", "run", "--host", "0.0.0.0", "src/main.py"]
