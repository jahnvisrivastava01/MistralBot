# 🤖 Mistral AI Chatbot

A simple AI chatbot built using **Python**, **LangChain**, **Mistral AI**, and **Streamlit**. This project was created to gain hands-on experience with Large Language Models (LLMs), prompt engineering, LangChain, and building both terminal-based and web-based AI applications.

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://jahnvisrivastava01-mistralbot-uichatbot-wcvxhc.streamlit.app/

---

## 📌 Features

### 💻 Terminal Chatbot
- Interactive command-line chatbot
- Powered by Mistral AI
- Uses LangChain message history
- Supports multiple AI personalities
- Continuous conversation until user exits

### 🌐 Streamlit Chatbot
- Clean and simple web interface
- Chat history using Streamlit Session State
- Real-time conversations
- Personality selection
- Built mainly for hands-on practice with Streamlit integration

---

## 🎭 AI Modes

- 😠 Angry Mode
- 😂 Funny Mode
- 😊 Normal Mode

Each mode changes the chatbot's behaviour using different system prompts.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- python-dotenv

---

## 📂 Project Structure

```
MistralBot/
│── chatbot.py          # Terminal Chatbot
│── UIChatbot.py        # Streamlit Chatbot
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/MistralBot.git
cd MistralBot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key
```

---

## ▶️ Run the Terminal Chatbot

```bash
python chatbot.py
```

---

## ▶️ Run the Streamlit Chatbot

```bash
streamlit run UIChatbot.py
```

---

## 📚 Learning Outcomes

This project helped me practice:

- Working with Large Language Models (LLMs)
- LangChain fundamentals
- Prompt Engineering
- Managing conversation history
- Streamlit application development
- Environment variables using `.env`
- Git & GitHub workflow

---

## 📝 Note

The Streamlit interface is  simple. It was developed primarily for hands-on practice and to understand how to integrate LLMs with a web interface using Streamlit, rather than focusing on advanced UI/UX design.

---

## 🔮 Future Improvements

- Markdown rendering
- Streaming responses
- Multiple LLM support
- Chat export
- Dark themed custom UI
- Conversation memory
- Response generation indicator

---

## 👩‍💻 Author

**Jahnvi Srivastava**

If you found this project interesting, feel free to ⭐ the repository!
