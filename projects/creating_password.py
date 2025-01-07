import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=['1','2','3','4','5','6','7','8','9','0']

n_letters=int(input("Enter the number of letters: \n"))
n_symbols=int(input("Enter the number of symbols: \n"))
n_numbers=int(input("Enter the number of numbers: \n"))

password=""

for i in range(1,n_letters+1):
      password+=random.choice(letters)

for i in range(1,n_symbols+1):
    password+=random.choice(symbols)
    
for i in range(1,n_numbers+1):
    password+=random.choice(numbers)
    
print(password)