class Category:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


async def get_all_categories() -> list[Category]:
    return [Category(id=i, name=f'Category {i}') for i in range(10)]
