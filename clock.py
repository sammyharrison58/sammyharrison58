import time
Time = input()
for x in range (time,0,-1):
    seconds = x% 60
    minutes = x/60 %60
    hours = x/3600
    print(f"{hours:02}:{minutes:02}:{seconds}")
    
    
