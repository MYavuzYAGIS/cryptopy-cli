[![Build Status](https://travis-ci.org/MYavuzYAGIS/cryptopy.svg?branch=master)](https://travis-ci.org/MYavuzYAGIS/cryptopy)

             / ___|  _ \ \ / /  _ \_   _/ _ \|  _ \ \ / /                  
            | |   | |_) \ V /| |_) || || | | | |_) \ V /                   
            | |___|  _ < | | |  __/ | || |_| |  __/ | |                    
             \____|_| \_\|_| |_|    |_| \___/|_|    |_|                    

cryptopy is a CLI based encryption-decryption tool.
Since it is using the click module, flags like --help etc are active.
By definition, the tool has 2 options, encrypt and decrypt, and requires 2 parameters: 1- A file to be encrypted or decrypted 2- A keyword that works both sides of the action. So the user needs to give the same keyword for the actions on the same file.
The program also asks to keep or remove the original file during encryption or the encrypted file during decryption.
y || n will suffice.
This is just the first version. The more muscular versions will arrive soon,hopefully. the script also makes the verification check, whether the files exists or not.
Use case example:
cryptopy [encrypt||decrypt] /path/to/file/ keyword
Enjoy and give me feedbacks! M Yavuz YAGIS
Change Log
1.0.0(03.09.2020)
-The first release.
