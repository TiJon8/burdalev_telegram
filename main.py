import asyncio

from aiogram import Bot, Dispatcher
from models import settings
from aiogram.filters.command import Command
from aiogram.filters import IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.types import (Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, ChatMemberUpdated)
from database_config import db_helper
from schemas import User, Bundle, SubType
from sqlalchemy import select, update


CHANNEL_ID = settings.CHANNEL_ID

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    async with db_helper.session_factory() as session:
        stmt = select(User).where(User.id == message.from_user.id)
        res = await session.execute(stmt)
        row = res.fetchone()
        if row is None:
            session.add(User(id=message.from_user.id, is_member=SubType.guest))
            await session.flush()
            await session.commit()

    inline_buttons = [
        [InlineKeyboardButton(text='Открыть', web_app=WebAppInfo(url=settings.WEBAPP_URL))]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_buttons)

    await bot.send_message(message.from_user.id, 'Приложение', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())