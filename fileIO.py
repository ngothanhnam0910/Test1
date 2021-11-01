# file = open("data.txt", "a")

# # "w" writting
# # "r" reading
# # "a" writting append # KO Xóa file cũ đi mà thêm vào cuối file
# file.write("cc \n")
# file.write("dd ")

# Đọc file
# file = open("data.txt", "r")

# data = file.read()
# print(data)

# write mode - write to a new file
with open("data.txt", "w") as file:
	file.write("Nam Ngo \n")
	file.write("Nam ngo Nam ngo ")

# write mode - write to a new file
with open("data.txt","w") as file:
	file.write("a \n")
	file.write("b \n")

# Append mode - write to a new file
with open("data.txt","a") as file:
	file.write("c \n") 
	file.write("d \n")
	file.write("e ")

# Đọc file
with open("data.txt","r") as file:
	data = file.read()
	print(data)
