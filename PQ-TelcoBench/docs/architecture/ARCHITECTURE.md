# PQ-TelcoBench 架構設計文檔

## 1. 系統概述

PQ-TelcoBench 是一個專門針對電信網路的後量子密碼(PQC)性能測試與互通性驗證平台,聚焦於 O-RAN 架構中的各個關鍵介面。

### 1.1 設計目標

- **性能基準測試**: 為 O-RAN 介面提供準確的 PQC 性能數據
- **互通性驗證**: 測試多廠商 PQC 實作的相容性
- **標準化支援**: 產出可供標準組織參考的量化數據
- **易於擴展**: 模組化設計,方便新增介面和演算法支援

### 1.2 核心價值

- ⭐ **業界第一**: 首個電信專用 PQC 測試平台
- ⭐ **填補空白**: 解決 O-RAN Alliance 和 3GPP 的測試需求
- ⭐ **開源優勢**: 促進社群協作與快速採用

## 2. 系統架構

### 2.1 整體架構圖

```
┌────────────────────────────────────────────────────────────────┐
│                     PQ-TelcoBench Platform                      │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ E2 Interface │  │ A1 Interface │  │ O1 Interface │         │
│  │   Testing    │  │   Testing    │  │   Testing    │  ...    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                  │                  │                  │
│         └──────────────────┴──────────────────┘                 │
│                            │                                     │
│                   ┌────────▼────────┐                           │
│                   │   PQC Library   │                           │
│                   │   (liboqs,      │                           │
│                   │    wolfSSL,     │                           │
│                   │    cuPQC)       │                           │
│                   └────────┬────────┘                           │
│                            │                                     │
│         ┌──────────────────┴──────────────────┐                │
│         │                                      │                │
│    ┌────▼─────┐                        ┌──────▼──────┐         │
│    │ Metrics  │                        │   Utils     │         │
│    │Collection│                        │  (Logger,   │         │
│    │          │                        │  Config)    │         │
│    └────┬─────┘                        └─────────────┘         │
│         │                                                        │
└─────────┼────────────────────────────────────────────────────── ┘
          │
          ▼
┌─────────────────────────────────────────┐
│         Monitoring Stack                 │
├─────────────────────────────────────────┤
│  Prometheus → Grafana → Time-Series DB  │
└─────────────────────────────────────────┘
```

### 2.2 模組化分層

#### 2.2.1 介面測試層 (Interface Testing Layer)

各 O-RAN 介面的專用測試模組:

- **E2 Interface Module** (`src/e2_interface/`)
  - 功能: Near-RT RIC ↔ RAN 元件測試
  - 關鍵指標: 毫秒級延遲、握手性能
  - 安全模式: PQ-TLS, PQ-mTLS, Hybrid

- **A1 Interface Module** (`src/a1_interface/`)
  - 功能: Non-RT RIC ↔ Near-RT RIC 測試
  - 關鍵指標: 策略下發延遲、吞吐量

- **O1 Interface Module** (`src/o1_interface/`)
  - 功能: SMO ↔ RAN 元件管理介面測試
  - 關鍵指標: 憑證管理、配置同步

- **F1 Interface Module** (`src/f1_interface/`)
  - 功能: O-DU ↔ O-CU 測試
  - 關鍵指標: PDCP 安全性能

- **N2/N3 Interface Module** (`src/n2n3_interface/`)
  - 功能: RAN ↔ 5G Core 測試
  - 關鍵指標: Q-Psec, PQ-DTLS 性能

#### 2.2.2 PQC 抽象層 (PQC Abstraction Layer)

統一的 PQC 操作介面 (`src/pqc_lib/`):

```python
class PQCProvider(ABC):
    def generate_keypair() -> Tuple[bytes, bytes]
    def kem_encapsulate(public_key) -> Tuple[bytes, bytes]
    def kem_decapsulate(secret_key, ciphertext) -> bytes
    def sign(secret_key, message) -> bytes
    def verify(public_key, message, signature) -> bool
```

**支援的後端**:
- **liboqs**: 主要 PQC 實作,支援所有 NIST 標準演算法
- **wolfSSL**: 商業級 PQC 實作
- **cuPQC**: NVIDIA GPU 加速版本
- **BoringSSL**: Google PQC 實作 (未來支援)

#### 2.2.3 工具層 (Utility Layer)

共用工具和輔助功能 (`src/utils/`):

- **Logger**: 結構化日誌記錄
- **Config Loader**: YAML/JSON 配置解析
- **Metrics Collector**: Prometheus 指標收集
- **Report Generator**: 測試報告生成

### 2.3 資料流程

```
測試配置 (YAML)
    │
    ▼
┌─────────────────┐
│ Benchmark Class │
└────────┬────────┘
         │
         ├─► generate_keypair() ──┐
         │                        │
         ├─► handshake_test()     ├─► PQC Provider
         │                        │    (liboqs/cuPQC)
         ├─► throughput_test()    │
         │                        │
         └─► collect_metrics() ───┘
                  │
                  ▼
         ┌───────────────┐
         │ BenchmarkResult│
         └───────┬────────┘
                 │
                 ├─► JSON Export
                 ├─► Prometheus Metrics
                 └─► Grafana Dashboard
```

