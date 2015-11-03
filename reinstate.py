import random as rm
from smile import *
from smile.mathdistract import MathDistract

# LIST GEN START
filenameL = "pools/living.txt"
filenameN = "pools/nonliving.txt"
numSets = 5*4


mathDistractorInst = '''You are about to be presented with a series of math problems, and you need to determine if the problem presented is correct or incorrect. 

::

    If the Problem is correct press F
    
::

    If the problem is incorrect press J
    
Press **ENTER** to continue 
'''

tempList = [];
L = open(filenameL)
N = open(filenameN)
LivingList = L.read().split('\n')
NonList = N.read().split('\n')
Instruc1 = '''In this experiment, you are going to see 3 lists of words. During the first list, you must correctly identify whether a word is of a living thing, or a nonliving thing.  

::

    Press F for a word that is a living thing, kind of person, or part of a living thing.

::

    Press J for a word that is a nonliving thing, part of a nonliving thing, or a dead thing that was once living.   
    
Try to remember as many words as possible, for you will be tested on them later.  

Press *ENTER* to continue.
'''
Instruc2 = '''In this list, you are going to be presented with words from the previous list, as well as words you have not seen before. Some words will be repeated in this list.

::

    Press F if it is a word you are seeing for the first time. 

::

    Press J if you have seen this word repeated, either from the first list or if this is the second time you are seeing an item from this list. 

To reiterate

::

    Press F for the first time you have seen a word

::

    Press J if you have seen this word once before.
    
When you are ready to begin, press *ENTER*
'''

Instruc3 = '''In this list, we ask that you tell us which list, either the first or the second, that the words you are about to view came from.  

::

    Press F if the word was presented in List 1

::

    Press J if the word was presented in List 2
    
When you are ready to begin, press *ENTER*

'''


#   [(ThrownAway, List2, List3, List2, ThrownAway,) (ThrownAway, List3, ThrownAway)]
cloneList = [None, None, None, None, None, None, None, None]

