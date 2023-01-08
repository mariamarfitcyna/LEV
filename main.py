import numpy as np
import re
import sys

def read(pairs_of_docs):
    filename_1 = ''
    filename_2 = ''
    with open(pairs_of_docs) as file:
        count_files = 0
        for line in file.readlines():
            count_files+=1
            if count_files == 1:
                filename_1 = line.strip()
            else:
                filename_2 = line.strip()
                count_files = 0
                #print("filenames: ", filename_1, filename_2)
                return (filename_1, filename_2)


def compare(file_1, file_2):
    with open(file_1, encoding='utf-8') as f1, open(file_2, encoding='utf-8') as f2:
        code_1 = f1.read()
        code_2 = f2.read()
        clean_code_1 = clear(code_1)
        clean_code_2 = clear(code_2)
        Leven = LEV(clean_code_1, clean_code_2)
        mean = (len(clean_code_1) + len(clean_code_2))/2
        return Leven/mean



def clear(string):
    match = re.search('#(\w*\s*){0,100000000}\s', string)
    try:
        h = match[0]
    except Exception:
        return string
    new_string = string[:match.start()] + string[match.end():]
    return new_string

def is_equal(letter1, letter2):
    return letter1 != letter2

def LEV(str1, str2):
    NAME_1 = str1
    NAME_2 = str2
    matrix = np.zeros((len(NAME_1) + 1, len(NAME_2)+1), dtype=int)
    matrix[:, 0] = np.arange(len(NAME_1) + 1)
    matrix[0] = np.arange(len(NAME_2) + 1)
    #print(matrix)
    for row_el in range(1, matrix.shape[0]):
        for column_el in range(1, matrix.shape[1]):
            matrix[row_el][column_el] = min(matrix[row_el-1][column_el] + 1, matrix[row_el][column_el-1] + 1, matrix[row_el-1][column_el-1] + is_equal(NAME_1[column_el-1], NAME_2[row_el-1]))

    #print(matrix)
    return matrix[-1][-1]


def main():
    answer = 0
    count_of_params = 0
    for param in sys.argv:
        count_of_params += 1
        if count_of_params == 1:
            docs = read(param)
            answer = compare(docs[0], docs[1])
        if count_of_params == 2:
            with open(param) as output_file:
                output_file.write(answer)
            
if __name__ == '__main__':
    main()