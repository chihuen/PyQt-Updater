import os
import sys


def main():
    ui_path = sys.argv[1]
    py_path = ui_path.replace('.ui', '.py')
    print("pyuic5 {ui_path} -o {py_path}".format(ui_path=ui_path, py_path=py_path))
    os.system("pyuic5 {ui_path} -o {py_path}".format(ui_path=ui_path, py_path=py_path))


if __name__ == '__main__':
    main()