from typing import Optional


class Employee:
    """Базовый класс Сотрудник."""
    
    def __init__(self, name: str, hours_worked: int, rate: float, bonus_coefficient: float):
        """
        Инициализация сотрудника.
        
        Args:
            name: Имя сотрудника
            hours_worked: Количество рабочих часов
            rate: Ставка за час
            bonus_coefficient: Коэффициент премии
        """
        self.name = name
        self.hours_worked = hours_worked
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient
        self.base_salary = 0.0
        self.bonus_amount = 0.0
    
    def calculate_bonus(self) -> float:
        """
        Метод 1: Рассчитать размер премии.
        
        Returns:
            Размер премии в денежных единицах
        """
        self.base_salary = self.hours_worked * self.rate
        self.bonus_amount = self.base_salary * self.bonus_coefficient
        return self.bonus_amount
    
    def salary_to_hours_ratio(self) -> float:
        """
        Метод 2: Соотношение зарплаты к рабочим часам.
        
        Returns:
            Средняя зарплата за один рабочий час
        """
        if self.hours_worked == 0:
            return 0.0
        
        total_salary = self.base_salary + self.bonus_amount
        return total_salary / self.hours_worked
    
    def calculate_total_salary(self) -> float:
        """Рассчитать общую зарплату (оклад + премия)."""
        return self.base_salary + self.bonus_amount
    
    def display_info(self) -> None:
        """Вывести информацию о сотруднике."""
        print(f"\n{'='*40}")
        print(f"Сотрудник: {self.name}")
        print(f"Должность: {self.__class__.__name__}")
        print(f"Отработано часов: {self.hours_worked}")
        print(f"Ставка в час: {self.rate:.2f}")
        print(f"Коэффициент премии: {self.bonus_coefficient:.2f}")
        print(f"Оклад: {self.base_salary:.2f}")
        print(f"Премия: {self.bonus_amount:.2f}")
        print(f"Общая зарплата: {self.calculate_total_salary():.2f}")
        print(f"Соотношение зарплаты к часам: {self.salary_to_hours_ratio():.2f}")
        print(f"{'='*40}")


class SeniorEmployee(Employee):
    """Класс Старший сотрудник."""
    
    def __init__(self, name: str, hours_worked: int, rate: float, 
                 bonus_coefficient: float, team_size: int):
        """
        Инициализация старшего сотрудника.
        
        Args:
            name: Имя сотрудника
            hours_worked: Количество рабочих часов
            rate: Ставка за час
            bonus_coefficient: Коэффициент премии
            team_size: Размер команды (уникальное поле)
        """
        super().__init__(name, hours_worked, rate, bonus_coefficient)
        self.team_size = team_size  
        self.team_management_bonus = 0.0
    
    def calculate_bonus(self) -> float:
        """
        Метод 1: Рассчитать размер премии для старшего сотрудника.
        Включает дополнительную премию за управление командой.
        """
        base_bonus = super().calculate_bonus()
        
        self.team_management_bonus = self.team_size * (self.rate * 0.5)
        self.bonus_amount += self.team_management_bonus
        
        return self.bonus_amount
    
    def salary_to_hours_ratio(self) -> float:
        """
        Метод 2: Соотношение зарплаты к рабочим часам для старшего сотрудника.
        """
        if self.hours_worked == 0:
            return 0.0
        
        total_salary = self.base_salary + self.bonus_amount
        return total_salary / self.hours_worked
    
    def display_info(self) -> None:
        """Вывести информацию о старшем сотруднике."""
        super().display_info()
        print(f"Размер команды: {self.team_size} человек")
        print(f"Премия за управление командой: {self.team_management_bonus:.2f}")


