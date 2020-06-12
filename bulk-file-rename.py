import os
import glob


def file_sort_bymod():
    files = glob.glob("files/*")
    files_sorted = files.sort(key=lambda x: os.path.getmtime(x))
    files_sorted_noext = [f.split('\\')[1] for f in files]

    for i, filename in enumerate(files_sorted_noext, 1):
        n = 1
        src = 'files\\' + filename
        n += 1

        if format_select == 1:
            dst = f'files\\{i}  {filename}'
            dst_read = dst.split('\\')[1]
            os.rename(src, dst)
            print(f'\n{i}  Renamed {filename} as > {dst_read}')
        elif format_select == 2:
            dst = f'files\\{i} -- {filename}'
            dst_read = dst.split('\\')[1]
            os.rename(src, dst)
            print(f'\n{i}  Renamed {filename} as > {dst_read}')
        elif format_select == 3:
            dst = f'files\\({i}) {filename}'
            dst_read = dst.split('\\')[1]
            os.rename(src, dst)
            print(f'\n{i}  Renamed {filename} as > {dst_read}')

    print(f"\nSuccessfully renamed {n} files!\n")


if __name__ == '__main__':
    print(
        "You are using Mr Beels' Bulk File Rename Script! \nCheck out : https://github.com/mrbeels \n\n    ( ͡° ͜ʖ ͡°) ¯\_(ツ)_/¯ \n")
    format_select = int(input(
        "\nFormats available : \n\n [1] i  filename \n [2] i -- filename\n [3] (i) filename\n\nType your format : "))
    file_sort_bymod()
