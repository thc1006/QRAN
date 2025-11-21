"""
PQ-TelcoBench: Post-Quantum Telecommunications Benchmarking Platform
====================================================================

A comprehensive benchmarking platform for Post-Quantum Cryptography
in telecommunications networks, focusing on O-RAN interfaces.

Modules:
    - e2_interface: E2 interface testing (RIC ↔ RAN components)
    - a1_interface: A1 interface testing (Non-RT RIC ↔ Near-RT RIC)
    - o1_interface: O1 interface testing (SMO ↔ RAN components)
    - f1_interface: F1 interface testing (O-DU ↔ O-CU)
    - n2n3_interface: N2/N3 interface testing (RAN ↔ 5G Core)
    - pqc_lib: Post-Quantum Cryptography library integrations
    - utils: Common utilities and helpers
"""

__version__ = "0.1.0"
__author__ = "Q-RAN Research Team"
__license__ = "Apache-2.0"

from typing import Dict, Any

# Package metadata
METADATA: Dict[str, Any] = {
    "name": "PQ-TelcoBench",
    "version": __version__,
    "description": "Post-Quantum Telecommunications Benchmarking Platform",
    "supported_interfaces": ["E2", "A1", "O1", "F1", "N2", "N3"],
    "supported_algorithms": {
        "kem": ["ML-KEM-512", "ML-KEM-768", "ML-KEM-1024"],
        "signature": ["ML-DSA-44", "ML-DSA-65", "ML-DSA-87"],
        "hash_signature": ["SLH-DSA"],
    },
}
