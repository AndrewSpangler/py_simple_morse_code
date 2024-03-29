# py_simple_morse_code 0.0.4<a name="mark0"></a>

![Morse Encoder](https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/text_to_morse.png)

![Morse Decoder](https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/morse_to_text.png)

![Live Decoder](https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/live_decoder.png)

- [About](#mark1)
- [Installation](#mark2)
- [Requirements](#mark3)
- [GUI Usage](#mark4)
- [Module Usage](#mark5)
- [Classes](#mark6)
	- [SignalProcessor](#mark7)
	- [MorseCodeTranslator](#mark8)
- [Functions](#mark9)
	- [encode_string_to_morse](#mark10)
	- [encode_string_to_beats](#mark11)
	- [encode_string_to_waveform](#mark12)
	- [encode_morse_to_beats](#mark13)
	- [encode_morse_to_waveform](#mark14)
	- [encode_beats_to_waveform](#mark15)
	- [decode_morse_to_string](#mark16)
	- [make_morse_visual_from_beats](#mark17)
	- [play_morse](#mark18)
	- [play_string](#mark19)
	- [play_waveform](#mark20)
- [Changelog](#mark21)
	- [0.0.4](#mark22)
	- [0.0.3](#mark23)
	- [0.0.2](#mark24)
	- [0.0.1](#mark25)
	- [0.0.0](#mark26)

---

# About<a name="mark1"></a>[^](#mark0)

A python module for interacting with morse code with live decoding feature.

Live Decoder In Action: https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/live_decoder.mp4

# Installation<a name="mark2"></a>[^](#mark0)

```python
Run `pip install py_simple_morse_code`
```
# Requirements<a name="mark3"></a>[^](#mark0)

pyaudio

scipy

numpy

# GUI Usage<a name="mark4"></a>[^](#mark0)

To launch the gui, install via pip and run `python -m py_simple_morse_code`

# Module Usage<a name="mark5"></a>[^](#mark0)

```python
from py_simple_morse_code import SignalProcessor, MorseCodeTranslator

signal_processor = SignalProcessor(mic_index=0, min_tone=800, max_tone=1200)
decoder = MorseCodeTranslator(words_per_minute=10)
last_content = ""
try:
    signal_processor.start_session()
    print("Begin processing")
    while True:
        decoder.update(signal_processor.process())
        if not decoder.parsed_content == last_content:
            last_content = decoder.parsed_content
            print(last_content)
except Exception as e:
    print("End processing")
    signal_processor.end_session()
    raise e
```
# Classes<a name="mark6"></a>[^](#mark0)

### SignalProcessor<a name="mark7"></a>[^](#mark6)
**Non-blocking CW signal processor. The .process() method returns true if a CW tone was found in the signal.**

```py
class SignalProcessor(object):
	def __init__(self, mic_index: int = 0, min_tone: int = 600, max_tone: int = 1500, sample_size: int = 512, sample_rate: int = 32000, high_pass_frequency: int = 4, low_pass_frequency: int = 10000):
		...
	def end_session(self) -> None:
		"""Ends the audio stream. *Returns None*"""
	def process(self) -> bool:
		"""Process a chunk of the audio stream from the buffer. *Returns None*"""
	def start_session(self) -> None:
		"""Start the audio stream. *Returns None*"""
```
### MorseCodeTranslator<a name="mark8"></a>[^](#mark6)
**A low-level morse code translator. Inputs should be debounced / sanitized     before being passed to the .update(state:bool) method. Tolerance only affects     word-sep deadbeats to account for hesitation / early resumes between words.**

```py
class MorseCodeTranslator(object):
	def __init__(self, words_per_minute: int = 24, debounce_time: float = 0.01, tolerance: int = 0):
		...
	def update(self, state: bool) -> None:
		"""Call this whenever input state changes. Alternatively call this at a set frequency with the current state. *Returns None*"""
```
# Functions<a name="mark9"></a>[^](#mark0)

### encode_string_to_morse<a name="mark10"></a>[^](#mark9)
> **Encodes text to morse code dots and dashes. *Returns a string***
> 
```python
def encode_string_to_morse(in_str: str, short_char: str = '.', long_char: str = '-', sep_char: str = ' ', replace_on_unknown: bool | str = '?', verbose: bool = True) -> str:
> 	...
```
### encode_string_to_beats<a name="mark11"></a>[^](#mark9)
> **Converts a plaintext string to a beats list. *Returns a list of bools***
> 
```python
def encode_string_to_beats(in_str: str, verbose: bool = True) -> list:
> 	...
```
### encode_string_to_waveform<a name="mark12"></a>[^](#mark9)
> **Encode a plaintext string to a waveform. *Returns a float32 1-dimensional numpy array***
> 
```python
def encode_string_to_waveform(in_str: str, tone: int = 1000, words_per_minute: int = 24, sample_rate: int = 32000, verbose: bool = True) -> numpy.ndarray:
> 	...
```
### encode_morse_to_beats<a name="mark13"></a>[^](#mark9)
> **Converts dots and dashes to a beats list. *Returns a list of bools***
> 
```python
def encode_morse_to_beats(morse: str, verbose: bool = True) -> list:
> 	...
```
### encode_morse_to_waveform<a name="mark14"></a>[^](#mark9)
> **Encode a morse string to a waveform. *Returns a float32 1-dimensional numpy array***
> 
```python
def encode_morse_to_waveform(morse: str, tone: int = 1000, words_per_minute: int = 24, sample_rate: int = 32000, verbose: bool = True) -> numpy.ndarray:
> 	...
```
### encode_beats_to_waveform<a name="mark15"></a>[^](#mark9)
> **Encode a beats list into a waveform. *Returns a float32 1-dimensional numpy array***
> 
```python
def encode_beats_to_waveform(beats: list, tone: int = 1000, words_per_minute: int = 24, sample_rate: int = 32000, verbose: bool = True, volume: float = 0.75, deadbeats: int = 0) -> numpy.ndarray:
> 	...
```
### decode_morse_to_string<a name="mark16"></a>[^](#mark9)
> **Decodes morse dots and dashes to plaintext. *Returns a string***
> 
```python
def decode_morse_to_string(morse: str, char_sep: str = ' ', word_sep: str = '  ', replace_on_unknown: str | bool = '?') -> str:
> 	...
```
### make_morse_visual_from_beats<a name="mark17"></a>[^](#mark9)
> **Converts a beats list to a visual representation in string form     using block chars (unicode char 2588). *Returns a string***
> 
```python
def make_morse_visual_from_beats(beats: list) -> str:
> 	...
```
### play_morse<a name="mark18"></a>[^](#mark9)
> **Converts dots and dashes to a waveform and plays it on system speakers. *Returns None***
> 
```python
def play_morse(morse: str, tone: int = 1000, words_per_minute: int = 24, sample_rate: int = 32000, verbose: bool = True) -> None:
> 	...
```
### play_string<a name="mark19"></a>[^](#mark9)
> **Converts plaintext to a waveform and play it on system speakers. *Returns None***
> 
```python
def play_string(in_str: str, tone: int = 1000, words_per_minute: int = 24, sample_rate: int = 32000, verbose: bool = True) -> None:
> 	...
```
### play_waveform<a name="mark20"></a>[^](#mark9)
> **Plays a waveform. *Return None***
> 
```python
def play_waveform(waveform: bytes, format=1, sample_rate=32000) -> None:
> 	...
```
# Changelog<a name="mark21"></a>[^](#mark0)

## 0.0.4<a name="mark22"></a>[^](#mark21)

Fix PyPi page links

## 0.0.3<a name="mark23"></a>[^](#mark21)

Add example usage and images to readme and clean up typehints

## 0.0.2<a name="mark24"></a>[^](#mark21)

Move __main__ module to src/py_simple_morse_code/__main__.py

## 0.0.1<a name="mark25"></a>[^](#mark21)

Fix __main__ module not being included in pip module.

## 0.0.0<a name="mark26"></a>[^](#mark21)

Create Project



Generated with [py_simple_readme](https://github.com/AndrewSpangler/py_simple_readme)