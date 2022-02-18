import sys
#import lesson_package.utils  # フルパスで書くとモジュールの場所がわかりやすい
from lesson_package import utils # 一般的に推奨
#from lesson_package import utils as u # 一般的に好まれない
# from lesson_package.utils import say_twice

# lesson_packageの関数呼び出し
r = utils.say_twice('hello')

print(r)
print(sys.argv)

for i in sys.argv:
    print(i)

