'''
Created on 15 May 2017

@author: wu
'''
import os


class path_to_conf_list(object):

    '''use to go through the folder to find certain files'''

    def __init__(self, path):

        self.path = path
        self.result_found = []

    def FindConffile(self, extension):
        # find certain file type (with extension name)in the path

        for (Rootpath, Foldernames, Filenames) in os.walk(self.path):
            for Names in Filenames:
                if extension in Names:

                    self.result_found.append(os.path.join(Rootpath, Names))

        print("{} files are found in folder {}".
              format(len(self.result_found), self.path))


path = r"H:\testConf"
test = path_to_conf_list(path)
test.FindConffile(extension="conf")
