FROM python:3.12-slim-bookworm

RUN apt-get update -y && apt-get install -y build-essential curl

# RUN curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --path /usr/local/bin
# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /gateway_service

COPY . /gateway_service

RUN uv sync --locked

EXPOSE 8001

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
