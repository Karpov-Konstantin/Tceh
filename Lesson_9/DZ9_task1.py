import re

def read_file(filename, ):
    print('reading file in')
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print('File not found')
    #



def counter(val_list):
    words_dict = {}
    for word in val_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict


if __name__ == '__main__':

    content = read_file('nasa_19950801.tsv', )
    #print(content)

    date_pattern_group = r'\d{9}'
    date = re.findall(date_pattern_group, content)
    #print(date)
    date_dict = counter(date)
    for key in date_dict:
        print (key, ' : ', date_dict[key])

    url_pattern_group = r'/.+[.]+\S*'
    url = re.findall(url_pattern_group, content)
    #print(url)
    url_dict = counter(url)
    for key in url_dict:
        print ( key, ' : ', url_dict[key])

    code_pattern_group = r'(?<=\t)\d..(?=\t)'
    code = re.findall(code_pattern_group, content)
    #print(code)
    code_dict = counter(code)
    for key in code_dict:
        print ( key, ' : ', code_dict[key])
