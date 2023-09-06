import icon_get
import shortcut_create
from shutil import move

desktop_address = icon_get.find_desktop_addr()
ORI_PATH = desktop_address
DST_PATH = desktop_address + "\\"
BACKUP_PATH = "./backup/"


def collect_ori_file(ori_file_list):
    try:
        for ori_file in ori_file_list:
            move(ORI_PATH + "\\" + ori_file, BACKUP_PATH)
        print("备份成功")
    except Exception as e:
        print(e)
        raise RuntimeError("备份失败，程序无法进行")


if __name__ == "__main__":
    normal_file_list, hidden_file_list, system_file_list = icon_get.file_in_dic(
        ORI_PATH
    )
    icon_get.get_file_icon_t(ORI_PATH, normal_file_list, 10)
    icon_get.png2ico()
    collect_ori_file(normal_file_list)
    shortcut_create.group_create_shortcut(DST_PATH)
