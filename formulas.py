from math import *
from scipy.integrate import quad as Int

def d_cos(number):
	return cos(number / 180 * pi)

e0 = 8.85e-12
ke = 8.99e9
elem = 1.6e-19

class PhysicalQuantity:
	def __init__(self,value = 0,unit = ''):
		self.value = value
		self.unit = unit

	def lonCapaNumber(number):
		return format(number, '.2e').replace("e-0", "e-").replace('e+0','e').replace('e0','')

	def __str__(self):
		return f'{Charge.lonCapaNumber(self.value)} {self.unit}'


class Electrostatics(PhysicalQuantity):
	def GaussLaw(Fl = None, q = None):
		if Fl is None:
			return solve(Flux,lambda q: q/e0,q)
		else:
			return solve(Charge,lambda Fl: Fl*e0,Fl)
class Charge(Electrostatics):

	def __init__(self,value = 0):
		self.value = value
		self.unit = 'C'

class ElectricField(Electrostatics):

	def __init__(self,value = 0):
		self.value = value
		self.unit = 'V/m'

	def definition(q1,r):
		return solve(ElectricField,lambda q1,r: ke * q1 / r**2, q1,r)

	def withinSphere(Q,R,r):
		return solve(ElectricField, lambda Q,R,r: ke*Q*r/R**3,Q,R,r)

	def lineCharge(r,lam):
		return solve(ElectricField,lambda r, lam: 2 * ke * lam / r,r,lam)
		
	def planeCharge(sigma):
		return solve(ElectricField,lambda sigma: sigma(2*e0),sigma)


class Flux(Electrostatics):

	def __init__(self,value = 0):
		self.value = value
		self.unit = 'N*m^2/C'

	def definition(E,A,theta = 0):
		return solve(Flux,lambda E, A, theta: E*A*d_cos(theta),E,A,theta)

def solve(quantity,formula,*arguments):
	solution = quantity(formula(*arguments))
	return str(solution)