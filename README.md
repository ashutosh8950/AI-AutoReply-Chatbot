# 🤖 AI AutoReply WhatsApp Bot

Automatically replies to WhatsApp Web messages using **Groq AI** (free) and **PyAutoGUI**.

## 🎥 How it Works
1. Bot opens Chrome with WhatsApp Web
2. Selects and copies the chat text every 5 seconds
3. Detects if the last message is from your target contact
4. Sends the chat to Groq AI and gets a funny Hinglish reply
5. Automatically pastes and sends the reply in WhatsApp

---

## 📁 Project Files

| File | Purpose |
|---|---|
| `01_get_cursor.py` | Find screen coordinates of your screen |
| `02_openai.py` | Test if your Groq API key is working |
| `03_bot.py` | Main bot (simple version) |
| `bot_v2.py` | Advanced bot with memory + smarter detection |
| `.env.example` | Template for your API key |

---

## ⚙️ Setup Instructions

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOURUSERNAME/ai-autoreply-bot.git
cd ai-autoreply-bot
```

### Step 2 — Install dependencies
```bash
pip install pyautogui pyperclip openai python-dotenv
```

### Step 3 — Get free Groq API key
- Go to https://console.groq.com
- Sign up free (no credit card needed)
- Click **API Keys** → **Create API Key**
- Copy the key

### Step 4 — Create your .env file
- Rename `.env.example` to `.env`
- Open it and paste your key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Step 5 — Find your screen coordinates
```bash
python 01_get_cursor.py
```
Hover your mouse over these 5 positions and note the coordinates:
- Chrome icon in taskbar
- Top-left of WhatsApp chat area
- Bottom-right of WhatsApp chat area
- Any empty area on screen
- WhatsApp message input box

### Step 6 — Update coordinates in bot file
Open `03_bot.py` and update:
```python
CHROME_ICON   = (????, ????)   # your values
DRAG_START    = (????, ????)
DRAG_END      = (????, ????)
TAB_CLICK     = (????, ????)
MESSAGE_INPUT = (????, ????)
```

### Step 7 — Set your contact name
```python
SENDER_NAME = "Your Contact Name"  # exact name as shown in WhatsApp
```

### Step 8 — Run the bot
```bash
python 03_bot.py
```

---

## 🛑 How to Stop
- Press `Ctrl+C` in terminal
- OR move mouse to top-left corner (0,0) — only in `bot_v2.py`

---

## 🧠 bot_v2.py Extra Features
- **Memory** — remembers past conversations across sessions
- **Smarter detection** — no duplicate replies
- **Kill switch** — move mouse to corner to pause
- **Human delay** — realistic typing pause before sending

---

## ⚠️ Important Notes
- Keep WhatsApp Web open in Chrome while bot is running
- Do not move your mouse while bot is selecting chat text
- Bot only works on Windows (PyAutoGUI limitation)
- Your screen resolution affects coordinates — always recalibrate

---

## 🆓 Free Tools Used
- [Groq API](https://console.groq.com) — Free AI API
- [PyAutoGUI](https://pyautogui.readthedocs.io) — Screen automation
- [LLaMA 3.3 70B](https://groq.com) — AI model via Groq
