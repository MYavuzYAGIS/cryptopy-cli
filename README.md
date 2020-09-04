

                                            / ___|  _ \ \ / /  _ \_   _/ _ \|  _ \ \ / /                  
                                           | |   | |_) \ V /| |_) || || | | | |_) \ V /                   
                                           | |___|  _ < | | |  __/ | || |_| |  __/ | |                    
                                            \____|_| \_\|_| |_|    |_| \___/|_|    |_|                    


**1)What is Cryptopy-cli?** 
Cryptopy-cli is a Command line interface(CLI) embedded encryption-decryption tool written in Python.

**2)What does it do?**
  **1) Encryption:**
      Accepts the file and a keyword- do not forget the keyword you used- reads the content of the file,
      ecrypts the content with SHA256 and writes the encrypted content into the new file `enc_file`.
      Asks the user whether to keep the original file or to remove it. If answer is to keep it, renames the file
      `original_file`. `y` || `n` will suffice for making choices.
      The script also makes the verification check, whether the files exists or not and calculates the duration of encryption.
      
      
**3)How to Install?**
 
        Easy: `pip install cryptopy-cli`

**4)how to Use?**

       Both encryption and decryption have similar use cases:
       
       on encryption:
       
       `cryptopy-cli [encrypt] [/path/to/file/] keyword`
       
       on decryption:
        `cryptopy-cli [decrypt] [/path/to/file/] keyword`
       




      
      =============
      
   ![Image](https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/encrypt.jpg)  
      
      
      
      AND AFTER THE ENCRYPTION:
      
      
   ![Image](https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/encrypted.png)  
      
      
      
   **2)Decryption:**
       Accepts the file and the **same keyword you used when encrypting the file**. Once the inputs are given, the script
       decrypts the file and copies the decrypted content to a file called `decoded`. 
       Also upon exit, asks the user whether to keep the ecrypted file or not. `y` || `n` will suffice for making choices.
       The script also makes the verification check, whether the files exists or not and calculates the duration of encryption.
   
      
      
      
  ![Image](https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/decryption.png)  
      
      
      
      
      
      -----COMPARING THE ORIGINAL FILE AND THE DECODED FILE
      
  ![Image](https://github.com/MYavuzYAGIS/cryptopy/blob/master/img/comparison.png)  
      
      
      
      
**==================================================**





**A Friendly Disclaimer:**

`This is just the first version. The more muscular versions will arrive soon,hopefully.
Enjoy and give me feedbacks! M Yavuz YAGIS`
