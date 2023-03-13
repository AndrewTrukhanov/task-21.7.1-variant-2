from cat2 import Cat2

cats = [
    {
        "animal": "кошка",
        "name": "Барон",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "animal": "кошка",
        "name": "Муся",
        "gender": "девочка",
        "age": 4,
    }
]

for cat in cats:
    cat_obj = Cat2()
    cat_obj.init_from_dict(cat)

    print(f"\nВид: {cat_obj.animal}, Имя: {cat_obj.name}, Пол: {cat_obj.gender}, Возраст: {cat_obj.age}")
