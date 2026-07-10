import json
from pathlib import Path

import streamlit as st


TODOS_FILE = Path(__file__).with_name("todos.json")


def load_tasks() -> list[dict[str, object]]:
    if not TODOS_FILE.exists():
        return []

    try:
        with TODOS_FILE.open("r", encoding="utf-8") as file:
            raw_tasks = json.load(file)
    except json.JSONDecodeError:
        st.warning("todos.json の形式が不正なため、空のタスクリストで開始します。")
        return []

    if not isinstance(raw_tasks, list):
        st.warning("todos.json の形式が不正なため、空のタスクリストで開始します。")
        return []

    valid_tasks: list[dict[str, object]] = []
    has_invalid_task = False

    for task in raw_tasks:
        if (
            isinstance(task, dict)
            and isinstance(task.get("text"), str)
            and isinstance(task.get("done"), bool)
        ):
            valid_tasks.append({"text": task["text"], "done": task["done"]})
        else:
            has_invalid_task = True

    if has_invalid_task:
        st.warning("todos.json に不正なデータが含まれているため、一部を除外しました。")

    return valid_tasks


def save_tasks(tasks: list[dict[str, object]]) -> None:
    with TODOS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


st.title("Streamlit TODO App")

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

task_text = st.text_input("タスクを入力してください", key="task_input")

if st.button("追加"):
    new_task = task_text.strip()
    if new_task:
        st.session_state.tasks.append({"text": new_task, "done": False})
        save_tasks(st.session_state.tasks)
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
                save_tasks(st.session_state.tasks)
                st.rerun()

        with col_delete:
            if st.button("削除", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                save_tasks(st.session_state.tasks)
                st.rerun()
else:
    st.info("まだタスクはありません。")
