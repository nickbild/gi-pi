from gi_sound import GiSound, GiSpeech
import time
from allophones import *


def main():
    ####
    ## Demo of AY-3-8910 sound chip.
    ####

    # # Initialize sound object with pin definition.
    # sound = GiSound(d0=8, d1=10, d2=12, d3=16, d4=18, d5=22, d6=24, d7=26, bc1=36, bdir=38, reset=40)

    # # Set mixer; 1=0N, 0=OFF; (toneA, toneB, toneC, noiseA, noiseB, noiseC)
    # sound.set_mixer(1, 1, 1, 0, 0, 0)
    # # Set volume; 1=0N, 0=OFF; (volumeA, volumeB, volumeC)
    # sound.set_volume(1, 1, 1)
    
    # for i in range(4096):
    #     # Set tone value, 0-4096; (toneA, toneB, toneC)
    #     sound.set_tone(i, i+20, i+40)
    #     time.sleep(0.001)

    # # Set noise, 0-31.
    # sound.set_noise(2)
    # sound.set_mixer(1, 1, 1, 1, 1, 1)

    # sound.set_tone(200, 200, 200)

    # # Define an envelope.
    # sound.set_envelope_freq(10000)              # 0-65535
    # sound.set_envelope_shape(0, 1, 1, 0)        # 1=0N, 0=OFF; (continue, attack, alternate, hold)
    # sound.enable_envelope(1, 1, 1)              # 1=0N, 0=OFF; (chanA, chanB, chanC)

    # time.sleep(2)
    
    # # Turn off all sound output.
    # sound.volume_off()

    ####
    ## Demo of SP0256-AL2 speech chip.
    ####

    speech = GiSpeech(a1=37, a2=35, a3=33, a4=31, a5=29, a6=23, ald=21, sby=15, rst=13)

    speech.speak(GG1)
    speech.speak(ER1)
    speech.speak(IY)
    speech.speak(TT1)
    speech.speak(IH)
    speech.speak(NG)
    speech.speak(SS)
    speech.speak(PA5)

    speech.speak(PP)
    speech.speak(RR1)
    speech.speak(OW)
    speech.speak(FF)
    speech.speak(EH)
    speech.speak(SS)
    speech.speak(SS)
    speech.speak(OR)
    speech.speak(PA5)

    speech.speak(FF)
    speech.speak(AO)
    speech.speak(LL)
    speech.speak(KK3)
    speech.speak(EH)
    speech.speak(NN1)
    speech.speak(PA5)

    speech.speak(SH)
    speech.speak(AE)
    speech.speak(LL)
    speech.speak(PA5)

    speech.speak(WW)
    speech.speak(IY)
    speech.speak(PA4)

    speech.speak(PP)
    speech.speak(LL)
    speech.speak(EY)
    speech.speak(PA5)

    speech.speak(EY)
    speech.speak(PA4)

    speech.speak(GG1)
    speech.speak(EY)
    speech.speak(MM)
    speech.speak(PA4)

    return


if __name__ == "__main__":
    main()
