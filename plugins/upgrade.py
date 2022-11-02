"""DarkLord"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily Upload limit 2GB
	Price 0
	
	_____________________________
	**Only Upgrade Upload Limit
	Not Support 4GB file Rename**
	
	10GB - 10rs 
	50GB -  30rs 
	100GB - 50rs 
	
	_____________________________
	**It's Support 4GB File Rename**

	**VIP 01** 
	Daily  Upload  limit 5GB
	Price Rs 25 🇮🇳/🌎 0.30$  per Month
	
	**VIP 02**
	Daily Upload limit 1OGB
	Price Rs 35  🇮🇳/🌎 0.42$  per Month
	
	**VIP 03**
	Daily Upload limit 30GB
	Price Rs 50  🇮🇳/🌎 0.61$  per Month
	
	**VIP 04**
	Daily Upload limit 50GB
	Price Rs 75 🇮🇳/🌎 0.91$  per Month
	
	**VIP 05**
	Daily Upload limit 100GB 
	Price Rs 110 🇮🇳/🌎 1.33$  per Month
	
	Pay Using Upi I'd 📲 
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	buttons = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🤴 Admin", url = "https://t.me/hellodarklord21")], 
        			[InlineKeyboardButton("PayPal 🌎", url = "soon"),
        			InlineKeyboardButton("💰 Paytm", url = "soon")],[InlineKeyboardButton("Cancel ✖️", callback_data = "cancel")  ]])
	await upgrade.message.edit(text = text, reply_markup = buttons)
