
import os
import sys

def rename_file(path):

    if type(path) == list: #in case the file name is seperated words the path is saved as list
        path = ' '.join(path) #concatenate the list items as one string

    #path = 'raw_image_data'
    files = os.listdir(path)


    for index, file in enumerate(files):
        os.rename((path+'/'+file), (path+'/'+(str(index+1) + '.jpg')))


def main():
    path = sys.argv[1:]
    rename_file(path)
if __name__ == "__main__":
    main()