#!/usr/bin/env python
import os
import sys
import json
import tomllib

example_code = """from py_simple_morse_code import SignalProcessor, MorseCodeTranslator

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
    raise e"""


try:
    from py_simple_readme import readme_generator
    from src.py_simple_morse_code.version import __version__ as version
    from src.py_simple_morse_code import (
        SignalProcessor,
        MorseCodeTranslator,
        decode_morse_to_string,
        encode_beats_to_waveform,
        encode_morse_to_waveform,
        encode_morse_to_beats,
        encode_string_to_beats,
        encode_string_to_morse,
        encode_string_to_waveform,
        make_morse_visual_from_beats,
        play_morse,
        play_string,
        play_waveform,
    )

    IGNORED_METHODS = []
    with open(os.path.join(os.path.dirname(__file__), "./pyproject.toml"), "rb") as f:
        config = tomllib.load(f)
    with open(os.path.join(os.path.dirname(__file__), "./changelog.json")) as f:
        changelog = json.load(f)
    name = config["project"]["name"]
    description = config["project"]["description"]
    author = config["project"]["authors"][0]["name"]
    dependencies = config["project"]["dependencies"]
    installation_message = f"""Available on pip - `pip install {name}`"""
    gen = readme_generator(title=f"{name} {version}", ignored=IGNORED_METHODS)
    gen.set_header_images(
        {
            "Morse Encoder": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/text_to_morse.png",
            "Morse Decoder": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/morse_to_text.png",
            "Live Decoder": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/live_decoder.png",
        }
    )
    gen.set_changelog(changelog)
    gen.add_heading_1("About", add_toc=True)
    gen.add_paragraph(description)
    gen.add_paragraph(
        "Live Decoder In Action: https://raw.githubusercontent.com/AndrewSpangler/py_simple_morse_code/main/docu/live_decoder.mp4"
    )
    gen.add_heading_1("Installation", add_toc=True)
    gen.add_code_block("Run `pip install py_simple_morse_code`")
    gen.add_heading_1("Requirements", add_toc=True)
    gen.add_paragraph("\n\n".join(dependencies))
    gen.add_heading_1("GUI Usage", add_toc=True)
    gen.add_paragraph(
        "To launch the gui, install via pip and run `python -m py_simple_morse_code`"
    )
    gen.add_heading_1("Module Usage", add_toc=True)
    gen.add_code_block(example_code)
    gen.add_heading_1("Classes", add_toc=True)
    gen.handle_class_list([SignalProcessor, MorseCodeTranslator])
    gen.add_heading_1("Functions", add_toc=True)
    gen.handle_function_list(
        [
            encode_string_to_morse,
            encode_string_to_beats,
            encode_string_to_waveform,
            encode_morse_to_beats,
            encode_morse_to_waveform,
            encode_beats_to_waveform,
            decode_morse_to_string,
            make_morse_visual_from_beats,
            play_morse,
            play_string,
            play_waveform,
        ]
    )
    with open(os.path.join(os.path.dirname(__file__), "README.md"), "w+") as f:
        f.write(gen.assemble())
    print(f"Generated readme")
except Exception as e:
    print(f"Error generating readme - {e}")
    sys.exit(1)
sys.exit(os.EX_OK)
