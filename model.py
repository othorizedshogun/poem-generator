"""Inference"""

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftConfig, PeftModel

ADAPTER_PATH = "./model/"

config = PeftConfig.from_pretrained(ADAPTER_PATH)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)

# Loading the LoRA model i.e base model along with the adapter
inference_model = PeftModel.from_pretrained(model, ADAPTER_PATH)

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

    def create_poem(self, inputs):
        """
        Wrapper to generate poems with the model.
        """
        inputs = self.tokenize(inputs, "encode")
        outputs = self.model.generate(
            **inputs,
            max_length=200,
            num_beams=10,
            no_repeat_ngram_size=2,
            length_penalty=0.8,
            early_stopping=True,
            temperature=0.61
        )
        return self.tokenize(outputs, "decode")

poem_gen_model = Inference(tokenizer, model)