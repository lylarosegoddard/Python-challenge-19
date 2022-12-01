import unittest
from app.guess import Guess

class TestGuess(unittest.TestCase):
  def test_guess_is_correct(self):
    guess = Guess(7)
    self.assertEqual("Thats correct", guess.comment())
    
  def test_guess_isnt_correct(self):
    guess = Guess(6)
    self.assertEqual("Thats incorrect", guess.comment())