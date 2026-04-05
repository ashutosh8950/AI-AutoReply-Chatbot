import pyautogui
import time
import pyperclip
import re
from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://api.groq.com/openai/v1",
)

def is_last_message_from_sender(chat_log, sender_name="Dinu Tiet Yadav"):
    # Split by WhatsApp timestamp pattern like [14:32, 31/03/2026]
    parts = re.split(r'\[\d{1,2}:\d{2},\s*\d{1,2}/\d{1,2}/\d{4}\]\s*', chat_log.strip())
    last_part = parts[-1] if parts else ""
    print(f"  Last part: {last_part[:80]}")  # debug
    return sender_name in last_part

# Step 1: Click on the chrome icon
pyautogui.click(1012, 1055)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Drag to select the chat text
    pyautogui.moveTo(693, 257)
    pyautogui.dragTo(1857, 914, duration=2.0, button='left')

    # Step 3: Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(424, 207)

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
        pyautogui.click(810, 979)
        time.sleep(1)

        # Step 6: Paste the response
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 7: Send the message
        pyautogui.press('enter')