ReturnList =[]
List1 = []
List2 = []
List3 = []
throwawayList = [0,4,5,7]
rm.shuffle(LivingList)
rm.shuffle(NonList)
for i in range(numSets):
    # Copy the list of None's to fill in later
    buildingList1 = list(cloneList)
    buildingList2 = []
    buildingList3 = []
    # Copy the list of 4 index's that always need to be filled at random. 
    throwaway = list(throwawayList)
    living = []
    nonliving = []
    for z in range(5):
        living.append(LivingList.pop())
        nonliving.append(NonList.pop())
    rm.shuffle(throwaway)
    # Cond = 0 [None, NonLiving, Nonliving, Living, None, None, Living, None]
    if(i%6 == 0):
        buildingList1[1] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                 # to List 2
        buildingList1[2] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                 # to List 3
        buildingList1[3] = {'stim':living.pop(),'liv_nonliv':'liv'}                    # to List 2
        buildingList1[6] = {'stim':living.pop(),'liv_nonliv':'liv'}                    # to List 3
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})   # Opposite of buildingList1[1]
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})      # Opposite of buildingList1[3]     
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})   # Opposite of buildingList1[2]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})      # Opposite of buildingList1[6]   
    # Cond = 1 [None, NonLiving, Living, Nonliving, None, None, Living, None]
    elif(i%6 == 1):
        buildingList1[1] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                 # to List 2
        buildingList1[2] = {'stim':living.pop(),'liv_nonliv':'liv'}                    # to List 3
        buildingList1[3] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                 # to List 2
        buildingList1[6] = {'stim':living.pop(),'liv_nonliv':'liv'}                    # to List 3
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})   # Opposite of buildingList1[1]
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})   # Opposite of buildingList1[3]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})      # Opposite of buildingList1[2]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})      # Opposite of buildingList1[6]
    # Cond = 2 [(None, Living, Nonliving, Living, None,) (None, Nonliving, None)]
    elif(i%6 == 2):
        buildingList1[1] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 2
        buildingList1[2] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 3
        buildingList1[3] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 2
        buildingList1[6] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 3
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[1]
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[3]
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[2]
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[6]
    # Cond = 3 [(None, Living, Living, Nonliving, None,) (None, Nonliving, None)]
    elif(i%6 == 3):
        buildingList1[1] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 2
        buildingList1[2] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 3
        buildingList1[3] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 2
        buildingList1[6] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 3
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[1]
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[3]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[2]
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[6]
        
    # Cond = 2 [(None, Nonliving, Living, Living, None,) (None, Nonliving, None)]
    elif(i%6 == 4):
        buildingList1[1] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 2
        buildingList1[2] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 3
        buildingList1[3] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 2
        buildingList1[6] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 3
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[1]
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[3]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})    # Opposite of buildingList1[2]
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})       # Opposite of buildingList1[6]
    # Cond = 2 [(None, Living, Nonliving, Nonliving, None,) (None, Living, None)]
    elif(i%6 == 5):
        buildingList1[1] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 2
        buildingList1[2] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 3
        buildingList1[3] = {'stim':nonliving.pop(),'liv_nonliv':'non'}                  # to List 2
        buildingList1[6] = {'stim':living.pop(),'liv_nonliv':'liv'}                     # to List 3
        buildingList2.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[1]
        buildingList2.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[3]
        buildingList3.append({'stim':LivingList.pop(),'liv_nonliv':'liv'})    # Opposite of buildingList1[2]
        buildingList3.append({'stim':NonList.pop(),'liv_nonliv':'non'})       # Opposite of buildingList1[6]
    
    # LIST 1 STIM FINISHING
    # Fill the throwaway spots that don't need to be counterbalanced(because they only see it once)
    buildingList1[throwaway.pop()] = {'stim':living.pop(),'liv_nonliv':'liv'}
    buildingList1[throwaway.pop()] = {'stim':living.pop(),'liv_nonliv':'liv'}
    buildingList1[throwaway.pop()] = {'stim':nonliving.pop(),'liv_nonliv':'non'}
    buildingList1[throwaway.pop()] = {'stim':nonliving.pop(),'liv_nonliv':'non'}
    
    # LIST 2 FINISHING
    # Add the repeated items of list 1 to list 2
    # buildingList2.append('stim':buildingList1[1]['stim'], 'liv_nonliv':buildingList1[1]['liv_nonliv'])
    # buildingList2.append('stim':buildingList1[3]['stim'], 'liv_nonliv':buildingList1[3]['liv_nonliv'])
    # Fill in the other items for list 2 that get repeated in List 2
    livingTest2Item = LivingList.pop()
    nonlivingTest2Item = NonList.pop()
    buildingList2.append({'stim':livingTest2Item,'liv_nonliv':'liv'})
    buildingList2.append({'stim':livingTest2Item,'liv_nonliv':'liv'})
    buildingList2.append({'stim':nonlivingTest2Item,'liv_nonliv':'non'})
    buildingList2.append({'stim':nonlivingTest2Item,'liv_nonliv':'non'})
    
    # Start Dictionary Construction
    listDic1 = []
    listDic2 = []
    listDic3 = []
    # Fill information in the dictionary for each index
    # In list 1
    for x in range(8):
        listDic1.append({'stim':buildingList1[x]['stim'],
                        'set_num':i,
                        'stim_num':x,
                        'cond':i%6,
                        'rep':None,
                        'liv_nonliv':buildingList1[x]['liv_nonliv'],
                        'first_appear_list':1,
                        'curr_list':1,})
    
    # Fill in each dictionary at index for List2
    # Start with the dictionaries that are already built
    listDic2.append(listDic1[1].copy())
    listDic2[0]['curr_list'] = 2
    listDic2[0]['rep'] = False
    listDic2.append(listDic1[3].copy())
    listDic2[1]['curr_list'] = 2
    listDic2[1]['rep'] = False
    for x in range(6):
        if x < 2:
            listDic2.append({'stim':buildingList2[x]['stim'],
                             'set_num':None,
                             'stim_num':None,
                             'cond':None,
                             'rep':False,
                             'liv_nonliv':buildingList2[x]['liv_nonliv'],
                             'first_appear_list':2,
                             'curr_list':2,})
        else:
            listDic2.append({'stim':buildingList2[x]['stim'],
                             'set_num':None,
                             'stim_num':None,
                             'cond':None,
                             'rep':True,
                             'liv_nonliv':buildingList2[x]['liv_nonliv'],
                             'first_appear_list':2,
                             'curr_list':2,})

    # Fill in each dictionary at index for List3
    # Start with the dictionaries that are already built from lists 1 and 2
    listDic3.append(listDic1[2].copy())
    listDic3[0]['curr_list'] = 3
    listDic3.append(listDic1[6].copy())
    listDic3[1]['curr_list'] = 3
    listDic3.append({'stim':buildingList3[0]['stim'],
                    'set_num':None,
                    'stim_num':None,
                    'cond':None,
                    'rep':None,
                    'liv_nonliv':buildingList3[0]['liv_nonliv'],
                    'first_appear_list':2,
                    'curr_list':3})
    listDic3.append({'stim':buildingList3[1]['stim'],
                    'set_num':None,
                    'stim_num':None,
                    'cond':None,
                    'rep':None,
                    'liv_nonliv':buildingList3[1]['liv_nonliv'],
                    'first_appear_list':2,
                    'curr_list':3})
    
    List1.append(listDic1)
    
    List2+=listDic2
    List3+=listDic3


