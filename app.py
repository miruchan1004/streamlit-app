import streamlit as st


st.title("Streamlit TODO App")

task_text = st.text_input("タスクを入力してください")

if st.button("追加"):
    if task_text.strip():
        st.success(f"タスクを受け付けました: {task_text}")
    else:
        st.warning("タスクを入力してから追加してください。")
