#!/usr/bin/python
import re
import nltk
import sys
import getopt
import math

def build_LM(in_file):
    """
    build language models for each label
    each line in in_file contains a label and a string separated by a space
    """
    print 'building language models...'

    # Store frequencies with add one smoothing
    model_table = {}
    LANGUAGES = ["indonesian", "malaysian", "tamil"]
    WINDOW_SIZE = 4
    # Store counts of each language
    language_counts = {}
    for language in LANGUAGES:
        language_counts[language] = 0

    input_file = file(in_file, 'r')
    for line in input_file:
        [label, text] = line.split(' ', 1)
        # Every string in window
        strings = [text[i : i + WINDOW_SIZE] for i in xrange(len(text) - WINDOW_SIZE - 1)]
        for string in strings:
            if not string in model_table:
                model_table[string] = {}
                for language in LANGUAGES:
                    # Introduce term into table for all LANGUAGES
                    model_table[string][language] = 1
                    # Increment count for every language
                    language_counts[language] += 1

            # Increment counts for language it actually appears in        
            model_table[string][label] += 1
            language_counts[label] += 1

    input_file.close()
    # Convert to probabilities
    for string, table in model_table.iteritems():
        for language, frequency in table.iteritems():
            table[language] = float(frequency) / language_counts[language]

    return (model_table, LANGUAGES, WINDOW_SIZE)

def test_LM(in_file, out_file, LM):
    """
    test the language models on new strings
    each line of in_file contains a string
    you should print the most probable label for each string into out_file
    """
    print "testing language models..."

    # Value for which we classify a string as part of one of our LANGUAGES.
    THRESHOLD_VALUE = 0.5

    (table, LANGUAGES, WINDOW_SIZE) = LM
    input_file = file(in_file, 'r')
    output_file = file(out_file, 'w')
    for line in input_file:
        num_missing = 0
        language_probs = {}
        for language in LANGUAGES:
            language_probs[language] = 0

        strings = [line[i : i + WINDOW_SIZE] for i in xrange(len(line) - WINDOW_SIZE - 1)]            
        for string in strings:
            # Ignore if doesn't exist
            if not string in table:
                num_missing += 1
                continue
            # Multiply
            for language in LANGUAGES:
                language_probs[language] += math.log(table[string][language])

        # Get max probability and language corresponding to that
        best_lang = max(language_probs, key = language_probs.get)
        proportion_missing = num_missing / float(len(strings))
        # Determine if other
        if proportion_missing > THRESHOLD_VALUE:
            best_lang = "other"
            
        output_file.write(best_lang + " " + line)

    input_file.close()
    output_file.close()

def usage():
    print "usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"

input_file_b = input_file_t = output_file = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'b:t:o:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == '-b':
        input_file_b = a
    elif o == '-t':
        input_file_t = a
    elif o == '-o':
        output_file = a
    else:
        assert False, "unhandled option"
if input_file_b == None or input_file_t == None or output_file == None:
    usage()
    sys.exit(2)

LM = build_LM(input_file_b)
test_LM(input_file_t, output_file, LM)
