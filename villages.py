import sys

def can_drive(num_villages,roads):
  """You should implement this function, which takes in the number
     of villages in the problem and a set of tuples representing
     the start end end village of each road. It returns 1 if one 
     can drive, or -1 if one cannot drive as per the instructions."""

  occurences = []
  
  for i in range(num_villages + 1):
    sum = 0
    for j in roads:
      for k in j:
        if k == i:
          sum += 1
    occurences.append(sum)

  noOfOdd = 0

  for i in occurences:
    if i % 2 != 0:
      noOfOdd += 1

  if noOfOdd >= 2:
    return -1
  
  return 1

  #pass
  
    
    

num_problems=int(sys.stdin.readline().strip())
output=""
for _ in range(num_problems):
  line=sys.stdin.readline().strip()
  num_villages,num_roads=list(map(int,line.split()))
  roads=set()
  for _ in range(num_roads):
    roads.add(tuple(map(int,sys.stdin.readline().strip().split())))
  print(can_drive(num_villages,roads))



  
  
