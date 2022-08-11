x=1
while x!="yes" or x!="no":
    x=input("Do you want a new password? ")
    if x!="yes" or x!="no":
        print("Your awnser should be yess or no")
    if x=="no":
        print()
    if x=="yess":
        import random
        uppercaseletter1=chr(random.randint(65,90))
        uppercaseletter2=chr(random.randint(64,90))
        lowercaseletter1=chr(random.randint(97,122))
        lowercaseletter2=chr(random.randint(97,122))
        digit1=chr(random.randint(48,57))
        digit2=chr(random.randint(48,57))
        punctiation1=chr(random.randint(32,152))
        punctiation2=chr(random.randint(32,152))
        print("Your new passaword is "+uppercaseletter1+uppercaseletter2+lowercaseletter1+lowercaseletter2+digit1+digit2+punctiation1+punctiation2)
