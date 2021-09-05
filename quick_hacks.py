from gi_sound import GiSound, GiSpeech
import time
from allophones import *


def main():
    sound = GiSound(d0=8, d1=10, d2=12, d3=16, d4=18, d5=22, d6=24, d7=26, bc1=36, bdir=38, reset=40)

    # Set mixer; 1=0N, 0=OFF; (toneA, toneB, toneC, noiseA, noiseB, noiseC)
    sound.set_mixer(1, 1, 1, 0, 0, 0)
    # Set volume; 1=0N, 0=OFF; (volumeA, volumeB, volumeC)
    sound.set_volume(1, 1, 1)
    sound.set_tone(600, 500, 400)
    time.sleep(0.2)
    sound.set_volume(0, 0, 0)
    time.sleep(0.2)
    sound.set_volume(1, 1, 1)
    time.sleep(0.2)
    sound.set_volume(0, 0, 0)

    speech = GiSpeech(a1=37, a2=35, a3=33, a4=31, a5=29, a6=23, ald=21, sby=15, rst=13)

    # Quick
    speech.speak(KK2)
    speech.speak(WW)
    speech.speak(IH)
    speech.speak(IH)
    speech.speak(KK2)
    speech.speak(PA5)

    # Haaaaaacks
    speech.speak(HH1)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(AE)
    speech.speak(KK2)
    speech.speak(SS)
    speech.speak(PA5)

    sound.set_mixer(1, 1, 1, 0, 0, 0)
    sound.set_volume(1, 1, 1)

    sound.set_tone(600, 500, 400)
    time.sleep(0.2)
    sound.set_tone(400, 300, 200)
    time.sleep(0.2)
    sound.set_tone(200, 100, 000)
    time.sleep(0.2)
    sound.set_tone(400, 300, 200)
    time.sleep(0.2)
    sound.set_tone(200, 100, 000)
    time.sleep(0.2)
    sound.set_tone(400, 300, 000)
    time.sleep(0.2)

    for i in range(200, 0, -1):
        sound.set_tone(i, int(i/2), int(i/4))
        time.sleep(0.003)
    
    # Turn off all sound output.
    sound.volume_off()

    return


if __name__ == "__main__":
    main()
