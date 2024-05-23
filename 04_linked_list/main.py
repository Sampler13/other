from typing import Any, Optional


class Node:
    def __init__(self, name: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        self.name = name
        self.next = next_node

    def __str__(self) -> str:
        return f'Node {str(self.name)}'


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is None:
            return 'LinkedList []'
        else:
            current = self.head
            values = [str(current.name)]
            while current.next:
                current = current.next
                values.append(str(current.name))
            return '[' + ', '.join(values) + ']'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        if index < 0 or index >= self.length:
            raise IndexError('Index out of range')

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1

    def get(self, index: int) -> Optional[Any]:
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.name


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
