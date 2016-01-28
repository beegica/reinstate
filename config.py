



# LIST GEN START
filenameL = "pools/living.txt"
filenameN = "pools/nonliving.txt"
numSets = 5*4







# EXPERIMENT VARIABLES
FIX_DUR = .5
INTER_FIX_DUR = .2
STIM_DUR = 2
INTER_STIM_DUR = .2
PRE_BLOCK_DUR = 3

FONT_SIZE = 20
RST_FONT_SIZE = 31
RST_WIDTH = 600

KEYS1 = ['F','J']
KEYS2 = ['F','G','H','J']



# Math Distractor Variables
num_vars = 3
math_distract_dur = 30
pam = True

# Continuous Recognition Variables
# The same as our Experiment Variables
num_cont_words = 100

# INSTRUCTIONS

continuousRecogInst = '''You are about to be presented with a series of words.
For each word, you need to identify whether or not you have seen it already in
this list.

::

    Press F for a word that you are positive you have seen before in this list.

::

    Press G for a word you think you have seen before.

::

    Press H for a word you think you haven't seen before.

::

    Press J for a word you are positive you haven't seen before.

Press Enter to continue on to the task.
'''

Instruc1 = '''In this experiment, you are going to see 3 lists of words. During
the first list, you must correctly identify whether a word is of a living
thing, or a nonliving thing.

::

    Press F for a word that is a living thing, kind of person, or part of a
    living thing.

::

    Press J for a word that is a nonliving thing, part of a nonliving thing, or
    a dead thing that was once living.

Try to remember as many words as possible, for you will be tested on them
later.

Press *ENTER* to continue.
'''

Instruc2 = '''In this list, you are going to be presented with words from the
previous list, as well as words you have not seen before. Some words will be
repeated in this list. You press a key to tell us wether or not you have seen
the presented word.

::

    Press F if it is a word you KNOW is a new word.

::

    Press G if it is a word that you THINK is a new word.

::

    Press H if it is a word that you THINK is a word you have seen before,
    repeated from this list or the last list.
::

    Press J if it is a word that you KNOW is a word you have seen before,
    repeated from this list or the last list.

To reiterate

::

    Press F if you are positive it is a new word.

::

    Press G if you think it is a new word.

::

    Press H if you think it is a repeated word.

::

    Press J if you are positive it is a repeated word.

When you are ready to begin, press *ENTER*
'''

Instruc3 = '''In the next set of words, we ask that you tell us which list the
presented word came from. You will have 4 choices depending on how sure you
are.

::

    Press F if it is a word you KNOW is from list 1.

::

    Press G if it is a word that you THINK is from list 1.

::

    Press H if it is a word that you THINK is from list 2.
::

    Press J if it is a word that you KNOW is from list 2.

To reiterate

::

    Press F if you are positive it is from list 1.

::

    Press G if you think it is from list 1.

::

    Press H if you think it is from list 2.

::

    Press J if you are positive it is from list 2.

When you are ready to begin, press *ENTER*

'''

mathDistractorInst = '''In this task, you will view a list of math equations.
Either they are correct, and the sum to the left of the equal sign equals the
value on the right, or they are incorrect, and the sum doesn't equal the value
on the right.

::

    Press F if the math equation is True.

::

    Press J if the math equation is False.

Press *Enter* to to start the math portion of this experiment.

'''