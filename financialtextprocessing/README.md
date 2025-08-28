# Assignment 1 — Flan-T5 + Financial PhraseBank

## Overview
- **Dataset:** [`financial_phrasebank`](https://huggingface.co/datasets/financial_phrasebank) (`sentences_allagree`)  
- **Model (used for demo):** [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small)  
  - **License:** Apache-2.0  
  - **Intended use:** General-purpose text-to-text tasks (classification, summarization, Q&A).  
- **Declared models for assignment:**  
  - Primary: `mistralai/Mistral-7B-Instruct-v0.2`  
  - Backup: `meta-llama/Meta-Llama-3-8B-Instruct`

**Task:** Sentiment classification (Positive / Neutral / Negative) of financial news sentences.

---

## Setup

Clone the repo and install requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Hugging Face Token (Required)

You need a Hugging Face account to download datasets/models.  

1. Create a token at: https://huggingface.co/settings/tokens (choose *Read* access).  
2. Log in once via CLI:

```bash
pip install huggingface_hub
huggingface-cli login
```

3. Alternatively, set your token as an **environment variable** in your shell:

```bash
export HUGGINGFACE_TOKEN=hf_xxxxxxxx
```

or in **Python code** (not recommended for sharing):

```python
from huggingface_hub import login
login("hf_xxxxxxxx")
```

---

## Run

Run on 1 random sample (default):

```bash
python main.py
```

Run on multiple samples, e.g. 5:

```bash
python main.py --n 5
```

---

## Prompting Strategy

**System Prompt**
```
You are a financial NLP assistant. 
Your task is to classify the sentiment of financial news sentences. 
Always choose exactly one label: Positive, Negative, or Neutral. 
Respond with only the label, followed by a short explanation on a new line starting with 'Why:'.
```

**User Prompt Example**
```
Sentence: Orion Corp reported a fall in its third-quarter earnings due to higher R&D costs and increased marketing expenses.
What is the sentiment of this sentence?
```

---

## Expected Output

When you run `python main.py --n 2`, you’ll see something like:

```
==== Report ====
Model: google/flan-t5-small
Dataset: financial_phrasebank/sentences_allagree

Sample 1
Input: Orion Corp reported a fall in its third-quarter earnings due to higher R&D costs and increased marketing expenses.
Gold: Negative
Pred: Negative
Why: The report describes falling earnings, which is negative.
Time: 1.20 s

Sample 2
Input: The company announced steady revenue growth in its overseas markets.
Gold: Positive
Pred: Positive
Why: Revenue growth is positive financial news.
Time: 1.15 s
===============
```

---
