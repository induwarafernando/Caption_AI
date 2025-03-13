from transformers import GPT2Tokenizer
from datasets import load_dataset

# Load the dataset (replace with your dataset if needed)
dataset = load_dataset("prakhars/instagram_captions", split="train")

# Load GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Ensure that the tokenizer has a pad token
tokenizer.pad_token = tokenizer.eos_token

# Tokenization function
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=50)

# Apply tokenization
dataset = dataset.map(tokenize_function, batched=True)

# Save processed dataset
dataset.save_to_disk("processed_dataset")

print("✅ Dataset tokenized and saved!")
