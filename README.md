# Retro Audio

Control the classic General Instrument SP0256-AL2 speech chip and AY-3-8910 sound generator with a Raspberry Pi and this Python library.

<p align="center">
<img src="https://raw.githubusercontent.com/nickbild/retro_audio/main/media/closeup_sm.jpg">
</p>

The SP0256-AL2 was originally avaialable in the early 1980s in speech add-ons for the VIC-20, Atari 8-bit computers, and the Tandy TRS-80.  Radio Shack sold the bare chip as the "Narrator Speech Processor".

The AY-3-8910 was first produced in 1978, and was in arcade and pinball games, the Intellivision and Vectrex game consoles, and in sound cards for the Apple II and TRS-80 Color Computer.

## How It Works

#### Library

A demonstration of the core functionalities can be found in [demo.py](https://github.com/nickbild/retro_audio/blob/main/demo.py):

Speech:

```python
# Initialize speech object with pin definition.
speech = GiSpeech(a1=37, a2=35, a3=33, a4=31, a5=29, a6=23, ald=21, sby=15, rst=13)

speech.speak(GG1)
speech.speak(ER1)
speech.speak(IY)
speech.speak(TT1)
speech.speak(IH)
speech.speak(NG)
speech.speak(SS)
speech.speak(PA5)
```

Sound generator:

```python
# Initialize sound object with pin definition.
sound = GiSound(d0=8, d1=10, d2=12, d3=16, d4=18, d5=22, d6=24, d7=26, bc1=36, bdir=38, reset=40)

# Set mixer; 1=0N, 0=OFF; (toneA, toneB, toneC, noiseA, noiseB, noiseC)
sound.set_mixer(1, 1, 1, 0, 0, 0)
# Set volume; 1=0N, 0=OFF; (volumeA, volumeB, volumeC)
sound.set_volume(1, 1, 1)

for i in range(4096):
    # Set tone value, 0-4096; (toneA, toneB, toneC)
    sound.set_tone(i, i+20, i+40)
    time.sleep(0.001)

# Set noise, 0-31.
sound.set_noise(2)
sound.set_mixer(1, 1, 1, 1, 1, 1)

sound.set_tone(200, 200, 200)

# Define an envelope.
sound.set_envelope_freq(10000)              # 0-65535
sound.set_envelope_shape(0, 1, 1, 0)        # 1=0N, 0=OFF; (continue, attack, alternate, hold)
sound.enable_envelope(1, 1, 1)              # 1=0N, 0=OFF; (chanA, chanB, chanC)

time.sleep(2)

# Turn off all sound output.
sound.volume_off()
```

Further details are availble in [the library](https://github.com/nickbild/retro_audio/blob/main/gi_sound.py).

## Media

Full setup:
![Full setup](https://raw.githubusercontent.com/nickbild/retro_audio/main/media/full_setup_sm.jpg)

SP0256-AL2 chip:
![SP0256-AL2](https://raw.githubusercontent.com/nickbild/retro_audio/main/media/sp0256_sm.jpg)

## Bill of Materials

- 1 x Raspberry Pi 400 (or another model)
- 1 x SP0256-AL2 speech chip
- 1 x 3.12 MHz crystal
- 2 x 22 pF capacitors (XTAL to ground)
- Speaker and audio amplification circuit (see [datasheet](https://github.com/nickbild/retro_audio/blob/main/spo256_datasheet.pdf))
- Miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
