orts_davhar_haalga = input()
toot = int(input())
res = [int(i)for i in orts_davhar_haalga.split()]
orts = res[0]
davhar = res[1]
haalga = res[2]
if toot%(davhar*haalga)==0:
    if toot%haalga == 0:
        print(int(toot%haalga),haalga)
    else:
        print(int((toot%haalga)+1), toot%haalga)
    
  
    
    
    