# with open('3/pi.txt') as file_obj:
# with open('/Users/zhixin/Personal/2022-Python/codes/3/pi.txt') as file_obj:
#     contents=file_obj.read()
# print(contents)

# with open('3/pi.txt') as file_obj:
#     for line in file_obj:
#         print(line.rstrip())
#     lines=file_obj.readlines()

# for line in lines:
#     print(line.rstrip())

# with open('3/write.txt', 'w') as file_obj:
#     file_obj.write('I love python\n')
#     file_obj.write('I love python\n')
#     file_obj.write('I love python\n')

### exception
# try:
#     print(5/0)
#     # print(5/1)
# except ZeroDivisionError:
# except BaseException:
#     # print("zero can't divide")
#     pass
# else:
#     print('divided')

# raise BaseException('1')
# try:
#     print(5/0)
# except:
#     print("zero can't divide")
# finally:
#     print('end')
#     raise BaseException

### json
# import json
# sports=['a','b','c']
# dicts={'a':'a'}

# with open('3/test.json','w') as f:
#     # json.dump(sports,f)
#     json.dump(dicts,f)

# with open('3/test.json') as f:
#     # print(f.read())
#     print(json.load(f))

### unit test
# def format_name(first_name, last_name):
#     name=f'{first_name} {last_name}'
#     return name.title()

# import unittest
# class NamesTest(unittest.TestCase):
#     def test1(self):
#         name=format_name('Joda', 'link')
#         self.assertEqual(name, 'Joda Link')

# if __name__=='__main__':
#     unittest.main()
