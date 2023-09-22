import streamlit as st
import functions

to_dos = functions.get_todo()

st.title("My to Do App")
st.subheader("This is my Todo App")
st.write("This App increases productivity")


def add_todo():
    todo_n = st.session_state["new_todo"]
    to_dos.append(todo_n.capitalize() + '\n')
    functions.write_todo(to_dos)



for index , todo in enumerate(to_dos):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox:
        to_dos.pop(index)
        functions.write_todo(to_dos)
        del st.session_state[todo]
        st.rerun()




st.text_input(label=" ", placeholder="Add a new to do..",
              on_change=add_todo, key='new_todo')

st.session_state