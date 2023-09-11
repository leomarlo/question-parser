import re
import sys

def extract_questions(text):
    """Extract sentences with question marks."""
    return [sentence.strip() for sentence in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text) if sentence.endswith('?')]

def extract_signifier_questions(text):
    """Extract sentences with question signifiers."""
    signifiers = ['why', 'how', 'when']
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [sentence.strip() for sentence in sentences if any(signifier in sentence.lower().split() for signifier in signifiers)]

def extract_or_questions(text):
    """Extract sentences with 'or'."""
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [sentence.strip() for sentence in sentences if ' or ' in sentence]

def main(input_filename, output_filename, bit_sequence):
    parsers = [extract_questions, extract_signifier_questions, extract_or_questions]

    # Convert number to bit sequence if needed
    # if isinstance(bit_sequence, int):
    #     bit_sequence = format(bit_sequence, '03b')

    with open(input_filename, 'r') as infile:
        text = infile.read()

    print('bit_sequence', bit_sequence)
    results = set()
    for i, bit in enumerate(bit_sequence):
        if bit == '1':
            results.update(parsers[i](text))

    with open(output_filename, 'w') as outfile:
        for result in results:
            outfile.write(result + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py input_filename output_filename bit_sequence")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    bit_sequence = sys.argv[3]

    # # Convert bit_sequence to int if it's a number
    # try:
    #     bit_sequence = int(bit_sequence)
    # except ValueError:
    #     pass

    # print(bit_sequence)

    main(input_filename, output_filename, bit_sequence)
