def bin2dec(a):
	res = 0
	rang = len(a) - 1
	for i in range(len(a)):
		if a[i] == "1":
			res += 2 ** rang
		rang -= 1
	return res
print(bin2dec('101'))
print(bin2dec('110'))
print(bin2dec('110010101111'))