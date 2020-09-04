#
     / ___|  _ \ \ / /  _ \_   _/ _ \|  _ \ \ / /                  
    | |   | |_) \ V /| |_) || || | | | |_) \ V /                   
    | |___|  _ < | | |  __/ | || |_| |  __/ | |                    
     \____|_| \_\|_| |_|    |_| \___/|_|    |_|                    
#

### What is cryptopy-cli?
`cryptopy-cli` is a command line interface (CLI) embedded encryption-decryption tool written in Python.

### What does it do?

#### Encryption:
Accepts the file and a password -**do not forget the password you used**- reads the content of the file, encrypts the content with SHA256 and writes the encrypted content into the new file `enc_file`.

Asks the user whether to keep the original file or to remove it. If answer is to keep it, renames the file `original_file`. `y` || `n` will suffice for making choices.

The script also makes the verification check, whether the files exists or not and calculates the duration of encryption.

#### Decryption:

Accepts the file and the **same password you used when encrypting the file**. Once the inputs are given, the script decrypts the file and copies the decrypted content to a file called `decoded`. 

Also upon exit, asks the user whether to keep the ecrypted file or not. `y` || `n` will suffice for making choices.

The script also makes the verification check, whether the files exists or not and calculates the duration of encryption.
      
### How to install?
 
Easy:

`pip install cryptopy-cli`

### How to use?

#### Encrypt a file:

`cryptopy-cli [encrypt] [/path/to/file/] password`

#### Decrypt a file:

`cryptopy-cli [decrypt] [/path/to/file/] password`
      
<img src="https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/encrypt.jpg" width="600px"></img>

**AND AFTER THE ENCRYPTION:**
     
<img src="https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/encrypted.png" width="600px"></img>
  
<img src="https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/decryption.png" width="600px"></img> 
      
**COMPARING THE ORIGINAL FILE AND THE DECODED FILE:**
      
<img src="https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/comparison.png" width="600px"></img>  
            
---

**A Friendly Disclaimer:**

This is just the first version. The more muscular versions will arrive soon,hopefully.
Enjoy and give me feedbacks!

-- M Yavuz YAGIS
