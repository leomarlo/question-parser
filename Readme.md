# Question Parser

The Question Parser is a Python script designed to extract specific types of questions from a given text file. The script uses three distinct parsers:

1. **Question Mark Parser**: Extracts all sentences ending with a question mark.
2. **Signifier Parser**: Extracts all sentences containing question signifiers such as "why", "how", and "when".
3. **Or Parser**: Extracts all sentences containing the word "or".

## Usage

To use the script, you need to provide three arguments:

1. The input filename (the file from which questions will be extracted).
2. The output filename (the file where the extracted questions will be saved).
3. A 3-bit sequence that determines which parsers to activate.

The bit sequence is read from left to right, with each bit corresponding to a parser. A bit value of `1` activates the parser, and a bit value of `0` deactivates it.

For example, the bit sequence `110` activates the first two parsers (Question Mark and Signifier) but deactivates the third parser (Or).

### Command Line Execution

To run the script from the command line, use the following format:

```
python question_parser.py [input_filename] [output_filename] [bit_sequence]
```

**Example**:

```
python qparser.py input.txt output.txt 110
```

This will extract questions from `input.txt` using the first two parsers and save the results to `output.txt`.

## Requirements

- Python 3.x

## Contact

Leonhard Horstmeyer (leonhard.horstmeyer@gmail.com)