import datetime as dt


FORMAT = '%H:%M:%S'  # Формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or data[0] is None:
        return False
    return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data and time <= max(storage_data.keys()):
        return False
    return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    steps_per_day = [step for step in storage_data.values()]
    return sum(steps_per_day) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    transfer_coef = 1000
    dist = STEP_M * steps / transfer_coef
    return dist


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    hour = current_time.hour + current_time.minute / 60
    mean_speed = dist / hour
    minutes = current_time.hour * 60 + current_time.minute
    spent_calories = (0.035 * WEIGHT + (mean_speed ** 2 / HEIGHT) * 0.029 * WEIGHT) * minutes
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


def show_message(pack_time, day_steps, dist, spent_calories, achievement):
    return f'''
Время: {pack_time.time()}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{achievement}
'''


def accept_package(data):
    """Обработать пакет данных."""

    if not check_correct_data(data):  # Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    pack_time = dt.datetime.strptime(data[0], FORMAT)  # Строка с временем в объект типа time.

    if not check_correct_time(pack_time):  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])  # Результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time)  # Результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Выбранное мотивирующее сообщение.
    storage_data[pack_time] = data[1]
    return print(show_message(pack_time, day_steps, dist, spent_calories, achievement))


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
