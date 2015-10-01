#!/usr/bin/env python2

def answer(str):
	postfix=[]	# postfix form of input (output)
	opstack=[]	# stack to hold operators
	# go token by token through infix input
	for token in str:
		if token in "0123456789":						# if the current token is an integer 0-9
			postfix.append(token)						# 	just append it to the output list
		elif token == "+" :							# if the current token is an addition operator (low precendence)...
			if len(opstack) > 0:						# 	if the stack has elements already...
				for op in reversed(opstack):				#		iterate through the stack (reverse b/c last elem = top of stack)
					if op == "*":					#			if the operator is multiplication (high prec.)
						postfix.append(opstack.pop())		#				pop the operator and append it to the output list
					else:						#		else (if a lower precendence oper is encounter (so another "+"))....stop popping
						break
				opstack.append(token)					# 			finally, append our "+" operator
			else:								#	if the top of the stack has low precedence than token (but in this case just a "+")
				opstack.append(token)					#		append the "+" to the stack
		elif token == "*":							# Multiplication operators have higher precedence than addition...so just push it to the stack
			opstack.append(token)
	# input, str, iteration complete...
	# now add any operators left on the stack to the output list
	while len(opstack) > 0:
		postfix.append(opstack.pop())
	# return our postfix notation by "joining" our postfix output list to a single string
	return "".join(postfix)

print answer("2*4*3+9*3+5")