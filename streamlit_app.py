"""Main Page for streamlit app"""
import streamlit as st

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftConfig, PeftModel

from inference import Inference

ADAPTER_PATH = "./model/"


def app():

    st.set_page_config(page_title="versiforge")

    # loading objects: config, tokenizer, model
    @st.cache_resource
    def load_config():
        return PeftConfig.from_pretrained(ADAPTER_PATH)
    @st.cache_resource
    def load_tokenizer():
        return AutoTokenizer.from_pretrained(config.base_model_name_or_path)
    @st.cache_resource
    def load_model():
        return AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)
    config = load_config()
    tokenizer = load_tokenizer()
    model = load_model()
    ## Loading the LoRA model i.e base model along with the adapter
    inference_model = PeftModel.from_pretrained(model, ADAPTER_PATH)
    poem_gen_model = Inference(tokenizer, inference_model)

    st.write("""
        # versiforge
        Randomly generate poems inputting just the form and/or topic.
    """)

    st.write("*__Craft yours!__*" )

    form = st.text_input(
        "Form",
        value="", max_chars=15, key=None, type="default",
        help=None, autocomplete=None, on_change=None, args=None,
        kwargs=None, placeholder="Structure you wish for the poem to be in e.g haiku, ballad...",
        disabled=False, label_visibility="visible"
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
            inputs = f"Input [Topic: {topic}]\nPoem:\n"
        elif topic=="":
            inputs = f"Input [Form: {form}]\nPoem:\n"
        else:
            inputs = f"Input [Form: {form}, Topic: {topic}]\nPoem:\n"     
        with st.spinner(text="In progress"):
            poem = poem_gen_model.create_poem(inputs)
            print(poem[len(inputs):])
            st.text(poem[len(inputs):])
app()