rm.shuffle(List1)
temp = []
for i in range(len(List1)): 
    temp+=List1[i]
List1 = temp
temp = []
rm.shuffle(List2)
rm.shuffle(List3)
'''
# Uncomment this if you would like to save out the 3 lists of dictionaries
import csv
with open('list1.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, List1[0].keys())
    writer.writeheader()
    for x in List1:
        writer.writerow(x)
with open('list2.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, List2[0].keys())
    writer.writeheader()
    for x in List2:
        writer.writerow(x)
with open('list3.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile, List3[0].keys())
    writer.writeheader()
    for x in List3:
        writer.writerow(x)
'''
# EXPERIMENT VARIABLES
FIX_DUR = .5
INTER_FIX_DUR = .2
STIM_DUR = 2
INTER_STIM_DUR = .2
RST_FONT_SIZE = 31
KEYS = ['F','J']
PRE_BLOCK_DUR = 3
FONT_SIZE = 20
# Math Distractor Variables
num_vars = 3
math_distract_dur = 30
pam = True

# EXPERIMENT PROGRAM START
exp = Experiment()

RstDocument(text=Instruc1, base_font_size=RST_FONT_SIZE, size=exp.screen.size)
with UntilDone():
    KeyPress(keys=['ENTER'])
Wait(PRE_BLOCK_DUR)
with Loop(List1) as trials1:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    exp.correct_resp = trials1.current['liv_nonliv']=='non' # CHANGE THIS LINE LATER FOR EEG (If EVER)
    lb = Label(text=trials1.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS, correct_resp=Ref.getitem(KEYS,exp.correct_resp)) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name = 'List1_SetsOfEight',
        trial_info = trials1.current,
        resp_time = kp.rt,
        correct = kp.correct)

# Math Distractor 1
RstDocument(text = mathDistractorInst, base_font_size=RST_FONT_SIZE, size=exp.screen.size)
with UntilDone():
    KeyPress(keys=['ENTER'])
MathDistract(num_vars=num_vars, duration=math_distract_dur)

# Block 2 : Rememberence Task
# Press F for new and J for old!
RstDocument(text = Instruc2, base_font_size=RST_FONT_SIZE, size=exp.screen.size, plus_and_minus=pam)
with UntilDone():
    KeyPress(keys=['ENTER'])
Wait(PRE_BLOCK_DUR)
with Loop(List2) as trials2:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    exp.correct_resp = trials2.current['first_appear_list'] == 1 or trials2.current['rep'] # Change this line for EEG if ever
    lb = Label(text=trials2.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS, correct_resp=Ref.getitem(KEYS,exp.correct_resp)) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name='List2_RepeatedItems',
        trial_info = trials2.current,
        resp_time = kp.rt,
        correct = kp.correct)
    
    
# Math Distractor 1
RstDocument(text = mathDistractorInst, base_font_size=RST_FONT_SIZE, size=exp.screen.size)
with UntilDone():
    KeyPress(keys=['ENTER'])
MathDistract(num_vars=num_vars, duration=math_distract_dur, plus_and_minus=pam)

# Block 3 : List Discrimination
# Hit F for list 1, and J for List 2
RstDocument(text = Instruc3, base_font_size=RST_FONT_SIZE, size=exp.screen.size)
with UntilDone():
    KeyPress(keys=['ENTER'])
Wait(PRE_BLOCK_DUR)
with Loop(List3) as trials3:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    exp.correct_resp = trials3.current['first_appear_list'] == 2
    lb = Label(text=trials3.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS, correct_resp=Ref.getitem(KEYS,exp.correct_resp)) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name='List3_ListDiscrim',
        trial_info = trials3.current,
        resp_time = kp.rt,
        correct = kp.correct)
        
Label(text='You have finished this experiment, Let the Experimenter know and they will setup the next experiment for you!')
with UntilDone():
    KeyPress(keys=['ENTER'])
exp.run()        
