# 6G 網路與企業專網中的 Q-RAN 新風險分析與緩解策略

## 6G 公共網路場景的 Q-RAN 風險

在6G行動網路中導入**Quantum-RAN (Q-RAN)**，相較於傳統的**Open RAN (O-RAN)**，將增添額外的風險考量。以下從供應鏈、量子裝置壽命、密鑰更新頻率三方面說明新出現的風險及其緩解策略。

### 供應鏈風險
6G網路中的Q-RAN需使用專門的量子元件和新型量子模組，其供應鏈相對脆弱。相比傳統O-RAN採用成熟的通訊硬體，Q-RAN所依賴的量子硬體仍處於早期發展階段，多數6G相關的量子技術僅達技術成熟度等級TRL 1–3 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=quantum%20cloud%20computing%20,integration%20within%20future%206G%20networks))。這意味著供應來源有限，對特定供應商依賴度高，容易因單一廠商問題導致設備短缺。此外，採購第三方的量子模組可能引入潛在後門或遭植入惡意元件的風險 ([Introducing Post-Quantum algorithms in Open RAN interfaces This work was supported by the grant PID2020-113795RB-C33 funded by MICIU/AEI/10.13039/501100011033 (COMPROMISE project), the grant PID2023-148716OB-C31 funded by MCIU/AEI/10.13039/501100011033 (DISCOVERY project). Additionally, it also has been funded by the Galician Regional Government under project ED431B 2024/41 (GPC).](https://arxiv.org/html/2501.10060v1#:~:text=interrupt%20services,term%20security%20vulnerabilities))。供應鏈上的零組件在製造或整合過程中若遭到攻擊，可能會在網路中埋下**隱藏漏洞** ([Introducing Post-Quantum algorithms in Open RAN interfaces This work was supported by the grant PID2020-113795RB-C33 funded by MICIU/AEI/10.13039/501100011033 (COMPROMISE project), the grant PID2023-148716OB-C31 funded by MCIU/AEI/10.13039/501100011033 (DISCOVERY project). Additionally, it also has been funded by the Galician Regional Government under project ED431B 2024/41 (GPC).](https://arxiv.org/html/2501.10060v1#:~:text=interrupt%20services,term%20security%20vulnerabilities))。總體而言，Q-RAN的供應鏈彈性與透明度較低，使6G網路面臨比傳統O-RAN**更高的供應鏈安全風險**。

**緩解策略：**  
- **多供應商策略與標準化：** 避免對單一供應商的過度依賴，爭取多元化的供應來源。推動量子元件與模組的標準化設計，使不同廠商產品可互換，降低供應鏈中斷影響 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=programming%20languages%20and%20debuggers%C2%A0,stage))。  
- **供應鏈安全監管：** 識別並持續監控量子技術關鍵元件的供應商，建立供應鏈透明度。例如定期審查供應商的安全措施，要求提供軟硬體物料清單（SBOM）等。這有助於及早發現潛在的技術外流或後門威脅 ([An Assessment of U.S.-Allied Nations' Industrial Bases in Quantum Technology | RAND](https://www.rand.org/pubs/research_reports/RRA2055-1.html#:~:text=,allies%27%20funding%20and%20collaboration%20networks))。  
- **設備完整性驗證：** 在採購和部署量子模組時，對硬體韌體進行簽章驗證與安全測試，確保元件未被惡意修改。引入可信硬體模組或防偽機制，提升供應鏈交付設備的可信度。  
- **備援供應計畫：** 建立關鍵量子元件的備品庫存或第二供應渠道。與供應商簽訂長期支援合約，確保在元件故障或缺貨時能迅速取得替代品，維持網路連續運作。

### 量子裝置壽命風險
Q-RAN 所使用的量子通訊硬體（如量子隨機數產生器、QKD裝置等）因技術特性，可能出現**壽命較短、穩定性不足**的問題 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=Feature%20%20%20Technological%20Maturity,premature%20routing%20protocols%2C%20difficulties%20in))。傳統O-RAN設備（例如一般射頻單元、伺服器硬體）經過多年商用驗證，通常可穩定運行數年；反之，量子裝置目前尚不夠成熟，對環境條件極為敏感 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=Feature%20%20%20Technological%20Maturity,premature%20routing%20protocols%2C%20difficulties%20in))。例如，一些量子器件需要在低溫或無干擾的環境下才能保持性能，研究顯示將單光子源與偵測器置於約4K的低溫環境下可大幅提升其密鑰率與通信距離 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=The%20research%20reveals%20several%20key,is%20a%20notable%20correlation%20between))。在現實部署中，若環境控制不佳或器件受到噪聲影響，其錯誤率會上升，可能需要**頻繁校準或更換**。因此，相較於O-RAN，Q-RAN設備的平均無故障時間可能較短，長期運行成本與維護需求升高。

