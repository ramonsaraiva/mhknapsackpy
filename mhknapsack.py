import random
from fractions import gcd

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

	def generate_q_and_r(self):
		#q > wsum & r ~ [1, q) and coprime to q -> gcd(r, q) == 1
		self.q = random.randint(self.wsum, self.wsum + 99999)

		self.r = random.randint(1, self.q)
		while gcd(self.r, self.q) != 1:
			self.r = random.randint(1, self.q)

ks = MHKnapsack()
print 'generating w...'
ks.generate_superinc(15, 10)
print 'w: '
print ks.w
print 'wsum: ' + str(ks.wsum)
print 'generating q & r...'
ks.generate_q_and_r()
print 'q: ' + str(ks.q)
print 'r: ' + str(ks.r)
