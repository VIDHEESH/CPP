def wildcard(pattern,string):
  l=[[0 for _ in range(len(string)+1) ] for _ in range(len(pattern)+1)]
  l[0][0]=1
  for i in range(1,len(pattern)+1):
    if pattern[i-1]=='*':
      l[i][0]=l[i-1][0]
  for i in range(1,len(pattern)+1):
    for j in range(1,len(string)+1):
      if pattern[i-1]=='*':
        l[i][j]=l[i-1][j] or l[i][j-1]
      elif pattern[i-1]=='?' or pattern[i-1]==string[j-1]:
        l[i][j]=l[i-1][j-1]
      else:
        l[i][j]=0
  return l[len(pattern)][len(string)]==1
