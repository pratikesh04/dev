class Op:
    def sum(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2


class MulOp(Op):
    def mul(self, n1, n2, n3):
        return n1 * n2 *n3

    def sum(self, n1, n2, n3):
        return n1 + n2 + n3

    def div(self, n1, n2):
        return n2/n1

def main():
	n1 = int(input("Enter 1st number"))
	n2 = int(input("Enter 2nd number"))
	n3 = int(input("Enter 3rd number"))
	x = Op()
	y = MulOp()
	print("sum from 1st method sum:",x.sum(n1,n2))
	print("sum from overloaded method sum:",y.sum(n1,n2,n3))
	print("Multiplication from 1st method Mul:",x.mul(n1,n2))
	print("Multiplication from overloaded method Mul:",y.mul(n1,n2,n3))
	print("Divison from method Div:",y.div(n1,n2))

if __name__ == '__main__':main()
	