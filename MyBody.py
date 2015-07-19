# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:03:00 2015

@author: heshenghuan
"""

import math

class MyBody:
    def __init__(self):
        self.VERSION = 0.0
        self.user = ''
        self.height = 0.0
        self.weight = []
        self.bmi = []
        self.date = []
        
    def read_data(self, path):
        file_handler = open(path, 'r')
        for line in file_handler.readlines():
            data = line.split()            
            self.date.append(data[0])
            self.weight.append(data[1])
            self.bmi.append(data[2])
        file_handler.close()
        
    def read_user_info(self, path):
        file_handler = open(path, 'r')
        line = file_handler.readline()
        self.user = line.split()[-1]
        line = file_handler.readline()
        self.height = line.split()[-1]