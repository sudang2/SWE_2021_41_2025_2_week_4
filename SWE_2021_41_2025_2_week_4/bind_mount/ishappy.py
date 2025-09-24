def isHappy(n):
  result=0
  temp=n
  list=[n]
  while True:
    for i in str(temp):
      result+=(int(i))**2
    if(result==1):
      return True
    else:
      for i in list:
        if(i==result):
          return False
      list.append(result)
      temp=result
      result=0

if __name__=="__main__":
  sample0_output=isHappy(19)
  sample1_output=isHappy(2)
  
  with open("/app/bind_mount/output.txt","w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
  
  print("Results saved to /app/bind_mount/output.txt")