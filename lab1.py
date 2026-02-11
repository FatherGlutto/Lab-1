# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union, Literal
'''Literal нужен для 3 класса, для определенных значений'''

class Guitar:
    def __init__(self, number_of_strings: int, frets: int):

        if not isinstance(number_of_strings, int):
            raise TypeError("Число струн должно быть целым числом")
        if number_of_strings != 6:
            raise ValueError("Для стандартной гитары количество струн должно быть 6")
        self.number_of_strings = number_of_strings

        if not isinstance(frets, int):
            raise TypeError("Число ладов должно быть целым числом")
        if frets != 24:
            raise ValueError("Для данной модели гитары количество ладов должно быть 24")
        self.frets = frets

    def new_guitar(self, number_of_strings: Union[int], frets: Union[int]) -> None:
        """
                Создает новую гитару с указанными параметрами.
                :param number_of_strings: Ожидаемое количество струн.
                :param frets: Ожидаемое количество ладов.
                :raises TypeError: Если number_of_strings или frets не являются целыми числами.
                :raises ValueError: Если количество струн или ладов не соответствует стандартам.

        Примеры:
            my_guitar = Guitar(6, 24)
            my_guitar.new_guitar(6, 24)
        """

        if not isinstance(number_of_strings, int):
            raise TypeError("Число струн должно быть целым числом.")
        if number_of_strings != 6:
            raise ValueError("Новая гитара должна иметь 6 струн.")

        if not isinstance(frets, int):
            raise TypeError("Число ладов должно быть целым числом.")
        if frets != 24:
            raise ValueError("Новая гитара должна иметь 24 лада.")

        self.number_of_strings = number_of_strings
        self.frets = frets
        # print(f"Новая гитара создана: {self.number_of_strings} струн, {self.frets} ладов.")



if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class User:

    def __init__(self, user_id: int, username: str, email: str):

        if not isinstance(user_id, int):
            raise TypeError("ID пользователя должен быть целым числом.")
        if user_id <= 0:
            raise ValueError("ID пользователя должен быть положительным числом.")
        self.user_id: int = user_id

        if not isinstance(username, str) or not username.strip():
            raise TypeError("Имя пользователя должно быть непустой строкой.")
        self.username: str = username

        if not isinstance(email, str) or not email.strip():
            raise TypeError("Email должен быть непустой строкой.")

        if "@" not in email:
            raise ValueError("Email должен содержать символ '@'.")
        self.email: str = email


    def update_profile(self, username: Union[int, None], email:Union[int, None]) -> None:
        ...

    """
    Обновление профиля пользователя.

    :param username: Новое имя пользователя. Если None, имя не изменяется.
    :param email: Новый адрес электронной почты. Если None, email не изменяется.
    :raises TypeError: Если username или email имеют некорректный тип.
    :raises ValueError: Если username или email пусты (недопустимо).
    :raises ValueError: Если новый email уже используется другим активным пользователем. """

class Sword:

    def __init__(self, blade_length: Union[int, float], material: Literal["steel", "iron", "obsidian"], enchantment_level: int = 0):
        """

        :param blade_length: Длина лезвия меча (в сантиметрах).
        :param material: Материал, из которого изготовлено лезвие. Допустимые значения: "steel", "iron", "obsidian".
        :param enchantment_level: Уровень зачарования меча. По умолчанию 0 (без зачарования).
        :raises TypeError: Если blade_length или enchantment_level имеют некорректный тип.
        :raises ValueError: Если blade_length не является положительным числом,
                            material не является одним из допустимых,
                            или enchantment_level отрицательный.

        """
        if not isinstance(blade_length, (int, float)):
            raise TypeError("Длина лезвия должна быть числом (int или float).")
        if not blade_length > 0:
            raise ValueError("Длина лезвия должна быть положительным числом.")
        self.blade_length: Union[int, float] = blade_length

        valid_materials = ["steel", "iron", "obsidian"]
        if not isinstance(material, str) or material not in valid_materials:
            raise ValueError(f"Материал лезвия должен быть одним из: {', '.join(valid_materials)}.")
        self.material: Literal["steel", "iron", "obsidian"] = material

        if not isinstance(enchantment_level, int):
            raise TypeError("Уровень зачарования должен быть целым числом.")
        if enchantment_level < 0:
            raise ValueError("Уровень зачарования не может быть отрицательным.")
        self.enchantment_level: int = enchantment_level

    def enchant(self, bonus_power: int) -> None:
        """
        Наделяет меч дополнительной магической силой (зачаровывает).

        :param bonus_power: Сила добавляемого зачарования.
        :raises TypeError: Если bonus_power имеет некорректный тип.
        :raises ValueError: Если bonus_power отрицательный.
"""
        if not isinstance(bonus_power, int):
            raise TypeError("Сила зачарования должна быть целым числом.")
        if bonus_power < 0:
            raise ValueError("Сила зачарования не может быть отрицательной.")

        self.enchantment_level += bonus_power

    def get_damage(self) -> float:
        ...
        """
        Рассчитывает примерный урон, который меч может нанести.
        Урон зависит от длины лезвия, материала и уровня зачарования.

        :return: Приблизительный показатель урона.
"""