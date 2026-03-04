import argparse
from pathlib import Path
import pyphen
import re
DICTIONARY = pyphen.Pyphen(lang='en_US')

def normalize_text(text):
    normalized_text = re.sub(r'[^\w\s]', '', text.lower())
    normalized_text = re.sub(r'\s+', ' ', normalized_text)
    return normalized_text

def text2syllables(text):
    text = text.strip()
    text = normalize_text(text)
    text_syllables = []
    for word in text.split(' '):
        syllables = DICTIONARY.inserted(word)
        syllables = syllables.split('-')
        text_syllables += syllables
    return text_syllables

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)

    all_files = list(data_dir.rglob('*.normalized.txt'))
    for i, file in enumerate(all_files):
        text = file.read_text()
        syllables = text2syllables(text)
        output_file = output_dir / file.name.replace('.normalized.txt', '.syllables.txt')
        output_file.write_text(' '.join(syllables))
        print(f'{i+1}/{len(all_files)}', end='\r')

if __name__ == '__main__':
    main()
