#popraw losowanie tych samych osób, poprawione ale printuje dwa razy B jak b jest równe A
from random import choice
from game_data import data
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

POSITION_A='Compare A: '
POSITION_B='Agnist B: '


def onlyAB():
  answer=None
  while answer!='A' and answer!='B':
    answer=input("Type 'A' for first account or 'B' for second one. ").upper()
    return answer

def compare(person_a_score, person_b_score,player_type):
  if person_a_score > person_b_score and player_type=='A' or person_a_score  < person_b_score and player_type=='B':
    return True
  else:
    return False

def choose_person():
  return choice(data)


def descriptions(position, previous):
  person_infos=choose_person()
  score=person_infos['follower_count']
  if previous!=None:
    while score==previous:
      person_infos=choose_person()
      score=person_infos['follower_count']
  name=person_infos['name']
  country=person_infos['country']
  desc=person_infos['description']
  print(f'{position}{name}, {desc} from {country}')
  return score

def battle():
  a_score=descriptions(POSITION_A, None)
  b_score=descriptions(POSITION_B, a_score)
  print('Hint: ', a_score,b_score)
  player_answer=onlyAB()
  return (compare(a_score,b_score, player_answer))

def game():
  clearConsole()
  gameprogress='True'
  player_score=0
  print('Welcome to Higer or Lower Game. You must guess which one of those accounts have more followers on Instagram.\nGood luck!')
  while gameprogress:
    print(f'\nCurrent score:{player_score}\n')
    result=battle()
    if result:
      player_score+=1
    else:
      gameprogress= False

  print(f'You finished the game with total score: {player_score}')
  again=input('Will you play again?(Y/ any button fo no)').upper()
  if again=='Y':
    game()

game()