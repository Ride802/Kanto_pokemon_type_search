# linked list

from node import Node

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head_node = Node(value)
        else:
            self.head_node = None  # Handle empty list case

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            value = current_node.get_value()
            if value is not None:  # Skip None values
                string_list += str(value) + "\n"
            schadule = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node is None:
            return
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            return
        while current_node and current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                return
            current_node = current_node.get_next_node()