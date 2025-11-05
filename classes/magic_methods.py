# """Aim of this module is to explore the magic methods of the python classes"""
#
# # Members in python
# class Simple_class:
#     """just a simple docstring"""
#     member = 10
#     _hidden_member = 15
#     __very_hidden_member = 20
#
#     def __init__(self, value):
#         self.value = value
#
#     def print_hello(self):
#         print(f"Hello: {self.value}")
#
#
#
# instance = Simple_class(10)
# print(instance.member)
# print(instance._hidden_member)
# # print(instance.__very_hidden_member)
# print(instance._Simple_class__very_hidden_member)
#
# print(dir(instance))
#
#
# # User defined context manager
# class ContextManager:
#
#
#     def __init__(self, val):
#         self.value = val
#
#     def __enter__(self):
#         print("entered context manager")
#         return "just an object representing context manager"
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("closed the context manager")
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#
# with ContextManager(15) as val:
#     print(val)


def is_doc(content):
    return False




class DOCFileContextManager:

    def __init__(self, path, mode, *args):
        self.path = path
        self.mode = mode


    def __enter__(self):
        self.file_obj = open(self.path, self.mode)
        if not is_doc(self.file_obj):
            raise Exception("vay qu")
            self.file_obj.close()
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass






def new_open(path, mode):
    return DOCFileContextManager(path, mode)



file_path = r"C:\Users\vdavtyan\Downloads\scripting_language (1)\scripting_language\Python_1.pptx"


with new_open(file_path, 'rt') as a:
    print('hey')
