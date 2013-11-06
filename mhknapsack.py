import random
from fractions import gcd

class MHKnapsack(object):
	w = []
	wsum = 0
	q = 0
	r = 0
	pk = []
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

	def generate_public_key(self):
		for wi in self.w:
			self.pk.append((self.r * wi) % self.q)

	def generate_message(self):
		m = []
		for i in range(len(self.w)):
			m.append(random.randint(0, 1))
		return m

	def generate_cryptogram(self, message):
		c = 0
		for i in range(len(message)):
			c += message[i] * self.pk[i]
		return c

	def try_decrypt(self, cryptogram):
		m = []
		pk = self.pk
		while (cryptogram > 0):
			nearest = 0
			for i in pk:
				print 'i: ' + str(i)
				if i <= cryptogram and i > nearest:
					nearest = i
					print 'nearest: ' + str(nearest)
			idx = self.pk.index(nearest)
			pk.remove(nearest)
			d = cryptogram - nearest
			print 'd: ' + str(d)
			cryptogram = cryptogram - nearest
			print 'cryptogram now: ' + str(cryptogram)
			m.append(idx)
		return m

ks = MHKnapsack()
print 'generating w...'
ks.generate_superinc(4, 10)
print 'w: '
print ks.w
print 'wsum: ' + str(ks.wsum)
print 'generating q & r...'
ks.generate_q_and_r()
print 'q: ' + str(ks.q)
print 'r: ' + str(ks.r)
print 'generating public key...'
ks.generate_public_key()
print 'public key:'
print ks.pk
message = ks.generate_message()
print 'message: '
print message
cryptogram = ks.generate_cryptogram(message)
print 'cryptogram: '
print cryptogram
print 'trying to decrypt..'
dec = ks.try_decrypt(cryptogram)
print 'dec: '
print dec
