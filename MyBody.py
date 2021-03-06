# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 19:03:00 2015

@author: heshenghuan
"""

import matplotlib.pyplot as pl
import getopt
import sys
import datetime

class MyBody:
    def __init__(self):
        self.VERSION = 0.0
        self.VERSION_DATE = "2015-07-21"
        self.user = ''
        self.height = 0.0
        self.weight = []
        self.bmi = []
        self.date = []
        self.read_user_info(r"../userinfo/user.txt")
        
    def print_user_info(self):
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
        
    def print_help(self):
        print "MyBody personal weight supervisory program.",
        print "ver",self.VERSION,self.VERSION_DATE
        print "@author: heshenghuan"
        print "usage: python MyBody.py options"
        print "options: -h           ->help"
        print "         -a float     ->add weight record"
        print "         -s           ->show the picture of weight change"
        print "         -d           ->delete the last record"
        print "         -p           ->print all the record"
        
    def get_arg(self, arg):
        error = False
        try:
            options,args = getopt.getopt(arg,"ha:sdp")
        except getopt.GetoptError:
            error = True
        
        if not error:
            for name, value in options:
                if name in ('-h', '--help'):
                    self.print_help()
                if name in ('-a'):
                    bmi = self.add_record(value)
                    self.bmi_analysis(bmi)
                if name in ('-s'):
                    self.show()
                if name in ('-d'):
                    self.del_record()
                if name in ('-p'):
                    self.print_record()
        else:
            #argument error, display help information
            print "Argument Error!"
            self.print_help()
            
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
        output.close()
        print "Add a record:",date,weight,bmi
        return float(bmi)
    
    def del_record(self):
        self.read_data(r"../userinfo/weights.txt")
        self.date.__delitem__(-1)
        self.weight.__delitem__(-1)
        self.bmi.__delitem__(-1)
        output = open(r"../userinfo/weights.txt","w")
        for i in range(len(self.date)):
            if i > 0:
                output.write('\n')
            output.write(self.date[i])
            output.write(' ')
            output.write("%.2f"%self.weight[i])
            output.write(' ')
            output.write("%.4f"%self.bmi[i])
        output.close()
        print "Deleted the last record."
    
    def print_record(self):
        self.read_data(r"../userinfo/weights.txt")
        print "date:         weight:   bmi:"
        #print "2015-07-30    75.77     25.2222"
        for i in range(len(self.date)):
            print self.date[i], "  ","%.2f"%(self.weight[i]), '   ',"%.4f"%(self.bmi[i])
        
        #calculate average weights for last 7 or less days
        aver_weights = 0.0
        w_sum = 0.0
        aver_bmi = 0.0
        b_sum = 0.0
        if len(self.date) > 7:
            for i in range(-7,0):
                w_sum += self.weight[i]
                b_sum += self.bmi[i]
            aver_weights = w_sum/7
            aver_bmi = b_sum/7
        else:
            for i in range(len(self.date)):
                w_sum += self.weight[i]
                b_sum += self.bmi[i]
            aver_weights = w_sum/len(self.date)
            aver_bmi = b_sum/len(self.date)
        print "\naverage weights for last 7 days: %.2f"%aver_weights,"kg"
        print "average BMI for last 7 days: %.4f"%aver_bmi
        self.bmi_analysis(aver_bmi)
    def bmi_analysis(self, bmi):
        if bmi<18.5:
            print "Underweight"
            print "You are underweight. Eat more, it\'s okay."
        if bmi>=18.5 and bmi<24.99:
            print "Normal"
            print "Your weight is normal."
        if bmi>=24.99 and bmi<28:
            print "Overweight"
            print "You are overweight. Please take more exercise"
            print "and pay attention to your diet."
        if bmi>=28 and bmi<32:
            print "Fat"
            print "You are obese. You need to lose weight."
        if bmi>32:
            print "Obese"
            print "You are very fat. You need doctor."
            
    def show(self):
        self.read_data(r"../userinfo/weights.txt")
        x = range(len(self.date))
        ax1 = pl.subplot(2,1,1)
        ax2 = pl.subplot(2,1,2)
        pl.sca(ax1)
        pl.plot(x,self.weight,'r*')
        pl.plot(x,self.weight,'b')
        pl.xticks(x,self.date)
        pl.xlabel("date")
        pl.ylabel("weight/kg")
        pl.ylim(50,80)
        pl.title("weight change line chart",loc="right")
        pl.sca(ax2)
        pl.plot(x,self.bmi,'r*')
        pl.plot(x,self.bmi,'b')
        pl.xticks(x,self.date)
        pl.xlabel("date")
        pl.ylabel("BMI")
        pl.ylim(15,40)
        pl.title("BMI change line chart",loc="right")
        pl.legend()
        pl.show()
        
if __name__ == "__main__":
    case = MyBody()
    case.get_arg(sys.argv[1:])