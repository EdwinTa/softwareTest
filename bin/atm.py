# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/28
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':
    main.run()
