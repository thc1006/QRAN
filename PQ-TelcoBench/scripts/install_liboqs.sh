#!/bin/bash
# Install liboqs (Open Quantum Safe) library

set -e

echo "Installing liboqs (Open Quantum Safe)..."

# Check if running on supported OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "Cannot detect OS. This script supports Ubuntu/Debian."
    exit 1
fi

# Install dependencies
echo "Installing build dependencies..."
if [ "$OS" = "ubuntu" ] || [ "$OS" = "debian" ]; then
    sudo apt-get update
    sudo apt-get install -y \
        build-essential \
        cmake \
        git \
        libssl-dev \
        ninja-build \
        wget
else
    echo "Unsupported OS: $OS"
    exit 1
fi

# Clone and build liboqs
echo "Cloning liboqs repository..."
cd /tmp
git clone --depth 1 --branch 0.12.0 https://github.com/open-quantum-safe/liboqs.git
cd liboqs

echo "Building liboqs..."
mkdir -p build
cd build
cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr/local ..
ninja
sudo ninja install

# Update library cache
echo "Updating library cache..."
sudo ldconfig

# Install Python bindings
echo "Installing liboqs-python..."
pip3 install --user liboqs-python

echo "liboqs installation complete!"
echo "Library installed to: /usr/local/lib"
echo "Headers installed to: /usr/local/include"

# Cleanup
cd /
rm -rf /tmp/liboqs

echo "Installation successful!"