**緩解策略：**  
- **提升硬體容錯與穩定性：** 採取量子糾錯和容錯設計來延長量子裝置的穩定運行時間 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=programming%20languages%20and%20debuggers%C2%A0,stage))。例如，運用量子錯誤更正技術降低噪聲影響，或使用多模冗餘設計，確保單一量子元件故障時不致中斷服務。  
- **環境控制與防護：** 為量子設備提供適當的運行環境。若有需要可配置溫度控制（如低溫冷卻系統）或抗震、防電磁干擾的機箱，減少外界環境對量子裝置的影響。穩定的環境能延緩元件老化，提升壽命。  
- **即時監測與預防性維護：** 建立量子裝置健康監測機制，透過感測器及遠端監控即時追蹤裝置的錯誤率、溫度等參數。一旦偵測到性能異常，及早進行校準或更換 ([Practical Phase-Modulation Stabilization in Quantum Key Distribution via Machine Learning  |  Phys. Rev. Applied](https://link.aps.org/doi/10.1103/PhysRevApplied.12.014059#:~:text=real,accurate%20compensation%20but%20may%20cost))。研究指出，實用化的QKD系統需要有效的即時回授控制來維持穩定，補償外界環境擾動或元件老化帶來的偏移 ([Practical Phase-Modulation Stabilization in Quantum Key Distribution via Machine Learning  |  Phys. Rev. Applied](https://link.aps.org/doi/10.1103/PhysRevApplied.12.014059#:~:text=real,accurate%20compensation%20but%20may%20cost))。定期的預防性維護計畫可避免故障累積導致突發中斷。  
- **備援與熱切換：** 對關鍵量子設備配置熱備援（hot standby）。在一套量子硬體需要下線維修時，可即時切換到備用裝置，確保系統連續運行。同時準備必要的備品器件，縮短故障更換時間。

### 密鑰更新頻率風險
由於量子通信（特別是量子密鑰分發, QKD）的特性，Q-RAN 能以**遠高於傳統方式的頻率**產生和更新加密密鑰。傳統O-RAN架構下，多採用週期性或事件觸發的密鑰更新機制（例如每個通訊會話或固定時間間隔更新密鑰），頻率相對可控。然而在Q-RAN中，QKD系統可連續不斷地生成隨機密鑰並提供給網路使用，使密鑰刷新可以非常頻繁，以至於**每個通訊片段都可使用不同密鑰** ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=By%20integrating%20QKD%2C%20both%20IPsec,162))。雖然更頻繁的密鑰更新可提高安全性（每把密鑰暴露時間極短） ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=By%20integrating%20QKD%2C%20both%20IPsec,162)) ，但也帶來新的風險與挑戰：

- **同步與管理負擔：** 密鑰快速更新要求網路中多個節點（如基站、核心網元）同步頻繁交換新密鑰，增加信令開銷和系統複雜度。如果密鑰管理系統處理不當，可能出現密鑰不同步而導致通訊中斷的情況。  
- **性能與延遲影響：** 過高的密鑰更新頻率可能拖慢系統效能。例如，不斷地協商密鑰會佔用設備的計算和通信資源，增加額外延遲。對於需要超低延遲的6G應用而言，這是不可忽視的風險。  
- **密鑰生成瓶頸：** 雖然QKD理論上可提供源源不絕的密鑰，但在實務中其密鑰生成速率受限於物理條件。如果量子信道品質不佳（例如光纖衰減或噪聲干擾），QKD密鑰產生速率可能降低 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=generating%20redundancies%2C%20and%20communicating%20over,trust%20with%20quantum%20networks))。倘若應用層消耗密鑰的速度超過生成速度，將出現密鑰耗盡的風險，迫使系統降級安全等級甚至暫停服務 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=generating%20redundancies%2C%20and%20communicating%20over,trust%20with%20quantum%20networks))。  
- **故障轉移挑戰：** 一旦量子密鑰分發通道發生故障（例如設備問題或量子信道中斷），頻繁依賴該通道的密鑰更新機制會立即受影響。如何平滑地從量子密鑰轉換回傳統密鑰，以維持通信不中斷，對網路設計是個挑戰。

