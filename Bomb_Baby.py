"""
The challenge specification
You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.
But there's a few catches. First, the bombs self-replicate via one of two distinct processes: Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created; Every Facula bomb spontaneously creates a Mach bomb.
For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.
Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.

Test cases
Inputs: (string) M = "2" (string) F = "1"

Output: (string) "1"

Inputs: (string) M = "4" (string) F = "7"

Output: (string) "4"

Inputs: (string) M = "2" (string) F = "4"

Output: (string) "impossible"

Understanding
I guess the best way to describe the problem is to imagine yourself starting with two numbers F and M, both of which have the value of 1. At the start you are currently in step 0, to progress a step you must either;

Add the value of F onto M to calculate a new M, or,
Add the value of M onto F to calculate a new F.
Because of the rules of the specification we can create some facts:

Because of the steps, F can never equal M if step n > 0.
If F > M we know that the last step to take place involved adding M to F.
If M > F we know that the last step to take place involved adding F to M.

"""
def solution(x,y):
    x=int(x,10)
    y=int(y,10)
    q=0
    while(y):
        q=q+ int(x/y)
        x,y=y,x%y
    if(x==1):
        return (str)q-1
    else:
        return "impossible"
