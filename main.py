name=input("Enter your name :")
print ("your welcomr ",name)
def displayMenu():
  print ("1. Add Matrices\n" +
         "2. Check Rotation\n" +
         "3. Invert Dictionary\n" +
        "4. Convert Matrix to Dictionary\n" +
         "5. Check Palindrome\n" +
         "6. Search for an Element & Merge Sort\n" +
         "7. Exit\n")

def AddMatrices():

  num_row1=int(input("Enter number of rows :"))
  num_co1l=int(input("enter number of columns :"))

  first_matrix= []
  second_matrix= []
  sum_matrix= []
  
  for row in range (num_row1):
    r = []
    for col in range (num_co1l):
      r.append(int(input("Enter element of first matrix :")))
    first_matrix.append(r)

  for row in range (num_row1):
    r = []
    for col in range (num_co1l):
      r.append(int(input("Enter element of second metrix:")))
    second_matrix.append(r)

  for i in range (len(first_matrix)):
    r = []
    for j in range (len(first_matrix[0])):
      r.append(first_matrix[i][j] + second_matrix[i][j])
    sum_matrix.append(r) 

  print (sum_matrix)
def CheckRotation():
  print ("Check Rotation")
  
def InvertDictionary():
  print ("Invert Dictionary")
  
def ConvertMatrixToDictionary():
  print ("Convert Matrix to Dictionary")
  
def CheckPalindrome():
  print ("Check Palindrome")
  
def SearchForElementAndMergeSort():
  print ("Search for an Element & Merge Sort")
  
def Exit():
  exit(1)
  

def choice ():
  displayMenu()
  choc = eval (input ("enter your choice from 1 to 7 :"))
  if choc == 1:
    AddMatrices()
  elif choc == 2:
    CheckRotation()
  elif choc == 3:
    InvertDictionary()
  elif choc == 4:
    ConvertMatrixToDictionary()
  elif choc == 5:
    CheckPalindrome()
  elif choc == 6:
    SearchForElementAndMergeSort()
  elif choc == 7:
    Exit()
  else:
    print ("invalid choice")
    choice()
  
choice()
  