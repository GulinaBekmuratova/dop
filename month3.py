async def echo(message: types.Message):
    bad_words = ['java', 'html', 'дурак', "дура"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.reply(f"Админ удалите {username} из группы")



async def ban(message: types.Message):
    if message.from_user.id == ADMIN:
        admin_author = await check_user_is_admin(message)
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                text = 'пользователь удален'
            )







