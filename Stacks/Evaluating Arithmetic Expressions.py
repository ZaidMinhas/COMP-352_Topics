from Stack import Stack


def sort_expression(expression):
	num = ""
	sort_list = []
	expression =expression.replace(" ", "")
	for i in expression:
		if (i == "." or i.isdigit()):
			num += i
		else:
			if len(num) != 0:
				sort_list.append(float(num))
			num = ""
			sort_list.append(i)

	sort_list.append(float(num))
	return sort_list


def eval_exp(expression):
	def run(top = 10):
		while number_stack.size() > 1 and getPriority(operator_stack.top()) <= top:
			y = number_stack.pop()
			x = number_stack.pop()
					
			f = getFunc(operator_stack.pop())
			number_stack.push(f(x,y))

	operator_stack = Stack()
	number_stack = Stack()
	operator = {
		   "^" : (1, lambda x,y : x**y),
		   "*" : (2, lambda x,y : x*y),
		   "/" : (2, lambda x,y : x/y),
		   "+" : (3, lambda x,y : x+y),
		   "-" : (3, lambda x,y : x-y),
		   "=" : (4,lambda x, y : x==y),
		   "<" : (4,lambda x, y : x<y),
		   ">" : (4,lambda x, y : x>y),
		}

	getPriority = lambda sym: operator[sym][0]
	getFunc = lambda sym: operator[sym][1]

	expr_list = sort_expression(expression)
	

	
	for token in range(len(expr_list)):
		#If number
		if (token %2 == 0):
			number_stack.push(expr_list[token])
			

		#If operator
		else:
			if (operator_stack.isEmpty() or (getPriority(operator_stack.top()) > getPriority(expr_list[token])) ):
				operator_stack.push(expr_list[token])
			else:
				run(getPriority(expr_list[token]))
				operator_stack.push(expr_list[token])
	
	run()
	
	return number_stack.pop()


if __name__ == "__main__":
	print("Arithmetic test:")
	print(eval_exp("2+4+2"))
	print(eval_exp("7*3/4/5"))
	print(eval_exp("1+2/3+4"))
	print(eval_exp("1-4/ 2 / 9"))
	print(eval_exp("1.01^10"))

	print("\nComparison test:")
	print(eval_exp("10-1 = 19"))
	print(eval_exp("12/2 < 32/4"))
	print(eval_exp("0.99^10 > 2"))