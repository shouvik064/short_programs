class Engine():
  def validationCheck(row,col):
    rowDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    colList = ['1','2','3','4','5','6','7','8']
    if row in rowDict:
      row1 = rowDict[row]
      if str(col) in colList:
        col1 = int(col)
      else:
        row1 = col1 = 0
        print("Chose wrong option. Please try again!")
    else:
      row1 = col1 = 0
      print("Chose wrong option. Please try again!")
    return row1,col1

  def bishop(cur_pos_x,cur_pos_y,next_pos_x,next_pos_y):
    if abs(cur_pos_x - next_pos_x) == abs(cur_pos_y - next_pos_y):
      return True
    else:
      return False

  def knight(cur_pos_x,cur_pos_y,next_pos_x,next_pos_y):
    if (next_pos_x == cur_pos_x + 1 or next_pos_x == cur_pos_x - 1) and (next_pos_y == cur_pos_y - 2 or next_pos_y == cur_pos_y + 2):
      return True
    elif (next_pos_y == cur_pos_y + 1 or next_pos_y == cur_pos_y - 1) and (next_pos_x == cur_pos_x - 2 or next_pos_x == cur_pos_x + 2):
      return True
    else:
      return False
    
  piece = str(input("Choose between bishop or knight: "))
  currentpos = str(input("Choose current position between a1 or h8: "))
  nextpos = str(input("Choose next position between a1 or h8: "))
  
  if piece == 'bishop':
    cur_pos_x,cur_pos_y = validationCheck(currentpos[0:1],currentpos[1:2])
    next_pos_x,next_pos_y = validationCheck(nextpos[0:1],nextpos[1:2])
    if cur_pos_x!=0 and cur_pos_y!=0 and next_pos_x!=0 and next_pos_y!=0:
      print(bishop(cur_pos_x,cur_pos_y,next_pos_x,next_pos_y))
  elif piece == 'knight':
    cur_pos_x,cur_pos_y = validationCheck(currentpos[0:1],currentpos[1:2])
    next_pos_x,next_pos_y = validationCheck(nextpos[0:1],nextpos[1:2])
    if cur_pos_x!=0 and cur_pos_y!=0 and next_pos_x!=0 and next_pos_y!=0:
      print(knight(cur_pos_x,cur_pos_y,next_pos_x,next_pos_y))
  else:
    print("Chose wrong option. Please try again!")

c_engine = Engine()
