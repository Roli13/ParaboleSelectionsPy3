import logging
import os

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def create_knowledge_graph(contents_of_input_file, name_of_input_file):
    # Through this function you have to use the contents of each file to create a knowledge graph
    # The output has to be saved in the data/output folder with the same name as data/input file
    # Note the writing to file has to be handled by you.
    before=[]
    after=[]
    fline_list=[]
    last_word_list=[]
    first_word_list=[]

    output=open(name_of_input_file+'.txt', 'a')
    content=contents_of_input_file
    for line in content:
        #print(line, end='')
        if 'is a' in line:
            flag=0
            before.append(line[:line.index('is a')-1])
            after.append(line[line.index('is a')+5:-2])
        if 'is an' in line:
            flag=1
            before.append(line[:line.index('is an')-1])
            after.append(line[line.index('is an')+6:-2])
        if 'is' in line and 'is a' not in line and 'is an' not in line:
            flag=2
            before.append(line[:line.index('is')-1])
            after.append(line[line.index('is')+3:-2])
        to_add=''
        l2=line.split()
        l2.insert(1,',')
        l2.insert(-1,',')
        for t in l2:
            to_add+=t+' '
        output.write(to_add[:-2]+'\n')

    content=contents_of_input_file
    for line in content:
        if 'is' not in line and after[0] in line or after[0]+'s' in line:
            l=line.split()
            l[-1]=before[0].lower()+'.'
            fline=''
            for i in range(len(l)):
                if i==0:
                    last_word_list.append(l[i])
                elif i==len(l)-2:
                    fline+=l[i]+' the '
                else:
                    fline+=l[i]+' '
            fline_list.append(fline[:-1])
            #print(fline_list[0])

    content=contents_of_input_file
    for line in content:
        if fline_list[0] in line:
            first_word=line[:line.index(fline_list[0])-1]
            first_word_list.append(first_word)

    #print(first_word_list, last_word_list)
    output.write(first_word_list[0]+' , is a , '+last_word_list[0])
    output.close()


#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "data//input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code
