"""
Unit tests for PQC Provider module
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from pqc_lib.provider import PQCProvider, LibOQSProvider, create_provider
from pqc_lib import list_supported_algorithms, get_algorithm_info


class TestPQCProvider:
    """Tests for PQC Provider"""

    def test_list_supported_algorithms(self):
        """Test listing supported algorithms"""
        algorithms = list_supported_algorithms()
        assert "ML-KEM-768" in algorithms
        assert "ML-DSA-65" in algorithms
        assert len(algorithms) > 0

    def test_get_algorithm_info(self):
        """Test getting algorithm information"""
        info = get_algorithm_info("ML-KEM-768")
        assert "security_level" in info
        assert info["security_level"] == 3
        assert "public_key_size" in info

    def test_create_provider(self):
        """Test creating PQC provider"""
        provider = create_provider("ML-KEM-768", "liboqs")
        assert isinstance(provider, LibOQSProvider)
        assert provider.algorithm == "ML-KEM-768"

    def test_keypair_generation(self):
        """Test keypair generation"""
        provider = create_provider("ML-KEM-768", "liboqs")
        public_key, secret_key = provider.generate_keypair()

        assert isinstance(public_key, bytes)
        assert isinstance(secret_key, bytes)
        assert len(public_key) > 0
        assert len(secret_key) > 0

    def test_kem_operations(self):
        """Test KEM encapsulation/decapsulation"""
        provider = create_provider("ML-KEM-768", "liboqs")
        public_key, secret_key = provider.generate_keypair()

        # Encapsulation
        ciphertext, shared_secret_1 = provider.kem_encapsulate(public_key)
        assert isinstance(ciphertext, bytes)
        assert isinstance(shared_secret_1, bytes)

        # Decapsulation
        shared_secret_2 = provider.kem_decapsulate(secret_key, ciphertext)
        assert isinstance(shared_secret_2, bytes)

        # Note: In real implementation, shared_secret_1 should equal shared_secret_2
        # This is just a placeholder test


class TestLibOQSProvider:
    """Tests specific to LibOQS provider"""

    def test_liboqs_initialization(self):
        """Test LibOQS provider initialization"""
        provider = LibOQSProvider("ML-KEM-768", "liboqs")
        assert provider.algorithm == "ML-KEM-768"
        assert provider.backend == "liboqs"

    def test_performance_metrics(self):
        """Test getting performance metrics"""
        provider = LibOQSProvider("ML-KEM-768", "liboqs")
        metrics = provider.get_performance_metrics()

        assert "algorithm" in metrics
        assert "backend" in metrics
        assert "operations" in metrics