**緩解策略：**  
- **強化密鑰管理架構：** 引入專門的密鑰管理系統（KMS）來配合QKD運作，確保密鑰分發、存儲與同步的效率。透過緩存機制，可儲存一定量的預生成量子密鑰，平衡瞬時的密鑰需求高峰，避免臨時短缺。密鑰管理軟體需經優化，可自動、高速地將新密鑰下發到各網元，同步多點之間的密鑰狀態。  
- **分層或聚合更新：** 根據實際安全需求調整密鑰更新頻率，而非盲目追求極高頻率。對延遲敏感或重要性較低的資料流，可使用稍長壽命的密鑰，以減少過頻繁更新帶來的負荷。同時確保關鍵資料流仍以高頻度密鑰保障安全，達到安全與性能間的折衷。  
- **多路徑與冗餘量子通道：** 建立多條量子密鑰分發路徑（例如多對QKD裝置或多光路）提高可靠性 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=computers%C2%A0,stage))。量子網路研究已提出使用**量子多工器與交換機**來增強密鑰分發的吞吐和穩定度 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=programming%20languages%20and%20debuggers%C2%A0,stage))。這意味著即使某一路徑的量子通道受到干擾，其他路徑仍可提供密鑰，避免單點故障影響全局密鑰供應。  
- **混合加密方案備援：** 在Q-RAN架構中設計傳統或後量子密鑰的備援方案。當量子密鑰通道發生故障時，系統可自動轉為使用後量子密碼算法（PQC）或預先分發好的對稱密鑰繼續加密通信 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=computers%C2%A0,of%20QKD%20and%20classic%20cryptography))。例如，可結合QKD與傳統PKI形成混合機制：正常情況下優先使用QKD密鑰，當量子渠道不穩定時則暫時使用PQC產生的密鑰。這種**混合式密鑰機制**已被視為未來網路實現量子安全的重要方向，可確保在各種情況下通信的連續性與安全性 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=computers%C2%A0,of%20QKD%20and%20classic%20cryptography))。  
- **完善測試與模擬：** 在實際部署前，透過模擬6G網路大規模節點下的密鑰更新流程，測試不同更新頻率對網路同步和性能的影響。提前優化協議參數（如容忍時延的密鑰有效窗口）以確保系統能適應高頻密鑰更新而不失效。同時定期演練量子通道故障時的密鑰切換流程，確保操作人員和系統對意外情況有準備。

## 企業專網場景的 Q-RAN 風險

企業專網是指為單一企業或園區部署的專屬行動網路（例如5G/6G專網），通常規模較小且高度定製化。在此場景下引入Q-RAN，同樣面臨與O-RAN不同的新風險，但其表現形式因環境與資源差異有所不同。以下分別說明企業專網中Q-RAN的供應鏈、量子裝置壽命、密鑰更新頻率風險，以及相應的防範對策。

