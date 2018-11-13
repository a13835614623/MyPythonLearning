#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2018年11月11日

@author: zzk
'''
def abs(n):
    '''
    Function to get absolute value of number.

    Example:
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
if __name__=='__main__':
    import doctest
    doctest.testmod()
