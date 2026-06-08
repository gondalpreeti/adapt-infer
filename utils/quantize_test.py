# utils/quantize_test.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

print("Downloading DistilGPT-2 baseline...")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model_fp32 = AutoModelForCausalLM.from_pretrained("distilgpt2")

print(r"FP32 Model successfully loaded into memory!")
# Next up: Implement .half() and torch.quantization.quantize_dynamic here!