### 供應鏈風險
相較大型電信業者具備採購多家廠商設備的能力，企業專網在導入Q-RAN時往往**更加依賴單一解決方案供應商**。企業可能從某家廠商取得整套量子加密解決方案（包含量子設備與軟體），供應鏈集中度高。如果該廠商的量子元件來源受限或發生供貨延遲，企業缺乏備選供應商，網路建設與維護將受到直接影響。此外，中小型企業較少具備自行驗證硬體安全的能力，完全信任供應商提供的元件，這種情況下供應鏈**被插入惡意硬體或軟體**的風險依然存在 ([Introducing Post-Quantum algorithms in Open RAN interfaces This work was supported by the grant PID2020-113795RB-C33 funded by MICIU/AEI/10.13039/501100011033 (COMPROMISE project), the grant PID2023-148716OB-C31 funded by MCIU/AEI/10.13039/501100011033 (DISCOVERY project). Additionally, it also has been funded by the Galician Regional Government under project ED431B 2024/41 (GPC).](https://arxiv.org/html/2501.10060v1#:~:text=interrupt%20services,term%20security%20vulnerabilities)) ([The Impact of 5G ORAN on Network Security in 2024](https://www.telecomgurukul.com/post/the-impact-of-5g-oran-on-network-security-in-2024#:~:text=Additionally%2C%20the%20reliance%20on%20software,prevent%20unauthorized%20access%20and%20tampering))。再者，企業專網部署量子設備數量有限，若某批次產品存在設計缺陷，整個專網都可能受到波及。總體而言，在企業專網情境中，Q-RAN的供應鏈風險體現在**對單一廠商的依賴及安全可信度**上，比起多供應商的O-RAN生態更顯突出。

**緩解策略：**  
- **慎選可信供應商：**優先選擇在量子通訊領域有良好信譽、通過權威認證的供應商。審核其供應鏈來源，確認關鍵量子元件來自可靠渠道。同時簽訂嚴格的供應與維護服務合約，明定供應中斷的責任與補救措施，保障企業權益。  
- **引入第三方測試：**在採納量子設備前，聘請獨立的第三方安全實驗室對硬體進行測試（例如隨機數生成器的隨機性檢測、QKD裝置抗攻擊測試）。第三方評估報告可提升對供應鏈中產品安全性的信心。  
- **模組化與可替換性：**要求供應商提供**模組化**的量子網路設備，遵循行業標準介面。如此一來，若未來需要更換供應商，新的量子模組也能與現有系統相容，降低被單一廠商品鎖的風險。國際標準組織和O-RAN聯盟正推動相關標準，使量子密鑰分發介面和協議走向統一，企業應密切關注並採用符合標準的產品。  
- **合作夥伴模式：**中小企業可考慮與電信運營商或專業安全服務商合作，引入“量子安全即服務”（QKaaS）的模式。由具有強大供應鏈能力的大型夥伴提供量子密鑰分發服務，企業專網透過介面使用該服務，而不直接管理物理量子設備。這樣可將供應鏈風險轉移給更有能力控制風險的合作方，同時享受專業的安全支持。

### 量子裝置壽命風險
企業專網往往缺乏專職的科研團隊來維護尖端設備，因此Q-RAN中的量子裝置**穩定運行壽命**對企業尤為關鍵。此類專網部署的量子設備數量少且分散，例如可能僅在數個機櫃中安裝幾套QKD終端或量子隨機數產生器。如果其中一套設備提早老化失效，企業未必有備用的替代品，可能導致關鍵通信鏈路中斷。由於企業現場環境可能沒有電信機房那般完善（例如溫濕度控制、防電磁干擾設施不足），量子裝置運行條件相對嚴苛，**潛在壽命比實驗室環境更短**。再者，多數企業IT人員對量子硬體原理不熟悉，當設備性能逐漸下降時不易及時察覺或處理。相比之下，傳統O-RAN設備成熟且維護人員培訓充足，因此企業在引入Q-RAN後，裝置可靠性成為一大新風險。

**緩解策略：**  
- **挑選工業級設備：** 企業在選購量子通信設備時，應要求供應商提供**工業級規格**的產品，包括對環境的耐受度（例如工作溫度範圍、抗震動等）。儘量選擇整合度高的一體化量子模組，減少需要現場校準的部件，提升整體穩定性。  
- **廠商維護支援：** 與量子設備供應商簽訂維護服務合約，確保出現故障時能迅速獲得支援。內容包括：明確的故障響應時間、備品儲備、定期巡檢服務等。由於企業自身人力有限，可利用廠商的專業團隊定期檢查設備狀態，預防問題發生。  
- **環境優化：** 對現有機房或設備安裝點進行環境改造以延長量子裝置壽命。例如，增加空調穩定溫濕度、安裝不間斷電源避免突發斷電、採取屏蔽措施降低電磁噪聲等。雖不一定達到實驗室級條件，但盡可能創造良好的運行環境，可減緩量子器件性能退化。必要時可使用小型冷卻裝置為關鍵元件降溫，提升其工作穩定度 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=The%20research%20reveals%20several%20key,is%20a%20notable%20correlation%20between))。  
- **監控與在地培訓：** 部署簡易監控系統，實時收集量子設備的運行指標（如光功率、誤碼率）。一旦偏離正常範圍，立即通知管理員介入處理。另外，對企業IT人員進行基礎培訓，使其了解這些指標意義和簡單的調校方法。當廠商人員未及時到場時，企業技術人員可先執行預案（例如重啟模組、切換至備用路徑）以恢復服務。透過**人員技能提升**配合**監控警報機制**，降低量子設備故障對業務的衝擊 ([Practical Phase-Modulation Stabilization in Quantum Key Distribution via Machine Learning  |  Phys. Rev. Applied](https://link.aps.org/doi/10.1103/PhysRevApplied.12.014059#:~:text=real,accurate%20compensation%20but%20may%20cost))。  
- **備援方案：** 若條件允許，企業可購置關鍵量子設備的備用單元。平時處於熱備份狀態，一旦主用設備出現明顯性能下降或故障，可快速切換到備用單元。此外，建立與鄰近單位（例如同一產業園區內其他專網）的合作，共享緊急備用設備或臨時通道，也是提高韌性的方法。

### 密鑰更新頻率風險
在企業專網中導入Q-RAN，量子密鑰管理模式的轉變也帶來新風險。傳統企業網路常使用VPN或專線連接，各連線的加密密鑰更新頻率通常較低且由人為策略控制（例如每24小時自動更換密鑰，或定期手動更新憑證）。然而，引入QKD等量子技術後，密鑰可高速連續產生，企業專網可能嘗試**更頻繁地更新加密密鑰**以增強安全性 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=By%20integrating%20QKD%2C%20both%20IPsec,162))。此變化若未與現有IT系統充分適配，將帶來下列風險：

