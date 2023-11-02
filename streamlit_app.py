"""Main Page for streamlit app"""

# from model import poem_gen_model

def app():
    import streamlit as st

    st.set_page_config(page_title="versiforg")

    st.write("""
        # versiforge
        Randomly generate poems inputting just the form and/or topic.
    """)

    st.write("*__Craft yours!__*" )

    form = st.text_input(
        "Form",
        value="", max_chars=15, key=None, type="default",
        help=None, autocomplete=None, on_change=None, args=None,
        kwargs=None, placeholder="Structure you wish for the poem to be in e.g haiku, ballad...", disabled=False, label_visibility="visible"
    )

    topic = st.text_input(
        "Topic",
        value="", max_chars=15, key=None, type="default",
        help=None, autocomplete=None, on_change=None, args=None,
        kwargs=None, placeholder="Desired topic here. e.g love, god, racism...",
        disabled=False, label_visibility="visible"
    )

    if st.button("Submit"):
        if form=="":
            input = """Input [Topic: {topic}]
            Poem:
            """.format(topic=topic)
        elif topic=="":
            input = """Input [Form: {form}]
            Poem:
            """.format(form=form)
        else:
            input = """Input [Form: {form}, Topic: {topic}]
            Poem:
            """.format(form=form, topic=topic)
            
        with st.spinner(text="In progress"):
            poem = poem_gen_model.create_poem(input)
            st.markdown(poem)

app()
