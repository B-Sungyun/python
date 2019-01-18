#!/usr/bin/env python3
#연습문제
#연습문제 1 : 세가지 다른 리스트를 만들고 각리스트를 합쳐보자. 그다음 for문과 각 리스트를 반복할 위치 인덱스(range(len()))을 이용하여 화면에 리스트의 인덱스와 해당하는 값을 출력해 보자.

list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = ["가","나","다","라","마","바","사","아","자","차","카","타","파","하"]
list3 = ["A","B","C","D","E","F","G"]

list_sum = list1 + list2 + list3

for idx in range(len(list_sum)):
	print("{0:d}: {1!s}".format(idx, list_sum[idx]))


#연습문제 2 : 동일한 길이를 가진 리스트 두개를 만든다. 이중 하나의 리스트에는 서로 고유한 문자열을 넣고, 빈 딕셔러니를 하나 추가로 만든다. 그다음 for문과 위치 인덱스, 그리고 고유한 문자열을 지닌 리스트의 각 값들이 이미 딕셔너리에 있는 키인지 확인하는 if문을 작성한다. 만약 딕셔너리에 없는 문자열이라면, 딕셔너리에 키를 저장하고 동일한 위치에 있는 다른 리스트의 값을 해당 키와 연관된 값으로 추가한다. 마지막으로 화면에 딕셔너리의 키아 각 연관된 값을 출력한다.

list_A = ["김치","스팸","삼겹살","고구마","계란","김치"]
list_B = ["계란","간장","고추장","우유","마요네즈","김"]
dict_a ={} 

for x in range(len(list_A)):
	if list_A[x] not in dict_a:
		dict_a[list_A[x]] = list_B[x]

for key,value in dict_a.items():
	print("{0!s}: {1!s}".format(key, value))

#연습문제 3 : 동일한 길이의 리스트들로 구성된 리스트를 하나 만든다. 각 리스트에 있는 값을 쉼표로 구분하되 마지막 값 뒤에는 개행문자를 붙여 화면에 출력해보자.
list_total = [[0,1,2],[3,4,5],[6,7,8]]
output = ''
for inner_list in list_total:
	max_index = len(inner_list)

	for idx in range(len(inner_list)):
		if idx < (max_index-1):
			output += str(inner_list[idx])+','
		else:
			output += str(inner_list[idx])+'\n'
print(output)

