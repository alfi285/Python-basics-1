#The sub() function

#The sub function replaces  the matches with the text of your choice

#Replace every white spaces character with the number 9

import re
txt = "The rain in Spain"
x = re.sub("\s","9", txt)
print(x)


y = re.sub("\s","9", txt,2)
print(y)
#REplaces with 9 from first 2 occurences