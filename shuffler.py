#import random
import random

#get lines from theinput file
lines = open('input.txt').readlines()
#shuffle the lines
random.shuffle(lines)
#write the lines to the output file
open('output.txt', 'w').writelines(lines)
print("the songs have been shuffled!")