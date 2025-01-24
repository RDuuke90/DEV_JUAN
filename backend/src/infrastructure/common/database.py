from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="sqlite://miners.db",
        modules={"models": ["src.infrastructure"]}
    ),

    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close_connections()
