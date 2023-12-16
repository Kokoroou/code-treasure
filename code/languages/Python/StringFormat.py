test = "This is a test which have both ' and \" and I can have as much \" as I want, but now I want a bip like \a \a \a"
r = f'This {test}'
m = '{:*^20}\n{:@>15}'.format('love','not love')

Name = ["Trương Tuấn Anh", "Trương Tú Linh", "Lương Đức Dũng", "Lê Việt Hoàng"]
Age = [19, 15, 15, 15]

print("+{:-^20}+{:-^10}+".format("Name", "Age"))
for i in range(4):
	print("|{:-^20}|{:-^10}|".format("-","-"))
	print("|{:<20}|{:^10}|".format(Name[i], Age[i]))
print("+{:-^20}+{:-^10}+".format("-", "-"))

