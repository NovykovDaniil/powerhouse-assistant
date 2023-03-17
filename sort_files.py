import os
import shutil, tarfile
import sys
from os import path
import re


class CreateDirectory:
    def create_directory(self, path_1):
        folder_name = ['images','video','documents','audio','archives','other']
        names = os.listdir(path_1)
        for i in folder_name:
            path_dir = os.path.join(path_1, i)
            if i not in names:
                os.makedirs(path_dir)


class Normalize:
    def normalize(self, path_1):
        a = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ё': 'e', 'e': 'e', 'ж': 'j',
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
        for i in names:
            path_file = os.path.join(path_1, i)
            if os.path.isfile(path_file):
                tbl = i.maketrans(a)
                c = i.translate(tbl)
                pref, suf = path.splitext(c)
                p = re.sub(r"(\W)", '_', pref)
                g = p + suf
                new_name = os.path.join(path_1, g)
                final = os.rename(path_file, new_name)
            else:
                self.normalize(path_file)
                

class SortFiles:
    
    path_root = os.path.join(sys.argv[1])
    
    
    def sort_files(self, path_1):
        folder_name = ['images','video','documents','audio','archives','other']
        suf_unknow = []
        suf_know = []
        names = os.listdir(path_1)
        for files in names:
            path_images = os.path.join(self.path_root, 'images')
            path_video = os.path.join(self.path_root, 'video')
            path_documents = os.path.join(self.path_root, 'documents')
            path_audio = os.path.join(self.path_root, 'audio')
            path_archives = os.path.join(self.path_root, 'archives')
            path_other = os.path.join(self.path_root, 'other')
            if files not in folder_name:
                path_dir = os.path.join(path_1, files)
                if os.path.isdir(path_dir):
                    self.sort_files(path_dir)
                    os.rmdir(path_dir)
                elif os.path.isfile(path_dir):
                    if '.png' in files or '.jpeg' in files or '.jpg' in files or '.svg' in files:
                        shutil.move(path_dir, path_images)
                        x, y = path.splitext(files)
                        suf_know.append(y) 
                    elif '.avi' in files or '.mp4' in files or '.mov' in files or '.mkv' in files:
                        shutil.move(path_dir, path_video)
                        x, y = path.splitext(files)
                        suf_know.append(y)
                    elif '.doc' in files or '.docx' in files or '.txt' in files or '.pdf' in files or '.xlsx' in files or '.pptx' in files:
                        shutil.move(path_dir, path_documents)
                        x, y = path.splitext(files)
                        suf_know.append(y)
                    elif '.mp3' in files or '.ogg' in files or '.wav' in files or '.amr' in files:
                        shutil.move(path_dir, path_audio)
                        x, y = path.splitext(files)
                        suf_know.append(y)
                    elif '.zip' in files or '.tar' in files or '.gz' in files:
                        pref, suf = path.splitext(files)
                        suf_know.append(suf)
                        path_name_archive = os.path.join(path_archives, pref)
                        shutil.unpack_archive(path_dir, path_name_archive)
                        os.remove(path_dir)
                    else:
                        shutil.move(path_dir, path_other)
                        n, m = path.splitext(files)
                        suf_unknow.append(m)
                else:
                    continue
            
        print(f'images - {os.listdir(path_images)}')
        print(f'video - {os.listdir(path_video)}')
        print(f'documents - {os.listdir(path_documents)}')
        print(f'audio - {os.listdir(path_audio)}')
        print(f'archives - {os.listdir(path_archives)}')
        print(f'other - {os.listdir(path_other)}')
        print(f'Перелік відомих розширень - {suf_know}')
        print(f'Перелік невідомих розширень - {suf_unknow}')
        

def main():
    CreateDirectory().create_directory(sys.argv[1])
    Normalize().normalize(sys.argv[1])
    SortFiles().sort_files(sys.argv[1])


if __name__ == '__main__':
    main()
