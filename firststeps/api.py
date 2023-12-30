from __future__ import annotations

def plus(a: int, b: int) -> int:
	return a + b

class ComplexNumber:
	def __init__(self, real: int, imag: int):
		self.real = real
		self.imag = imag
	
	def plus(self, cn: ComplexNumber):
		self.real += cn.real
		self.imag += cn.imag
	
	def __str__(self) -> str:
		return f'({self.real}, {self.imag})'