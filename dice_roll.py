# # Example of use: for all necessary skills pass
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

    result_text = f"Бросаем кубик, чтобы определить результат...\n"

    # Функция для определения текста результата
    def determine_result_text(success_value):
        if success_value < 0:
            return f"негативные последствия на {abs(success_value)}%"
        else:
            return f"успех на {success_value}%"

    result_text += f"19-20: {determine_result_text(success_19_20)}\n"
    result_text += f"15-18: {determine_result_text(success_15_18)}\n"
    result_text += f"10-14: {determine_result_text(success_10_14)}\n"
    result_text += f"5-9: {determine_result_text(success_5_9)}\n"
    result_text += f"1-4: {determine_result_text(success_1_4)}\n\n"
    result_text += f"Выпало {dice_roll} - это означает "

    if dice_roll >= 19:
        result_text += determine_result_text(success_19_20)
    elif dice_roll >= 15:
        result_text += determine_result_text(success_15_18)
    elif dice_roll >= 10:
        result_text += determine_result_text(success_10_14)
    elif dice_roll >= 5:
        result_text += determine_result_text(success_5_9)
    else:
        result_text += determine_result_text(success_1_4)

    return result_text


