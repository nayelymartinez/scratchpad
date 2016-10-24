# Author: Nayely E Martinez (nayely.e.martinez@gmail.com)
# Date: 10/23/16
# Desc: Demo code demonsratining polymorphism (subtyping).

class Planet(object):
	def habitable():
		raise NotImplementedError

	def numMoons():
		raise NotImplementedError

class Earth(Planet):
	def habitable():
		print("Habitable")

	def numMooons():
		return 1



