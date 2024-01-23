def calculate_average_skill_difference(skill_data):
    total_diff = 0
    for skill in skill_data:
        player_skill = skill['player_skill']
        required_skill = skill['required_skill']
        diff = (player_skill - required_skill) / required_skill * 100
        total_diff += diff

    average_diff = total_diff / len(skill_data)
    return average_diff

# Пример использования
skill_data = [
    {"player_skill": 8, "required_skill": 70},
    {"player_skill": 9, "required_skill": 100},
    # Добавьте здесь другие словари
]

average_difference = calculate_average_skill_difference(skill_data)
print("Средняя разница:", average_difference)