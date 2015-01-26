from nltk.parse.generate import generate
from nltk import CFG
import random

grammar = """greeting -> g
  g -> w NP | NP
  w -> 'with'
  NP ->  AP NP | N c N | N
  c -> 'and'
  AP -> AvP A | A
  AvP -> 'truly' | 'very' | 'most' | 'extra'
  A -> 'best' |  'warmest' |  'greatest' | 'warm' |  'kind' |  'kindest' |  'extra'
  N -> 'wishes' |  'greetings' |  'regards' |  'cheers' |  'thanks' |  'tidings' |  'yours' | 'blessings'
  """

g = CFG.fromstring(grammar)

sentences = []

for sentence in generate(g, depth=6):
  sentences.append(' '.join(sentence))

for i in range(1):
  print(random.choice(sentences))
