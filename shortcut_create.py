from win32com.client import Dispatch
from os import listdir, getcwd

ICON_ADDRESS = "./icon_location/"
DST_ADDRESS = "./fake_desktop/"
TARGET = "https://ys.mihoyo.com/"


def create_shortcut(path, target="", icon=""):
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()


def group_create_shortcut(dist_folder=DST_ADDRESS):
    file_list = listdir(ICON_ADDRESS)
    work_path = getcwd()
    print(file_list)
    for file in file_list:
        file_name = file[:-4]
        if file_name[-4:] == ".lnk" or file_name[-4:] == ".url":
            path = dist_folder + file_name
        else:
            path = dist_folder + file_name + ".lnk"
        target = TARGET
        icon = work_path + "/" + ICON_ADDRESS + file_name + ".ico"
        create_shortcut(path, target, icon)


if __name__ == "__main__":
    group_create_shortcut()
