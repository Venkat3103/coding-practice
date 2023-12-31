class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        print(pos)
        for i in moves:
            if i=="U":
                pos[1]+=1
            if i=="D":
                pos[1]-=1
            if i=="L":
                pos[0]-=1
            if i=="R":
                pos[0]+=1
        if pos[0]==0 and pos[1]==0:
            return True
        else:
            return False
            
#https://leetcode.com/problems/robot-return-to-origin/description/