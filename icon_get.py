import os
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from PIL.Image import open

ICON_ADDRESS = "./icon_location/"


def find_desktop_addr() -> str:
    """

    :rtype: str
    :return: The address of Desktop
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")


def file_in_dic(addr: str):
    """
    在文件夹中搜索文件并分类
    :rtype: list with str in it
    :param addr: folds address
    :return: normal_file_list, hidden_file_list, system_file_list
    """
    _system_file_list = []
    _hidden_file_list = []
    _normal_file_list = os.listdir(addr)
    count = 0
    for item in _normal_file_list[:]:
        count += 1
        if item.startswith("~$"):
            _system_file_list.append(item)
            _normal_file_list.remove(item)
        elif item.startswith("~"):
            _hidden_file_list.append(item)
            _normal_file_list.remove(item)
        else:
            continue
    return _normal_file_list, _hidden_file_list, _system_file_list


def get_file_icon(file_path, file_list, count):
    """
    获得文件图标
    :param count: 线程标记
    :param file_path: 文件路径
    :param file_list: 文件列表
    """
    for item in file_list:
        print("当前活跃线程: %d\t处理 [%s]" % (count, item))
        os.system(
            "extracticon.exe %s %s"
            % (file_path + "\\" + item, ICON_ADDRESS + item + ".png")
        )


def get_file_icon_t(file_path, file_list, number_of_t=3):
    """
    获取文件图标多线程版
    :param file_path: 文件路径
    :param file_list: 文件列表
    :param number_of_t: 线程数
    """
    last_file = os.listdir(ICON_ADDRESS)
    for file in last_file:
        os.remove(ICON_ADDRESS + file)

    count = 1
    len_of_file_list = len(file_list)
    step = int(len_of_file_list / number_of_t + 0.999999999)
    thread_list = [file_list[i : i + step] for i in range(0, len_of_file_list, step)]
    print("文件列表总长度:%d\t线程数:%d\t单文件长度:%d" % (len_of_file_list, number_of_t, step))

    pool = ThreadPoolExecutor()
    future_list = []
    for list_for_one_thread in thread_list:
        t = pool.submit(
            lambda p: get_file_icon(*p), (file_path, list_for_one_thread, count)
        )
        future_list.append(t)
        count += 1
    wait(future_list, return_when=ALL_COMPLETED)


def png2ico(size=256) -> None:
    print("Changing .png to .ico")
    file_lists = os.listdir(ICON_ADDRESS)
    for png in file_lists:
        img = open(ICON_ADDRESS + png)
        img.resize((size, size)).save(
            ICON_ADDRESS + png.rpartition(".")[0] + ".ico", format="ICO"
        )
        os.remove(ICON_ADDRESS + png)


if __name__ == "__main__":
    desktop_address = find_desktop_addr()
    path = desktop_address
    normal_file_list, hidden_file_list, system_file_list = file_in_dic(path)
    get_file_icon_t(path, normal_file_list, 10)
    png2ico()