## 3. 關鍵設計決策

### 3.1 為何選擇 Python?

- **快速原型開發**: MVP 在 3-4 週內完成
- **豐富的生態系統**: 測試、數據處理、視覺化庫完善
- **liboqs 支援**: 官方 Python binding 成熟
- **易於整合**: 與 Docker, K8s, Prometheus 整合簡單

**性能關鍵路徑考量**:
- PQC 核心操作由 C library (liboqs) 執行
- Python 僅負責測試編排和結果收集
- 未來可用 Go 重寫性能敏感模組

### 3.2 模組化設計原則

1. **鬆耦合**: 各介面模組獨立,可單獨測試
2. **高內聚**: 相關功能集中在同一模組
3. **可擴展**: 新增演算法或介面只需實作介面
4. **可測試**: 每個模組都有對應單元測試

### 3.3 安全考量

- **密鑰管理**: 測試密鑰僅在記憶體中,不持久化
- **隔離環境**: 使用 Docker 容器隔離測試環境
- **審計日誌**: 所有操作都有詳細日誌記錄
- **最小權限**: 容器以非 root 使用者執行 (未來實作)

## 4. 技術選型

### 4.1 核心依賴

| 組件 | 選擇 | 原因 |
|------|------|------|
| PQC Library | liboqs 0.12.0+ | NIST標準化演算法完整支援 |
| 測試框架 | pytest | 功能強大,插件豐富 |
| 容器化 | Docker + Compose | 跨平台部署,環境一致性 |
| 編排 | Kubernetes | 生產級擴展性 |
| 監控 | Prometheus | 時間序列數據,業界標準 |
| 視覺化 | Grafana | 豐富的儀表板功能 |

### 4.2 可選增強

- **GPU 加速**: NVIDIA cuPQC (需 CUDA 環境)
- **分散式測試**: Celery + Redis (未來實作)
- **CI/CD**: GitHub Actions (未來實作)

## 5. 部署架構

### 5.1 開發環境

```
本地機器
├─ Docker Desktop
│  ├─ PQ-TelcoBench 容器
│  ├─ Prometheus 容器
│  └─ Grafana 容器
└─ Python 虛擬環境 (venv)
```

### 5.2 生產環境 (未來)

```
Kubernetes Cluster
├─ Namespace: pq-telebench
│  ├─ Deployment: pq-telebench (3 replicas)
│  ├─ Service: pq-telebench-service
│  ├─ PersistentVolumeClaim: results-storage
│  └─ ConfigMap: benchmark-config
├─ Namespace: monitoring
│  ├─ Prometheus Operator
│  ├─ Grafana
│  └─ Alert Manager
└─ Namespace: oran-testbed
   ├─ Near-RT RIC
   ├─ O-DU Simulator
   └─ O-CU Simulator
```

## 6. 性能考量

### 6.1 預期性能指標

基於初步研究,預期的性能基準:

| 操作 | 古典 (RSA-2048) | PQC (ML-KEM-768) | GPU加速 PQC |
|------|----------------|------------------|-------------|
| 密鑰生成 | 50ms | 0.5ms | 0.05ms |
| 封裝 | - | 0.3ms | 0.03ms |
| 解封裝 | - | 0.4ms | 0.04ms |
| 簽章 | 5ms | 3ms | 0.3ms |
| 驗證 | 0.5ms | 2ms | 0.2ms |

*註: 數據基於 cuPQC 論文和 liboqs 基準測試*

### 6.2 擴展性設計

- **水平擴展**: K8s 多 Pod 並行測試
- **垂直擴展**: GPU 加速單個測試吞吐
- **批次處理**: 多個測試案例排程執行

## 7. 未來路線圖

### Phase 1 (Q1 2025) - MVP ✅ 進行中
- E2 介面基礎測試
- liboqs 整合
- Docker 環境

### Phase 2 (Q2 2025)
- A1/O1/F1/N2/N3 介面支援
- 多廠商互通性測試
- GPU 加速 (cuPQC)

### Phase 3 (Q3 2025)
- Web UI 儀表板
- 自動化報告生成
- CI/CD 整合

### Phase 4 (Q4 2025)
- O-RAN SC 貢獻
- 標準化提案
- 學術論文發表

## 8. 參考架構

本設計參考以下架構:

- **O-RAN Architecture** (O-RAN Alliance)
- **NIST PQC Framework**
- **Prometheus 監控架構**
- **Kubernetes CRD 模式**

## 9. 附錄

### 9.1 術語表

- **KEM**: Key Encapsulation Mechanism (密鑰封裝機制)
- **DSA**: Digital Signature Algorithm (數位簽章演算法)
- **mTLS**: Mutual TLS (雙向 TLS)
- **RIC**: RAN Intelligent Controller (RAN 智慧控制器)
- **SMO**: Service Management and Orchestration

### 9.2 相關標準

- NIST FIPS 203/204/205 (PQC Standards)
- O-RAN WG11 Security Specifications
- 3GPP TS 33.501 (5G Security)
- ETSI TS 104 015 (Hybrid PQC)
