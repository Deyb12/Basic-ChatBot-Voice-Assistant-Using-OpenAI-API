# DevBot AI – ChatBot & Voice Assistant

An interactive **chatbot voice assistant** built with **Streamlit**, **OpenAI API**, and **gTTS (Google Text-to-Speech)**.
It answers user queries in natural language and provides a **voice-over response**.

---

## 🚀 Features

* **Chat Console** – Ask any question and get instant AI-powered answers.
* **Voice Assistant** – Converts chatbot replies into speech using gTTS.
* **Conversation History** – Scrollable panel to track user–bot interaction.
* **Interactive UI** – Built with Streamlit for a simple web-based experience.
* **Custom Branding** – Styled interface with animations and personalized footer.

---

## 🛠️ Tech Stack

* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **Backend/AI:** [OpenAI GPT-3](https://platform.openai.com/)
* **Voice:** [gTTS](https://pypi.org/project/gTTS/)
* **Other:** Base64, HTML/CSS styling

---

## 📂 Project Structure

```
Basic-ChatBot-Voice-Assistant/
├── chat.py                 # Main Streamlit app
├── requirements.txt        # Python dependencies
└── .devcontainer/          # Dev container setup (VS Code)
    └── devcontainer.json
```

---

## ⚙️ Installation & Setup

1. **Clone repository**

   ```bash
   git clone <repo-url>
   cd Basic-ChatBot-Voice-Assistant
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set OpenAI API key**

   * Create a `.streamlit/secrets.toml` file:

     ```toml
     api_secret = "your-openai-api-key"
     ```

4. **Run Streamlit app**

   ```bash
   streamlit run chat.py
   ```

   The app will be available at:

   ```
   http://localhost:8501
   ```

---

## 🔊 Usage

* Type a question in the text box.
* Click **Send**.
* The bot will display and **speak** the response.

---

## 👨‍💻 Author

* **Built with ❤ by [Dave Fagarita](https://github.com/Deyb12)**

---

## 📜 License

This project is for **educational purposes only**.
You may modify and use it for learning or experiments.
