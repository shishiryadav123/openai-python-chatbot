# 🤖 OpenAI Python CLI Chatbot

A lightweight command-line chatbot built with **Python** and powered by **OpenAI's GPT API**. Talk to ChatGPT directly from your terminal—no browser required.

---

## 🧠 Features

- 💬 Real-time conversation in your terminal
- ⚡ Powered by GPT-3.5 / GPT-4 (via OpenAI API)
- 🔐 Uses `.env` for secure API key management
- 🧪 Minimal dependencies and easy setup

---

## 📁 Project Structure

```bash
openai-python-chatbot/
│
├── main.py                         
├── requirements.txt     
├── .env                 
└── README.md
```

## 🧰 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/openai-python-chatbot.git
cd openai-python-chatbot

# Create virtual environment
python -m venv venv
source venv\Scripts\activate 

# Install dependencies
pip install -r requirements.txt

```

🔑 Setup
Get your OpenAI API key from: https://platform.openai.com/account/api-keys

Create a .env file in the root directory:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

🚀 Run the Chatbot
```bash
python main.py
```

✅ You’ll now see a prompt like:

```
🤖 ChatGPT CLI — Type 'exit' to quit

🧑 You:
```





