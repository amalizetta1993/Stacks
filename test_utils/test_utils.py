import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from Stack import *

class TestNode(unittest.TestCase):
   
    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.next_node, node_1)
        self.assertEqual(node_2.next_node.data, 5)

class TestStack(unittest.TestCase):
    
    stack = Stack()
    
    def test1_init(self):
        self.assertEqual(self.stack.stack_size, 5)
        self.assertEqual(self.stack.top, None)
        
    def test2_push(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')
        self.stack.push('test_data')
        self.stack.push('test_data')
        self.stack.push('test_data')
        self.stack.push('test_data')
        self.assertEqual(self.stack.push('test_data'), "Стэк переполнен")
        self.stack.clear_stack()
        
    def test3_pop(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.pop(), "Стэк пуст")
        
    def test4_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push('test_data')
        self.assertEqual(self.stack.is_empty(), False)        
        self.stack.clear_stack()
                
    def test5_is_full(self):
        self.assertEqual(self.stack.is_full(), False)
        for _ in range(self.stack.stack_size):
            self.stack.push('test_data')
        self.assertEqual(self.stack.is_full(), True)           
        self.stack.clear_stack()
                
    def test6_clear_stack(self):
        for _ in range(self.stack.stack_size):
            self.stack.push('test_data')
        self.stack.clear_stack()
        self.assertEqual(self.stack.is_empty(), True)         
        
    def test7_get_data(self):
        self.stack.push('test_data')
        self.stack.push('test_data1')
        self.stack.push('test_data3')
        self.assertEqual(self.stack.get_data(0), 'test_data3')
        self.assertEqual(self.stack.get_data(4), "Out of range")       
        self.stack.clear_stack()
        
    def test8_size_stack(self):
        self.stack.push('test_data')
        self.stack.push('test_data1')
        self.stack.push('test_data3')
        self.assertEqual(self.stack.size_stack(), 3)
        self.stack.clear_stack()         
        self.assertEqual(self.stack.size_stack(), 0)
        
    def counter_int(self):
        self.stack.push(3)
        self.stack.push('test_data1')
        self.stack.push(1.5)
        self.stack.push('1')
        self.assertEqual(self.stack.counter_int(), 1)
        self.stack.clear_stack()         

        


