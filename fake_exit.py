# For @UniBorg

"""fake exit
\n.fexit"""



from telethon import events
from datetime import datetime
import importlib.util
import asyncio
import random
import importlib.util
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.fexit (.*)")
async def timer_blankx(e):
 txt=e.text[7:] + '\n\n`Processing....` '
 j=1
 k=j
 for j in range(j):
  await e.edit(txt + str(k))
  k=k-1
  await asyncio.sleep(1)
 if e.pattern_match.group(1) == 'f':
  await e.edit("`Legend is leaving this chat.....!` `Goodbye aren't forever. It was a pleasant time with you guys..` ")
