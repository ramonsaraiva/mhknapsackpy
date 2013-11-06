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
				if i <= cryptogram and i > nearest:
					nearest = i
			if nearest == 0:
				break

			d = cryptogram - nearest
			cryptogram = cryptogram - nearest

ks = MHKnapsack()
print 'generating w...'
ks.generate_superinc(9999, 10)
print 'generating q & r...'
ks.generate_q_and_r()
print 'generating public key...'
ks.generate_public_key()
message = ks.generate_message()
print 'generating cryptogram...'
cryptogram = ks.generate_cryptogram(message)
print 'trying to decrypt..'
dec = ks.try_decrypt(cryptogram)
print 'decrypted.'
print 'dec: '
print dec
