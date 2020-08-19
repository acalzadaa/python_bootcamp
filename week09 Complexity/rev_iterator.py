class RevIterator:
  lists_internal = []

  def __init__(self, lists):
    self.lists = lists

  def __iter__(self):
    self.index = len(self.lists)-1
    return self

  def __next__(self):
    if self.index >= 0:
      dato = self.lists[self.index]
      self.index -= 1
      return dato
    else: 
      raise StopIteration

for i in RevIterator([1,2,3,5,6,7,8,9]):
  print(i)