"""
Post-Quantum Cryptography Library Module
=========================================

Provides abstraction layer for various PQC implementations including:
- liboqs (Open Quantum Safe)
- wolfSSL
- BoringSSL
- NVIDIA cuPQC (GPU acceleration)

Supported Algorithms (NIST FIPS):
    - FIPS 203: ML-KEM (Module-Lattice-Based Key Encapsulation Mechanism)
    - FIPS 204: ML-DSA (Module-Lattice-Based Digital Signature Algorithm)
    - FIPS 205: SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)
"""

from enum import Enum
from typing import Dict, List


class PQCAlgorithmType(Enum):
    """Types of PQC algorithms"""

    KEM = "kem"  # Key Encapsulation Mechanism
    SIGNATURE = "signature"  # Digital Signature
    HASH_SIGNATURE = "hash_signature"  # Hash-based Signature


class PQCBackend(Enum):
    """Supported PQC backends"""

    LIBOQS = "liboqs"  # Open Quantum Safe
    WOLFSSL = "wolfssl"
    BORINGSSL = "boringssl"
    CUPQC = "cupqc"  # NVIDIA GPU-accelerated


# NIST FIPS standardized algorithms
NIST_STANDARD_ALGORITHMS: Dict[str, Dict] = {
    # FIPS 203: ML-KEM
    "ML-KEM-512": {
        "type": PQCAlgorithmType.KEM,
        "security_level": 1,
        "public_key_size": 800,
        "secret_key_size": 1632,
        "ciphertext_size": 768,
    },
    "ML-KEM-768": {
        "type": PQCAlgorithmType.KEM,
        "security_level": 3,
        "public_key_size": 1184,
        "secret_key_size": 2400,
        "ciphertext_size": 1088,
    },
    "ML-KEM-1024": {
        "type": PQCAlgorithmType.KEM,
        "security_level": 5,
        "public_key_size": 1568,
        "secret_key_size": 3168,
        "ciphertext_size": 1568,
    },
    # FIPS 204: ML-DSA
    "ML-DSA-44": {
        "type": PQCAlgorithmType.SIGNATURE,
        "security_level": 2,
        "public_key_size": 1312,
        "secret_key_size": 2560,
        "signature_size": 2420,
    },
    "ML-DSA-65": {
        "type": PQCAlgorithmType.SIGNATURE,
        "security_level": 3,
        "public_key_size": 1952,
        "secret_key_size": 4032,
        "signature_size": 3309,
    },
    "ML-DSA-87": {
        "type": PQCAlgorithmType.SIGNATURE,
        "security_level": 5,
        "public_key_size": 2592,
        "secret_key_size": 4896,
        "signature_size": 4627,
    },
}


def get_algorithm_info(algorithm_name: str) -> Dict:
    """Get information about a PQC algorithm"""
    return NIST_STANDARD_ALGORITHMS.get(algorithm_name, {})


def list_supported_algorithms() -> List[str]:
    """List all supported PQC algorithms"""
    return list(NIST_STANDARD_ALGORITHMS.keys())


__all__ = [
    "PQCAlgorithmType",
    "PQCBackend",
    "NIST_STANDARD_ALGORITHMS",
    "get_algorithm_info",
    "list_supported_algorithms",
    "PQCProvider",
]
