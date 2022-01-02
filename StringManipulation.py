def selfIntroduction():
	name = input("Your name: ")
	school = input("Your school: ")
	major = input("Your major: ")
	#method1
	print(f"My name is {name}. I study at {school}, and my major is {major}.")
	#method2
	print("My name is {}. I study at {}, and my major is {}.".format(name, school, major))
	#method3
	print("My name is " + name + ". I study at " + school + ", and my major is " + major + ".")

if __name__ == "__main__":
	selfIntroduction()
