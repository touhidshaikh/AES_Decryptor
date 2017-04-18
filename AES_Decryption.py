#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import argparse

PWD = os.getcwd()

def banner():
    banner = """\
\033[1;31;40m     _    _____ ____   \033[1;32;40m ____                       _             \033[0m
\033[1;31;40m    / \  | ____/ ___|  \033[1;32;40m|  _ \  ___  ___ _ __ _ __ | |_ ___  _ __ \033[0m
\033[1;31;40m   / _ \ |  _| \___ \  \033[1;32;40m| | | |/ _ \/ __| '__| '_ \| __/ _ \| '__|\033[0m
\033[1;31;40m  / ___ \| |___ ___) | \033[1;32;40m| |_| |  __/ (__| |  | |_) | || (_) | |   \033[0m
\033[1;31;40m /_/   \_\_____|____/  \033[1;32;40m|____/ \___|\___|_|  | .__/ \__\___/|_|   \033[0m
\033[1;31;40m                       \033[1;32;40m                     |_|                  \033[0m
\033[1;31;40mvisit : http://www.touhidshaikh.com Author : \033[1;33;40m @touhidshaikh22\033[0m  
"""
    return banner

def cmdline(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return err

def combinations(words, length):
    if length == 0:
        return []
    result = [[word] for word in words]
    while length > 1:
        new_result = []
        for combo in result:
            new_result.extend(combo + [word] for word in words)
        result = new_result[:]
        length -= 1
    return result

def main():

    if (len(sys.argv) > 1):

        print banner()


        parser = argparse.ArgumentParser()

        parser = argparse.ArgumentParser(description='This is AES decryptor for Encrypted files. For Decryption, System required openssl utils in you system.')
        requiredNamed = parser.add_argument_group('required named arguments')
        requiredNamed.add_argument("-i","--infile", help="Full path of Encrypted File.",required=True)
        requiredNamed.add_argument("-w","--wordlist", help="Full path of Wordlist File",required=True)
        requiredNamed.add_argument("-o","--ofilename", help="Output file name.",required=True)
        requiredNamed.add_argument("-m","--mode", help="Select any from aes-256-cbc or aes-256-ecb",required=True)

        args = parser.parse_args()

        efile = args.infile
        wordlist = args.wordlist
        mode = args.mode
        ofilename = args.ofilename

        words = [line.strip() for line in open(wordlist)]
        print("\n")
        res = combinations(words, 1)
        c = len(res)-1
        for idx, result in enumerate(res):

            str1 = "openssl %s -d -md sha256 -in %s -out %s -pass pass:"%(mode,efile,ofilename)
            str1 = str1+result[0]
            if cmdline(str1) == "":
                print("\n\033[1;32;40mKey Found! The key is:\033[0m\033[1;32;40m "+result[0]+"\033[0m")
                print "\033[1;31;40mOutput File Name : \033[1;32;40m %s \033[0m"%(ofilename)
                sys.exit()
            print(str(idx)+"/"+str(c)+" password : "+result[0]+" Attempted key ")
        print("\n")

    else:
        print banner()
        print """Usage %s [-h] --infile INFILE --wordlist WORDLIST \n--ofilename OFILENAME --mode MODE"""%(sys.argv[0])
if __name__ == '__main__':
    main()
