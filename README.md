# cURL 下載器 (PDF 版本)
> 適用於部分無法右鍵另存 PDF 的檔案

這工具可以讓你直接使用 cURL 命令列下載指定資源的工具

目前提供下載方式：

可以自己選一種喜好的方式進行
- 直接命令列 cURL 下載的方法
- 執行 download.py 下載
- 自己部署 flask 後在自己本地網頁下載
- 或者點擊我部署好的網頁 [點我](https://curl-download.koyeb.app/)

# 快速開始

## 如何取得 cURL (重要)
> GoogleChomre 版本：139.0.7258.139 (正式版本) 通過測試

步驟如下：
1. 開啟「開發人員工具」
2. 點選「網路」頁籤
3. 以「.pdf」作為過濾關鍵字
4. 等待目標頁面下載完成後於下方出現pdf檔案
5. 對該檔案右鍵複製出 cURL （會獲得一串 curl 'https://... 的URL）

<details>
<summary>點我打開圖片支援</summary>
<img width="770" height="650" alt="sample" src="https://github.com/user-attachments/assets/681d0a86-4797-4d2b-8f77-a1262e6aa479" />
</details>


## 直接命令列 cURL 下載的方法

在步驟五獲得的 curl 命令列後面加上 -o <檔案名.pdf> 即可進行下載

請在命令提示字元執行：
```
curl 'https://... -o <your_pdf_filename.pfd>
```

## 執行 download.py 下載
需要自行把 curl 覆蓋到 curl_command.txt，download.py 會讀取該文件

覆蓋完成後直接執行即可！會自動解析 PDF 檔名

請在命令提示字元執行：

```
python3 download.py
``` 

## 自己部署 flask 後在自己本地網頁下載

基於 Flask 的網頁服務，可以在網頁上貼上 cURL 指令，伺服器會幫你下載檔案並提供下載連結。

可以自選 Docker 部署，並自動定期清理 `/tmp` 暫存檔案。


### 1. 本地執行

```bash
pip install flask
python app.py
```

預設服務會在 [http://localhost:5001](http://localhost:5001) 提供網頁介面。

---

### 2. Docker 執行

#### 建立映像檔

```bash
docker build -t flask-curl-downloader .
```

#### 啟動容器

```bash
docker run -p 5001:5001 flask-curl-downloader
```

---

## 檔案自動清理

- 服務會每 24 小時自動清空 `/tmp` 目錄，避免磁碟空間爆滿。
- 清理邏輯寫在 `run.sh`，可依需求調整。

---

## 目錄結構

```
.
├── app.py         # Flask 主程式
├── run.sh         # 啟動腳本，包含自動清理
├── Dockerfile     # Docker 建置檔
└── ...
```

---

## 注意事項

- 下載的檔案會暫存於伺服器 `/tmp` 目錄，非直接下載到用戶端。


## 不仿可以試試看Koyeb部署（非工商）

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=flask-curl-downloader-python&type=git&repository=Xhinmin%2Fflask-curl-downloader-python&branch=main&builder=dockerfile&instance_type=free&regions=was&instances_min=0&autoscaling_sleep_idle_delay=300&ports=5001%3Bhttp%3B%2F&hc_protocol%5B5001%5D=tcp&hc_grace_period%5B5001%5D=5&hc_interval%5B5001%5D=30&hc_restart_limit%5B5001%5D=3&hc_timeout%5B5001%5D=5&hc_path%5B5001%5D=%2F&hc_method%5B5001%5D=get)
---
