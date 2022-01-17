#popraw losowanie tych samych osób
from random import choice
from game_data import data
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

POSITION_A='Compare A: '
POSITION_B='Agnist B: '
gameprogress='True'
player_score=0

def onlyAB():
  answer=None
  while answer!='A' and answer!='B':
    answer=input("Type 'A' for first account or 'B' for second one. ").upper()

def compare(person_a_score, person_b_score,player_type):
  if (person_a_score > person_b_score and player_type=='A') or (person_a_score  <person_b_score and player_type=='B'):
    return True
  else:
    return False

def choose_person():
  return choice(data)


def descriptions(position):
  person_infos=choose_person()
  name=person_infos['name']
  country=person_infos['country']
  desc=person_infos['description']
  score=person_infos['follower_count']
  print(f'{position}{name}, {desc} from {country}')
  return score

def battle():
  a_score=descriptions(POSITION_A)
  b_score=descriptions(POSITION_B)
  player_answer=onlyAB()
  print('Hint: ', a_score,b_score)
  print(compare(a_score,b_score, player_answer))


print('Welcome to Higer or Lower Game. You must guess which one of those accounts have more followers on Instagram.\nGood luck!')
battle()