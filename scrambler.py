import sys
import random

def scrambleWord(word):
  ret = ""
  wsize = len(word)
  for i in range(0, wsize):
    rando = int(random.random() * (wsize - i))
    ret = ret + word[rando]
    word = word[:rando] + word[rando+1:]
  return ret

if __name__ == "__main__":
  end = ""
  for i in sys.argv[1:]:
    end = end + scrambleWord(i) + " "
  print(end)