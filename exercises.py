#!/usr/bin/env python3
#연습문제
#연습문제 1 : 세가지 다른 리스트를 만들고 각리스트를 합쳐보자. 그다음 for문과 각 리스트를 반복할 위치 인덱스(range(len()))을 이용하여 화면에 리스트의 인덱스와 해당하는 값을 출력해 보자.

list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = ["가","나","다","라","마","바","사","아","자","차","카","타","파","하"]
list3 = ["A","B","C","D","E","F","G"]

list_sum = list1 + list2 + list3

for idx in range(len(list_sum)):
	print("{0}: {1}".format(idx, list_sum[idx]))


