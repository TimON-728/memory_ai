import json
import networkx as nx

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
    

def find_all_conn(query_obj, conn_gr, visited):
    try:
        with open('memory.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            obj_1_data = data.get(query_obj, {})

            if (query_obj in visited) or (not obj_1_data):
                return
            
            visited.add(query_obj)

            obj_1 = LogicalObject(query_obj, obj_1_data)

            for key, value in obj_1.connections.items():
                conn_gr.add_edge(obj_1.value, key, relation=value)

                find_all_conn(key, conn_gr, visited)

            return

    except FileNotFoundError:
        return "Ошибка: Файл memory.json не найден!"
    except json.JSONDecodeError:
        return "Ошибка: Файл поврежден и не является валидным JSON!"


def parser(query):
    if query[0] == '?':
        try:
            with open('memory.json', 'r', encoding='utf-8') as file:
                data = json.load(file) 
                
                conn_gr = nx.Graph()
                visited = set()

                find_all_conn(query[1], conn_gr, visited)

            if nx.has_path(conn_gr, source=query[1], target=query[2]):
                print("Путь существует!") 
                
                path = nx.shortest_path(conn_gr, source=query[1], target=query[2])
                relations = []
                strict_ops = ("<", ">", ">=", "<=")

                relations.append(path[0])
                for i in range(len(path)-1):
                    v = path[i]
                    u = path[i+1]
                    relations.append(conn_gr[u][v]['relation'])
                    relations.append(u)
                    print(relations)

                while len(relations) > 3:
                    if "==" in relations:
                        i = 0
                        while i < (len(relations)-1) and relations.count("==") > 1:
                            if relations[i] == "==":
                                relations.remove(relations[i])
                                relations.remove(relations[i])

                            i += 1
                    elif any(relations.count(op) >= 2 for op in strict_ops):
                        cnt_of_repeat = 0
                        for i in range(len(relations)-3):
                            if relations[i] == relations[i+2]:
                                relations.remove(relations[i])
                                relations.remove(relations[i])
                        if cnt_of_repeat == 0:
                            break
                    else:
                        break

                if len(relations) == 3:
                    print(relations[1])
                    add_to_memory(relations[0], relations[1], relations[2])
                else:
                    print("Не удалось найти точное отношение")
                    print(relations)

            else:
                print("Связи нет")
                    
        except FileNotFoundError:
            return "Ошибка: Файл memory.json не найден!"
        except json.JSONDecodeError:
            return "Ошибка: Файл поврежден и не является валидным JSON!"
        
