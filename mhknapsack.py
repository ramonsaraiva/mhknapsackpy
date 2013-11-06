import random

class MHKnapsack(object):
	w = []
	wsum = 0
	q = 0
	r = 0
	b = []

	def generate_superinc(self, size, bound):
		del self.w[:]
		self.wsum = 0

		for i in range(size):
			r = random.randint(self.wsum, self.wsum+bound)
			self.w.append(r)
			self.wsum += r

ks = MHKnapsack()
ks.generate_superinc(15, 10)
print ks.w
print ks.wsum

