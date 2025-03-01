#/usr/bin/env python3

"""Модуль организации стека и работы с ним.

В модуле есть 2 класса:
1. Node:
    - метод инициализации __init__
    
2. Stack:
    - метод инициализации __init__
    - метод push (добавляет элемент в стек)
    - метод pop (удаляет элемент из стека)
    - метод is_empty (проверяет, пустой стек или нет)
    - метод is_full (проверяет, заполнился стек целиком или нет)
    - метод clear_stack(очистка всего стека)
    - метод get_data (получаем нужные данные из стека)
    - метод size_stack (узнаем размер стека)
    - метод counter_int (считаем целые числа в стеке)
 
"""

class Node:
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack: 
    
    def __init__(self, stack_size=5, top=None):
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        while self.top:
            self.pop()

    def get_data(self, index):
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(2.5)
# stack.push("sta")
# print(stack.counter_int())
