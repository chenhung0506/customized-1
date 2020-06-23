initial python3 enviroment
pip install -r requirements.txt

# Voice Service deploy

部屬所有語音相關服務

## git struct 
```
.
├── CHANGELOG.md
├── README.md
├── conf
├── env
│   └── default
│       └── dev.env
├── modules
│   ├── ASR_Worker_Emotibot
│   │   └── docker-compose.yaml
│   ├── Gender_Worker_Emotibot
│   │   └── docker-compose.yaml
│   ├── Infra
│   │   ├── docker-compose-ssl.yaml
│   │   ├── docker-compose.yaml
│   │   └── minio_192.168.3.26.crt
│   ├── SER_Worker_Emotibot
│   │   └── docker-compose.yaml
│   ├── UniMRCP_Emotibot
│   │   └── docker-compose.yaml
│   ├── Voice_Master_Emotibot
│   │   ├── docker-compose.yaml
│   │   └── worker_config.yaml
│   └── port.yaml
└── scripts
    ├── deploy.sh
    ├── function.sh
    └── test.sh
```

## 部屬流程

1. 複製或者建立新環境的設定檔。(放置在 env 資料夾下)
2. 根據各模塊需求修改 dev.env (詳細請參考底下”模塊“內說明)
3. 修改 ./scripts/deploy.sh 中 ENABLE_MODULE_ARRARY 選擇需要部署的模塊
3. 執行

```bash
> ./scripts/deploy.sh deploy
> 輸入你所新增的環境資料夾名稱
```

## 網路

- 部署預設使用 docker network bridge: asr\_service\_network ，如果沒有的話部署腳本會自己建立。
- 可以透過在 dev.env 中配置，EXTERNA\_NETWORK\_NAME 接入現有的 docker 網路。
- voice\_master\_emotibot 連接到個語音服務模塊預設是透過 service name ，所以必須要在同一個 docker network 中。目前僅支持單機部署。

## 模塊

### Voice\_Master\_Emotibot

語音相關服務主要接口，任務分配與語音資源管理
	
### ASR\_Worker\_Emotibot

語音識別服務的主要處理模塊

- 部屬時模型會從 MINio 上抓取，如果是私有部署沒有部署 MINio 的情況下要先將模型的 .tar.gz 檔案放到 ~/voice/asr_models/ 下。
- 部署模型請向語音組 @Karol 確認版本

### SER\_Worker\_Emotibot

語音情緒辨識服務的主要處理模塊

### Gender\_Worker\_Emotibot

語音性別辨識服務的主要處理模塊

### UniMRCP\_Emotibot

提供語音識別的 MRCP 接口的模塊，主要是給 FreeSWITCH\_Emotibot 使用

- network\_mode: 預設是 host 而不是 bridge，要注意

### Infra

配置 MINio 的相關設定

- Voice\_Master\_Emotion: 錄音檔存放
- ASR\_Worker\_Emotibot: 模型配置

## 測試
```bash
docker exec -it voice_master_emotibot /test.sh (optional: service)
``` 
optional:
- recognize: 測試語音識別
- gender: 測試語音性別
- emotion: 測試語音情緒

比如要測試語音識別和語音性別

```bash
docker exec -it voice_master_emotibot /test.sh recognize gender
```
- 只能測試本機的部署