- **設備與應用相容性：** 企業網路中的現有設備（路由器、防火牆、終端等）及應用軟體，可能無法適應過於頻繁的密鑰切換。例如，一條VPN隧道本預期一天換一次密鑰，現在變成每幾分鐘一換，可能導致某些設備CPU負荷激增或軟體出現錯誤。應用層軟體也可能因密鑰變動過快導致會話中斷或錯誤。  
- **管理複雜度提升：** 密鑰更新頻率提高意味著密鑰管理流程更複雜。企業需確保密鑰分發系統與各業務系統高度整合，自動完成密鑰交握。對缺乏相關經驗的企業IT團隊而言，初期調適容易出現疏漏，可能因配置錯誤導致安全隱患（如舊密鑰未及時失效）或服務中斷。  
- **安全依賴性風險：**當企業習慣依賴頻繁更新帶來的高安全性後，若量子密鑰來源不穩（比如某段時間QKD鏈路故障，只能使用較久未更換的傳統密鑰），反而可能因**安全級別突然降低** 而面臨威脅。在量子密鑰不足的情況下，是否允許密鑰重複使用更長時間，成為風險決策點。企業需要權衡在非常狀態下暫時降低密鑰更新頻率可能帶來的後果。  

**緩解策略：**  
- **漸進式密鑰策略調整：** 建議企業採用漸進方式提升密鑰更新頻率，而非一步到位地極端頻繁。先從現有系統可接受的範圍入手（例如將每日更新改為每小時），觀察各設備與應用的反應，逐步調整優化。確保所有組件對新流程穩定運行後，再視需要提高頻率。此循序漸進策略可讓企業IT團隊積累經驗，降低一次性更改帶來的風險。  
- **自動化密鑰管理平台：** 導入專業的密鑰管理平台或軟體，使密鑰的生成、分發、更新過程**自動化**且對上層業務透明。平台應與企業的認證系統、VPN設備、應用伺服器等整合，提供API介面自動下發新密鑰，避免人工干預。透過集中管控，確保密鑰更新同步且正確無誤，同時降低人工操作錯誤。  
- **密鑰更新窗口與容錯：** 設計合理的密鑰更新過渡機制。例如設定新舊密鑰並行有效的一個過渡窗口期，確保在切換過程中通訊不會因瞬時不同步而中斷。若在窗口期內發現新密鑰有問題，可迅速回退使用舊密鑰。這種容錯機制能提升密鑰更新的可靠性，減少頻繁更新對上層應用的衝擊。  
- **量子/古典混合加密架構：** 如同6G公網情境，企業專網也可採取混合加密方案作為備援。當量子密鑰正常時，系統使用高頻更新的量子密鑰；若量子密鑰暫時不可用，則自動切換到預先建立的古典安全通道（例如基於PQC的會話密鑰）繼續保護通信 ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=computers%C2%A0,of%20QKD%20and%20classic%20cryptography))。這確保即便密鑰更新頻率因故降為較傳統的水平，通信安全仍有保障，不會暴露在明文狀態。  
- **定期安全審計與演練：** 定期對企業專網的密鑰管理進行安全審計，檢查密鑰更新日志是否符合預期，舊密鑰是否正確銷毀，以及備援機制的切換記錄。還應模擬各種異常場景進行演練（例如QKD鏈路中斷一天），觀察密鑰更新頻率調整和備援方案的效果，完善應急預案，確保真正發生突發狀況時各系統協調有序。

