# **QORE\_ONAP\_SECCOM.pdf 全文內容擷取與分析**

## **Page 1: 封面**

**標題:**

* R CORAN LABS  
* QORE: QUANTUMIZED CORE SOLUTION (QORE: 量子化核心解決方案)  
* BEYOND 5G CORE SOLUTION INTEGRATED WITH POST QUANTUM CRYPTOGRAPHY (整合後量子密碼學的 B5G 核心解決方案)  
* QUANTUM SECURE 5G CORE (量子安全 5G 核心)

## **Page 2: 背景故事 (Back Story)**

圖片與新聞摘要分析:  
此頁面展示了多張截圖，強調量子運算對現有網路安全的威脅及相關法規進展。

1. **法規截圖 (Congress.gov):**  
   * **H.R.7535 \- Quantum Computing Cybersecurity Preparedness Act** (量子運算網路安全準備法案)  
   * 117th Congress (2021-2022)  
   * Status: **Became Public Law No: 117-280** (於 12/21/2022 成為公法)  
   * Sponsor: Rep. Khanna, Ro \[D-CA-17\]  
2. **新聞標題:**  
   * "GSMA, IBM and Vodafone Establish Post-Quantum Telco Network Taskforce" (GSMA、IBM 和 Vodafone 成立後量子電信網路工作小組)  
   * "Telefonica, IBM Join Forces to Develop Quantum-Safe Security Solutions" (Telefonica 與 IBM 聯手開發量子安全解決方案)  
   * "Post-Quantum Cryptography Alliance Launches to Advance Post-Quantum Cryptography" (後量子密碼學聯盟成立)  
   * GSMA 發布文件: "Post Quantum Cryptography \- Guidelines for Telecom Use Cases Version 2.0 (04 October 2024)"  
3. 密碼學過渡表 (Transition Table):  
   這張表格列出了現有密碼學算法在未來量子威脅下的安全性預測。

| Key Establishment Scheme (密鑰建立方案) | Parameters (參數) | Transition (過渡期建議) |
| :---- | :---- | :---- |
| **Finite** Field DH and **MQV** \[SP80056A\] | 112 bits of security strength | Deprecated after 2030 (2030後棄用) Disallowed after 2035 (2035後禁用) |
|  | ≥ 128 bits of security strength | Disallowed after 2035 |
| **Elliptic Curve DH and MQC** \[SP80056A\] | 112 bits of security strength | Deprecated after 2030 Disallowed after 2035 |
|  | ≥ 128 bits of security strength | Disallowed after 2035 |
| **RSA** \[SP80056B\] | 112 bits of security strength | Deprecated after 2030 Disallowed after 2035 |
|  | ≥ 128 bits of security strength | Disallowed after 2035 |

## **Page 3: 我們的倡議 (Our Initiatives)**

**主要分為兩大領域的整合：Telecom** (電信) 與 **PQC (後量子密碼學)。**

**1\. Telecom (電信端):**

* **已完成深入原始碼閱讀與文件化:**  
  * Magma Core  
  * OpenAirInterface (OAI) Core  
  * Open5GS Core  
  * Free5GC Core  
  * Aether/SD-Core  
* **核心網路比較基準:**  
  * 效能 (Performance)、穩定性 (Stability)、互操作性 (Interoperability) & 可擴展性 (Scalability)  
  * 安全性 (Security) \- 識別漏洞與缺失的保護機制。使用了 Fuzzing tools (模糊測試工具)、開源假基地台 (open source fake base stations)、33.xxx 技術規範等。  
* *引言:* "Telco guys don't know about PQC" (電信人員不懂 PQC)

**2\.** PQC (密碼學端):

* 實作了多種後量子密碼學 (PQC) 演算法。  
* 研究並分析了多個開源 PQC 函式庫。  
* 測試與基準化 (Benchmarked) PQC 函式庫以評估其效率與安全性。  
* 探索硬體加速技術以優化 PQC 效能。  
* QRNG \+ PQC workaround (量子隨機數生成器 \+ PQC 替代方案)。  
* *引言:* "PQC guys don't know about Telecom" (PQC 人員不懂電信)

**結論:** 兩者結合形成了 **Post Quantum Telecom Network (Foundation of QORE)** (後量子電信網路 \- QORE 的基礎)。

