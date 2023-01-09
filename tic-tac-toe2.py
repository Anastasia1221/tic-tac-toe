from typing import List


class Field ():
  field = ""\
  " |1|2|3|\n"\
  "1|{0}|{1}|{2}|\n"\
  "2|{3}|{4}|{5}|\n"\
  "3|{6}|{7}|{8}|"

  def print(self, matrix:List[List[str]]) -> None:
    print(self.field.format(*[matrix[i][j] for i in range(3) for j in range(3)]))
    
class TTT():
  field = Field()

  matrix=[ \
      ['-','-','-'], \
      ['-','-','-'], \
      ['-','-','-']]

  def print(self) -> None:
    self.field.print(self.matrix)

  def input(self,x:int , y:int, symbol:str) -> bool:
    self.matrix[x][y] = symbol
    self.print()
    return self.check(symbol)

  def check(self, symbol:str) -> bool: 
    if not(('-') in self.field.field.format(*[self.matrix[i][j] for i in range(3) for j in range(3)])):
        print("draw")
        return True

    for i in range(3):
      if self.matrix[i][0] + self.matrix[i][1] + self.matrix[i][2] in ('000', 'XXX'):
        print("you win " + symbol)
        return True

      if self.matrix[0][i] + self.matrix[1][i] + self.matrix[2][i] in ('000', 'XXX'):
        print("you win " + symbol)
        return True

    if ''.join([self.matrix[i][i] for i in range(3)]) in ('000', 'XXX') :
       print("you win " + symbol)
       return True

    if ''.join([self.matrix[2-i][i] for i in range(3)]) in ('000', 'XXX'):
       print("you win " + symbol)
       return True

    return False


class TTT_UI():
  ttt = TTT()

  def start(self) -> None:
    symbol = "X"
    self.ttt.print()

    while True:
      print("Участник " + symbol + " , введите номер строки и столбца")

      x = input("row ") # через while
      if not (x in ('1','2','3')):
        print("введите номер строки, используя числа 1,2,3")
        continue
      x = int(x)-1  

      y = input("col ")
      if not (y in ('1','2','3')):
        print("введите номер столбца, используя числа 1,2,3")
        continue
      y = int(y)-1

      if self.ttt.matrix[x][y] != '-':
        print("Ячейка уже используется, введите другие координаты")
        continue

  
      if self.ttt.input(x, y, symbol):
        break
    
      if symbol == "X":
        symbol = "0"
      else:
        symbol = "X"

  
game = TTT_UI()
game.start()
