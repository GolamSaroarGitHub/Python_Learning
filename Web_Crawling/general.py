import os


def creat_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project '+directory)
        os.mkdir(directory)## creating directory
    else:
        print('The Project is already set up')
creat_project_dir('thenewboston')

# Create queue and crawled files

def create_data_files(project_name,base_url):

    queue=project_name+'/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,base_url)
        if not os.path.isfile(crawled):
            write_file(crawled, '')

#creates a new file

def write_file(path,data):

    f= open(path,'w')
    f.write(data)
    f.close()

create_data_files('thenewboston','https://thenewboston.com/')

# add data onto an existing file

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

#Delete the contents