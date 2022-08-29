# copy code

import shutil
source_folder = input('enter the file directory to be copied: ')
destination_folder = input('enter the directory to paste it: ')
shutil.copy(source_folder, destination_folder)
print('file copied\U0001F609')
