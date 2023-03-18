import os
import shutil
import sys
from os import path
import re


class CreateDirectory:
    def create_directory(self, path_1):
        folder_name = ['images','video','documents','audio','archives','other']
        names = os.listdir(path_1)
        for folders in folder_name:
            path_dir = os.path.join(path_1, folders)
            if folders not in names:
                os.makedirs(path_dir)


class Normalize:
    def normalize(self, path_1):
        words_list = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ё': 'e', 'e': 'e', 'ж': 'j',
             'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
             'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
             'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
             'я': 'ya', 'є': 'je', 'і': 'i', 'ї':'ji', 'ґ': 'g', 'А': 'A', 'Б': 'B', 'В': 'V',
             'Г': 'G', 'Д': 'D', 'Ё': 'E', 'Е': 'E', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'J',
             'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
             'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch',
             'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'Є': 'Je', 'І': 'I',
             'Ї':'Ji', 'Ґ': 'G'}
        names = os.listdir(path_1)
        for words in names:
            path_file = os.path.join(path_1, words)
            if os.path.isfile(path_file):
                tbl = words.maketrans(words_list)
                change_words = words.translate(tbl)
                pref, suf = path.splitext(change_words)
                change_title = re.sub(r"(\W)", '_', pref)
                join_words = change_title + suf
                new_name = os.path.join(path_1, join_words)
                final = os.rename(path_file, new_name)
            else:
                self.normalize(path_file)
                

class SortFiles:
    path_root = sys.argv[1]
    
    def sort_files(self, path_1):  
        ignore_name = ['images','video','documents','audio','archives','other']
        list_files = {('png', 'jpeg', 'jpg', 'svg'): 'images',
                      ('.avi', '.mp4', '.mov', '.mkv'): 'video',
                      ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'): 'documents',
                      ('.mp3', '.ogg', '.wav', '.amr'): 'audio',
                      ('.zip', '.tar', '.gz'): 'archives'}
        names = os.listdir(path_1)
        path_other = os.path.join(self.path_root, 'other')
        for files in names:
            if files not in ignore_name:
                path_dir = os.path.join(path_1, files)
                if os.path.isdir(path_dir):
                    self.sort_files(path_dir)
                    os.rmdir(path_dir)
                elif os.path.isfile(path_dir):
                    for expansion in list_files:
                        if files.split('.')[-1] in expansion:
                            new_path = os.path.join(self.path_root, list_files[expansion])
                            shutil.move(path_dir, new_path)
                        else:
                            shutil.move(path_dir, path_other)
                        break
                else:
                    continue


CreateDirectory().create_directory(sys.argv[1])
Normalize().normalize(sys.argv[1])
SortFiles().sort_files(sys.argv[1])