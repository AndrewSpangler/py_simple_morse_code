#!/usr/bin/env python
import os
import sys
import json
import tomllib

try:
    from py_simple_readme import readme_generator
    from src.py_simple_morse_code.version import __version__ as version
    from src.py_simple_morse_code import (
        SignalProcessor,
        MorseCodeTranslator,
        decode_morse_to_string,
        encode_beats_to_waveform,
        encode_morse_string_to_waveform,
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
    gen.set_changelog(changelog)
    gen.add_heading_1("About", add_toc=True)
    gen.add_paragraph(description)
    gen.add_heading_1("Requirements", add_toc=True)
    gen.add_unordered_list(dependencies)
    gen.add_heading_1("Classes", add_toc=True)
    gen.handle_class_list([SignalProcessor, MorseCodeTranslator])
    gen.add_heading_1("Functions", add_toc=True)
    gen.handle_function_list(
        [
            encode_string_to_morse,
            encode_string_to_beats,
            encode_string_to_waveform,
            encode_morse_to_beats,
            encode_morse_string_to_waveform,
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
except Exception as e:
    sys.exit(1)
sys.exit(os.EX_OK)
