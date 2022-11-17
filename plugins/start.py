from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("YouTube", url="https://www.youtube.com")],
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>!\nI'm PopCorn! I will help You download any YouTube video you want. Just send me a link.\n/help for more info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
