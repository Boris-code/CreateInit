# -*- coding: utf-8 -*-
'''
Created on 2018-09-29 12:26
---------
@summary: 创建__init__.py
---------
@author: liubo
'''


import sublime_plugin
import os
import json


class CreateInitCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        __all__ = []

        path = self.view.file_name()
        path = os.path.dirname(path)
        for file in os.listdir(path):
            if file.endswith('.py') and not file.startswith('__init__'):
                model = file.split(".")[0]
                __all__.append(model)

        init_file = os.path.join(path, '__init__.py')
        with open(init_file, 'w') as file:
            text = '__all__ = %s' % json.dumps(__all__, ensure_ascii=False, indent=4, skipkeys=True)
            file.write(text)
