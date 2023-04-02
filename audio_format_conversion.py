from pydub import AudioSegment
import os
import tqdm


def print_format_menu():
    print("""
        1. mp3
        2. wav
        3. flv
        4. ogg
        5. raw
    """)


def order2format(num):
    if num == 1:
        return "mp3"
    elif num == 2:
        return "wav"
    elif num == 3:
        return "flv"
    elif num == 4:
        return "ogg"
    elif num == 5:
        return "raw"


def getTransform(format, filepath):
    if format == "mp3":
        return AudioSegment.from_mp3(filepath)
    elif format == "wav":
        return AudioSegment.from_wav(filepath)
    elif format == "flv":
        return AudioSegment.from_flv(filepath)
    elif format == "ogg":
        return AudioSegment.from_ogg(filepath)
    elif format == "raw":
        return AudioSegment.from_raw(filepath)


def transform(originFormat, newFormat, filePath, fileName, newPath=None):
    converter = getTransform(originFormat, filePath + "\\" + fileName)
    if newPath:
        newPath = newPath + "\\" + fileName.split(".")[0] + "." + newFormat
    else:
        newPath = filePath + "\\" + fileName.split(".")[0] + "." + newFormat

    converter.export(newPath, format=newFormat)
    print(newPath + " save")


if __name__ == '__main__':
    filePath = input("文件路径:")
    newPath = input("新的文件路径:")
    print_format_menu()
    originFormat = order2format(int(input("原格式(输入对应序号):")))
    newFormat = order2format(int(input("新格式(输入对应序号):")))
    files = 0
    if os.path.isdir(filePath):
        for file in os.listdir(filePath):
            transform(originFormat, newFormat, filePath, file, newPath)
    else:
        transform(originFormat, newFormat, filePath, newPath)
    print("finish")
