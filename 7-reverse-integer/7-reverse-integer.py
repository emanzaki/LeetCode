class Solution:
    def reverse(self, x: int) -> int:
        z=""
        flag=0
        if x<0:
            flag=1
            x*=-1
        y=str(x)
        for a in range(len(y)):
	        z+=y[-a-1]
        if flag ==1:
            if (-int(z)>-2**31):
                return -int(z)  
            else:
                return 0
        else:
            if (int(z)<2**31-1):
                return int(z)
            else:
                return 0