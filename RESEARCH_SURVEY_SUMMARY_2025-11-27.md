# 大規模網路調研摘要
## 2025-11-27

---

## 調研概述

- **調研方式**: 內建 WebSearch (MCP omnisearch 未啟動)
- **搜尋次數**: 16次深度搜尋
- **更新文檔**: `RESEARCH_TOPICS_2025-11.md` (v1.0 → v2.0)

---

## 調研摘要

| 搜尋領域 | 關鍵發現 |
|---------|---------|
| **Q-RAN/PQC in O-RAN** | E2介面PQ-IPsec/PQ-DTLS架構已有QORE框架實作 |
| **CV-QKD部署** | 120km+經典通道共存、3倍密鑰率提升 |
| **GPU加速** | cuPQC達143倍加速 (H100)、1330萬keygen/秒 |
| **密碼敏捷性** | 僅5%組織完全自動化、2029年47天憑證週期 |
| **量子糾纏網路** | BearlinQ柏林測試床99%保真度連續17天 |
| **混合QKD+PQC** | 中國電信1000km部署、Singtel東南亞首個混合QSN |
| **xApp/rApp安全** | 對抗攻擊可降低ML準確度、量子防禦潛力 |
| **IoT邊緣** | ZT-IoTrust框架、輕量PQC挑戰 |
| **O-RAN SC安全** | NIST評估顯示<30%安全標準覆蓋 |
| **衛星QKD** | 中國2025年發射新量子衛星、地面站網路擴展 |
| **量子同步** | QNS可達飛秒級精度、解決PTP累積誤差 |
| **QRNG** | 3 Gbps晶片、Samsung Galaxy Quantum 6整合 |

---

## 新增5個研究主題 (總計20個)

| # | 主題 | 創新度 | 可行性 |
|---|------|--------|--------|
| 16 | QSDC與時敏網路整合 | ★★★★★ | ★★★☆☆ |
| 17 | QRNG晶片整合O-RAN | ★★★★☆ | ★★★★★ |
| 18 | Open Fronthaul PQ-MACsec | ★★★★☆ | ★★★★☆ |
| 19 | 量子非線性同步(QNS) | ★★★★★ | ★★★☆☆ |
| 20 | QRL量子強化學習xApp | ★★★★★ | ★★★★☆ |

---

## 更新後的優先建議

### 立即啟動 (短期 6-12個月)

| 優先級 | 主題 | 原因 |
|--------|------|------|
| 🥇 | 主題13: GPU加速PQC | cuPQC已整合OQS，工具成熟 |
| 🥈 | 主題17: QRNG整合 | 商業晶片可得，整合門檻低 |
| 🥉 | 主題6: PQC側信道評估 | 2025 SoK論文提供方法論 |
| 4 | 主題12: 密碼敏捷性平台 | Sectigo報告驗證急迫性 |

### 中期突破 (12-24個月)

| 優先級 | 主題 | 原因 |
|--------|------|------|
| 🥇 | 主題2: CV-QKD Open Fronthaul | 120km+經典共存已驗證 |
| 🥈 | 主題18: PQ-MACsec | FPGA實作可行性已證明 |
| 🥉 | 主題20: QRL xApp | QRL 20倍加速論文剛發表 |
| 4 | 主題7: 量子零信任 | QORE框架可參考 |

### 長期願景 (24-36個月)

| 優先級 | 主題 | 原因 |
|--------|------|------|
| 🥇 | 主題1: E2糾纏輔助 | BearlinQ驗證糾纏分發可行 |
| 🥈 | 主題16: QSDC-TSN | 首個整合框架剛發表 |
| 🥉 | 主題19: 量子同步 | Nature論文提供理論基礎 |
| 4 | 主題5: 衛星-地面融合 | 中國2025年發射新衛星 |

---

## 關鍵參考來源 (2025年11月最新)

### CV-QKD與量子網路
- [CV-QKD 120km with Classical Channels](https://journals.aps.org/prl/abstract/10.1103/zy2d-m3ch)
- [Enhanced CV-QKD Protocol](https://www.nature.com/articles/s42005-025-02317-5)
- [Deutsche Telekom BearlinQ](https://www.telekom.com/en/media/media-information/archive/breakthrough-for-the-quantum-internet-1090094)
- [Heriot-Watt Quantum Network](https://www.hw.ac.uk/news/2025/shop-bought-cable-powers-quantum-breakthrough-2)

### GPU加速與性能
- [NVIDIA cuPQC Introduction](https://developer.nvidia.com/blog/introducing-nvidia-cupqc-for-gpu-accelerated-post-quantum-cryptography/)
- [cuPQC + OQS Integration](https://pqca.org/news/2025/post-quantum-cryptography-alliance-brings-accelerated-computing-to-post-quantum-cryptography-with-nvidia-cupqc/)
- [QORE Framework](https://arxiv.org/html/2510.19982v1)

### 密碼敏捷性
- [Sectigo 2025 Crypto Agility Report](https://www.sectigo.com/resource-library/2025-state-of-crypto-agility-report-preparing-for-post-quantum)
- [NIST PQC Migration Project](https://www.nccoe.nist.gov/crypto-agility-considerations-migrating-post-quantum-cryptographic-algorithms)

### O-RAN安全
- [O-RAN Alliance Security Update 2025](https://www.o-ran.org/blog/o-ran-alliance-security-update-2025)
- [NIST O-RAN Security Project](https://www.nist.gov/programs-projects/advanced-security-architectures-next-generation-wireless)
- [Q-RAN Architecture](https://arxiv.org/html/2510.19968)

### 混合QKD+PQC
- [China Telecom Hybrid System](https://thequantuminsider.com/2025/05/20/china-telecom-launches-hybrid-quantum-safe-encryption-system-completes-1000-kilometer-secure-call/)
- [Singtel Hybrid QSN](https://www.crnasia.com/news/2025/cybersecurity/singapore-gears-up-for-post-quantum-cryptography-threats)

### GSMA與標準化
- [GSMA Post Quantum Era Programme](https://www.gsma.com/solutions-and-impact/technologies/security/post-quantum/)
- [GSMA PQ.03 Guidelines](https://www.gsma.com/newsroom/wp-content/uploads/PQ.03-Post-Quantum-Cryptography-Guidelines-for-Telecom-Use-v1.0.pdf)

### 量子同步與QSDC
- [QNS for Future Networks](https://www.nature.com/articles/s41598-025-92038-0)
- [QSDC-TSN Integration](https://www.mdpi.com/1099-4300/27/3/221)
- [QRL for 6G Networks](https://arxiv.org/html/2511.01070v1)

---

## MCP 設定備註

`.mcp.json` 配置了 omnisearch (Tavily + Perplexity)，但工具未載入。
可嘗試重啟 Claude Code 以啟用 MCP 功能進行更深入的調研。

```json
{
  "mcpServers": {
    "omnisearch": {
      "command": "npx",
      "args": ["-y", "mcp-omnisearch@latest"],
      "env": {
        "TAVILY_API_KEY": "...",
        "PERPLEXITY_API_KEY": "..."
      }
    }
  }
}
```

---

**記錄時間**: 2025-11-27
**文檔版本**: 1.0
