from datasets import load_dataset

# Load dataset from Hugging Face
dataset = load_dataset("prakhars/instagram_captions", split="train")

# Print a sample caption
print("Sample Caption:", dataset[0]["text"])
