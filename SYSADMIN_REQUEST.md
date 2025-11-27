# 系統管理員權限與環境配置請求

**申請人**: thc1006
**申請日期**: 2025-11-22
**專案**: Q-RAN / PQ-TelcoBench
**緊急程度**: 中等

---

## 📋 執行摘要

我正在進行 **Q-RAN (量子安全開放無線接取網路)** 研究專案,目前已完成:
- ✅ 專案文檔分析與戰略規劃
- ✅ PQ-TelcoBench 程式框架建立
- ✅ Docker/K8s 配置文件準備

但遇到系統環境限制,需要系統管理員協助配置開發環境。

---

## 🚨 當前問題

### 1. Docker 存取權限問題

```bash
# 症狀
$ docker ps
permission denied while trying to connect to the Docker daemon socket...

# 原因
$ groups
users ecgTeam  # 不在 docker 組

$ ls -la /var/run/docker.sock
srw-rw---- 1 root docker  # 需要 docker 組權限
```

**影響**: 無法執行容器化開發與測試

### 2. Python 環境不完整

```bash
# 症狀
$ python3 -m venv venv
ensurepip is not available

$ python3 -m pip
No module named pip

# 缺少套件
- python3-pip
- python3-venv
```

**影響**: 無法建立 Python 虛擬環境,無法安裝依賴套件

### 3. Sudo 權限受限

```bash
$ sudo -l
User thc1006 may run the following commands:
    (root) NOPASSWD: /bin/mount, /bin/umount
# 僅有 mount/umount 權限
```

**影響**: 無法自行安裝系統套件或修改系統配置

---

## ✅ 需要的協助

### 請求 1: 加入 Docker 組 (最高優先級)

```bash
sudo usermod -aG docker thc1006
```

**目的**: 允許使用者執行 Docker 命令而不需 sudo

**驗證方式**:
```bash
# 重新登入後
$ groups
users ecgTeam docker  # 應該包含 docker

$ docker ps  # 應該可以執行
```

### 請求 2: 安裝 Python 開發套件

```bash
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential
```

**目的**: 啟用 Python 虛擬環境和套件管理

**驗證方式**:
```bash
$ python3 -m pip --version
pip XX.X.X

$ python3 -m venv test_venv
$ source test_venv/bin/activate
(test_venv) $  # 成功建立虛擬環境
```

### 請求 3: 安裝 Kubernetes 工具 (可選,次要優先級)

```bash
# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# 或使用 snap
sudo snap install kubectl --classic
```

**目的**: 用於 Kubernetes 部署測試 (開發後期需要)

---

## 📦 專案背景說明

### 專案簡介

**PQ-TelcoBench** 是業界第一個電信專用的後量子密碼(PQC)性能測試平台,專注於 O-RAN 架構。

### 研究意義

- **國際趨勢**: NIST 2024年8月發布 PQC 標準 (FIPS 203/204/205)
- **產業需求**: O-RAN Alliance 2025年啟動 PQC 工作項
- **技術空白**: 當前缺乏電信專用的 PQC 測試工具

### 為何需要 Docker?

1. **隔離環境**: PQC 函式庫(liboqs)需要特定編譯環境
2. **可重現性**: 確保測試環境一致性
3. **O-RAN 模擬**: 需要容器化的網路元件測試床
4. **標準化部署**: 符合產業最佳實踐

### 專案時程

- **Phase 1** (當前 - 3個月): E2介面測試 MVP
- **Phase 2** (3-6個月): 多介面支援
- **Phase 3** (6-9個月): GPU加速優化
- **Phase 4** (9-12個月): 標準化貢獻與開源發布

---

## 🔐 安全考量

### 為何需要 Docker 組權限?

- Docker 組權限等同於 root 權限,我們理解這個安全風險
- 但對於容器化開發,這是標準做法
- 我們將:
  - 僅在專案目錄下執行容器
  - 不執行來路不明的映像檔
  - 遵循最小權限原則

### 資料安全

- 測試數據僅存於 `/home/thc1006/dev/QRAN/` 目錄
- 不涉及生產數據或敏感資訊
- 所有密鑰為測試用途,不持久化

---

## 🛠️ 替代方案 (如無法批准完整請求)

如果無法提供 Docker 組權限,我們可以:

### 方案 A: Rootless Docker

```bash
# 安裝 rootless Docker
dockerd-rootless-setuptool.sh install
```

- 不需 root 權限
- 使用者命名空間隔離
- 但性能略低,配置複雜

### 方案 B: 使用 Podman

```bash
sudo apt-get install podman
```

- 無 daemon 架構
- 不需特殊權限
- 但與 Docker Compose 相容性較差

### 方案 C: 雲端開發環境

- 使用 GitHub Codespaces 或 GitPod
- 但延遲較高,且需要網路連線

---

## 📊 預期成果

成功配置環境後,我們將能夠:

1. ✅ 執行 E2 介面 PQC 性能測試
2. ✅ 產生可視化的基準測試報告
3. ✅ 貢獻至 O-RAN 開源社群 (O-RAN SC)
4. ✅ 發表學術論文至 IEEE 會議

---

## 📝 額外資訊

### 目錄結構

```
/home/thc1006/dev/QRAN/
├── CLAUDE.md                     # 專案戰略規劃文檔
├── PQ-TelcoBench/                # 主要專案
│   ├── src/                      # 源碼
│   ├── tests/                    # 測試
│   ├── docker-compose.yml        # Docker 配置
│   ├── kubernetes/               # K8s 部署檔
│   └── docs/architecture/        # 架構文檔
└── 研究文檔/                      # 6份詳細研究筆記
```

### 磁碟空間需求

- Docker 映像檔: ~2GB
- Python 虛擬環境: ~500MB
- 測試結果數據: ~1GB
- **總計**: 約 4GB

### 網路需求

- Docker Hub: 下載基礎映像檔
- GitHub: 克隆 liboqs 等開源專案
- PyPI: 安裝 Python 套件

---

## 🤝 聯絡方式

如有任何問題或需要更多資訊,請隨時聯繫:

- **使用者**: thc1006
- **專案路徑**: `/home/thc1006/dev/QRAN/`
- **Email**: [您的Email]

---

## ⏱️ 時效性

- **最佳完成時間**: 1-2個工作天
- **替代方案準備時間**: 若無法批准,我會嘗試 Rootless Docker (需額外 3-5 天設置)

---

## ✍️ 簽名確認

我確認:
- ✅ 理解 Docker 組權限的安全影響
- ✅ 僅用於學術研究與開發目的
- ✅ 遵守系統使用政策
- ✅ 不執行未經審查的第三方容器

**申請人**: thc1006
**日期**: 2025-11-22

---

**感謝您的協助!這對我們的研究專案至關重要。** 🙏