## **Page 4: 安全威脅分析 (Secure Against Several Attacks)**

此頁面展示了多個攻擊場景的圖解，說明現有架構的脆弱性與 QORE 的防護點。

**場景** 1: 針對切片 (Slice) 的攻擊

* **Slice A (安全):** 展示了 NF (Network Function) 之間使用 **PQ-mTLS** (後量子雙向 TLS) 進行通訊，並通過 SCP (Service Communication Proxy)。  
* **Slice** B **(受攻擊):** 展示了一個 **Rogue SCP (惡意 SCP)** 試圖攔截流量。  
* **機制:** NRF (Network Repository Function) 發放 Grant Token。如果 Token 存取被拒絕 (Token access denied)，則攻擊失敗。

**場景 2: Quantum in the Middle (QITM) \- 量子中間人攻擊**

* **圖示:** 攻擊者位於兩個 NF 之間。  
* **現狀:** 即便使用 mTLS 加密，攻擊者 (QITM) 仍可能解密 (Might able to see even if it's encrypted)。  
* **對策:** 使用 PQ-mTLS 防禦。

**場景 3: IMSI Catcher (IMSI 擷取器)**

* **圖示:** 5G UE (用戶設備) 與 UDM (統一數據管理) 之間的通訊。  
* **過程:**  
  * UE 端: **PQC User Identity Concealment (SUPI)** \- 使用 PQC 隱藏用戶身份。  
  * 傳輸中: **SUCI (Ciphertext)** \- 加密後的身份。  
  * 攻擊者: IMSI Catcher 試圖攔截，但顯示 "Not able to see" (無法查看)。  
  * UDM 端: **PQC User Identity Deconcealment (SUCI)** \- 解密還原身份。

**場景 4: Unknown AMF Injection / DoS Attack (未知 AMF 注入 / 阻斷服務攻擊)**

* 展示了一系列信令流程 (NGSetup Request, etc.)。  
* 攻擊者試圖作為 Rogue AMF 或 Rogue gNB 介入。  
* 關鍵流程包含 Token Hijack (Token 劫持) 和針對 N4 介面的 DoS 攻擊。  
* **Quantum-Powered IMSI Catchers** 被列為潛在威脅。

## **Page 5: 安全規範與框架 (Security Specifications & Frameworks)**

列出了 QORE 遵循的標準與技術規範：

* **NIST:** FIPS 203, 204, 205; NIST IR 8547 (過渡至 PQC 標準)。  
* **IETF RFC:** 9113, 9110, 6083, 7748, 5448, 8784, 9242, 6749, 6750, 8773, 8446, 9370。  
* **框架:** GSMA PQTN Framework, MITRE Fight Framework。  
* **3GPP** TS **(技術規範):**  
  * TS 33.501 (5G 系統安全架構)  
  * TS 33.522 (SCAS; SCP)  
  * TS 33.117 (一般安全保障要求)  
  * TS 33.310 (NDS; 認證框架)  
  * TS 35.205 (MILENAGE 演算法)  
  * TS 33.512 (SCAS; AMF)  
  * TS 33.515 (SCAS; SMF)  
  * TS 33.516 (SCAS; AUSF)  
  * TS 33.518 (SCAS; NRF)

## **Page 6: 開源參考實作 (Open Source Reference Implementation)**

展示了 QORE 整合的開源項目與元件結構。

| 類別 | 組件/項目 | 關聯庫 (Libraries) |
| :---- | :---- | :---- |
| **Libraries (函式庫)** | wolfSSL, CIRCL (Cloudflare), PQ-Clean, LibOQS, Bouncy Castle, OQS-Provider, Rustpq-pqcrypto, BoringSSL, OpenSSL, RUSTLS | (這些是基礎密碼學庫) |
| **UE (用戶端)** | UERANSIM | OpenSSL, cuPQC |
| **RAN (無線接入網)** | O-RAN, 5G SOLUTIONS | cuPQC, AWS-LC |
| **CORE (核心網)** | AETHER, SD-CORE, Open5GS, OPENAIRINTERFACE, free5GC, MAGMA | (與上述庫整合) |

## **Page 7: LF Ecosystem For Quantum Secure Network**

展示了 Linux Foundation (LF) 生態系及其他標準組織在量子安全網路中的角色。

* **組織:** The Linux Foundation, Post-Quantum Cryptography Alliance, 3GPP, O-RAN Software Community, LF Connectivity, LF Networking, ETSI, GSMA, IEEE, NIST, IETF。  
* **項目:** OQS Liboqs, OQS OQS-Provider, PQ Code Package, XFAPI, AETHER, NEPHELO, SD-RAN, ONAP, Magma, Open-mplane, SD-CORE, DCNTI。

## **Page 8: 傳統核心安全架構 (Classical Core Security Architecture)**

**圖表分析:** 展示了標準 5G 核心網的架構與其使用的傳統安全協議。

* **網元** (Network **Functions):** NWDAF, SCP, NRF, UDR, UDM, NSSF, CHF, AUSF, AMF, PCF, SMF, UPF。  
* **介面 (Interfaces):** N1/N2, N3, N4, N7, N10, N11, N12, N13, N35, N36, SBI (Service Based Interface)。  
* **使用的協議 (Legend):**  
  * **紅色:** mTLS (雙向 TLS) \- 用於 SBI。  
  * **粉色:** ECC \+ DRBG (橢圓曲線 \+ 確定性隨機位元生成器) \- 用於 UDM/AUSF 相關金鑰生成。  
  * **橘色:** IPSec \- 用於 N4 (SMF-UPF) 和 N3 (RAN-UPF)。  
  * **深藍色:** AES-128 \- 用於加密。  
  * **淺藍色:** OAuth 2.0 \- 用於授權 (如 NRF)。  
  * **綠色:** DTLS/IPSec \- 用於 N1/N2 (RAN-AMF)。

## **Page 9: QORE: Post-Quantum Core (後量子核心)**

**圖表分析:** 展示了 QORE 升級後的架構，對應 Page 8 的位置，但協議已升級為 PQC 版本。

* **升級後的協議** (Legend):  
  * **紅色:** **PQ-mTLS \+ QRNG/TRNG** (後量子 mTLS \+ 量子/真隨機數生成器) \- 用於 SBI。  
  * **粉色:** **ML-KEM \+ QRNG/TRNG** (Module-Lattice Key Encapsulation Mechanism) \- 用於金鑰封裝。  
  * **橘色:** **PQ-IPSec \+ QRNG/TRNG** \- 用於 N4 (SMF-UPF)。  
  * **深藍色:** **AES-256** (升級自 AES-128) \- 提供更強的對稱加密。  
  * **淺藍色:** **PQ-Token based Authorization** (後量子 Token 授權)。  
  * **綠色:** **PQ-IPSec / PQ-DTLS \+ QRNG/TRNG** \- 用於 N1/N2 和 N3。

## **Page 10: 比較圖 (Classical vs Post Quantum Core)**

這是一個詳細的 "Box" 對比圖，展示了從傳統到量子安全核心的具體算法替換。

**左圖: Classical Core (傳統核心)**

* **Key Agreement:** ECC (橢圓曲線)  
* **Digital Certificates:** Classical Signature Scheme (傳統簽章)  
* **Symmetric Key:** AES-128  
* **Random number:** DRBG  
* **Transport Security:** mTLS, IPSec, DTLS  
* **功能:** ECIES Scheme, 5G-AKA, Milenage 等。

**右圖: Post Quantum Core (QORE)**

* **KeyGen, Encaps, Decaps (原 Key Agreement):** **ML-KEM**  
* **Digital Certificates:** **ML-DSA** (Module-Lattice Digital Signature Algorithm)  
* **Symmetric Key:** **AES-256**  
* **Random number:** **TRNG / QRNG** (真/量子隨機數)  
* **Transport Security:** **PQ-mTLS**, **PQ-IPsec**, **PQ-DTLS**  
* **功能:** **PQ-IES Scheme**, 長期金鑰保護等。

## **Page 11: 從 CORE 遷移到 Post-Quantum CORE (Migration Table)**

詳細的協議遷移對照表：

| Functionality (功能) | Classical Mechanism (傳統機制) | Post Quantum Mechanism (後量子機制) |
| :---- | :---- | :---- |
| **Random Number** | DRBG | **TRNG/QRNG** |
| **SBI Communication** | mTLS | **PQ-mTLS** (mTLS **1.3 with PQ)** |
| **Digital Signature in x.509 Certificate** | Classical Signature Scheme | **ML-DSA** |
| **Symmetric Key / N2 CP Message** | AES-128 / DTLS/IPSec | **AES-256** / PQ-DTLS (DTLS 1.3 **with PQ) / PQ-IPSec** |
| **N3/N4** | IPSec | **PQ-IPSec (IKEv2 with PQ)** |
| **ECIES Scheme** | Classical Cryptographic Algorithm (Curve25519, Secp256r1) | **Homogeneous:** ML-KEM **Hybrid:** ML-KEM \+ Classical Cryptographic Algorithm |

## **Page 12: PQ-Service Based Interface (SBI) 規格**

詳細列出了 SBI 介面的參數值。

| Field | Value |
| :---- | :---- |
| **Certificate Signature Algorithm** | **Homogeneous:** ML-DSA-44/65/87 **Hybrid:** ML-DSA\_Ed448, ML-DSA\_Ed25519 \+ Any TLS v1.3/1.2 Classical Signature Schemes |
| **Signature Length** | 3293 octets \+ Classical Signature length (e.g. 64 octets for Ed25519) |
| **Key Exchange Mechanism** | **Homogeneous:** ML-KEM (512/768/1024) **Hybrid:** ECDHE\_ML-KEM (e.g. X25519MLKEM768) |
| **Key Exchange Length (Public key)** | 1216 octets (ML-KEM\_768: 1184 octets, X25519/P256: 32 octets) |
| **Key Exchange CipherText Length** | 1088 octets |
| **AEAD Algorithm** | AES256\_GCM, ChaCha20\_Poly1305 |
| **enckeylen** | 32 octets (256 bits) |
| **TLS KDF** | HMAC-based Expand & Extract KDF (HKDF)/PRF for TLS v1.2 |
| **Fallback Methods** | TLS v1.2, Classical signature algorithms supported |

## **Page 13: PQ-SBI Analysis (日誌分析)**

這頁展示了實際的伺服器日誌與封包擷取截圖，證明系統正在運行 PQC。

**關鍵日誌資訊:**

* **\[INFO\] New PQ TLS connection established.**  
* **Client Supported Signature Schemes:** 包含 ML-DSA-65, Ed448-Dilithium3 等。  
* **Client Supported Curves:** MLKEM768, X25519MLKEM768, SecP256r1MLKEM768。  
* **Server Certificate:**  
  * Issuer: Coran Labs  
  * **Signature Algorithm: ML-DSA-65**  
  * Validity: 2024-10-23 to 2025-10-23  
* **Key Share Entry:** Group: X25519Kyber768Draft00, Length: 1216。

## **Page 14: PQ-IES: PQ-SUPI Concealment (身份隱藏)**

展示了兩種模式的詳細密鑰生成與交換流程圖。

**1\. Homogeneous (純後量子):**

* 使用 **ML-KEM KeyGen**。  
* 流程涉及 Encapsulation (封裝) 與 Decapsulation (解封裝) 來交換 Symmetric Key (AES-256)。  
* 使用 ANSI-X9.63-KDF 導出金鑰。

**2\. Hybrid (混合模式):**

* 結合了 **ML-KEM** 與 **ECC (ECDH X25519)**。  
* 同時生成 Classical Key Pair 和 PQ Key Pair。  
* 最終的 Shared Secret 是兩者的結合，增強過渡期的安全性。

## **Page 15: Level of Security (安全等級金字塔)**

將安全等級分為 4 級 (1 最低，4 最高)。

* **Level 1 (Profile A):** Curve25519 \+ DRBG  
* **Level 2 (Profile B):** Secp256 \+ DRBG  
* **Level 3 (Profile C):** **Homogeneous PQ Cryptography (ML-KEM \+ QRNG)** (紅色虛線框選，QORE 重點)  
* **Level 4 (Profile D):** **Hybrid PQ Cryptography (ML-KEM \+ ECC \+ QRNG)** (紅色虛線框選，QORE 重點)

## **Page 16: Encryption Scheme (II) 參數對照表**

對比 Page 15 中四個 Profile 的詳細密碼學參數。

| Parameters | Profile A | Profile B | Profile C (PQ) | Profile D (Hybrid) |
| :---- | :---- | :---- | :---- | :---- |
| **Domain parameters** | Curve25519 | secp256r1 | **ML-KEM \+ QRNG** | **(Curve25519/secp256r1)** \+ **ML-KEM \+ ECC** |
| **KDF** | ANSI-X9.63-KDF | ANSI-X9.63-KDF | ANSI-X9.63-KDF | ANSI-X9.63-KDF |
| **MAC** | HMAC-SHA-256 | HMAC-SHA-256 | **HMAC-SHA-256/384** | **HMAC-SHA-256/384** |
| **ENC (Encryption)** | AES-128 | AES-128 | **AES-256** | **AES-256** |
| **enckeylen** | 16 octets | 16 octets | **32 octets (256 bits)** | **32 octets** |
| **Backwards compatibility** | false | false | false | **Compatible** (若 ML\_KEM 被攻破仍有 X25519 保護) |

## **Page 17: PQ-Zero Trust Architecture (零信任架構)**

展示了 SCP (Service Communication Proxy) 與 NRF 之間的 **PQ-JWT Token** 交互流程。

**Model D SCP (Direct?):**

1. SCP 向 NRF 發送 Nnrf\_PQ\_JWTToken\_Get\_Request。  
2. NRF 使用其 **PQ-Private Key** 生成並簽署 **PQ JWT Token**。  
3. SCP 獲取 Token 後發送給 NF Service Producer。  
4. Producer 使用 NRF 的 **PQ Public Key** 驗證 Token。

Model C SCP:  
流程類似，但由 NF Service Consumer 請求 Token，而不是 SCP 代表它請求（依圖示箭頭流向差異）。強調所有 Token 簽發與驗證皆使用後量子簽章。

## **Page 18: Q-RAN: Quantum Secure O-RAN (量子安全開放無線接入網)**

展示了 O-RAN 架構中各介面的安全升級。

* **SMO (Non-RT RIC) \<-\> Near-RT RIC (A1介面):** QRNG-Based (PQ-mTLS)。  
* **Near-RT RIC \<-\> O-CU/O-DU (E2介面):** QRNG-Based (PQ-IPSec or PQ-DTLS)。  
* **O-FH (Front Haul):** QRNG-Based (MACsec with PQ based EAP-TLS)。  
* **O-RU \<-\> O-DU:** M-Plane 使用 PQ-mTLS。  
* **O-CU-CP \<-\> 5G Core (N2):** QRNG-Based (PQ-IPSec or PQ-DTLS)。  
* **O-CU-UP \<-\> UPF (N3):** QRNG-Based (PQ-IPSec)。

## **Page 19: E2E Interoperability testing with Q-RAN (端對端互操作性測試)**

**左圖:** 詳細的 O-RU, PQ-DU 架構圖。

* 展示了 **Intel FlexRAN**, **Nvidia Aerial**, **OAI L1** 等不同的 PHY 層實作。  
* 透過 **nFAPI**, **xFAPI** 等介面連接到 **PQ-DU**。

**右圖:** PQ-CU 與 5G CORE 的連接流程。

* **PQ-CU** 內部包含 QRNG 模組生成 Seed。  
* KeyGen 使用 Seed 生成 Public/Private Keys。  
* 透過 **PQC (Encapsulation/Decapsulation)** 機制與 **PQC 5G CORE** 建立安全連接。

## **Page 20: 結論 (Summary)**

**QORE** 是整合了 PQC 的下一代量子安全 5G 核心網。

**核心價值:**

* **Future-Proof Security:** 防禦 CRQCS (Cryptographically Relevant Quantum Computers) 威脅。  
* **Migration Strategy:** 提供結構化的遷移路線圖。  
* **Regulatory Compliance:** 符合 NIST, GSMA, IETF, 3GPP 標準。  
* **Saves you from Cryptocrastination:** 避免 "密碼學拖延症" (Cryptocrastination)。  
* **Optimized Performance:** 確保 PQC 整合不影響效能。  
* **Interoperability & Scalability:** 與現有 5G 基礎設施無縫整合。  
* \*\*