# Example of use: for all necessary skills pass
# skill_data = [
#     {"player_skill": 8, "required_skill": 70}, # Matching skill 1
#     {"player_skill": 9, "required_skill": 100}, # Matching skill 2
#     # Add other skills here
# ]


# Run this function
# roll_dice(skill_data)


import random


def calculate_average_skill_difference(skill_data):
    total_diff = 0
    for skill in skill_data:
        player_skill = skill['player_skill']
        required_skill = skill['required_skill']
        diff = (player_skill - required_skill) / required_skill * 100
        total_diff += diff

    average_diff = int(total_diff / len(skill_data))
    return average_diff


def calculate_success(skill_data):
    average_diff = calculate_average_skill_difference(skill_data)
    success_19_20 = max(10, min(200, 100 + average_diff))
    success_15_18 = max(0, min(150, 70 + average_diff))
    success_10_14 = max(-10, min(100, 40 + average_diff))
    success_5_9 = max(-50, min(50, 10 + average_diff))
    success_1_4 = max(-100, min(0, average_diff))

    return success_19_20, success_15_18, success_10_14, success_5_9, success_1_4


def simulate_dice_roll():
    return random.randint(1, 20)


def roll_dice(skill_data):
    success_19_20, success_15_18, success_10_14, success_5_9, success_1_4 = calculate_success(skill_data)
    dice_roll = simulate_dice_roll()

    def determine_result_text(success_value):
        return f"успех на {success_value}%" if success_value >= 0 else f"негативные последствия на {abs(success_value)}%"

    success_values = {
        19: success_19_20,
        15: success_15_18,
        10: success_10_14,
        5: success_5_9,
        1: success_1_4
    }

    success_threshold = next(threshold for threshold in sorted(success_values.keys(), reverse=True) if dice_roll >= threshold)
    success_value = success_values[success_threshold]
    success = success_value >= 0

    result_text = f"Бросаем кубик, чтобы определить результат...\n"

    # Функция для определения текста результата
    for threshold in sorted(success_values.keys(), reverse=True):
        result_text += f"{threshold}: {determine_result_text(success_values[threshold])}\n"
    result_text += f"\nВыпало {dice_roll} - это означает {determine_result_text(success_value)}"

    return {
        "result_text": result_text,
        "dice_roll": dice_roll,
        "success": success
    }

# For tests
# print(roll_dice(skill_data))
