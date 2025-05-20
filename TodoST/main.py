import streamlit as st

nav = st.sidebar.radio("Navigation Menu", ["Om Mig","Todo"])

if nav == "Om Mig":
    st.title("Om Mig")

    st.subheader("Vem är Hugo")
    st.text("Hej! \n" +
            "\nLorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
            "\nwhen an unknown printer took a galley of type and scrambled it to make a type "
            "\nspecimen book. It has survived not only five centuries, but also the leap into"
            "\nelectronic typesetting, remaining essentially unchanged. It was popularised "
            "\nin the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,"
            "\nand more recently with desktop publishing software like Aldus PageMaker "
            "\nincluding versions of Lorem Ipsum.")

    st.subheader("Vad gör jag?")
    st.text("Hej! \n" +
            "\nLorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
            "\nwhen an unknown printer took a galley of type and scrambled it to make a type "
            "\nspecimen book. It has survived not only five centuries, but also the leap into"
            "\nelectronic typesetting, remaining essentially unchanged. It was popularised "
            "\nin the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,"
            "\nand more recently with desktop publishing software like Aldus PageMaker "
            "\nincluding versions of Lorem Ipsum.")

if nav == "Todo":
    # Initialize session state for todos
    if 'todos' not in st.session_state:
        st.session_state.todos = []

    st.title("Huggo todo")

    # Add todo
    st.subheader("Add a new todo")
    new_todo = st.text_input("Enter todo", key="new_todo_input")

    if st.button("Add todo"):
        if new_todo:
            st.session_state.todos.append(new_todo)
            st.success(f"Todo added: {new_todo}")
        else:
            st.warning("Please enter a todo.")

    # Show current todos
    st.subheader("Current todos")
    if st.session_state.todos:
        for i, todo in enumerate(st.session_state.todos):
            st.write(f"{i+1}. {todo}")
    else:
        st.write("No todos yet.")

    # Delete todo
    st.subheader("Delete a todo")
    if st.session_state.todos:
        todo_to_delete = st.selectbox("Select a todo to delete", st.session_state.todos)

        if st.button("Delete selected todo"):
            st.session_state.todos.remove(todo_to_delete)
            st.success(f"{todo_to_delete} was deleted.")
    else:
        st.info("Nothing to delete.")


