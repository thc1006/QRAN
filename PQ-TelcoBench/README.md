# PQ-TelcoBench: Post-Quantum Telecommunications Benchmarking Platform

## 📋 專案概述

PQ-TelcoBench 是業界第一個專門針對電信網路的後量子密碼(PQC)性能測試與互通性驗證平台。

### 核心目標
- 為 O-RAN 各介面提供 PQC 性能基準測試
- 驗證多廠商 PQC 實作的互通性
- 提供量化的安全性能數據,支援標準化工作

## 🎯 主要功能

### 1. 介面級性能測試
- **E2 介面**: RIC ↔ RAN 元件
- **A1 介面**: Non-RT RIC ↔ Near-RT RIC
- **O1 介面**: SMO ↔ RAN 元件
- **F1 介面**: O-DU ↔ O-CU
- **N2/N3 介面**: RAN ↔ 5G Core

### 2. 性能指標
- 延遲(Latency): 握手時間、往返時間
- 吞吐量(Throughput): 加密/解密速率
- 資源使用: CPU/GPU/記憶體
- 證書鏈長度影響分析

### 3. 比較基準
- RSA-2048 vs ML-KEM-768
- ECDSA vs ML-DSA-65
- 純PQC vs 混合模式
- CPU vs GPU加速

## 🏗️ 架構

```
PQ-TelcoBench/
├── src/                    # 核心源碼
│   ├── e2_interface/       # E2介面測試模組
│   ├── a1_interface/       # A1介面測試模組
│   ├── o1_interface/       # O1介面測試模組
│   ├── f1_interface/       # F1介面測試模組
│   ├── n2n3_interface/     # N2/N3介面測試模組
│   ├── pqc_lib/            # PQC演算法整合
│   └── utils/              # 共用工具
├── tests/                  # 測試套件
│   ├── unit/               # 單元測試
│   ├── integration/        # 整合測試
│   └── performance/        # 性能測試
├── benchmarks/             # 基準測試
│   ├── results/            # 測試結果
│   └── datasets/           # 測試數據集
├── docs/                   # 文檔
│   ├── architecture/       # 架構文檔
│   ├── api/                # API文檔
│   └── tutorials/          # 教學文檔
├── config/                 # 配置文件
└── scripts/                # 輔助腳本
```

## 🛠️ 技術棧

### 核心技術
- **語言**: Python 3.10+, Go 1.21+
- **PQC 函式庫**: liboqs, oqs-provider, wolfSSL
- **GPU 加速**: NVIDIA cuPQC
- **測試框架**: pytest, Go testing
- **容器化**: Docker, Docker Compose
- **監控**: Prometheus, Grafana
- **O-RAN 整合**: O-RAN SC 平台

### PQC 演算法支援
- **密鑰封裝**: ML-KEM-512/768/1024 (FIPS 203)
- **數位簽章**: ML-DSA-44/65/87 (FIPS 204)
- **哈希簽章**: SLH-DSA (FIPS 205)

## 🚀 快速開始

### 環境需求
- Python 3.10+
- Docker & Docker Compose
- GPU (可選,用於 cuPQC 加速測試)
- 8GB+ RAM
- 20GB+ 磁碟空間

### 安裝

```bash
# 克隆專案
git clone <repository-url>
cd PQ-TelcoBench

# 安裝Python依賴
pip install -r requirements.txt

# 安裝 liboqs (系統層級)
./scripts/install_liboqs.sh

# 啟動測試環境(需要Docker)
docker-compose up -d
```

### 執行基礎測試

```bash
# E2介面性能測試
python -m src.e2_interface.benchmark --algorithm ML-KEM-768

# 執行完整測試套件
pytest tests/

# 生成基準報告
python -m src.utils.report_generator --output benchmarks/results/
```

## 📊 開發階段

### Phase 1 (Month 1-3) - 基礎框架 ✅ 進行中
- [x] 專案結構建立
- [ ] E2介面測試實作
- [ ] 基礎 PQC 整合(liboqs)
- [ ] 單元測試覆蓋

### Phase 2 (Month 4-6) - 多介面支援
- [ ] A1/O1/F1 介面實作
- [ ] 多廠商測試環境
- [ ] 整合測試框架

### Phase 3 (Month 7-9) - GPU 加速優化
- [ ] cuPQC 整合
- [ ] 性能優化
- [ ] Web 監控界面

### Phase 4 (Month 10-12) - 標準化與發布
- [ ] 標準化提案
- [ ] 完整文檔
- [ ] 開源社群發布

## 🎓 參考資料

### 標準文檔
- NIST FIPS 203/204/205 (PQC Standards, 2024)
- O-RAN Alliance Security Specifications
- 3GPP TS 33.501 (5G Security Architecture)

### 學術論文
- Rathi, V., et al. "Q-RAN: Quantum-Resilient O-RAN Architecture" (2024)
- García-Revillo, J., et al. "Introducing Post-Quantum algorithms in Open RAN interfaces" (2025)

### 開源專案
- [Open Quantum Safe](https://openquantumsafe.org/)
- [NVIDIA cuPQC](https://developer.nvidia.com/cupqc)
- [O-RAN Software Community](https://docs.o-ran-sc.org/)

## 📝 授權

Apache 2.0 License

## 🤝 貢獻

歡迎貢獻! 請閱讀 [CONTRIBUTING.md](./docs/CONTRIBUTING.md) 了解詳情。

## 📧 聯繫

- 專案維護者: [您的資訊]
- Issue 追蹤: [GitHub Issues]
- 討論區: [GitHub Discussions]

---

**⭐ 如果這個專案對您有幫助,請給我們一個星標!**

*建立日期: 2025-11-22*
*基於 Q-RAN 研究專案戰略規劃*
