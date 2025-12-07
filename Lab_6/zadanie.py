import xml.etree.ElementTree as ET

def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'name': workout_elem.find('name').text,
                'age': int(workout_elem.find('age').text),
                'weight': int(workout_elem.find('weight').text),
                'fitness_level': workout_elem.find('fitness_level').text,
                'workouts': []
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []
