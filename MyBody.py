# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:03:00 2015

@author: heshenghuan
"""

import math
import getopt
import sys
import datetime

class MyBody:
    def __init__(self):
        self.VERSION = 0.0
        self.user = ''
        self.height = 0.0
        self.weight = []
        self.bmi = []
        self.date = []
        
        self.read_user_info(r"../userinfo/user.txt")
        print "MyBody ver", self.VERSION,
        print "personal weight supervisory program.",
        print "@author: heshenghuan 2015"
        print "-"*79
        print "User's information:"
        print "User:", self.user
        print "Height(m):", self.height
        
    def read_data(self, path):
        file_handler = open(path, 'r')
        for line in file_handler.readlines():
            data = line.split()            
            self.date.append(data[0])
            self.weight.append(float(data[1]))
            self.bmi.append(float(data[2]))
        file_handler.close()
        
    def read_user_info(self, path):
        file_handler = open(path, 'r')
        line = file_handler.readline()
        self.user = line.split()[-1]
        line = file_handler.readline()
        self.height = float(line.split()[-1])
        
    def get_arg(self, arg):
        try:
            options,args = getopt.getopt(arg,"ha:",["help"])
        except getopt.GetoptError:
            print "argument error"
        
        for name, value in options:
            if name in ('-h', '--help'):
                print "help info"
            if name in ('-a'):
                self.add_record(value)
    
    def add_record(self, weight):
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        output = open(r"../userinfo/weights.txt","a")
        output.write("\n")
        output.write(date)
        output.write(' ')
        weight = "%.2f"%float(weight)
        bmi = "%.4f"%(float(weight)/(self.height*self.height))
        output.write(weight)
        output.write(' ')
        output.write(str(bmi))
        output.write(' ')
        output.close()
        print "Add a record:",date,weight,bmi
        
if __name__ == "__main__":
    case = MyBody()
    case.get_arg(sys.argv[1:])