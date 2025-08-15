### 以下為 MAC OS 的虛擬環境建立

#### 建立虛擬環境

```
python3 -m venv myenv
```
#### 啟動虛擬環境
```
source myenv/bin/activate 
```
#### 關閉虛擬環境
```
deactivate
```
#### FastAPI docs
```
http://localhost:{port}/docs 
```

#### 使用 docker 的 postgres 建立資料庫

```
docker run --name fastapi_postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:15.1 
```