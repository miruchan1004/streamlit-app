import streamlit as st


st.title("Streamlit TODO App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task_text = st.text_input("タスクを入力してください", key="task_input")

if st.button("追加"):
    new_task = task_text.strip()
    if new_task:
        st.session_state.tasks.append({"text": new_task})
        st.session_state.task_input = ""
        st.rerun()
    else:
        st.warning("タスクを入力してから追加してください。")

st.subheader("タスクリスト")

if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{index}. {task['text']}")
else:
    st.info("まだタスクはありません。")
