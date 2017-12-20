class Rule:
	EQU = 1
	IMPL = 2
	def __init__(self, op, left, right):
		self.op = op
		self.left = left
		self.right = right

	def __str__(self):
		if (self.op == Rule.EQU):
			return (self.left + " <=> " + self.right);
		elif (self.op == Rule.IMPL):
			return (self.left + " => " + self.right);
