import random

class MHKnapsack(object):
	si = []
	q = 0
	r = 0
	b = []

	def generate_superinc(self, size, bound):
		del self.si[:]
		acsum = 0

		for i in range(size):
			r = random.randint(acsum, acsum+bound)
			self.si.append(r)
			acsum += r

		return self.si

	def

ks = MHKnapsack()
print ks.generate_superinc(15, 10)

