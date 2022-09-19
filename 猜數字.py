#猜數字(1~100)
import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請輸入數字: ')
	num = int(num)
	if num > r:
		print('比', num, '小')
	elif num < r:
		print('比', num, '大')
	else:
		print('你終於猜對了!!')
		break
	print('這是你猜的第', count, '次')
print('你總共猜了', count, '次')