import ntpath,zlib,base64
key='#'
t='.txt'
j='.jpg'
jp='.jpeg'
p='.png'
m='.ogg'
mp='.mp4'
def filename_path(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def compress(file_name,path='./'):
     backupname = file_name + '.' + self.backupextension
    if file_name.lower().endswith(t):
        file=open(file_name,"r")
        text =file.read()
        code =  base64.b64encode(zlib.compress(text,9))
        with open("compressed_file_name.zlib","wb") as myfile:
            myfile.write(code)
            key='text'
            return './' + 'compressed_file_name.zlib'
    elif file_name.lower().endswith(m):
        from pydub import AudioSegment
        sound = AudioSegment.from_file("file_name")
        sound.export("compressed_file_name", format="mp3", bitrate="128k")
    elif file_name.lower().endswith(mp):
        pass
    elif file_name.lower().endswith(jp) or file_name.lower().endswith(j) or file_name.lower().endswith(p):
        from PIL import Image, ImageFile
        from sys import exit, stderr
        from os.path import getsize, isfile, isdir, join
        from os import remove, rename, walk, stat
        from stat import S_IWRITE
        from shutil import move
        from argparse import ArgumentParser
        from abc import ABCMeta, abstractmethod
        class ProcessBase:
            """Abstract base class for file processors."""
            __metaclass__ = ABCMeta

            def __init__(self):
                self.extensions = []
                self.backupextension = 'compressimages-backup'

            @abstractmethod
            def processfile(self, file_name):
                """Abstract method which carries out the process on the specified file.
                Returns True if successful, False otherwise."""
                if(file_name==NONE):
                    return false
                else:
                    return true
            def processdir(self, path):
                """Recursively processes files in the specified directory matching
                the self.extensions list (case-insensitively)."""

                filecount = 0 # Number of files successfully updated

                for root, dirs, files in walk(path):
                    for file in files:
                        # Check file extensions against allowed list
                        lowercasefile = file.lower()
                        matches = False
                        for ext in self.extensions:
                            if lowercasefile.endswith('.' + ext):
                                matches = True
                                break
                        if matches:
                            # File has eligible extension, so process
                            fullpath = join(root, file)
                            if self.processfile(fullpath):
                                filecount = filecount + 1
                return filecount

        class CompressImage(ProcessBase):
            """Processor which attempts to reduce image file size."""
            def __init__(self):
                ProcessBase.__init__(self)
                self.extensions = ['jpg', 'jpeg', 'png']

            def processfile(self, file_name):
                """Renames the specified image to a backup path,
                and writes out the image again with optimal settings."""
                try:
                    # Skip read-only files
                    if (not stat(file_name)[0] & S_IWRITE):
                        print ('Ignoring read-only file "' + file_name + '.')
                        return False
                    if isfile(backupname):
                        print ('Ignoring file "' + file_name + '" for which existing backup file is present.')
                        return False

                    rename(file_name, backupname)
                except Exception as e:
                    stderr.write('Skipping file "' + file_name + '" for which backup cannot be made: ' + str(e) + '\n')
                    return False

                ok = False

                try:
                    # Open the image
                    with open(backupname, 'rb') as file:
                        img = Image.open(file)

                        # Check that it's a supported format
                        format = str(img.format)
                        if format != 'PNG' and format != 'JPEG':
                            print ('Ignoring file "' + file_name + '" with unsupported format ' + format)
                            return False

                        # This line avoids problems that can arise saving larger JPEG files with PIL
                        ImageFile.MAXBLOCK = img.size[0] * img.size[1]

                        # The 'quality' option is ignored for PNG files
                        img.save(file_name, quality=90, optimize=True)
                    # Check that we've actually made it smaller
                    origsize = getsize(backupname)
                    newsize = getsize(file_name)

                    if newsize >= origsize:
                        print ('Cannot further compress "' + file_name + '.')
                        return False

                    # Successful compression
                    ok = True
                except Exception as e:
                    stderr.write('Failure whilst processing "' + file_name + '": ' + str(e) + '\n')
                finally:
                    if not ok:
                        try:
                            move(backupname, file_name)
                        except Exception as e:
                            stderr.write('ERROR: could not restore backup file for "' + file_name + '": ' + str(e) + '\n')

                key='jpeg+png+jpg' 
                return ok
    elif file_name.lower().endswith('.zlib'):
        print('This file is already compressed')
        return -2
    else :
        print('This file format is not supported')
        return -1
    return backupname
"""#decompression    
def decompress(file_name,path='./'):
    from PIL import Image, ImageFile
    from sys import exit, stderr
    from os.path import getsize, isfile, isdir, join
    from os import remove, rename, walk, stat
    from stat import S_IWRITE
    from shutil import move
    from argparse import ArgumentParser
    from abc import ABCMeta, abstractmethod  
    if file_name.lower().endswith('.zlib'):
        if key=='text':
            pass
        elif key=='jpeg+png+jpg':
            
            class RestoreBackupImage(ProcessBase):
                 """Processor which restores image from backup."""
 
                 def __init__(self):
                        ProcessBase.__init__(self)
                        self.extensions = [self.backupextension]

                 def processfile(self, filename):
                        """Moves the backup file back to its original name."""
                        try:
                            move(filename, filename[: -(len(self.backupextension) + 1)])
                            return True
                        except Exception as e:
                            stderr.write('Failed to restore backup file "' + filename + '": ' + str(e) + '\n')
                            return False
             
            class DeleteBackupImage(ProcessBase):
                """Processor which deletes backup image."""
             
                def __init__(self):
                    ProcessBase.__init__(self)
                    self.extensions = [self.backupextension]
             
                def processfile(self, filename):
                    """Deletes the specified file."""
                    try:
                        remove(filename)
                        return True
                    except Exception as e:
                        stderr.write('Failed to delete backup file "' + filename + '": ' + str(e) + '\n')
                        return False
    else:
        print('This file format is not supported')
        return -1
"""        
def decompress(file_name,path='./'):
    str_object1 = open('compressed_file', 'rb').read()
    str_object2 = zlib.decompress(str_object1)
    f = open('my_recovered_log_file', 'wb')
    f.write(str_object2)
    f1=open('str_object2','r')
    x=f1.read()
    print("decompressed file:")
    print(x)
    f1.close()
    f.close()
    
o=input('Select the desired option \n 1.Compress a file. \n 2.Decompress a file. \n 3.Check if the file is already compressed. \n ')
path=raw_input('Please give the file path \n')
if o==1:
    result=compress(filename_path(path),path)
elif o==2:
    result=decompress(file_path(path),path)
else:
    result=compress(filename_path(path),path)
if o!=-1:
    print('The compressed file is stored at ')
    print(result)
elif o!=-2:
    print('The compressed file is stored at ')
    print(result)
x=raw_input('Enter any key to exit the terminal')    
