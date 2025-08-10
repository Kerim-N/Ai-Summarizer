# 📝 AI Text Summarizer (OpenAI API)

This is a **Python command-line tool** that summarizes the content of a text file using OpenAI's GPT models.

---

## 📌 Features
- Reads text from a `.txt` file.
- Sends it to an OpenAI Chat model (default: `gpt-3.5-turbo`).
- Returns a clean, concise summary.
- Allows choosing a different GPT model via a command-line argument.

---

## 📂 How It Works
1. The script reads your text file.
2. It sends the content to OpenAI's API with a **"Summarize this text"** instruction.
3. The GPT model processes the text and returns a short summary.
4. The summary is printed in the terminal.

---

## 📦 Requirements
- Python 3.8+
- An OpenAI API key ([Get it here](https://platform.openai.com/))
- Installed Python packages:
  ```bash
  pip install openai argparse
