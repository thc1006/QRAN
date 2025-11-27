"""
Pytest configuration and fixtures
"""

import pytest
from pathlib import Path


@pytest.fixture
def test_data_dir():
    """Fixture providing test data directory"""
    return Path(__file__).parent / "data"


@pytest.fixture
def sample_config():
    """Fixture providing sample benchmark configuration"""
    return {
        "algorithm": "ML-KEM-768",
        "iterations": 10,
        "security_mode": "pq_tls",
    }


@pytest.fixture
def mock_keypair():
    """Fixture providing mock PQC keypair"""
    return (
        b"mock_public_key_" + b"0" * 1000,
        b"mock_secret_key_" + b"0" * 2000,
    )
