def computepay(h, r):
	if h <= 40:
		a= h*r
		return a
	else:
		regularpay= 40 * rate
		overtime= hrs- 40
		rt= overtime*(rate*1.5)
		pay= rt + regularpay
		return pay
hrs = float(input("Enter Hours:"))
rate= float(input('Valor por hora'))
p = computepay(hrs, rate)
print("Pay", p)