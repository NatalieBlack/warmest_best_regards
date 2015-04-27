from nltk.parse.generate import generate
from nltk import CFG
import random
from rauth import OAuth1Service
from config import tumblrrestclient1,tumblrrestclient2,tumblrrestclient3,tumblrrestclient4
import pytumblr

client = pytumblr.TumblrRestClient( tumblrrestclient1, tumblrrestclient2, tumblrrestclient3, tumblrrestclient4)


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

for i in range(len(sentences)):
  s = random.choice(sentences).capitalize() + ","
  ans = raw_input(s + " y or n?")
  if ans == 'y':
    client.create_quote("warmestbestregards", state="queue", quote=s, tags=["beep boop"])
