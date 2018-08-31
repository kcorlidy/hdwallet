from mnemonic import Mnemonic as mc
from bip32utils import BIP32Key
from binascii import unhexlify,hexlify
import sys

class key(object):
	def __init__(self,m):
		self.version = "ver1.0"
		self.m = m

	def b2h(self,b):
		h = hexlify(b)
		return h if sys.version < '3' else h.decode('utf8')

	@staticmethod
	def gen_seed(data,lang="english"):
		data = data if type(data) == bytes else bytes(data,"utf8")
		m = key(m = mc(lang).to_mnemonic(unhexlify(data)))
		return m

	@staticmethod
	def gen_mnen(strength):
		#gen_mnemonic
		m = key(m = mc(lang).generate(strength))
		return m

	def root_key(self,passphrase=""):
		seed = mc.to_seed(self.m, passphrase=passphrase)
		xprv = BIP32Key.fromEntropy(seed).ExtendedKey() 
		xpub = BIP32Key.fromEntropy(seed).ExtendedKey(private=False) 
		return xprv,xpub

	def cointype(self):
		return None


def main():
	print(key.gen_seed(data="a9495fe923ce601f4394c8a7adadabc3").root_key())

if __name__ == '__main__':
	main()