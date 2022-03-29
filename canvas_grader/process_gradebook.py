#helper functions:
def standardize(entry):
    if str(entry) == "nan":
        return 0.0
    return entry

def get_headers(df):
    headers = []
    for each in df:
        headers.append(each)
    return headers

def display_header_list(header_list,label):
    if len(label) != 0:
        print(label)
    print(header_list)
    
def check_valid_headers(header_list,to_keep_list):
    to_return = True
    for each in to_keep_list:
        if each not in header_list:
            print("Missing: {}".format(header_list)); to_return = False
    return to_return