import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for key,value in kwargs.items():
            for j in range(0,value):
                self.contents.append(key)
    def draw(self,ballsToDraw):
        if(ballsToDraw>=len(self.contents)):
            drawed=self.contents.copy()
            self.contents.clear()
            return drawed
        draws=[]
        contentsL=list(self.contents)
        for i in range(0,ballsToDraw):
            j=random.randint(0,len(contentsL)-1)
            draws.append(contentsL.pop(j))
        self.contents.clear()
        for ball in contentsL:
            self.contents.append(ball)
        return draws

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success=0
    myHat=hat.contents.copy()
    for i in range(0,num_experiments):
        drawed=hat.draw(num_balls_drawn)
        test=True
        for key,value in expected_balls.items():
            if(len(list(filter (lambda x : x == key, drawed))) < value):
                test=False
                break
        if(test):
            success+=1
        hat.contents=myHat.copy()
    return success/num_experiments
