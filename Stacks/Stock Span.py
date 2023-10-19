from Stack import Stack

def StockSpan(stocks):
	#First element will have a score of 1
	shadow_stack = Stack()
	shadow_stack.push(1)
	scores = [1]

	for i in range(1, len(stocks)):
		#Every score starts from 1
		current_score = 1
		prev = i-1
		while prev >= 0 and stocks[i] > stocks[prev]:
			#if the prev stock is smaller then add its stack to the current list 
			prev_score = shadow_stack.top()
			#get index of stock that was taller than prev stock
			prev -= prev_score
			shadow_stack.pop()
			#add total score
			current_score += prev_score

		#push current score to list, will be 1 if while loop does not run
		shadow_stack.push(current_score)
		scores.append(current_score)

	return scores

if __name__ == "__main__":
	print(StockSpan([100,60,10,20,10,40,70]))
