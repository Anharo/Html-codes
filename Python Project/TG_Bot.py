from typing import Final
from telegram import Update
from telegram.ext import *
f = open('token.txt','r')
TOKEN: Final = f.read()
Bot_USERNAME: Final ='@goodxd_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello i am a good bot i can talk to your group members nicely')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('SO  WHAT YOU NEED HELP :) ')

async def shut_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bye bye have a nice day or night whatever :0')

def handle_response(text: str)->str:
     processed: str = text.lower()

     if 'Hello' in processed:
         return 'Hello i am a Good bot nice to meet you'
     if 'how are you' in processed:
         return 'i am fine i am a bot though what will happen to me lol !'
     if 'what can you do' in processed:
         return 'sorry i dont do much now but i will be updated in few months of days :0'
     if 'i am bored' in processed:
          print('wait you can check these youtube channel if you are bored')
          print('1)Carryminati: you can check his old videos if there is no new video')
          print('2)Mr beast: he upload monthly there will be some videos that you havent watched')
          return 'thats my suggestions you can find more recommendations by youtube'
     if 'you are a bot right' in processed:
         return 'so what do you think i am ;)'
     return 'I am sorry but i dont understand so really sorry :('
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text


    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    # Command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('shut', shut_command))
    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Error
    app.add_error_handler(error)
    print("polling....")
    app.run_polling(poll_interval=2)
