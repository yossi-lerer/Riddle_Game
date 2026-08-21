from riddle import FourAnswerRiddle, TwoAnswerRiddle, OpenRiddle
from game import RiddleGame, Player
from riddle_crud import RiddleRepository
from menu import Menu


ridd = RiddleRepository("answers.json")
yossi = Player("yossi")
run_game = RiddleGame(yossi, ridd.get_all_riddles())

run_game = RiddleGame(yossi, ridd.get_all_riddles())
menu = Menu(run_game, ridd)
menu.menu_selection()