class Director(Employee):
    """Класс Директор."""
    
    def __init__(self, name: str, hours_worked: int, rate: float, 
                 bonus_coefficient: float, company_profit: float):
        """
        Инициализация директора.
        
        Args:
            name: Имя сотрудника
            hours_worked: Количество рабочих часов
            rate: Ставка за час
            bonus_coefficient: Коэффициент премии
            company_profit: Прибыль компании (уникальное поле)
        """
        super().__init__(name, hours_worked, rate, bonus_coefficient)
        self.company_profit = company_profit  
        self.profit_bonus = 0.0
    
    def calculate_bonus(self) -> float:
        """
        Метод 1: Рассчитать размер премии для директора.
        Включает премию от прибыли компании.
        """
        base_bonus = super().calculate_bonus()
        
        self.profit_bonus = self.company_profit * 0.01
        self.bonus_amount += self.profit_bonus
        
        return self.bonus_amount
    
    def salary_to_hours_ratio(self) -> float:
        """
        Метод 2: Соотношение зарплаты к рабочим часам для директора.
        Учитывает, что у директора может быть ненормированный рабочий день.
        """
        if self.hours_worked == 0:
            return 0.0
        
        total_salary = self.base_salary + self.bonus_amount
        
        if self.hours_worked > 160:
            effective_hours = self.hours_worked * 1.5
        else:
            effective_hours = self.hours_worked
            
        return total_salary / effective_hours
    
    def display_info(self) -> None:
        """Вывести информацию о директоре."""
        super().display_info()
        print(f"Прибыль компании: {self.company_profit:.2f}")
        print(f"Премия от прибыли: {self.profit_bonus:.2f}")


def demonstrate_work():
    """Демонстрация работы классов."""
    
    print("=" * 50)
    print("ЛАБОРАТОРНАЯ РАБОТА №6")
    print("ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ")
    print("=" * 50)
    
    employees = [
        Employee("Иванов И.И.", 160, 500.0, 0.15),
        SeniorEmployee("Петров П.П.", 170, 750.0, 0.20, 5),
        Director("Сидоров С.С.", 180, 1000.0, 0.25, 5000000.0),
        SeniorEmployee("Кузнецова А.В.", 165, 700.0, 0.18, 8),
        Employee("Смирнов Д.К.", 155, 450.0, 0.10)
    ]
    
    for emp in employees:
        bonus = emp.calculate_bonus()
        
        ratio = emp.salary_to_hours_ratio()
        
        emp.display_info()
    
    print("\n" + "=" * 50)
    print("СВОДНЫЙ АНАЛИЗ:")
    print("=" * 50)
    
    total_salary_all = sum(emp.calculate_total_salary() for emp in employees)
    avg_ratio = sum(emp.salary_to_hours_ratio() for emp in employees) / len(employees)
    
    print(f"Общая сумма зарплат всех сотрудников: {total_salary_all:.2f}")
    print(f"Среднее соотношение зарплаты к часам: {avg_ratio:.2f}")
    
    most_efficient = max(employees, key=lambda e: e.salary_to_hours_ratio())
    print(f"Самый эффективный сотрудник: {most_efficient.name} "
          f"({most_efficient.__class__.__name__})")
    print(f"Его соотношение зарплаты к часам: {most_efficient.salary_to_hours_ratio():.2f}")


def interactive_mode():
    """Интерактивный режим для тестирования."""
    
    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 50)
    
    while True:
        print("\nВыберите тип сотрудника:")
        print("1. Обычный сотрудник")
        print("2. Старший сотрудник")
        print("3. Директор")
        print("4. Выход")
        
        choice = input("Ваш выбор (1-4): ").strip()
        
        if choice == "4":
            print("Выход из программы.")
            break
        
        if choice not in ["1", "2", "3"]:
            print("Неверный выбор. Попробуйте снова.")
            continue
        
        name = input("Введите имя сотрудника: ").strip()
        hours = int(input("Введите количество рабочих часов: "))
        rate = float(input("Введите ставку за час: "))
        bonus_coef = float(input("Введите коэффициент премии: "))
        
        if choice == "1":
            employee = Employee(name, hours, rate, bonus_coef)
        elif choice == "2":
            team_size = int(input("Введите размер команды: "))
            employee = SeniorEmployee(name, hours, rate, bonus_coef, team_size)
        else:  
            company_profit = float(input("Введите прибыль компании: "))
            employee = Director(name, hours, rate, bonus_coef, company_profit)
        
        employee.calculate_bonus()
        employee.salary_to_hours_ratio()
        employee.display_info()


if __name__ == "__main__":
    demonstrate_work()
    
    interactive_mode()