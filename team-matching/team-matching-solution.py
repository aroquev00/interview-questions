import math

def aux(team, level):
  strong = team
  weak = (2 ** (level + 1)) - strong + 1
  if level == top_level - 1:
    matches.append(strong)
    matches.append(weak)
    return
  else:
    aux(strong, level + 1)
    aux(weak, level + 1)
  

def prepare_matches(n):
  global top_level
  top_level =  math.log2(n)
  global matches
  matches = list()
  aux(1,0)
  return matches

if __name__ == "__main__":
  print(prepare_matches(16))
