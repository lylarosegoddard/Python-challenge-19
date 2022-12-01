class Guess:
  def __init__(self, guess):
    self.guess = guess

  def comment(self):
    if self.guess == 7:
      return "Thats correct"
    return "Thats incorrect"