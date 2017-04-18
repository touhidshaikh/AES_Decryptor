# AES_Decryptor
This tool help you to decryption of AES Encrypted file in very easy way.



     _    _____ ____    ____                       _             
    / \  | ____/ ___|  |  _ \  ___  ___ _ __ _ __ | |_ ___  _ __ 
   / _ \ |  _| \___ \  | | | |/ _ \/ __| '__| '_ \| __/ _ \| '__|
  / ___ \| |___ ___) | | |_| |  __/ (__| |  | |_) | || (_) | |   
 /_/   \_\_____|____/  |____/ \___|\___|_|  | .__/ \__\___/|_|   
                                            |_|                  
visit : http://www.touhidshaikh.com Author :  @touhidshaikh22  

usage: aes_bruteforce_decryptor.py [-h] -i INFILE -w WORDLIST -o OFILENAME -m
                                   MODE

This is AES decryptor for Encrypted files. For Decryption, System required
openssl utils in you system.

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -i INFILE, --infile INFILE
                        Full path of Encrypted File.
  -w WORDLIST, --wordlist WORDLIST
                        Full path of Wordlist File
  -o OFILENAME, --ofilename OFILENAME
                        Output file name.
  -m MODE, --mode MODE  Select any from aes-256-cbc or aes-256-ecb


##Example : 
python aes_bruteforce_decryptor.py -i to_enc.txt.enc -w pass1.lst -o outputfile.txt -m aes-256-cbc
