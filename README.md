# AES_Decryptor
This tool help you to decryption of AES Encrypted file in very easy way.

                 
visit : http://www.touhidshaikh.com Author :  @touhidshaikh22  

usage: aes_bruteforce_decryptor.py [-h] -i INFILE -w WORDLIST -o OFILENAME -m MODE                                                    
This is AES decryptor for Encrypted files. For Decryption, System required openssl utils in you system.                                                                                                       


optional arguments:                                                                                                                 
-h, --help            show this help message and exit
 
 required named arguments:                                                                                                          
-i INFILE, --infile INFILE       Full path of Encrypted File.                                                                         
-w WORDLIST, --wordlist WORDLIST    Full path of Wordlist File                                                                      
-o OFILENAME, --ofilename OFILENAME   Output file name.                                                                               
-m MODE, --mode MODE  Select any from aes-256-cbc or aes-256-ecb                                                                                      


#Example :                                                                                                                            
python aes_bruteforce_decryptor.py -i to_enc.txt.enc -w pass1.lst -o outputfile.txt -m aes-256-cbc
