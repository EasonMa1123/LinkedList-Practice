class hashTable:
  
  def __init__(self,intianl_size = 10):
    self.__table =[[] for _ in range(intianl_size)]
    self.__ItemAmount = 0 
    self.__TableSize = intianl_size


  def __hash(self,value):
    return (value+(int(self.__TableSize/value))) % self.__TableSize

  def __ChangeSize(self):
      new_size = int(((self.__ItemAmount//10)+1))*10
      self.__ItemAmount = 0 
      self.__TableSize = new_size
      tempItemTable = []
      for i in self.__table:
        for l in i:
          tempItemTable.append(l)
      self.__table = [[] for _ in range(self.__TableSize)]
      for x in tempItemTable:
        self.__appendValue(x)

  def addValue(self,value):
    if self.__ItemAmount > self.__TableSize:
      self.__ChangeSize()
    self.__appendValue(value)


  def __appendValue(self,value):
    hashed_value = self.__hash(value if type(value) == int else sum(ord(i) for i in value))
    if value in self.__table[hashed_value]:
      return
    else:
      self.__table[hashed_value].append(value)
      self.__ItemAmount += 1


  def __str__(self):
    return str(self.__table)
  
  def cotain (self,value):
    hashed_value = self.__hash(value if type(value) == int else sum(ord(i) for i in value) )
    if value in self.__table[hashed_value]:
      return True
    else:
      return False 
