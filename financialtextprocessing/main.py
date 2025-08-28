#!/usr/bin/env python3
"""
Assignment 1 — Flan-T5 + Financial PhraseBank
"""

import time, argparse
from datasets import load_dataset
from transformers import pipeline

MODEL_NAME = "google/flan-t5-small"

SYSTEM_PROMPT = (
    "You are a financial NLP assistant. "
    "Your task is to classify the sentiment of financial news sentences. "
    "Always choose exactly one label: Positive, Negative, or Neutral. "
    "Respond with only the label, followed by a short explanation on a new line starting with 'Why:'."
)

def label_to_text(i: int) -> str:
    return {0: "Negative", 1: "Neutral", 2: "Positive"}.get(int(i), "Unknown")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1, help="number of samples to run")
    args = parser.parse_args()

    ds = load_dataset("financial_phrasebank", "sentences_allagree", trust_remote_code=True)
    exs = ds["train"][:args.n]

    pipe = pipeline("text2text-generation", model=MODEL_NAME, device=-1)

    print("==== Report ====")
    print(f"Model: {MODEL_NAME}")
    print("Dataset: financial_phrasebank/sentences_allagree")
    for i, (sentence, gold_label) in enumerate(zip(exs["sentence"], exs["label"])):
        gold_text = label_to_text(gold_label)
        user_prompt = f"Sentence: {sentence}\nWhat is the sentiment of this sentence?"
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"
        t0 = time.time()
        out = pipe(full_prompt, max_new_tokens=32, do_sample=False)
        dt = time.time() - t0
        pred = out[0]["generated_text"].strip()
        print(f"\nSample {i+1}")
        print(f"Input: {sentence}")
        print(f"Gold: {gold_text}")
        print(f"Pred: {pred}")
        print(f"Time: {dt:.2f} s")
    print("===============")

if __name__ == "__main__":
    main()
