# Импортируйте необходимые модули
import datetime as dt


FORMAT = '%H:%M:%S'  # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if len(data) != 2 or data[0] is None:
        return False
    return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True
    if storage_data and time <= max(storage_data.keys()):
        return False
    return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните эту сумму.
    steps_per_day = [step for step in storage_data.values()]
    return sum(steps_per_day) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.
    transfer_coef = 1000  # Коэффициент перевода значения расстояния из метров в километры
    dist = STEP_M * steps / transfer_coef
    return dist


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.
    # current_time = dt.datetime.time()
    hour = current_time.hour + current_time.minute / 60
    mean_speed = dist / hour
    minutes = current_time.hour * 60 + current_time.minute
    spent_calories = (0.035 * WEIGHT + (mean_speed ** 2 / HEIGHT) * 0.029 * WEIGHT) * minutes
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


# Место для функции show_message.
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

    # Распакуйте полученные данные.
    pack_time = dt.datetime.strptime(data[0], FORMAT)  # Преобразуйте строку с временем в объект типа time.

    if not check_correct_time(pack_time):  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])  # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, pack_time)  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Запишите выбранное мотивирующее сообщение.
    # Вызовите функцию show_message().
    # Добавьте новый элемент в словарь storage_data.
    # Верните словарь storage_data.
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = data[1]
    return print(show_message(pack_time, day_steps, dist, spent_calories, achievement))


# Данные для самопроверки. Не удаляйте их.
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
