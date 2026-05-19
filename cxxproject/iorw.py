
import os
import shutil

def read_json(json_file:str) -> dict:
    with open(json_file,"r") as f:
        return __import__("json").load(f)

def write_json(json_file:str,data:dict) -> None:
    with open(json_file,"w") as f:
        __import__("json").dump(data,f)

def read_file(txt_file:str) -> list[str]:
    with open(txt_file,"r") as f:
        return f.readlines()

def write_file(txt_file:str,data:list[str]) -> None:
    with open(txt_file,"w") as f:
        f.writelines(data)

def copy_file(source_file:str,dest_file:str) -> None:
    shutil.copy(source_file,dest_file)

def copy_dir(source_dir:str,dest_dir:str) -> None:
    shutil.copytree(source_dir,dest_dir)

#todo this could be generalized with a dictionnary
#that contains all the # variables to replace
def generate_file_from_template(template_file:str,
                                target_file:str,
                                project_name:str) -> None:
    #reading the template
    file=read_file(template_file)
    new_data=[]
    temp_buffer=""
    for line in file:
        if("°" in line):
            temp_buffer=line.replace("°",project_name)
            new_data.append(temp_buffer)
        else:
            new_data.append(line)
    #creating the new file from the template
    write_file(target_file,new_data)

def create_directories(directories:list[str]) -> None:
    for directory in directories:
        os.makedirs(directory,exist_ok=True)

#todo this could be generalized
def concatenate_paths(prefix:str,suffix:str) -> str:
    return prefix+"/"+suffix
