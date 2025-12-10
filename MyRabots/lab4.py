import numpy as np

ITEMS = {
    'r': (3, 25), 'p': (2, 15), 'a': (2, 15), 'm': (2, 20),
    'i': (1, 5),  'k': (1, 15), 'x': (3, 20), 't': (1, 25),
    'f': (1, 15), 'd': (1, 10), 's': (2, 20), 'c': (2, 20),
}
ITEM_NAMES = list(ITEMS.keys())
ITEM_SIZES = [ITEMS[name][0] for name in ITEM_NAMES]
ITEM_VALUES = [ITEMS[name][1] for name in ITEM_NAMES]

STARTING_SCORE = 10
MAX_CAPACITY_MAIN = 9
TOTAL_ITEMS_SCORE = sum(ITEM_VALUES)

MIN_REQUIRED_TAKEN_SCORE = (TOTAL_ITEMS_SCORE - STARTING_SCORE) // 2 + 1 

def solve_knapsack_dp(item_names, item_sizes, item_values, capacity):
    N = len(item_names)
    W = capacity
    
    DP = np.zeros((N + 1, W + 1), dtype=int)

    for i in range(1, N + 1):
        size = item_sizes[i - 1]
        value = item_values[i - 1]

        for w in range(W + 1):
            if size <= w:
                DP[i, w] = max(DP[i - 1, w], DP[i - 1, w - size] + value)
            else:
                DP[i, w] = DP[i - 1, w]
    
    w = W
    taken_items = []
    max_value = DP[N, W]
    
    for i in range(N, 0, -1):

        if max_value != DP[i - 1, w]:
            item = item_names[i - 1]
            taken_items.append(item)
            max_value -= item_values[i - 1]
            w -= item_sizes[i - 1]
            
    return sorted(taken_items), sum(item_sizes[item_names.index(item)] for item in taken_items), DP[N, W]

def display_inventory_3x3(items, items_map):
    
    inventory = [['.' for _ in range(3)] for _ in range(3)]
    
    i = 0
    r, c = 0, 0
    
    for item in items:
        size, _ = items_map[item]
        
        for _ in range(size):
            if r < 3:
                inventory[r][c] = item
                c += 1
                if c >= 3:
                    c = 0
                    r += 1
            else:
                
                break

    print("\n[Инвентарь 3x3 (упрощенное отображение)]")
    for row in inventory:
        print(f"[{', '.join(row)}]")
    print("----------------------------------------")




taken_items_9, size_9, taken_score_9 = solve_knapsack_dp(
    ITEM_NAMES, ITEM_SIZES, ITEM_VALUES, MAX_CAPACITY_MAIN
)

final_score_9 = STARTING_SCORE + taken_score_9 - (TOTAL_ITEMS_SCORE - taken_score_9)

print("## 💎 РЕШЕНИЕ ОСНОВНОГО ЗАДАНИЯ (Вариант 10, 9 ячеек)")
print(f"   Минимально требуемый балл (взятые предметы): {MIN_REQUIRED_TAKEN_SCORE}")

if taken_score_9 >= MIN_REQUIRED_TAKEN_SCORE:
    print("\n✅ ОПТИМАЛЬНЫЙ НАБОР:")
    print(f"   Предметы: {', '.join(taken_items_9)}")
    print(f"   Занято ячеек: {size_9} / {MAX_CAPACITY_MAIN}")
    print(f"   Сумма очков взятых: {taken_score_9}")
    print(f"   ИТОГОВЫЕ ОЧКИ ВЫЖИВАНИЯ: {final_score_9}")
    display_inventory_3x3(taken_items_9, ITEMS)
else:
    print(f"\n❌ Оптимальный набор ({taken_score_9} очков) не обеспечивает положительный итоговый счет.")




MAX_CAPACITY_EXTRA = 7
taken_items_7, size_7, taken_score_7 = solve_knapsack_dp(
    ITEM_NAMES, ITEM_SIZES, ITEM_VALUES, MAX_CAPACITY_EXTRA
)

print("\n" + "="*50)
print(f"## 🔒 РЕШЕНИЕ ДОПЗАДАНИЯ (7 ячеек)")

if taken_score_7 >= MIN_REQUIRED_TAKEN_SCORE:
    final_score_7 = STARTING_SCORE + taken_score_7 - (TOTAL_ITEMS_SCORE - taken_score_7)
    print("✅ Решение найдено:")
    print(f"   Предметы: {', '.join(taken_items_7)}")
    print(f"   Сумма очков взятых: {taken_score_7}")
    print(f"   ИТОГОВЫЕ ОЧКИ ВЫЖИВАНИЯ: {final_score_7}")
else:
    print("❌ РЕШЕНИЕ ОТСУТСТВУЕТ")
    print(f"   Максимально возможное количество очков, которое можно набрать в 7 ячейках: {taken_score_7}")
    print(f"   ({taken_score_7} < {MIN_REQUIRED_TAKEN_SCORE} — не обеспечивает положительный итоговый счет).")