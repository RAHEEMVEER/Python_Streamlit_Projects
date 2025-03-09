import streamlit as st

if "todo" not in st.session_state:
    st.session_state.todo = []

st.title("To-Do List App")
user_input = st.text_input("Enter your task:")

if st.button("Add Task"):
    st.session_state.todo.append(user_input)

for i, task in enumerate(st.session_state.todo):
    st.write(f"**{i + 1}. {task}**")

if st.session_state.todo:
    delete_index = st.selectbox("Delete Task", range(1, len(st.session_state.todo) + 1))
    if st.button("Delete Task"):
        del st.session_state.todo[delete_index - 1]
        st.rerun() 