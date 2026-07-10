# Streamlit TODO App

Issue #2 の要件に沿って、`st.session_state` を使ったタスク追加と一覧表示を行う構成です。

## セットアップ手順

### 1. 仮想環境の作成

```powershell
python -m venv venv
```

### 2. 仮想環境の有効化（Windows）

```powershell
venv\Scripts\activate
```

### 3. 依存ライブラリのインストール

```powershell
pip install -r requirements.txt
```

## 起動方法

```powershell
streamlit run app.py
```

## 画面の内容

- タイトル（`st.title`）
- タスク入力欄（`st.text_input` + `key`）
- 追加ボタン（`st.button`）
- `st.session_state` で保持するタスクリスト表示
