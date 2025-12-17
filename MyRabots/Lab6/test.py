import random
from typing import Dict, Type, Tuple, Optional


class Plant:
    """Базовый класс для растений."""
    exp: int
    penalty: int
    
    def drop(self) -> int:
        """Возвращает количество урожая."""
        raise NotImplementedError


class PotatoPlant(Plant):
    """Класс картофельного растения."""
    exp = 1
    penalty = 1
    MIN_YIELD = 0
    MAX_YIELD = 10
    
    def __init__(self):
        self.potato = random.randint(self.MIN_YIELD, self.MAX_YIELD)
    
    def drop(self) -> int:
        """Возвращает количество картофеля."""
        return self.potato
    
    def __str__(self) -> str:
        return "PotatoPlant"


class CarrotPlant(Plant):
    """Класс морковного растения."""
    exp = 2
    penalty = 2
    
    def drop(self) -> int:
        """Возвращает количество моркови."""
        return 1
    
    def __str__(self) -> str:
        return "CarrotPlant"


class Field:
    """Класс поля с растениями."""
    
    def __init__(self, size: int):
        self.size = size
        self.plants: list[Plant] = []
    
    def grow(self) -> None:
        """Выращивает случайные растения на поле."""
        self.plants = []
        plant_classes = [PotatoPlant, CarrotPlant]
        
        for _ in range(self.size):
            plant_class = random.choice(plant_classes)
            plant = plant_class()
            self.plants.append(plant)
    
    def drop(self) -> Tuple[Type[Plant], int]:
        """Выкапывает случайное растение с его удалением."""
        if not self.plants:
            raise ValueError("На поле нет растений!")
        
        plant = random.choice(self.plants)
        number = plant.drop()
        plant_type = type(plant)
        self.plants.remove(plant)
        
        return plant_type, number
    
    def drop_all(self) -> Tuple[Type[Plant], int]:
        """Проверяет урожай случайного растения без его удаления."""
        if not self.plants:
            raise ValueError("На поле нет растений!")
        
        plant = random.choice(self.plants)
        number = plant.drop()
        plant_type = type(plant)
        
        return plant_type, number
    
    def is_empty(self) -> bool:
        """Проверяет, пусто ли поле."""
        return len(self.plants) == 0


class Task:
    """Класс задания для игрока."""
    
    CROP_TARGETS = {
        PotatoPlant: {"min": 0, "max": 100},
        CarrotPlant: {"min": 0, "max": 20}
    }
    
    def __init__(self, giver: "NPC"):
        self.giver = giver
        self.is_completed = False
        self.crop: Dict[Type[Plant], Dict[str, int]] = {}
        self._init_crop()
    
    def _init_crop(self) -> None:
        """Инициализирует цели для каждого типа растений."""
        for plant_class, targets in self.CROP_TARGETS.items():
            self.crop[plant_class] = {
                "target": random.randint(targets["min"], targets["max"]),
                "current": 0
            }
    
    def check_completed(self) -> bool:
        """Проверяет, выполнено ли задание."""
        self.is_completed = all(
            data["current"] >= data["target"]
            for data in self.crop.values()
        )
        
        if self.is_completed:
            print("Выполнено! Пора сдавать задание.")
        
        return self.is_completed
    
    def update(self, plant_type: Type[Plant], amount: int) -> None:
        """Обновляет прогресс по заданию."""
        if plant_type in self.crop:
            self.crop[plant_type]["current"] += amount
        
        self._print_progress()
        self.check_completed()
    
    def _print_progress(self) -> None:
        """Выводит текущий прогресс по заданию."""
        for plant_class, data in self.crop.items():
            plant_name = plant_class.__name__.replace("Plant", "")
            print(f"{plant_name}: {data['current']}/{data['target']}")


