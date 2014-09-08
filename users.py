# -*- coding: utf-8 -*-
import os
import hashlib

STRPWD = '729670FEBEAB7C1C82C6BA5B676BAF68'

def getUpperMD5(strPassword):
    '''获取全大写的MD5值'''
    return hashlib.md5(strPassword).hexdigest().upper()

def valid_password(password):
    '''校验密码是否正确，如果正确则返回True，否则返回False'''
    if getUpperMD5(password) == STRPWD:
        return True
    else:
        return False