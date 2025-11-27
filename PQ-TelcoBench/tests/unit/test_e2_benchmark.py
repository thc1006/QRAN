"""
Unit tests for E2 Interface Benchmark module
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from e2_interface.benchmark import BenchmarkConfig, E2Benchmark, BenchmarkResult


class TestBenchmarkConfig:
    """Tests for BenchmarkConfig"""

    def test_default_config(self):
        """Test default configuration values"""
        config = BenchmarkConfig()
        assert config.algorithm == "ML-KEM-768"
        assert config.iterations == 100
        assert config.security_mode == "pq_tls"

    def test_custom_config(self):
        """Test custom configuration"""
        config = BenchmarkConfig(
            algorithm="ML-KEM-1024",
            iterations=50,
            security_mode="hybrid_tls",
        )
        assert config.algorithm == "ML-KEM-1024"
        assert config.iterations == 50
        assert config.security_mode == "hybrid_tls"


class TestE2Benchmark:
    """Tests for E2Benchmark class"""

    def test_benchmark_initialization(self, sample_config):
        """Test benchmark initialization"""
        config = BenchmarkConfig(**sample_config)
        benchmark = E2Benchmark(config)
        assert benchmark.config.algorithm == "ML-KEM-768"

    def test_invalid_algorithm(self):
        """Test that invalid algorithm raises error"""
        with pytest.raises(ValueError):
            config = BenchmarkConfig(algorithm="INVALID_ALG")
            E2Benchmark(config)

    def test_handshake_test_runs(self, sample_config):
        """Test that handshake test completes"""
        config = BenchmarkConfig(**sample_config)
        benchmark = E2Benchmark(config)
        result = benchmark.run_handshake_test()

        assert isinstance(result, BenchmarkResult)
        assert result.test_name == "E2_Handshake_Test"
        assert result.algorithm == "ML-KEM-768"

    def test_throughput_test_runs(self, sample_config):
        """Test that throughput test completes"""
        config = BenchmarkConfig(**sample_config)
        benchmark = E2Benchmark(config)
        result = benchmark.run_throughput_test()

        assert isinstance(result, BenchmarkResult)
        assert result.test_name == "E2_Throughput_Test"


class TestBenchmarkResult:
    """Tests for BenchmarkResult"""

    def test_result_to_dict(self):
        """Test converting result to dictionary"""
        result = BenchmarkResult(
            test_name="Test",
            algorithm="ML-KEM-768",
            security_mode="pq_tls",
            iterations=100,
        )
        result_dict = result.to_dict()

        assert "test_name" in result_dict
        assert "latency" in result_dict
        assert "throughput" in result_dict
        assert result_dict["algorithm"] == "ML-KEM-768"

    def test_result_to_json(self, tmp_path):
        """Test exporting result to JSON"""
        result = BenchmarkResult(
            test_name="Test",
            algorithm="ML-KEM-768",
            security_mode="pq_tls",
            iterations=100,
        )

        output_file = tmp_path / "test_result.json"
        result.to_json(str(output_file))

        assert output_file.exists()
        content = output_file.read_text()
        assert "ML-KEM-768" in content
