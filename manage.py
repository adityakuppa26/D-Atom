import ntpath,zlib,base64
def filename_path(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def compress(file_name,path='./'):
  if file_name.lower().endswith('.txt')
   file=open("file_name.txt","r")
   text =file.read()
   code =  base64.b64encode(zlib.compress(text,9))
   with open("compressed_file_name.zlib","wb") as myfile:
       myfile.write(code)
  elif file_name.lower().endswith('.mp3'):
    pass
  elif file_name.lower().endswith('.mp4'):
    pass
  elif file_name.lower().endswith('.jpeg'):
    pass
  elif file_name.lower().endswith('.png'):
    pass
  elif file_name.lower().endswith('.zlib'):
    print('This file is already compressed')
    return -2
  else :
    print('This file format is not supported')
    return -1
def decompress(file_name,path='./'):
    if file_name.lower().endswith('.zlib'):
        pass
    else:
        print('This file format is not supported')
        return -1
o=input('Select the desired option \n 1.Compress a file. \n 2.Decompress a file. \n 3.Check if the file is already compressed. \n ')
p=raw_input('Please give the file path \n')
if o==1:
    result=compress(filename_path(p),p)
elif o==2:
    result=decompress(file_path(p),p)
else:
    result=compress(filename_path(p),p)
if o!=-1 or o!=-2:
    print('The compressed file is stored at ')
    print(result)
    
