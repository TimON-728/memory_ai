import json
from logical_block import parser

def get_from_memory(query):
    try:
        with open('memory.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            result = data.get(query)
            
            if result is not None:
                return result
            else:
                print('Не знаю, сейчас подумаю')
                return parser(query)
                
    except FileNotFoundError:
        return "Ошибка: Файл memory.json не найден!"
    except json.JSONDecodeError:
        return "Ошибка: Файл поврежден и не является валидным JSON!"