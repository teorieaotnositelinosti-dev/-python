

nums = []
with open("sequence.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            nums.append(float(line))

group1 = [n for n in nums if -3 <= n <= 3]
group2 = [n for n in nums if n < -3 or n > 3]

p1 = len(group1) / len(nums) * 100
p2 = len(group2) / len(nums) * 100

print("Всего чисел:", len(nums))
print("Числа от -3 до 3:", len(group1), f"({p1:.2f}%)")
print("Остальные:", len(group2), f"({p2:.2f}%)")

print("\nДиаграмма процентного соотношения:")
print("[-3..3]   : " + "#" * int(p1 // 1))
print("Остальные: " + "#" * int(p2 // 1))
