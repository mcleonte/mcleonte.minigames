from random import randint
import sys
from typing import Literal
from ast import literal_eval

class TicTacToe:
  """
  Simple Tic Tac Toe terminal game
  """

  def __init__(self, player_symbol: Literal["x", "o"] = "x"):
    self.player_symbol = sys.argv[-1] if sys.argv[-1] in (
        "x", "o") else player_symbol
    self.opponent_symbol = "o" if self.player_symbol == "x" else "x"
    self.empty_symbol = "-"
    self.mx = [["-"] * 3 for _ in range(3)]
    self.move_count = 0

  def print(self):
    for row in self.mx:
      print(*row, sep=" ")

  def is_over(self):

    # horizontal checkes
    for row in range(3):
      if len(set(self.mx[row])) == 1 and \
          self.mx[row][0] != self.empty_symbol:
        self.end_game(self.mx[row][0], f"row {row}")

    # vertical checks
    for col in range(3):
      if len(set(self.mx[row][col] for row in range(3))) == 1 and \
          self.mx[0][col] != self.empty_symbol:
        self.end_game(self.mx[0][col], f"column {col}")

    # first diagonal check
    if len(set(self.mx[i][i] for i in range(3))) == 1 and \
        self.mx[0][0] != self.empty_symbol:
      self.end_game(self.mx[0][0], "diagonal 1")

    # second diagonal check
    if len(set(self.mx[i][-1 - i] for i in range(3))) == 1 and \
        self.mx[0][-1] != self.empty_symbol:
      self.end_game(self.mx[0][-1], "diagonal 2")

    # no more moves check
    if self.move_count == 9:
      self.end_game()

  def end_game(self, winner=None, reason=None):
    match winner:
      case self.player_symbol:
        print(f"You win! Completed {reason}!")
      case self.opponent_symbol:
        print(f"You loose... Snoozed on {reason}")
      case _:
        print("No more moves! It's a tie!")
    sys.exit()

  def is_taken(self, i, j):
    return self.mx[i][j] != self.empty_symbol

  def player_turn(self):
    while True:
      try:
        digit = literal_eval(input("Enter single digit (1-9) for next move:"))
        if not isinstance(digit, int):
          raise TypeError
        if not 1 <= digit <= 9:
          raise ValueError
      except TypeError:
        print("That is not a digit!")
        continue
      except ValueError:
        print("Wrong digit")
        continue
      i, j = (digit-1) // 3, (digit-1) % 3
      if self.is_taken(i, j):
        print("That square is already taken")
        continue
      break
    self.mx[i][j] = self.player_symbol
    self.end_turn()

  def opponent_turn(self):
    while True:
      i, j = randint(0, 2), randint(0, 2)
      if self.is_taken(i, j):
        continue
      break
    self.mx[i][j] = self.opponent_symbol
    print(f"Oponent move: row {i} col {j}")
    self.end_turn()

  def end_turn(self):
    self.move_count += 1
    self.print()
    self.is_over()

  def run(self):
    self.print()
    while True:
      self.player_turn()
      self.opponent_turn()
      print()


def main():
  TicTacToe().run()


if __name__ == "__main__":
  main()
