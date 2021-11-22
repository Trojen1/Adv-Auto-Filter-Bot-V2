#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

from .user import User

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"""Yahallo😋 I'm Ichigo 🥰
 
You Can Download Any Romance/Shoujo Manga Using Me 💛😜
💛My Owner is @tr0j3n 🖤
💛If You Have Got Any Problem 'bout Me Please Contact him or @Peaceful_Wolf_016 😈

💛Join @waifuNetBots To Get Help 💛

💛My Owner's And Dev's Harem & From Here You Can See My Sisters: @waifuNetwork"""
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("I'm Going To Sleep Bye Byeeee💛")
