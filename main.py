from random import choice
from game_data import data

POSITION_A='Compare A: '
POSITION_B='Agnist B: '

def choose_person():
  return choice(data)


def descriptions(position):
  person_infos=choose_person()
  name=person_infos['name']
  country=person_infos['country']
  desc=person_infos['description']
  score=person_infos['follower_count']
  print(f'{position}{name}, {desc} from {country}')

print('Welcome to Higer or Lower Game. You must guess which one of those accounts have more followers on Instagram. Good luck!')

descriptions(POSITION_A)