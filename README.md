<h1 align="center">🤖 Gemini AI Chatbot</h1>

<p align="center">
  <strong>A simple terminal chatbot powered by Google Gemini.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Gemini-API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-Terminal-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/PRs-Welcome-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/API-Free%20Tier-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>

---

## 🛠️ Tech Stack

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,git,github,vscode&perline=4" />
  </a>
</p>

| Technology | Purpose |
|---|---|
| <img src="https://skillicons.dev/icons?i=python" width="20" /> **Python** | Core language |
| ✨ **Google Gemini API** | AI responses |
| 📦 **google-genai** | Official Python SDK |
| <img src="https://skillicons.dev/icons?i=git" width="20" /> **Git** | Version control |
| <img src="https://skillicons.dev/icons?i=github" width="20" /> **GitHub** | Code hosting |
| <img src="https://skillicons.dev/icons?i=vscode" width="20" /> **VS Code** | Code editor |

---

## 📖 About

**Gemini AI Chatbot** is a lightweight command-line chatbot built with Python and the Google Gemini API. It remembers your conversation, so you can ask follow-up questions just like a real chat.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **Chat Memory** | Remembers previous messages in the session |
| ⚡ **Fast Replies** | Powered by Gemini Flash model |
| 🛡️ **Error Handling** | Handles server busy, API errors and unexpected issues |
| 🚪 **Easy Exit** | Type `exit` or press `Ctrl + C` to quit |
| 🆓 **Free to Use** | Works with the free Gemini API key |

---

## 🖥️ Preview

```
================================
       GEMINI AI CHATBOT
================================
Type 'exit' to close the chatbot.
--------------------------------

You: Hello!

Bot: Hi there! How can I help you today?

You: exit

Bot: Goodbye!
```

---

## 📋 Prerequisites

- [Python 3.9+](https://www.python.org/downloads/) installed
- A Google account (for the free API key)
- Internet connection

Check your Python version:

```bash
python --version
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository (or copy the code)

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

> Don't have Git? Just copy the code and paste it into a file named `chatbot.py`.

### 2️⃣ Install the required library

```bash
pip install google-genai
```

### 3️⃣ Get your free Gemini API key

1. Open 👉 [Google AI Studio - API Keys](https://aistudio.google.com/api-keys)
2. Sign in with your Google account
3. Click **Create API key**
4. Copy the key

### 4️⃣ Add the API key in the code

Open `chatbot.py` and replace the placeholder:

```python
client = genai.Client(
    api_key="YOUR_API_KEY"
)
```

### 5️⃣ Run the chatbot

```bash
python chatbot.py
```

Now type your question after `You:` and press Enter. 🎉

---

## 🔐 Safer Way: Use an Environment Variable (Recommended)

Instead of writing the API key in your code, store it in an environment variable so it never leaks to GitHub by mistake.

**1. Set the key**

Windows (CMD):
```bash
setx GEMINI_API_KEY "your_api_key_here"
```

Mac / Linux:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**2. Change this part of the code**

```python
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
```

> On Windows, close and reopen the terminal after running `setx`.

---

## 💻 Commands

| Command | Action |
|---|---|
| `exit` | Close the chatbot |
| `Ctrl + C` | Force stop |
| Empty Enter | Ignored (asks again) |

---

## 🧯 Error Handling

| Error | Meaning | Fix |
|---|---|---|
| `ServerError` | Gemini server is busy | Wait and try again |
| `ClientError` | Wrong or expired API key, or bad request | Check your API key and model name |
| `ModuleNotFoundError` | Library not installed | Run `pip install google-genai` |
| Rate limit / quota | Free tier limit reached | Wait a few minutes |

---

## 🏗️ Project Structure

```
Gemini-Chatbot/
│
├── chatbot.py
└── README.md
```

---

## 🛡️ Security Note

- ❌ Never upload your real API key to GitHub
- ✅ Use environment variables
- ✅ If your key leaks, delete it from AI Studio and create a new one

---

## 👨‍💻 Contributors

| Contributor | Role |
|---|---|
| [@akshayjha7](https://github.com/akshayjha7) | Repository Creator |

---

<p align="center">
  <strong>🤖 Gemini AI Chatbot</strong>
  <br/>
  Made with ❤️ using Python & Google Gemini
</p>