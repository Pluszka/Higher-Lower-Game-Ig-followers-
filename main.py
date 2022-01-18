#popraw losowanie tych samych osób, poprawione ale printuje dwa razy B jak b jest równe A
from random import choice
from game_data import data
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

import art

LOGO=art.logo
VS=art.vs

POSITION_A='Compare A: '
POSITION_B='Agnist B: '

def previous_winner(position,previous_result):
  if position==POSITION_A and previous_result!=None:
    for vips in data:
      if previous_result==vips['follower_count']:
        return vips
  else:
    return choose_person()

def next_a(letter, ansA, ansB):
  if letter=='A':
    return ansA
  else:
    return ansB


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


def descriptions(position, previous, previous_result):
  person_infos=previous_winner(position,previous_result)
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

def battle(previosu_right_amount):
  a_score=descriptions(POSITION_A, None, previosu_right_amount)
  print(VS)
  b_score=descriptions(POSITION_B, a_score, previosu_right_amount)
  player_answer=onlyAB()
  return (compare(a_score,b_score, player_answer)),player_answer, a_score, b_score

def game():
  clearConsole()
  gameprogress='True'
  player_score=0
  right_followers=None
  print(LOGO)
  print('Welcome to Higer or Lower Game. You must guess which one of those accounts have more followers on Instagram.\nGood luck!')
  while gameprogress:
    print(f'\nCurrent score:{player_score}\n')
    result=battle(right_followers)
    right_followers=next_a(result[1], result[2], result[3])
    result=result[0]
    if result:
      player_score+=1
    else:
      print('You failed.')
      gameprogress= False

  print(f'You finished the game with total score: {player_score}')
  again=input('Will you play again?(Y/ any button fo no)').upper()
  if again=='Y':
    game()

game()
clearConsole()
print('See you next time.')