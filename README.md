## 原神，启动！

*原友推广小脚本*

> 你还在为没办法向朋友推广原神而担忧吗？你还在担心你的至亲好友错过这款绝世佳作吗？
> 不要紧，从今天起，你有一个绝佳的机会，使用 “原神，启动！”小组件，向你的亲友推广
> 原神罢！

### 食用方式

---

#### python,启动！

安装requirements中的运行库（具体为：PIL + pywin32），然后直接运行main.py即可

#### 我不知道如何使python,启动

下载release中打包好的文件

### 使用效果

---

会自动将桌面所有文件备份到```./backup```文件夹，并创建看上去几乎一样的图标，实际上全都链接到原神官网

### 注意事项

---

- 需要保证根目录有```./backup``` ```./icon_location```文件夹，```extracticon.exe```文件，并且目录```./backup```为空
- 恢复文件将桌面快捷方式都删掉，并把```./backup```文件夹里的东西塞回桌面即可
- 千万不要将本文件夹放在桌面执行（详见：完全可以预见的BUG）
- 理论上不会误删任何文件，但是最好还是手动备份

### 完全可以预见的BUG/问题

---

- 当文件在桌面运行时，他会移动自己，产生错误
- 使用了extraction.exe（来自: [ExtractIcon](https://github.com/bertjohnson/ExtractIcon)）部分图标可能出现略微的错误
- 并不能显示缩略图
- 会有快捷方式小箭头
- 无法保持原始的桌面文件排序/位置

## Genshin, Start!



*A script popularized genshin impact*

> Are you still worried about promoting the Genshin Impact to your friends? Are you still worried about your loves missing out on this MASTERPIECE?
> No worry, there you have a chance today, using "genshin, start" to introduce genshin to people around you!

### Usage

---

#### python, start

Just do pip install to requirements.txt(PIL/pywin32), and run main.py

#### python, HOW TO start?

Download the packaged file from release

### Effect

---

Will automatically back up all files on the desktop to the```./backup``` folder and create ICONS that look almost identical and actually all link to the Genshin Impact website

### Mention

---

- Guarantee ```./backup``` ```./icon_location```, ```extracticon.exe``` in the root, with```./backup``` empty
- To recover the file, just move out the file from```./backup```
- NEVER USE THE PROGRAM ON DESKTOP!!!!!! (Detail: All the BUGs can be seen)
- You are not suppose to losing any file(or folder) by this. However, copy it to a safe place is a cleverer choice.

### All the BUGs can be seen

---

- When the file is running on the desktop, the program moves itself, causing errors
- Using extraction.exe（From: [ExtractIcon](https://github.com/bertjohnson/ExtractIcon)）Some ICONS may be slightly wrong
- Does not display thumbnails
- There will be shortcuts small arrows
- Unable to keep original desktop file order/location