# PQ-TelcoBench Dockerfile
# Multi-stage build for optimal image size

# Stage 1: Builder - Install dependencies and build liboqs
FROM ubuntu:24.04 AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libssl-dev \
    python3 \
    python3-pip \
    python3-dev \
    ninja-build \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Build and install liboqs (Open Quantum Safe)
WORKDIR /tmp
RUN git clone --depth 1 --branch 0.12.0 https://github.com/open-quantum-safe/liboqs.git && \
    cd liboqs && \
    mkdir build && \
    cd build && \
    cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr/local .. && \
    ninja && \
    ninja install

# Install liboqs-python
RUN pip3 install --no-cache-dir liboqs-python

# Stage 2: Runtime
FROM ubuntu:24.04

LABEL maintainer="Q-RAN Research Team"
LABEL description="PQ-TelcoBench - Post-Quantum Telecommunications Benchmarking Platform"
LABEL version="0.1.0"

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

# Copy liboqs from builder
COPY --from=builder /usr/local /usr/local

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH \
    PATH=/app/venv/bin:$PATH

# Create app directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY pyproject.toml .
COPY src/ ./src/
COPY tests/ ./tests/
COPY config/ ./config/
COPY scripts/ ./scripts/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Create directories for results and logs
RUN mkdir -p /app/benchmarks/results /app/logs

# Expose Prometheus metrics port (if needed)
EXPOSE 9090

# Default command
CMD ["python3", "-m", "src.e2_interface.benchmark"]
