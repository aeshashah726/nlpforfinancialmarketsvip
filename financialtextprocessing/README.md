# Assignment 1 — Flan-T5 + Financial PhraseBank

**Model (used for demo):** [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small)  
- **License:** Apache-2.0  
- **Intended use:** General-purpose text-to-text tasks (e.g., classification, summarization, Q&A).  
- **Why chosen:** Very small model that can run on CPU locally.  
- **Declared models for assignment:**  
  - Primary: `mistralai/Mistral-7B-Instruct-v0.2`  
  - Backup: `meta-llama/Meta-Llama-3-8B-Instruct`

**Dataset:** [`financial_phrasebank`](https://huggingface.co/datasets/financial_phrasebank) (`sentences_allagree`)  
- Contains financial news sentences with gold labels: Negative, Neutral, Positive.  
- License: CC BY-SA 3.0  

**Task:** Sentiment classification (Positive / Neutral / Negative) of financial news sentences.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Hugging Face login

If downloads fail, log in once:

```bash
pip install huggingface_hub
huggingface-cli login
```

Create a token here: https://huggingface.co/settings/tokens (read-only).

## Run

Run on 1 sample (default):

```bash
python main.py
```

Run on multiple samples, e.g. 5:

```bash
python main.py --n 5
```

## Prompting Strategy

- **System Prompt:**

```
You are a financial NLP assistant. 
Your task is to classify the sentiment of financial news sentences. 
Always choose exactly one label: Positive, Negative, or Neutral. 
Respond with only the label, followed by a short explanation on a new line starting with 'Why:'.
```

- **User Prompt Example:**

```
Sentence: Orion Corp reported a fall in its third-quarter earnings due to higher R&D costs and increased marketing expenses.
What is the sentiment of this sentence?
```

The code concatenates these into the model input to guide responses.

