
Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~
print('Q1) Do you like Dawn or Dusk?')

print(' 1) Dawn')
print(' 2) Dusk')

answer = int(input("Enter answer (1-2): "))

if answer == 1:
    Gryffindor +=1
    Ravenclaw +=1

elif answer == 2:
    Hufflepuff +=1
    Slytherin +=1

else:
    print("Wrong input")

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  Hufflepuff += 1
elif answer == 2:
  Slytherin +=1
elif answer == 3:
  Ravenclaw +=1
elif answer == 4:
  Gryffindor +=1
else:
  print('Wrong input.')
    
# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~
    
print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  Slytherin +=1
elif answer == 2:
  Hufflepuff +=1
elif answer == 3:
  Ravenclaw +=1
elif answer == 4:
  Gryffindor +=1
else:
  print('Wrong input.')
  
print(Gryffindor)
print(Ravenclaw)
print(Hufflepuff)
print(Slytherin)


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
