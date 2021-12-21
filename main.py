import asyncio

from pytgcalls import idle

from config import call_py


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Started!|
    ------------------
"""
    )
    await call_py.join_chat(GROUP_ID)
    await call_py.send_message(GROUP_ID, "I Used Your Code For Music")
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
