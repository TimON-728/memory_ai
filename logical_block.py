import json

def add_to_memory(key, value, filename='memory.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[key] = value

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


'''class MyNumber:
    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        if not isinstance(other, MyNumber):
            other = MyNumber(other)
                
        result = self.value

        for _ in range(other.value):
            result += 1

        add_to_memory(f"{self.value} + {other.value}", result)
        return MyNumber(result)


    def __sub__(self, other):
        if not isinstance(other, MyNumber):
            other = MyNumber(other)
                
        result = self.value

        for _ in range(other.value):
            result -= 1

        add_to_memory(f"{self.value} - {other.value}", result)
        return MyNumber(result)        


    def __mul__(self, other):
        if not isinstance(other, MyNumber):
            other = MyNumber(other)
        
        result = 0

        for _ in range(other.value):
            result += self.value

        add_to_memory(f"{self.value} * {other.value}", result)
        return MyNumber(result)    


    def __truediv__(self, other):
        if not isinstance(other, MyNumber):
            other = MyNumber(other)

        negative = False
        if self.value < 0:
            self.value = abs(self.value)
            negative = True

        if other.value < 0:
            other.value = abs(other.value)
            negative = True
        
        integer_part = self.value

        int_result = ""
        float_result = ""
        cnt = 0

        while integer_part >= other.value:
            integer_part -= other.value
            cnt += 1

        int_result += str(cnt)

        for _ in range(5): 
            if integer_part == 0:
                break
            
            integer_part *= 10
            cnt = 0
            
            while integer_part >= other.value:
                integer_part -= other.value
                cnt += 1
            
            float_result += str(cnt)


        if float_result:
            result = f"{int_result},{float_result}"
        else:
            result = f"{int_result}"

        if negative:
            result = -result

        add_to_memory(f"{self.value} / {other.value}", result)
        return MyNumber(result) 
    

    def __repr__(self):
        return str(self.value)


def parser(row_data):
    query = row_data.split()

    a = MyNumber(int(query[0]))
    b = MyNumber(int(query[2]))
    if query[1] == '+':
        return(a + b)
    elif query[1] == '-':
        return(a - b)
    elif query[1] == '*':
        return(a * b)
    elif query[1] == '/':
        return(a / b)'''


