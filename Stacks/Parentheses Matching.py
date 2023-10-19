from Stack import Stack

def Bracket(open, close, string):
	#Initiate the stack that will take in open brackets
	open_stack = Stack()

	#Combine both bracket lists
	tokens = open + close
	n = len(open)

	for i in string:

		#If character is not a bracket, then ignore it and go to next character
		try:
			score = tokens.index(i)
		except ValueError:
			continue

		#Check if open bracket
		if  score < n:
			#Add bracket to stack
			open_stack.push(score)
		else:
			#if stack is empty and there is a closed bracket, then there is no open bracket to close it
			if (open_stack.size() == 0):
				return False

			#if difference of index is equal to n then correct pair
			if (score - open_stack.top() == n):
				open_stack.pop()
			else:
				return False

	#if stack still has open brackets then need more closed brackets
	return open_stack.isEmpty()
			


if __name__ == "__main__":
	open_brackets = ["{", "[", "(", "<"]
	close_brackets = ["}", "]", ")", ">"]
	
	print(Bracket(open_brackets, close_brackets, "( )(( )){([( )])}"))
	print(Bracket(open_brackets, close_brackets, "((( )(( )){([( )])}"))
	print(Bracket(open_brackets, close_brackets, ")(( )){([( )])}"))
	print(Bracket(open_brackets, close_brackets, "({[ ])}"))
	print(Bracket(open_brackets, close_brackets, "("))
