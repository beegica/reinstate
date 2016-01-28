
tempList = [];
L = open(filenameL)
N = open(filenameN)
LivingList = L.read().split('\n')
NonList = N.read().split('\n')


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
                        'curr_list':1,
                        'correct_resp':KEYS1[buildingList1[x]['liv_nonliv']=='non']})
    # Fill in each dictionary at index for List2
    # Start with the dictionaries that are already built
    listDic2.append(listDic1[1].copy())
    listDic2[0]['curr_list'] = 2
    listDic2[0]['rep'] = False
    listDic2[0]['correct_resp'] = [KEYS2[2], KEYS2[3]]
    listDic2.append(listDic1[3].copy())
    listDic2[1]['curr_list'] = 2
    listDic2[1]['rep'] = False
    listDic2[1]['correct_resp'] = [KEYS2[2], KEYS2[3]]
    for x in range(6):
        if x < 2:
            listDic2.append({'stim':buildingList2[x]['stim'],
                             'set_num':None,
                             'stim_num':None,
                             'cond':None,
                             'rep':False,
                             'liv_nonliv':buildingList2[x]['liv_nonliv'],
                             'first_appear_list':2,
                             'curr_list':2,
                             'correct_resp':[KEYS2[0],KEYS2[1]]})
        else:
            listDic2.append({'stim':buildingList2[x]['stim'],
                             'set_num':None,
                             'stim_num':None,
                             'cond':None,
                             'rep':True,
                             'liv_nonliv':buildingList2[x]['liv_nonliv'],
                             'first_appear_list':2,
                             'curr_list':2,
                             'correct_resp':[KEYS2[2],KEYS2[3]]})

    # Fill in each dictionary at index for List3
    # Start with the dictionaries that are already built from lists 1 and 2
    listDic3.append(listDic1[2].copy())
    listDic3[0]['curr_list'] = 3
    listDic3[0]['correct_resp'] = [KEYS2[0], KEYS2[1]]
    listDic3.append(listDic1[6].copy())
    listDic3[1]['curr_list'] = 3
    listDic3[1]['correct_resp'] = [KEYS2[0], KEYS2[1]]
    listDic3.append({'stim':buildingList3[0]['stim'],
                     'set_num':None,
                     'stim_num':None,
                     'cond':None,
                     'rep':None,
                     'liv_nonliv':buildingList3[0]['liv_nonliv'],
                     'first_appear_list':2,
                     'curr_list':3,
                     'correct_resp':[KEYS2[2],KEYS2[3]]})
    listDic3.append({'stim':buildingList3[1]['stim'],
                     'set_num':None,
                     'stim_num':None,
                     'cond':None,
                     'rep':None,
                     'liv_nonliv':buildingList3[1]['liv_nonliv'],
                     'first_appear_list':2,
                     'curr_list':3,
                     'correct_resp':[KEYS2[2],KEYS2[3]]})

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


ListContRec = []
for i in range(num_cont_words):
    if(i%2 == 0):
        temp = LivingList.pop()
    else:
        temp = NonList.pop()

    ListContRec.append(temp)

rm.shuffle(ListContRec)
recog_dic=[]
test = ()
for x in ListContRec:
    if x in test:
        condition = KEYS2[0]
    else:
        condition = KEYS2[3]
    test+=(x,)
    recog_dic.append({'stim': x,
                     'correct': condition})


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