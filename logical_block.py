import json

def add_to_memory(key, conn, value, filename='memory.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[key][value] = conn

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


class LogicalObject:
    def __init__(self, value, connections):
        self.value = value
        self.connections = {}
        for key, value_1 in connections.items():
            self.connections[key] = value_1
    


def parser(query):
    if query[0] == '?':
        try:
            with open('memory.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                obj1_data = data.get(query[1], {})
                obj2_data = data.get(query[2], {})

                obj1 = LogicalObject(query[1], obj1_data)
                obj2 = LogicalObject(query[2], obj2_data)

                conn_1_to_2 = obj1.connections.get(obj2.value)
                conn_2_to_1 = obj2.connections.get(obj1.value)

                if conn_1_to_2:
                    print(f'{obj1.value} {conn_1_to_2} {obj2.value}')
                    add_to_memory(obj2.value, conn_1_to_2, obj1.value)
                elif conn_2_to_1:
                    print(f'{obj2.value} {conn_2_to_1} {obj1.value}')
                    add_to_memory(obj1.value, conn_2_to_1, obj2.value)
                else:
                    print(f'Связи между {obj1.value} и {obj2.value} нет.')
                    
        except FileNotFoundError:
            return "Ошибка: Файл memory.json не найден!"
        except json.JSONDecodeError:
            return "Ошибка: Файл поврежден и не является валидным JSON!"
        