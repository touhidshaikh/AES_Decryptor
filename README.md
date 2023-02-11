# AES Decryptor

AES Decryptor is a tool to decrypt encrypted files using OpenSSL.

## Requirements

- openssl utils
- Python3

## Usage
Usage: 
```python
python3 aes_decryptor.py [-h] --infile INFILE --wordlist WORDLIST --ofilename OFILENAME --mode MODE
```

### Options
```bash
-h, --help show this help message and exit
-i INFILE, --infile INFILE
Full path of Encrypted File.
-w WORDLIST, --wordlist WORDLIST
Full path of Wordlist File
-o OFILENAME, --ofilename OFILENAME
Output file name.
-m MODE, --mode MODE Select any from aes-256-cbc or aes-256-ecb
```

## Example
```bash
python3 aes_decryptor.py -i encrypted.file -w wordlist.txt -o decrypted.file -m aes-256-cbc
```


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

visit : http://www.touhidshaikh.com Author :  @touhidshaikh22