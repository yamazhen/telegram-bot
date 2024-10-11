from telegram.ext import ContextTypes
import pandas as pd
import os

async def delete_message(chat_id: int, message_id: int, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    for key in list(context.user_data.keys()):
        if context.user_data[key] == message_id:
            context.user_data[key] = None

def save_to_excel(phone_number: str):
    file_path = "phone_numbers.xlsx"
    phone_number = str(phone_number).strip()
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        existing_numbers = df["Phone Number"].astype(str).str.strip()
        if phone_number in existing_numbers.values:
            return
    else:
        df = pd.DataFrame(columns=["Phone Number"])

    new_data = pd.DataFrame({"Phone Number": [str(phone_number)]})
    df = pd.concat([df, new_data], ignore_index=True)

    df.to_excel(file_path, index=False)
