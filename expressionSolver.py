# make a mathematical expression solver which solves the given mathimatical 
# expression without checking the precedence

expression = raw_input("Enter a mathematical expression: ")
numerics = []
ops = ['+','-','*','/']
exp_ops = []
number = ""
found_op = False
for i in range(len(expression)):
	for j in range(len(ops)):
		if (expression[i] == ops[j]):
			numerics.append(int(number))
			number = ""

			exp_ops.append(expression[i])
			found_op =True
			continue
	if (found_op):
		found_op = False
		continue
	number += expression[i]
	if (i == (len(expression)-1)):
		numerics.append(int(number))

resultant = 0
for i in range(len(exp_ops)):
	if( i==0 ):
		if(exp_ops[i] == '+'):
			resultant += float(numerics[i]+numerics[i+1])
		elif(exp_ops[i] == '-'):
			resultant += float(numerics[i]-numerics[i+1])
		elif(exp_ops[i] == '*'):
			resultant += float(numerics[i]*numerics[i+1])
		elif(exp_ops[i] == '/'):
			resultant += float(numerics[i]/numerics[i+1])
	else:
		if(exp_ops[i] == '+'):
			resultant = float(resultant + numerics[i+1])
		elif(exp_ops[i] == '-'):
			resultant = float(resultant-numerics[i+1])
		elif(exp_ops[i] == '*'):
			resultant = float(resultant*numerics[i+1])
		elif(exp_ops[i] == '/'):
			resultant = float(resultant/numerics[i+1])

print("Numeric Values in the expression: ",numerics)
print("Operators Used in the expression: ",exp_ops)
print("Result without Precedence checking: "resultant)