import json
from logical_block import parser

def get_from_memory(query):
    try:
        with open('memory.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            result = list(query.split())
            
            print('Думаю...')
            parser(result)
                
    except FileNotFoundError:
        return "Ошибка: Файл memory.json не найден!"
    except json.JSONDecodeError:
        return "Ошибка: Файл поврежден и не является валидным JSON!"