class NPC:
    """Базовый класс NPC."""
    EXP_TASK_BONUS = 10
    
    def __init__(self, name: str):
        self.name = name
        self.prices = {
            PotatoPlant: 1,
            CarrotPlant: 2
        }
    
    def give_task(self) -> Task:
        """Выдает задание игроку."""
        return Task(self)
    
    def complete_task(self, player: "Player", task: Task) -> None:
        """Завершает задание и награждает игрока."""
        if not task.check_completed():
            print(f"{self.name}: Ещё рано сдавать.")
            return
        
        total_money = 0
        for plant_class, data in task.crop.items():
            number = data["current"]
            money = self.prices[plant_class] * number
            total_money += money
            player.money += money
        
        player.exp += self.EXP_TASK_BONUS
        print(f"{self.name}: Задание выполнено! Вы получили {total_money} "
              f"монет и {self.EXP_TASK_BONUS} опыта.")


class Grandma(NPC):
    """Класс бабушки с дополнительными возможностями."""
    PIROZHOK_CHANCE = 0.2
    PIROZHOK_STAMINA_BONUS = 10
    
    def __init__(self):
        super().__init__("Бабушка")
        self.prices = {
            PotatoPlant: 2,
            CarrotPlant: 3
        }
    
    def _give_pirozhok(self, player: "Player") -> None:
        """Дает пирожок игроку."""
        player.stamina += self.PIROZHOK_STAMINA_BONUS
        print(f"{self.name} дала пирожок! "
              f"+{self.PIROZHOK_STAMINA_BONUS} к выносливости.")
    
    def complete_task(self, player: "Player", task: Task) -> None:
        """Завершает задание с шансом дать пирожок."""
        super().complete_task(player, task)
        
        if task.is_completed and random.random() <= self.PIROZHOK_CHANCE:
            self._give_pirozhok(player)


class Player:
    """Класс игрока."""
    
    MAX_STAMINA = 100
    
    def __init__(self, name: str):
        self.name = name
        self.money = 0
        self.exp = 0
        self.stamina = self.MAX_STAMINA
        self.current_task: Optional[Task] = None
    
    def rest(self) -> None:
        """Восстанавливает выносливость игрока."""
        self.stamina += 10
        if self.stamina > self.MAX_STAMINA:
            self.stamina = self.MAX_STAMINA
        
        print(f"{self.name} отдохнул. Выносливость: {self.stamina}")
    
    def dig(self, field: Field) -> None:
        """Копает растения на поле."""
        if self.current_task is None:
            print("Нет задания.")
            return
        
        if self.stamina <= 0:
            print("Сил нет, отдохни.")
            return
        
        if field.is_empty():
            print("На поле нет растений!")
            return
        
        try:
            plant_type, amount = field.drop()
            self.exp += plant_type.exp
            self.stamina -= plant_type.penalty
            
            plant_name = plant_type.__name__.replace("Plant", "").lower()
            print(f"{self.name} выкопал {amount} ед. {plant_name}.")
            
            self.current_task.update(plant_type, amount)
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    def submit_task(self) -> None:
        """Сдает текущее задание."""
        if self.current_task is None:
            print("Нет задания.")
            return
        
        self.current_task.giver.complete_task(self, self.current_task)
        
        if self.current_task.is_completed:
            self.current_task = None
    
    def ask_task(self, npc: NPC) -> None:
        """Берет задание у NPC."""
        self.current_task = npc.give_task()
        print(f"Получено задание от {npc.name}.")
    
    def __str__(self) -> str:
        """Строковое представление состояния игрока."""
        return (f"{self.name}: Деньги={self.money}, "
                f"Опыт={self.exp}, Выносливость={self.stamina}")


def main() -> None:
    """Основная функция игры."""
    field = Field(size=10)
    field.grow()
    
    grandma = Grandma()
    player = Player("Anton")
    
    print("=== Добро пожаловать в игру! ===")
    print(player)
    print()
    
    player.ask_task(grandma)
    print()
    
    for i in range(5):
        print(f"------ Попытка {i + 1} ------")
        player.dig(field)
        print()
    
    player.submit_task()
    print()
    
    print("---- Итог ----")
    print(player)


if __name__ == "__main__":
    main()