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
- タスクごとの完了チェック（`st.checkbox`）
- タスクごとの削除ボタン（`st.button`）
- `st.session_state` で保持するタスクリストの状態更新

## データ永続化

- アプリ起動時に、`app.py` と同じ階層の `todos.json` が存在すれば読み込みます。
- タスクの追加・完了切り替え・削除を行うたびに、最新のタスクリストを `todos.json` に保存します。
- これにより、ブラウザ再読み込みやサーバー再起動後もタスクが保持されます。
