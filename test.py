# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

def sortkey(name):
    val = int(name.split()[1].split('.')[0])
    return val

# Function to rename multiple files
def main():

    tagnum = open("taglisttext.txt")
    tagnum_lst = tagnum.read().split("\n")

    doc_list = list(os.listdir("PA-F-008/"))[:-1]
    sort_file = sorted(doc_list, key = sortkey)
    count = 0

    for filename in sort_file:
        dst ="MEOL-PAF008-20-0" + str(count + 360) + "-" + tagnum_lst[count] + ".pdf"
        src ="PA-F-008/"+ filename
        dst ="PA-F-008/"+ dst
        count = count + 1

        # rename() function will
        # rename all the files
        os.rename(src, dst)

main()
