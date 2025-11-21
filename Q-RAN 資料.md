[LF Networking Post Quantum Safety](https://lf-networking.atlassian.net/wiki/spaces/LN/pages/362151937/Post+Quantum+Safety)


### QORE 專案簡報摘要（2025年3月26日）

- **專案名稱**：QORE（屬於 5G SBP 專案）
- **主導團隊**：Coran Labs
- **簡報對象**：ONAP SECCOM（ONAP 安全委員會）
- **簡報結果**：獲得良好回饋
- **下一步**：將向 ORAN WG1 進行簡報
- **其他事項**：若有其他 LF/LFN 專案對 QORE 有興趣，請聯繫團隊安排簡報

![image003](https://hackmd.io/_uploads/Sy4sOJSAJx.png)

事實上，我們的 PoC 和工作解決方案已經準備好了。過去幾年，我們一直積極致力於從經典安全性向後量子安全的遷移。作為該計劃的一部分，我們開發了開源專案－QORE（量子安全核心）和Q-RAN（量子安全O-RAN），實現了端對端量子安全核心和O-RAN網路。此外，我們也研究了各種項目的遷移策略。


我附上了一張圖，其中初步概述瞭如何使用一些現有的 LF 聯盟專案來遷移 LF 專案以支援量子安全。

[QORE（Quantumised 5G Core）](https://www.youtube.com/watch?v=w1ac3SMiGmM)是由 Coran Labs 開發的專案，旨在透過整合後量子加密技術（Post-Quantum Cryptography, PQC）和量子隨機數生成器（Quantum Random Number Generator, QRNG），提升 5G 核心網路的安全性。


另外，我們的「後量子電信網路開源參考實作」現在已經上線了。這個資源展示了開源專案如何強化資安、防範具備密碼破解能力的量子電腦（CRQCs）。雖然它主要是針對電信領域，不過也可以當作其他專案的參考範例。想了解更多內容可以參考我們的文章，我們也很推薦你看看其他相關的文章和部署影片喔！

---


![image](https://hackmd.io/_uploads/H1jEskBCJx.png)

以下是整理後的**重點摘要**，以及翻譯成**台灣繁體中文口語邏輯**的版本：

---

## 📌 重點整理：

1. **QORE 支援兩種後量子安全機制**：  
   - **純後量子（Post-Quantum）**
   - **混合後量子（Hybrid Post-Quantum）**  
   這種混合方式符合 ETSI TS 104 015 v1.1.1 的技術規範。

2. **在 5G 系統中的授權機制**：
   - 可結合 **屬性式加密（ABE）** 與 **具存取控制的金鑰封裝機制（KEMAC）**，  
     來控制哪些 Network Functions（NFs）能存取其他特定的 NFs。
   - 僅當 NF 符合目標 NF 所要求的屬性時，才允許存取。
   - 但這樣的實作會相當複雜，需要**大幅修改現有架構與演算法**。

3. **基礎金鑰封裝機制的推薦做法**：
   - 應優先採用 **ML-KEM** 和 **ML-DSA**（NIST、GSMA PQTN 和 IETF 均有推薦）
   - QORE 已開始實作這些標準。
   - 實作完成後，可再探索如 KEMAC 等更進階的機制與延伸應用。

### 詢問
關於這個主題，這邊附上一份簡報連結，是針對 5G Advanced Release 中的 MDA 架構與 MnS Type A、B、C 的相關說明。從簡報內容可以看到，無論是 Core 還是 RAN 端的 NRM 模型，都需要實作，這其實早在 LTE EPS 時代（3GPP Release 8~14）就已存在。

所以也希望你在方案裡能標示出，是否有考慮這個部分（「有」或「沒有」），更重要的是請說明為什麼這樣設計？

另外要注意的是，O-RAN 聯盟在 2024 年 10 月的 SMO 規範中，也有引用 3GPP MDA，並且有一個獨立章節「Recommended SBA Architecture」來說明。這點在簡報中也有提到，建議一併納入考量。

關於 AI/ML 模型的訓練與傳送、CAPIF 以及用戶授權或身份識別的議題，這次我沒有特別深入，不過這些內容其實在標準中都有明確定義。尤其是 5G Advanced 裡面「User」的定義，已經不再只限於「人」，這點未來在簡報裡提一下會比較完整。

你這次方案中專注在 N4 的應用（可能是因為 PFCP），但我會建議同時考慮到：

如何對外公開網路拓撲（例如第三方 ISP/ICP 的接入）

新的角色定義，例如在「未來工廠」場景下，新增的「服務營運商」角色（Service Operator），這是除了原本的 MNO、ISP、ICP 外新增的重要參與者。

最後還想提一點，5G Advanced 標準裡對於**資料粒度（granularity）**的分類變得更細，會依照不同應用情境進行差異化定義，這對於服務效率跟資源配置也有幫助，可以作為方案補充方向。


### 回復
我想特別強調一下，QORE 同時支援 **純後量子** 跟 **混合後量子** 的安全機制，而這種混合架構的想法，也與 ETSI TS 104 015 v1.1.1 的標準是一致的。

在 5G 系統中，我們可以結合像是 **屬性式加密（ABE）** 和 **具存取控制的金鑰封裝機制（KEMAC）** 來加強授權流程。舉例來說，只有擁有特定屬性的 Network Function（NF） 才能存取對應的目標 NF。這樣能有效強化安全性。

不過要實作這個機制並不簡單，因為它需要對整個系統架構和演算法進行大量修改。

因此在一開始，我們建議先依照 NIST、GSMA PQTN 和 IETF 的建議，實作 **ML-KEM** 與 **ML-DSA** 做為金鑰封裝的核心機制。QORE 已經在進行這方面的實作。等這個基礎建好之後，再往上擴展或實驗像 KEMAC 這類更進階的應用，就會比較容易。

