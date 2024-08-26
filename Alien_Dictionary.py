#Function to add a directed edge between characters u and v
def addEdge(adj,u,v):
  adj[ord(u)-ord('a')].append(ord(v)-ord('a'))
#Depth-First Search (DFS) function to check for cycles in the graph
def dfs(adj,col,curr,isCyclic):
  #Mark the current node as visited and in the current path
  col[curr]=1
  for x in adj[curr]:
    if col[x]==1:
      #If the node is already in the current path, a cycle is detected
      isCyclic[0]=True
      return
    elif col[x]==0:
      #Recursively visit adjacent nodes
      dfs(adj,col,x,isCyclic)
  #Mark the current node as visited and not in the current path
  col[curr]=2
#Function to check if a cycle exists in the graph using DFS
def checkCycle(adj,col,k):
  isCyclic=[False]
  for i in range(k):
    if col[i]==0:
      dfs(adj,col,i,isCyclic)
  return isCyclic[0]
#DFS- based topological sorting utility function
def topologicalSortUtil(adj,u,visited,st):
  visited[u]=True
  for v in adj[u]:
    if not visited[v]:
      topologicalSortUtil(adj,v,visited,st)
  st.append(u)
#Function to perform topological sorting
def topologicalSort(adj,V):
  visited=[False]*V
  st=[]

  for i in range(V):
    if not visited[i]:
      topologicalSortUtil(adj,i,visited,st)
  #Print the characters in topological order
  while st:
    print(chr(st.pop() + ord('a')),end=" ")
#Function to process the words and find the character order
def printOrder(words):
  #To track the frequency of characters
  frq=[0]*26
  #Count of unique characters
  k=0
  #Count unique characters and their frequencies
  for word in words:
    for char in word:
      frq[ord(char)-ord('a')]+=1
      if frq[ord(char)-ord('a')]==1:
        k+=1
  #Create adjacency list for the graph
  adj=[[] for _ in range(k)]
  #Build the graph by iterating through adjacent words
  for i in range(len(words)-1):
    word1,word2=words[i],words[i+1]
    j=0
    while j<len(word1) and j<len(word2):
      if word1[j]!=word2[j]:
        #Add edges based on character order
        addEdge(adj,word1[j],word2[j])
        break
      j+=1
  #color array for cycle detection
  col=[0]*k
  isCyclic=[False]
  if checkCycle(adj,col,k):
    #Detect and handle cycles
    print("Valid Order is not possible")
    return
  #Perform topological sorting and print character order
  topologicalSort(adj,k)
#Driver Code
if __name__=="__main__":
  words=["baa","abcd","abca","cab","cad"]
  printOrder(words)

      
