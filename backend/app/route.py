from helpers.router import ClassRoute


class Route(ClassRoute):
    async def get(self) -> dict[str, str]:
        return {"Hello": "World"}
