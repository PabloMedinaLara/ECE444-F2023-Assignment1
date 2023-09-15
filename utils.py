class utils:
	def reversed(x):
		if x == int(x):
			reverse = int(str(x)[::-1])
		else:
			reverse = None
		return reverse
	def formatter(x):
		if x == int(x):
			return bin(x), oct(x)
		else:
			return None
