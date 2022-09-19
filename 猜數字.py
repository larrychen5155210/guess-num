#猜數字(隨機數字)
import random
import time

print("這是一個猜隨機數字的遊戲")
time.sleep(1) #程式暫停1秒
start = input('請決定隨機數字的起始值: ')
end = input('請決定隨機數字的結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
print('遊戲開始')
time.sleep(1)
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