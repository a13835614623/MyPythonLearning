#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月11日

@author: zzk
'''


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def log(text):

        def decorator(func):

            def wrapper(*args, **kw):
                print('%s %s()...' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator


import unittest


class Test_Dict(unittest.TestCase):

    @log('Test_Dict:call ')
    def test_init(self):
        d = Dict(a=1, b='zzk')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'zzk')
        self.assertTrue(isinstance(d, dict))

    @log('Test_Dict:call ')
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    @log('Test_Dict:call ')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    @log('Test_Dict:call ')
    def test_keyerror(self):
        # 通过d['empty']访问不存在的key时，断言会抛出KeyError
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    @log('Test_Dict:call ')
    def test_attrerror(self):
        # d.empty访问不存在的key时，我们期待抛出AttributeError        
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()
