#! /usr/local/bin/python3
import sys
import string
import random
import numpy as np
import pandas
from collections import Counter
import matplotlib.pyplot as plt


def hesh_0(v, key):
    """
    a really bad addative hash with extremely high collision rate for small inputs
    includes an int private key
    """

    key = int(key)
    v = bytearray(v, encoding='utf-8')
    
    l = len(v) 
    o = 0

    for i in range(l):
        for j in range(key):
            o += v[i]

    return o

def hesh_1(v, key):
    """
    a basic XOR hash with an int private key.
    choose prime integers as keys for minimal collision rate.
    """

    key = int(key)
    v = bytearray(v, encoding='utf-8')
    
    l = len(v) 
    o = 0

    for i in range(l):
        for j in range(key):
            o  ^= v[i]

    return o

def hesh_2(v, key):
    """
    this is the bare minimum which should be acceptable.
    this is a rotating hash with an additional int private key
    """

    key = int(key)
    v = bytearray(v, encoding='utf-8')
    
    l = len(v) 
    o = 0

    for i in range(l):
        o = (o << key) ^ (o >> 13) ^ v[i]

    return o


if __name__ == '__main__':
    print("hesh: a suite of hash functions designed by eli s. hickox")
    print("usage: ./heshlib.py [hash number] [key] [text to hash, or -t to test the hash]")

    hesh_fn = sys.argv[1]
    key = sys.argv[2]

    print('using hesh_'+sys.argv[1])
    print('input: '+sys.argv[3])

    if(hesh_fn == '0'):
        hashed = hesh_0(sys.argv[3], key)
        print(hashed)

        if len(sys.argv) > 3 and sys.argv[3] == '-t':
            print("testing and plotting distribution of hesh_"+sys.argv[1])

            num_datums = 1000
            datum_len = 256

            test_data = [''] * num_datums
            plot = [''] * num_datums

            for i in range(num_datums):
                test_data[i] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(datum_len))
                plot[i] = str(hesh_0(test_data[i], key))


            uniqe_vals = set(plot)
            words_by_freq = {}

            for i in uniqe_vals:
                words_by_freq[i] = plot.count(i)

            print(test_data)
            print(plot)
            print(words_by_freq)
            print("tested "+str(num_datums)+ " strings, and got "+str(len(uniqe_vals))+" unique hashes")

            counts = Counter(plot)
            df = pandas.DataFrame.from_dict(counts, orient='index')
            df.plot(kind='bar')
            plt.show()
            
    elif(hesh_fn == '1'):
        hashed = hesh_1(sys.argv[3], key)
        print(hashed)

        if len(sys.argv) > 3 and sys.argv[3] == '-t':
            print("testing and plotting distribution of hesh_"+sys.argv[1])

            num_datums = 1000
            datum_len = 256

            test_data = [''] * num_datums
            plot = [''] * num_datums

            for i in range(num_datums):
                test_data[i] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(datum_len))
                plot[i] = str(hesh_1(test_data[i], key))


            uniqe_vals = set(plot)
            words_by_freq = {}

            for i in uniqe_vals:
                words_by_freq[i] = plot.count(i)

            print(test_data)
            print(plot)
            print(words_by_freq)
            print("tested "+str(num_datums)+ " strings, and got "+str(len(uniqe_vals))+" unique hashes")

            counts = Counter(plot)
            df = pandas.DataFrame.from_dict(counts, orient='index')
            df.plot(kind='bar')
            plt.show()

    elif(hesh_fn == '2'):
        hashed = hesh_2(sys.argv[3], key)
        print(hashed)

        if len(sys.argv) > 3 and sys.argv[3] == '-t':
            print("testing and plotting distribution of hesh_"+sys.argv[1])

            num_datums = 1000
            datum_len = 256

            test_data = [''] * num_datums
            plot = [''] * num_datums

            for i in range(num_datums):
                test_data[i] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(datum_len))
                plot[i] = str(hesh_2(test_data[i], key))


            uniqe_vals = set(plot)
            words_by_freq = {}

            for i in uniqe_vals:
                words_by_freq[i] = plot.count(i)

            print(test_data)
            print(plot)
            print(words_by_freq)
            print("tested "+str(num_datums)+ " strings, and got "+str(len(uniqe_vals))+" unique hashes")

            counts = Counter(plot)
            df = pandas.DataFrame.from_dict(counts, orient='index')
            df.plot(kind='bar')
            plt.show()
    

    

    
