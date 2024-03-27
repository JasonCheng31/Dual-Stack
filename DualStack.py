class DualStack:
  def __init__(self, size):
    self.stack = [None] * size      #Create an empty stack using a list
    self.size = size                #Assign a fixed size with the attribute 'size'
    self.count = 0                  #Counter for the amount of elements in stack 1
    self.count2 = 0                 #Counter for the amount of elements in stack 2
    self.Top = size - 1             #Sets the top index for the second stack
    self.Bottom = 0                 #Sets the bottom index for the first stack 

  def push1(self, data):
    if self.Bottom > self.Top:  # Checks for stack overflow
      raise Exception ("Stack Overflow")
    else:
      self.stack[self.Bottom] = data   #Pushes data to the stack 1
      self.Bottom += 1                
      self.count +=1                  

  def push2(self, data):
    if self.Top < self.Bottom:  # Checks for stack overflow
      raise Exception ("Stack Overflow")
    else:
      self.stack[self.Top] = data   #Pushes data to the stack 2
      self.Top -= 1
      self.count2 +=1

  def pop1(self):
    if self.count == 0: #Checks for stack underflow
      raise Exception ("Stack Underflow")
    else: 
      # Pops data from stack 1
      poppedElement=self.stack[self.Bottom - 1] 
      self.stack[self.Bottom - 1]= "None"
      self.Bottom -=1
      self.count -=1
      return poppedElement

  def pop2(self):
    if self.count2 == 0:    #Checks for stack underflow
      raise Exception ("Stack Underflow")
    else:
      # Pops data from stack 2
      poppedElement2 = self.stack[self.Top + 1]
      self.stack[self.Top + 1] = "None"
      self.Top +=1
      self.count2 -=1
      return poppedElement2

  def peek1(self):
    if self.count == 0: #Checks if stack 1 is empty
      raise Exception ("Stack Underflow")
    else:
      return self.stack[self.Bottom-1]  #Returns the top element of stack 1

  def peek2(self):
    if self.count2 == 0:    #Checks if stack 2 is empty
      raise Exception ("Stack Underflow")
    else:
      return self.stack[self.Top + 1]   #Returns the top element of stack 2
  def isFull(self):
    return self.count + self.count2 == self.size     #Checks if both stacks combined are full
  def isEmpty1(self):
    return self.count == 0  #Checks if stack 1 is empty
  def isEmpty2(self):
    return self.count2 == 0 #Checks if stack 2 is empty
