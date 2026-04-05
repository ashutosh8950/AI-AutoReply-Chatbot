import pyautogui
import time
import pyperclip
import re
import os
from openai import OpenAI
from dotenv import load_dotenv

# ─────────────────────────────────────────
# CONFIG — edit these values
# ─────────────────────────────────────────
load_dotenv()  # reads API key from .env file

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),   # ← key loaded from .env file
    base_url="https://api.groq.com/openai/v1",
)

SENDER_NAME = "SENDER NAME"   # ← change to your contact's exact WhatsApp name

# Screen coordinates — run 01_get_cursor.py to find yours
CHROME_ICON   = (1012, 1055)
DRAG_START    = (693,  257)
DRAG_END      = (1857, 914)
TAB_CLICK     = (424,  207)
MESSAGE_INPUT = (810,  979)

# ─────────────────────────────────────────
# SMARTER MESSAGE DETECTION — works for any year
# ─────────────────────────────────────────
def is_last_message_from_sender(chat_log, sender_name=SENDER_NAME):
    parts = re.split(r'\[\d{1,2}:\d{2},\s*\d{1,2}/\d{1,2}/\d{4}\]\s*', chat_log.strip())
    last_part = parts[-1] if parts else ""
    return sender_name in last_part

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

# Step 1: Click on the chrome icon
pyautogui.click(*CHROME_ICON)
time.sleep(1)

print(f"🤖 Bot started — watching for messages from '{SENDER_NAME}'")

while True:
    time.sleep(5)

    # Step 2: Drag to select the chat text
    pyautogui.moveTo(*DRAG_START)
    pyautogui.dragTo(*DRAG_END, duration=2.0, button='left')

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.press('escape')

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()

    print(chat_history)
    print("Should reply:", is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"
                },
                {
                    "role": "system",
                    "content": "Do not start your reply with a timestamp or name like [21:02, 12/6/2026] Rohan Das:"
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response = completion.choices[0].message.content
        print("Bot Response:", response)
        pyperclip.copy(response)

        # Step 5: Click on the message input box
        pyautogui.click(*MESSAGE_INPUT)
        time.sleep(1)

        # Step 6: Paste the response
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 7: Send the message
        pyautogui.press('enter')
