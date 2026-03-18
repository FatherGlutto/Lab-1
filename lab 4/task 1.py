
from typing import Optional


class Vehicle:
    """
    Базовый класс, описывающий транспортное средство.

    Attributes:
        brand (str): Производитель транспорта.
        max_speed (int): Максимальная скорость (км/ч).
        _engine_started (bool): Состояние двигателя (инкапсулированный атрибут).

    """

    def __init__(self, brand: str, max_speed: int) -> None:
        """
        Инициализация транспортного средства.

        brand: Название производителя.
        max_speed: Максимальная скорость.

        """

        if not isinstance(brand, str) or not brand.strip():
            raise TypeError("brand должен быть непустой строкой")

        if not isinstance(max_speed, int):
            raise TypeError("max_speed должен быть целым числом")

        if max_speed <= 0:
            raise ValueError("max_speed должен быть положительным")

        self.brand: str = brand
        self.max_speed: int = max_speed
        self._engine_started: bool = False  # инкапсулированный атрибут

    def start_engine(self) -> None:
        """
        Запускает двигатель транспорта.

        """
        self._engine_started = True

    def stop_engine(self) -> None:
        """
        Останавливает двигатель транспорта.

        """
        self._engine_started = False

    def move(self, distance: float) -> float:
        """
        Выполняет движение транспорта.

        :param distance: Расстояние (км)
        :return: Время движения (часы)

        """
        if distance <= 0:
            raise ValueError("distance должно быть положительным")

        return distance / self.max_speed

    def __str__(self) -> str:

        return f"Транспорт: {self.brand}, max_speed={self.max_speed}"

    def __repr__(self) -> str:

        return f"Vehicle(brand={self.brand!r}, max_speed={self.max_speed})"


# --------------------------------------------------


class ElectricCar(Vehicle):
    """
    Дочерний класс электромобиля.

    Расширяет базовый класс Vehicle. Добавляет атрибут батарея.

        battery_capacity (float): Ёмкость батареи
        charge_level (float): Текущий заряд
    """

    def __init__(self, brand: str, max_speed: int, battery_capacity: float, charge_level: float = 100.0) -> None:
        """
        Расширенный конструктор электромобиля.

        brand: Производитель.
        max_speed: Максимальная скорость.
        battery_capacity: Ёмкость батареи.
        charge_level: Начальный заряд.
        """

        # наследуем конструктор базового класса
        super().__init__(brand, max_speed)

        if battery_capacity <= 0:
            raise ValueError("battery_capacity должна быть положительной")

        if not (0 <= charge_level <= 100):
            raise ValueError("charge_level должен быть от 0 до 100")

        self.battery_capacity: float = battery_capacity
        self.charge_level: float = charge_level

    # Унаследованный метод start_engine используется без изменений

    def charge(self, amount: float) -> None:
        """
        Заряжает автомобиль.

        amount: Процент зарядки.
        """
        if amount <= 0:
            raise ValueError("amount должен быть положительным")

        self.charge_level = min(100.0, self.charge_level + amount)

    # Перегрузка метода
    def move(self, distance: float) -> float:
        """
        Перегруженный метод движения.

        Причина перегрузки:
        Электромобиль расходует заряд батареи при движении,
        в отличие от обычного транспорта.

        distance: Расстояние
        return: Время движения
        """

        if self.charge_level <= 0:
            raise RuntimeError("Батарея разряжена")

        # вызываем базовую реализацию
        time = super().move(distance)

        # условный расход батареи
        consumption = distance * 0.2
        self.charge_level = max(0.0, self.charge_level - consumption)

        return time

    def __str__(self) -> str:
        """Расширенное строковое представление."""
        return (
            f"Электромобиль {self.brand}, "
            f"скорость={self.max_speed}, "
            f"заряд={self.charge_level:.1f}%"
        )

    def __repr__(self) -> str:
        return (
            f"ElectricCar(brand={self.brand!r}, "
            f"max_speed={self.max_speed}, "
            f"battery_capacity={self.battery_capacity}, "
            f"charge_level={self.charge_level})"
        )


# --------------------------------------------------


if __name__ == "__main__":
    # Пример использования

    car = ElectricCar("Tesla", 250, 75.0)

    print(car)
    car.start_engine()

    time = car.move(50)
    print(f"Время поездки: {time:.2f} ч")

    car.charge(10)
    print(car)