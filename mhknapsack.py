import random
from fractions import gcd

class MHKnapsack(object):
	w = []
	wsum = 0
	q = 0
	r = 0
	pk = []
	b = []

	def gen_superinc(self, size, bound):
		del self.w[:]
		self.wsum = 0

		for i in range(size):
			r = random.randint(self.wsum, self.wsum+bound)
			self.w.append(r)
			self.wsum += r

	def gen_q_and_r(self):
		#q > wsum & r ~ [1, q) and coprime to q -> gcd(r, q) == 1
		self.q = random.randint(self.wsum, self.wsum + 99999)

		self.r = random.randint(1, self.q)
		while gcd(self.r, self.q) != 1:
			self.r = random.randint(1, self.q)

	def gen_public_key(self):
		for wi in self.w:
			self.pk.append((self.r * wi) % self.q)

	def gen_message(self):
		m = []
		for i in range(len(self.w)):
			m.append(random.randint(0, 1))
		return m

	def gen_cryptogram(self, message):
		c = 0
		for i in range(len(message)):
			c += message[i] * self.pk[i]
		return c

	def bruteforce(self, cryptogram):
		m = []
		pk = self.pk
		print 'decomposing..'
		count = 0
		while (cryptogram > 0):
			nearest = 0
			for i in pk:
				if i <= cryptogram and i > nearest:
					nearest = i
			if nearest == 0:
				break

			d = cryptogram - nearest
			cryptogram = cryptogram - nearest
			count += 1
			if count % 100 == 0:
				print 'decomposed ' + str(count) + ' times..'

ks = MHKnapsack()
print 'generating w...'
ks.gen_superinc(10000, 10)
print 'generating q & r...'
ks.gen_q_and_r()
print 'generating public key...'
ks.gen_public_key()
message = ks.gen_message()
print 'generating cryptogram...'
cryptogram = ks.gen_cryptogram(message)
print 'trying to decrypt..'
dec = ks.bruteforce(cryptogram)
print 'decrypted.'
