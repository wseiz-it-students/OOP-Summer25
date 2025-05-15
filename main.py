class Person:
  def __init__(self, name, age,adress):
    self.name = name
    self.age = age
    self.adress = adress
p1 = Person("cemkazimkaya", 21,"marszalkowska87")

print(p1.name)
print(p1.age)
print(p1.adress)

class student:
     def __init__(self ,name,index_number,last_name,nationality):
      self.name = name
      self.index_number = index_number 
      self.last_name = last_name 
      self.nationality = nationality 
p2 = student("john",206,"hawkins","american")   

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)       

 
    
p2 = student("matylda",103,"abramowicz","polish")   

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)    


p2 = student("mustafa",428,"korkmaz","turkish")   

print(p2.name)
print(p2.index_number)
print(p2.last_name)
print(p2.nationality)