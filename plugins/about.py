from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("Bot:- @TechRenameX_Robot\nCreator:- @hellodarklord21\nLanguage:- Python3\nLibrary:- Pyrogram 2.0\nServer:- Heroku")
