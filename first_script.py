#!/usr/bin/env python3
from math import exp, log, sqrt

print("Output #1: I'm excited to learn Python.")

#두 수를 더한다.
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))
	#{0:d}에서 :는 변수의 표시 형식과 값을 분리한다. d는 십진수 숫자라는 의미

#두 리스트를 더한다.
a = [1,2,3,4]
b = ["first","second","third","fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a,b,c))

#정수
x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
	#숫자 3을 4제곱
print("Output #6: {0}".format((int(8.3)/int(2.7))))

#실수
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))

#math
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

#문자열
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))
print("Output #15: {0:s}".format('This is a long string. Without the backslash\
	it would run off of the page on the right in the text editor and be very\
	difficult to read and edit. By using the backslash you can split the long\
	string into smaller string on separate lines so that the whole string is easy\
	to view in the text editor.'))
print("Output #16: {0:s}".format('''You can use triple single quotes 
	for multi-line comment string.'''))
print("Output #17: {0:s}".format("""You can use triple double quotes 
	for multi-line comment string."""))

#문자열 연산
string1 = "This is a"
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is","very"*4,"beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))

#split
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
	#두번째 인수 수 만큼 나눈다. 2번만 나눔
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
	.format(string1_list2[0],string1_list2[1],string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[3],\
	string2_list[-1]))
	#-1은 마지막으로 돌아가는 듯

#join
print("Output #25: {0}".format(','.join(string2_list)))

#strip_공백
string3 = " Remove  unwanted characters  from this string.\t\t  \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))
#strip_문자
string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30:{0:s}".format(string4))
string4 = "$$This unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

#replace
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ","!@!")
print("Output #32: (with !@!):{0:s}".format(string5_replace))
string5_replace = string5.replace(" ",",")
print("Output #33: (with commas):{0:s}".format(string5_replace))

string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize"
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37: (on each word):")
for word in string5_list:
	print("{0:s}".format(word.capitalize()))