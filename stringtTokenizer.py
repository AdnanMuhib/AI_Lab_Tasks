## make your string tokenizer 
# user should input a string , then input the token
# split the string on the basis of token and display the splitted words on the basis of token
string1 = raw_input("Enter a string: ")
string1 = str(string1)
token = raw_input("Enter token: ")
arr = []
temp = ""
for i in range(len(string1)):
	if not(string1[i] == token):
		temp += string1[i]
		if (i == (len(string1)-1)):
			arr.append(temp)		
		continue
	arr.append(temp)
	temp = ""
print(arr)