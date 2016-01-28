from smile.common import *
from smile.state import Subroutine


@Subroutine
def Continuous_Recog(self, list_dic, fix_dur, stim_dur,inter_fix_dur, inter_stim_dur, font_size, keys, log_results):
    self.resaults = []
    with Loop(list_dic) as trial:
        Label(text='+', duration=fix_dur, font_size=font_size)
        Wait(inter_fix_dur)
        Label(text=trial.current['stim'], duration=stim_dur, font_size=font_size)
        with Meanwhile():
            kp = KeyPress(keys=keys, correct_resp=trial.current['correct'])
        Wait(inter_stim_dur)
        self.resaults += [Ref.object(dict)(correct=kp.correct,
                          pressed=kp.pressed,
                          reaction_time=kp.rt,
                          stim=trial.current)]
        with If(log_results):
            Log(name='cont_recog_log',
                correct=kp.correct,
                pressed=kp.pressed,
                reaction_time=kp.rt,
                stim=trial.curren)
