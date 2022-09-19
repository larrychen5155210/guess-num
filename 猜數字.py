#猜數字(1~100)
import random

r = random.randint(1, 100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num > r:
		print('比', num, '小')
	elif num < r:
		print('比', num, '大')
	else:
		print('你終於猜對了!!')
		break