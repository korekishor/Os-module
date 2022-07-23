from fileinput import filename
import os
from datetime import datetime
from posixpath import dirname
import time


# print(dir(os))

"""
currentworkingdirectory=os.getcwd()
# print(currentworkingdirectory)

os.chdir('C:/Users/Kishor Kore/Desktop/')

print(os.getcwd())

"""


"""
print(os.listdir('C:/Users/Kishor Kore/Desktop/'))

"""


"""
os.chdir('C:/Users/Kishor Kore/Desktop/os module')

os.mkdir('os-module2')
os.makedirs('os-module3/sub-module')

print(os.listdir())

os.rmdir('os-module2')
os.removedirs('os-module3/sub-module')

print(os.listdir())

os.rename('os-module2.py','newnamemodule.py')

"""


"""

data=os.stat('osmodule1.py')
print(data)
print(data.st_size)
print(data.st_mtime)
# in human readebale time data
mod_time=datetime.fromtimestamp(data.st_mtime)
print(mod_time)

"""



"""
os.chdir('C:/Users/Kishor Kore/Desktop')

for dirpath,dirname,filename in os.walk('C:/Users/Kishor Kore/Desktop/'):
    print(dirpath)
    print(dirname)
    print(filename)
    print()

"""


"""
os.chdir('C:/Users/Kishor Kore/Desktop/')
print(os.path.exists('C:/Users/Kishor Kore/Desktop/'))
print(os.path.isdir('C:/Users/Kishor Kore/Desktop/'))
print(os.path.splitext('C:/Users/Kishor Kore/Desktop/'))
"""

# print(dir(os.path))


"""

['__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', '_abspath_fallback',
'_get_bothseps', '_getfinalpathname', '_getfinalpathname_nonstrict', '_getfullpathname',
'_getvolumepathname', '_nt_readlink', '_readlink_deep', 'abspath', 'altsep', 'basename',
'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 
'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime',
'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase',
'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile',
'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
print(os.path.getsize('c:/Users/Kishor Kore/Desktop/'))
print(os.path.getmtime('c:/Users/Kishor Kore/Desktop/'))
print(os.path.getatime('c:/Users/Kishor Kore/Desktop/'))
print(os.path.getctime('c:/Users/Kishor Kore/Desktop/'))

"""


"""
get_dir=os.getcwd()
# print(get_dir)

time.sleep(2)

os.chdir('c:/Users/Kishor Kore/Desktop/')
os.makedirs('new_dirs')
os.rename('new_dirs','new_dirs2')

time.sleep(2)

os.removedirs('new_dirs2')
"""

# help(os)


















