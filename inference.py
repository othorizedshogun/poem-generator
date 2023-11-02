"""Inference"""
import streamlit as st

# def create_poem(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt")
#     outputs = model.generate(
#         **inputs,
#         max_length=200,
#         num_beams=10,
#         no_repeat_ngram_size=2,
#         length_penalty=0.8,
#         early_stopping=True,
#         temperature=0.61
#     )
#     print(tokenizer.decode(outputs[0], skip_special_tokens=True))


class Inference:
    "Inference class"
    def __init__(self, gen_model_tokenizer, gen_model):
        self.tokenizer = gen_model_tokenizer
        self.model = gen_model   
    def tokenize(self, inputs, action):
        """
        Wrapper to tokenize inputs and outputs from the model.
        """
        if action == "encode":
            tok_data = self.tokenizer(inputs, return_tensors="pt")
        elif action == "decode":
            tok_data = self.tokenizer.decode(inputs[0], skip_special_tokens=True)
        else:
            return None
        return tok_data
    @st.cache_data
    def create_poem(_self, inputs):
        """
        Wrapper to generate poems with the model.
        """
        inputs = _self.tokenize(inputs, "encode")
        outputs = _self.model.generate(
            **inputs,
            max_length=200,
            num_beams=10,
            no_repeat_ngram_size=2,
            length_penalty=0.8,
            early_stopping=True,
            temperature=0.61
        )
        return _self.tokenize(outputs, "decode")
