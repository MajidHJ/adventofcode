import os

base = os.path.dirname(os.path.abspath(__file__))
ipath = os.path.join(base, 'input.txt')
opath = os.path.join(base, 'output.txt')


playhead = 50
zero_counter = 0
logger = []
with open(ipath) as f :
    for i in f :
        logger.append (f'playhead: {playhead}')
        logger.append (f'Rotation: {i}')
        if i.startswith('R'):
            for j in range(int(i.strip('R'))):
                playhead +=1
                if playhead == 100: 
                    playhead = 0
                
                if playhead==0 :
                    logger.append ('------Zero clicked------')
                    zero_counter +=1




        elif i.startswith('L'):
            for j in range(int(i.strip('L'))):
                playhead -=1
                if playhead == -1:
                    playhead = 99
                    
                if playhead==0 :
                    logger.append ('------Zero clicked------')
                    zero_counter +=1


with open(opath,'w') as f:
    for i in logger:
        f.writelines('\n'+i)


print(zero_counter)
        
