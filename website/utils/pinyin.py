# -*- coding: gbk -*-
# $Id$
# Copyright 2010 Yefe<yefe@ichuzhou.cn>
import os


class Hanzi2Pinyin(object):
    def __init__(self):
        self.table = {}
        try:
            fp = open(os.path.join(os.path.dirname(__file__), 'pinyin.txt'))
        except IOError:
            raise Exception("Can't load data from pinyin.txt\nPlease make sure this file exists.")
        else:
            self.data = fp.read().decode('gbk')
            for l in self.data.split('\n'):
                self.table[l[0]] = l[1:]
            fp.close()

    def convert(self, value):
        pinyin = []
        tASCII = ''
        # �ַ����
        for c in value.lower() + ' ': # �Ӹ��ո��һ��ѭ�� ����β���ַ���ʧ����
            # ��ʵ֤�� ord �� has_key Ҫ��ʡ���ܣ� ord ��ǰ�������ж�
            i = ord(c)
            if (i >= 48 and i <= 57) or (i >= 97 and i <= 122): # 48-57[0-9]   97-122[a-z]
                tASCII += c
                continue
            
            tASCII and pinyin.append(tASCII)
            tASCII = ''
            
            if self.table.has_key(c):
                pinyin.append(self.table[c])
                continue
        
        return pinyin


if __name__ == '__main__':
    import time
    t = u'Prep ���    �� ����I Love China! 2010��8�� !@    #   $%^   &* ()_+   Append'
    s = time.time()
    p = Hanzi2Pinyin() # you class
    print 'init:', time.time() - s
    s = time.time()
    print '-'.join(p.convert(t)) # you convert
    for i in xrange(0,10000):
        p.convert(t) # you convert
    print 'convert:', time.time() - s


