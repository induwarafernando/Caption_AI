from transformers import Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer, DataCollatorForLanguageModeling
from datasets import load_from_disk
import torch

# Load the processed dataset
dataset = load_from_disk("processed_dataset")

# Remove unnecessary columns
dataset = dataset.remove_columns(["text", "label"])  # Ensure correct format

# Load GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Ensure padding token is set correctly
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

# Define Data Collator (for batch padding)
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,  # Not using masked language modeling
)

# Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,  # Ensure batch sizes match
    per_device_eval_batch_size=8,
    num_train_epochs=3,  # Adjust if needed
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=100,
    save_total_limit=2,
    fp16=torch.cuda.is_available(),  # Enable FP16 if GPU is available
    push_to_hub=False,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=dataset,
    tokenizer=tokenizer,  # Pass tokenizer explicitly
    data_collator=data_collator,
)

# Train the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")
print("✅ Model fine-tuned and saved!")
