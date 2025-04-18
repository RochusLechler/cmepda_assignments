import argparse
from loguru import logger
#import collections
import time
import matplotlib.pyplot as plt

start_time = time.time()

parser = argparse.ArgumentParser(      #takes input from command line and makes sense of it
                    prog='wordcount',
                    description='Program counts the relative frequency of letters in a book or any given .txt-file',
                    epilog='Cheerio')

parser.add_argument('infile')   #argument starting with -- is optional; otherwise it's mandatory
parser.add_argument('--plot', action='store_true',        #optional argument
                    help='Plot a bar chart of the relative frequencies')

alphabet_lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def process_file(file_path, plot):
    ''' Process one file and count the occurrences of each character

    Arguments:
    file_path: str
        path to the input file
    '''
    logger.info(f'Opening input file {file_path}')
    with open(file_path) as input_file:
        data = input_file.read()
    logger.info(f'Done, {len(data)} character(s) found')
#    counts = collections.Counter(map(str.lower, data))
    count_dictionary = {}
    for k, character in enumerate(alphabet_lower_case):
        counter = data.count(character) + data.count(alphabet_capital[k])
        count_dictionary[character] = counter


    if plot:
        logger.info('Plotting stuff')
        plot = plt.hist(count_dictionary.keys(),count_dictionary.values())


    return count_dictionary, plot

elapsed_time = time.time() - start_time

if __name__ == '__main__':       # if exectuing from the terminal; __name__ always exists
    args = parser.parse_args()
    dict, histo = process_file(args.infile, args.plot)
    logger.info(f'The computation took {elapsed_time} seconds')
    logger.info(f'Occurrences: {dict}')
    plt.show()

# always use if __name__ == '__main__': , when you only want things to be executed from command line
