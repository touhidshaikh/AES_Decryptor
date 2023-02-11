import subprocess
import sys
import os
import argparse

def banner():
    banner = """\
aaa
"""
    return banner

def cmdline(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as error:
        return error.stderr.decode('utf-8').strip()

def combinations(words, length):
    if length == 0:
        return []
    result = [[word] for word in words]
    while length > 1:
        new_result = []
        for combo in result:
            new_result.extend([combo + [word] for word in words])
        result = new_result
        length -= 1
    return result

def main():
    if len(sys.argv) > 1:
        print(banner())

        parser = argparse.ArgumentParser(description='This is AES decryptor for Encrypted files. For Decryption, System required openssl utils in you system.')
        required_named = parser.add_argument_group('required named arguments')
        required_named.add_argument("-i", "--infile", help="Full path of Encrypted File.", required=True)
        required_named.add_argument("-w", "--wordlist", help="Full path of Wordlist File", required=True)
        required_named.add_argument("-o", "--ofilename", help="Output file name.", required=True)
        required_named.add_argument("-m", "--mode", help="Select any from aes-256-cbc or aes-256-ecb", required=True)

        args = parser.parse_args()

        efile = args.infile
        wordlist = args.wordlist
        mode = args.mode
        ofilename = args.ofilename

        with open(wordlist, 'r') as f:
            words = [line.strip() for line in f.readlines()]

        print("\n")
        res = combinations(words, 1)
        c = len(res) - 1
        for idx, result in enumerate(res):
            str1 = f"openssl {mode} -d -md sha256 -in {efile} -out {ofilename} -pass pass:{result[0]}"
            output = cmdline(str1)
            if not output:
                print(f"\n\033[1;32;40mKey Found! The key is:\033[0m\033[1;32;40m {result[0]} \033[0m")
                print(f"\033[1;31;40mOutput File Name: \033[1;32;40m {ofilename} \033[0m")
                sys.exit()
            print(f"{idx + 1}/{c} password: {result[0]} attempted")
        print("\n")
    else:
        print(banner())
        print("Usage %s [-h] --infile INFILE --wordlist WORDLIST \n--ofilename OFILENAME --mode MODE" % (sys.argv[0]))
if __name__ == '__main__':
    main()

