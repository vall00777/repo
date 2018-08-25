mn = int(input('Enter minutes: '))
if mn >= 0 and mn <= 14:
	print('first quarter')
if mn >= 15 and mn <= 29:
	print('second quarter')
if mn >= 30 and mn <= 44:
	print('third quarter')
if mn >= 45 and mn <= 59:
	print('fourth quarter')
