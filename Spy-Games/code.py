# --------------
##File path for the file 
file_path 

#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    
    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence


#Calling the function to read file
sample_message=read_file(file_path)

#Printing the line of the file
print(sample_message)

#Code ends here


# --------------
##File path for the file 
file_path_1
file_path_2

#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
    
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    
    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence


#Calling the function to read file
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
#Printing the line of the file
print(message_1)
print(message_2)


def fuse_msg(message_a,message_b):
    quotient=message_b//message_a    
    return quotient

secret_msg_1=str(fuse_msg(2,3))
print(secret_msg_1)

#Code ends here


# --------------
#Code starts here
file_path_3

def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence

message_3=read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if str(message_c) == 'Red':
        sub = 'Army General'
        return str(sub)
        
    elif str(message_c) == 'Green':
        sub = 'Data Scientist'
        return str(sub)
        
    elif str(message_c) == 'Blue':
        sub = 'Marine Biologist'
        return str(sub)
secret_msg_2=str(substitute_msg(message_3))
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e ):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=set(a_list)-set (b_list)
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)
    
   








# --------------
#Code starts here
file_path_6

def readfile(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence

message_6=readfile(file_path_6)
print(message_6)

def extract_msg(message_f):
    a_list=message_f.split()
    even_word=filter(lambda x: (len(x)%2==0),a_list)
    b_list=list(even_word)
    print(b_list)
    final_msg=" ".join(b_list)
    return final_msg

secret_msg_4=extract_msg(message_6)
print(secret_msg_4)




# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

#Combining the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
#     #Opening a file named 'secret_message' in 'write' mode
    file = open(path, 'a+')

#     #Writing to the file
    file.write(secret_msg)

#     #Closing the file
    file.close()

# #Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here


