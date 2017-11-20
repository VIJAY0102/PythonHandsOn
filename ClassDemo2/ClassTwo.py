from ClassOne import ClassOne


class ClassTwo:

	def main(self, arg1, arg2):
		return ClassOne().fun(arg1, arg2)


if __name__ == '__main__':
	print(ClassTwo().main(2,4))
