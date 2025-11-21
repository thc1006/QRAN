"""
E2 Interface Testing Module
============================

This module provides benchmarking and testing capabilities for the E2 interface
in O-RAN architecture (Near-RT RIC ↔ RAN components).

The E2 interface is critical for near-real-time control and optimization of
RAN elements, with latency requirements in the millisecond range.

Key Features:
    - PQC handshake performance testing
    - Latency measurement (握手時間、往返時間)
    - Throughput analysis (加密/解密速率)
    - Multi-vendor interoperability validation
    - Classical vs PQC comparison

Supported PQC Algorithms:
    - ML-KEM (Key Encapsulation Mechanism)
    - ML-DSA (Digital Signature Algorithm)
    - Hybrid modes (Classical + PQC)
"""

from typing import Dict, List, Optional
from enum import Enum


class E2SecurityMode(Enum):
    """E2 interface security modes"""

    CLASSICAL_TLS = "classical_tls"  # Traditional RSA/ECDSA
    PQ_TLS = "pq_tls"  # Pure Post-Quantum
    HYBRID_TLS = "hybrid_tls"  # Hybrid Classical+PQ
    PQ_MTLS = "pq_mtls"  # PQ Mutual TLS


class E2InterfaceType(Enum):
    """E2 interface types"""

    E2_SETUP = "e2_setup"
    E2_CONTROL = "e2_control"
    E2_SUBSCRIPTION = "e2_subscription"
    E2_INDICATION = "e2_indication"


__all__ = [
    "E2SecurityMode",
    "E2InterfaceType",
    "E2Benchmark",
    "E2Connection",
]
