import streamlit as st


st.title("Streamlit TODO App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task_text = st.text_input("タスクを入力してください", key="task_input")

if st.button("追加"):
    new_task = task_text.strip()
    if new_task:
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.session_state.task_input = ""
        st.rerun()
    else:
        st.warning("タスクを入力してから追加してください。")

st.subheader("タスクリスト")

if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        col_check, col_delete = st.columns([6, 1])
        is_done = task.get("done", False)

        with col_check:
            checked = st.checkbox(
                task["text"],
                value=is_done,
                key=f"check_{index}",
            )
            if checked != is_done:
                st.session_state.tasks[index]["done"] = checked
                st.rerun()

        with col_delete:
            if st.button("削除", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()
else:
    st.info("まだタスクはありません。")
