list = [1,0,1,1,1,1,1,1,1,0,0,0,1]
#longest sequence of 1

def longest_sequence(list):
    count=0
    max_count=0
    for i in list:
        if i==1:
            count+=1
            if count>max_count:
                max_count=count
        else:    
            count=0
    return max_count

print("longest sequence of 1:",longest_sequence(list))

import re  
outputstring=""  
string="I am a 'Developer'"


#print the string inside single quotes

outputstring=re.findall(r"'(.*?)'",string)
finalstring=re.sub(r"'(.*?)'","'",outputstring[0])
print(finalstring)

#output string: Developer

    
sting2="aabbbcd"

def count_char(string):
    count=1
    output=""
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1
        else:
            output=output+str(count)+string[i]
            count=1
    output=output+str(count)+string[i+1]
    return output

print("output string:",count_char(sting2))

#output string: 2a3b1c1d








#even and odd numer 1 to 100 using classes and functions

class NumberClassifier:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_odd(self):
        return not self.is_even()

def classify_number(number):
    classifier = NumberClassifier(number)
    if classifier.is_even():
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Example usage:
for i in range(1, 100):
    print(classify_number(i))


