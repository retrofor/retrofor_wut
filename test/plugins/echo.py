from iamai import Plugin


class Echo(Plugin):
    async def handle(self) -> None:
        await self.event.reply(self.event.message.replace("echo ", ""))

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type == "message_sent" or self.event.type == "message":
            return self.event.message.startswith("echo ")
        else:
            return False
