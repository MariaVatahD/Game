
class Сharacter():
    
  def __init__(self, name, health, armor, power, weapon, atack):
      self.name = name
      self.health = health
      self.armor = armor
      self.power = power
      self.weapon = weapon
      self.atack = atack 
    
  
  def print_info(self):
      print('Новий герой!!!')
      print('Ім я Героя :', self.name)
      print('Здоров я:', self.health)
      print('Броня:', self.armor)
      print('Енергія:', self.power)
      print('Зброя:', self.weapon)
      print(' ')
    
  def element_atack(self, enemy):
      while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
              print(enemy.name, 'Впав(-ла) у бою.')
              break
            enemy.strike(self)
            if self.health <= 0:
              print(self.name, 'Впав(-ла) у бою.')
              break
            if enemy.health <= 100000 and enemy.armor <= 0:
              print('Герой', enemy.name, 'атакує', self.name, 
                      'за допомогою своєї зброї:', enemy.weapon)          
              enemy.power = enemy.power + enemy.atack 
              print('Здоровя персонажа', self.name,":", self.health)
            if self.health <= 100000 and self.armor <= 0:
              print('Герой', self.name, 'атакує', enemy.name, 
                    'за допомогою своєї зброї:', self.weapon) 
              self.power = self.power + self.atack
              print('Здоровя персонажа', enemy.name,":", enemy.health)
                 
  def strike(self, enemy):
      print('Герой', self.name, 'атакує', enemy.name)
      enemy.armor = enemy.armor - self.power
      if enemy.armor <= 0:
        enemy.health = enemy.health + enemy.armor
        enemy.armor = 0

      print('Броня', enemy.name, enemy.armor, 'і здоровя', enemy.health)
  
  def fight(self, enemy):
      while self.health > 0 and enemy.health > 0:
        self.strike(enemy)  
        if enemy.health <= 0:
          print(enemy.name, 'Впав(-ла) у бою.')
          break
        enemy.strike(self)
        if self.health <= 0:
          print(self.name, 'Впав(-ла) у бою.')
          break
        if self.health <= 500:
          print("Бій майже закінчився гравець", self.name, 
                "близький до програшу!!!") 
        if enemy.health <= 500:
          print("Бій майже закінчився гравець", enemy.name,
              "близький до програшу!!!")
          
      