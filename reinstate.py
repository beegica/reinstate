import random as rm
from smile.common import *
from mathdistract import MathDistract
from continuous_recog import Continuous_Recog

execfile("config.py")
execfile("gen_stim.py")


# EXPERIMENT PROGRAM START
exp = Experiment()

RstDocument(text=Instruc1, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])

Label(text='Get Ready for the task!', duration=PRE_BLOCK_DUR)
Wait(PRE_BLOCK_DUR/2)
with Loop(List1) as trials1:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    #exp.correct_resp = trials1.current['liv_nonliv']=='non' # CHANGE THIS LINE LATER FOR EEG (If EVER)
    lb = Label(text=trials1.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS1, correct_resp=trials1.current['correct_resp']) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name = 'List1_SetsOfEight',
        trial_info = trials1.current,
        resp_time = kp.rt,
        correct = kp.correct)

# Math Distractor 1
RstDocument(text = mathDistractorInst, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])
MathDistract(num_vars=num_vars, duration=math_distract_dur, plus_and_minus=pam)

# Block 2 : Rememberence Task
# Hit F and G for new, and H and J for old
RstDocument(text = Instruc2, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])

Label(text='Get Ready for the task!', duration=PRE_BLOCK_DUR)
Wait(PRE_BLOCK_DUR/2)
with Loop(List2) as trials2:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    #exp.correct_resp = trials2.current['first_appear_list'] == 1 or trials2.current['rep'] # Change this line for EEG if ever
    lb = Label(text=trials2.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS2, correct_resp=trials2.current['correct_resp']) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name='List2_RepeatedItems',
        trial_info = trials2.current,
        resp_time = kp.rt,
        correct = kp.correct)


# Math Distractor 1
RstDocument(text = mathDistractorInst, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])
MathDistract(num_vars=num_vars, duration=math_distract_dur, plus_and_minus=pam)

# Block 3 : List Discrimination
# Hit F and G for list 1, and H and J for List 2
RstDocument(text = Instruc3, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])

Label(text='Get Ready for the task!', duration=PRE_BLOCK_DUR)
Wait(PRE_BLOCK_DUR/2)
with Loop(List3) as trials3:
    Label(text = '+', font_size=FONT_SIZE, duration=FIX_DUR)
    Wait(INTER_FIX_DUR)
    #exp.correct_resp = trials3.current['first_appear_list'] == 2
    lb = Label(text=trials3.current['stim'], duration=STIM_DUR, font_size=FONT_SIZE)
    with Meanwhile():
        kp = KeyPress(keys=KEYS2, correct_resp=trials3.current['correct_resp']) # Change this line later for EEG (IF EVER)
    Wait(INTER_STIM_DUR)
    Log(name='List3_ListDiscrim',
        trial_info = trials3.current,
        resp_time = kp.rt,
        correct = kp.correct)

# Continuous Recognition
RstDocument(text = continuousRecogInst, base_font_size=RST_FONT_SIZE, width=RST_WIDTH, height=exp.screen.height)
with UntilDone():
    KeyPress(keys=['ENTER'])
Continuous_Recog(list_dic=recog_dic, fix_dur=FIX_DUR, inter_stim_dur=INTER_STIM_DUR, stim_dur=STIM_DUR, inter_fix_dur=INTER_FIX_DUR, font_size=FONT_SIZE, keys=KEYS2, log_results=True)

Label(text='You have finished this experiment, let the Experimenter know you have finished')
with UntilDone():
    KeyPress(keys=['ENTER'])
exp.run()
