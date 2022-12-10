import os

def conv_jsonfile(file_name):
    file_path = '{0}/{1}.json'.format(os.getcwd(), file_name)
    with open(file_path, 'w') as f:
        f.write(str(r).replace("\'", "\""))
