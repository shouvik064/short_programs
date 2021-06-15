def anagram(str1,str2):
  str1=str1.lower()
  str2=str2.lower()

  if string1 != None and string2 != None:
    if (len(str1) == len(str2)):
      sorted_str1 = sorted(str1)
      sorted_str2 = sorted(str2)

      if sorted_str1 == sorted_str2:
        return True
      else:
        return False
    else:
      return False
  else:
    return False

str1 = input("Enter first word: ")
str2 = input("Enter second word: ")
print(anagram(str1,str2))