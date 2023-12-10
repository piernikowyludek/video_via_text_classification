from transformers import LlamaTokenizerFast, LlamaForCausalLM
import torch

# explore transformers pipeline
# make a nice config file - like LlamaConfig

def generate_text(prompt, model_name="EleutherAI/llama2", max_length=50):
    # different model "meta-llama/Llama-2-13b-chat-hf"
    # Load tokenizer and model
    tokenizer = LlamaTokenizerFast.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(model_name)

    # Encode the prompt
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    # Generate text
    output = model.generate(input_ids, max_length=max_length)

    # Decode and print the output text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Example usage
prompt = "Once upon a time"
print(generate_text(prompt))