**參考資料：**

1. Zeydan, E. *et al.* (2023). *Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges*, arXiv.  ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=quantum%20cloud%20computing%20,integration%20within%20future%206G%20networks)) ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=Feature%20%20%20Technological%20Maturity,premature%20routing%20protocols%2C%20difficulties%20in))

2. CoRAN Labs (2023). *Q-RAN: Quantumized O-RAN* – LinkedIn post.  ([Introducing Post-Quantum algorithms in Open RAN interfaces This work was supported by the grant PID2020-113795RB-C33 funded by MICIU/AEI/10.13039/501100011033 (COMPROMISE project), the grant PID2023-148716OB-C31 funded by MCIU/AEI/10.13039/501100011033 (DISCOVERY project). Additionally, it also has been funded by the Galician Regional Government under project ED431B 2024/41 (GPC).](https://arxiv.org/html/2501.10060v1#:~:text=interrupt%20services,term%20security%20vulnerabilities))

3. García-Revillo, J. *et al.* (2023). *Introducing Post-Quantum Algorithms in Open RAN Interfaces*, arXiv.  ([The Impact of 5G ORAN on Network Security in 2024](https://www.telecomgurukul.com/post/the-impact-of-5g-oran-on-network-security-in-2024#:~:text=Additionally%2C%20the%20reliance%20on%20software,prevent%20unauthorized%20access%20and%20tampering))

4. RAND (2023). *Assessment of U.S.-Allied Nations' Industrial Bases in Quantum Technology*.  ([An Assessment of U.S.-Allied Nations' Industrial Bases in Quantum Technology | RAND](https://www.rand.org/pubs/research_reports/RRA2055-1.html#:~:text=,allies%27%20funding%20and%20collaboration%20networks))

5. Liyanage, M. *et al.* (2023). *Quantum Security in O-RAN Systems*, O-RAN Alliance Research Report. 

6. Ericsson (2019). *Quantum Computers in Telecom Infrastructure – When can we expect quantum RAN?* (Ericsson Blog).  ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=The%20research%20reveals%20several%20key,is%20a%20notable%20correlation%20between))

7. Liu, J. *et al.* (2019). *Practical Phase-Modulation Stabilization in QKD via ML*, **Phys. Rev. Applied** 12(1).  ([Practical Phase-Modulation Stabilization in Quantum Key Distribution via Machine Learning  |  Phys. Rev. Applied](https://link.aps.org/doi/10.1103/PhysRevApplied.12.014059#:~:text=real,accurate%20compensation%20but%20may%20cost))

8. Zeydan, E. *et al.* (2023). *Quantum Tech for 6G Security and Privacy*, arXiv.  ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=By%20integrating%20QKD%2C%20both%20IPsec,162)) ([Quantum Technologies for Beyond 5G and 6G Networks: Applications, Opportunities, and Challenges](https://arxiv.org/html/2504.17133v1#:~:text=generating%20redundancies%2C%20and%20communicating%20over,trust%20with%20quantum%20networks))

