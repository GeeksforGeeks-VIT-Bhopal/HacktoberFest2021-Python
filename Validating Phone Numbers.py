import re;
N = int(input());
for x in range(0,N):
    S = input();
    match = re.search('[789]\d+',S);    
    if match and len(match.group()) == 10:
        print("YES");        
    else:
        print("NO");