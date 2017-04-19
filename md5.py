#!/usr/bin/env python

import struct
import math
import sys

class md5:
    def __init__(self,message = ""):
        # Initial value for magic number
        self.hashs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]
        # Continue with previous hash if message provided ( get back the magic number )
        if message:
           self.hashs = [ sum([ int(message[i+j:i+j+2],16) << (j*4) for j in xrange(0,8,2) ]) for i in xrange(0,len(message),8) ]
        self.functions = [lambda b, c, d: (b & c) | (~b & d)] + \
                         [lambda b, c, d: (d & b) | (~d & c)] + \
                         [lambda b, c, d: b ^ c ^ d] + \
                         [lambda b, c, d: c ^ (b | ~d)]
        self.indexs = [lambda i: i] + \
                      [lambda i: (5*i + 1)%16] + \
                      [lambda i: (3*i + 5)%16] + \
                      [lambda i: (7*i)%16]
        self.rotates = [7,12,17,22]*4+[5,9,14,20]*4+[4,11,16,23]*4+[6,10,15,21]*4
        self.constants = [ int((abs(math.sin(i+1)) * 2**32)) & 0xFFFFFFFF for i in xrange(64) ]
    def leftRotate(self,x,n):
        x &= 0xFFFFFFFF
        return (x << n) | (x >> (32-n)) & 0xFFFFFFFF
    def calculate(self,block):
        data = struct.unpack("16I",block)
        a, b, c, d = self.hashs
        for i in xrange(64):
            f = self.functions[i/16](b,c,d)
            g = self.indexs[i/16](i)
            bb = (b + self.leftRotate(a + f + self.constants[i] + data[g],self.rotates[i])) & 0xFFFFFFFF
            a, b, c, d = d, bb, b, c
        for index,value in enumerate([a, b, c, d]):
            self.hashs[index] += value
            self.hashs[index] &= 0xFFFFFFFF
    def padding(self,message):
        length = (56-len(message)%64+64)%64
        return message + ('\x80' + '\x00'*(length-1) if length else '') + struct.pack('Q',len(message)*8)
    def hash(self,message):
        message = self.padding(message)
        # Every 64 bytes will be a block
        for i in xrange(0,len(message),64):
            self.calculate(message[i:i+64])
        # Append magic number together ( answer )
        return "".join([ hex((x >> (i*8)) & 0xFF)[2:] for x in self.hashs for i in xrange(4) ])
        
if __name__ == '__main__':
    m = md5()
    if len(sys.argv) != 2:
        print "usage: python md5.py (value)"
        exit(1)
    print m.hash(sys.argv[1])
