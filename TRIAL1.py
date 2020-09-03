import os,sys,time,hashlib,click,shutil
try:
    #from Crypto.Hash import SHA256
    from Crypto.Cipher import AES
    from Crypto import Random
    from Crypto.Hash import SHA256
except ImportError:
    sys.path.append('/library/frameworks/python.framework/versions/3.8/bin/python3')
    #from Crypto.Hash import SHA256
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto import Random  
from pyfiglet import Figlet, figlet_format
from termcolor import colored, cprint


############################### Enryption Script ############################




########################## Initialization Function ##################################
#-----------------------------with some added styling-------------------------------#


@click.group(help='Give a text file to be processed and a magical passcode for show to begin')
@click.version_option(version='0.01', prog_name='cryptopy')
def main():
    color='green'
    banner='                CRYPTOPY'
    cprint(figlet_format(banner), color)
    #for styling and ASCII purposes.
    print('PLEASE TYPE --help FOR FURTHER HELP')

############################ Run the script from this file##############################






@main.command('encrypt')
@click.argument('textfile')
@click.argument('passcode')
# Encryption function takes two arguments : a textfile to read from and a passcode for auth.
def encrypt(textfile, passcode):
    '''Requires a textfile to read from and a passcode for auth.'''
    click.echo("===================Let's Roll!===============================")
    passcode=passcode.encode()
    # We accepted the passcode as passcode and encoded it to password
    key = hashlib.sha256(passcode).digest()
    #KEY CREATED for AES encryption, of which format is in bytes
    mode = AES.MODE_CBC
    #MODE SET
    #the mode, which is a constant and gives the mode of encryption
    #CBC mode is ciphertext block chaining mode. takes cryptographic key and a mode and IV. IV can be none.
    #If IV is not given, it will create one randomly. 
    
    IV= Random.new().read(16)
    #IV= 16 * b'\x00'

    # Converted it into bytes in order to escape from TypeError 
    # TypeError: Object type <class 'str'> cannot be passed to C code
    #IV SET.
    #as the last prerequisite, the initialization vector is defined since the
    #encryption requires a pass a mode to encrypt it and a IV.
    
    lock = AES.new(key, mode, IV=IV)
    #LOCK CREATED
    #so we build our lock with these variables.
    base=os.path.basename(textfile)
    #we will use this os module so its good to keep it short as a global var.

    
    # File Existence Check:
    if not os.path.exists(textfile):
            print('The file:  %s does not exist. Program quitting' %(textfile))
        # if there is no such a file, the script will Quit
            SystemExit
    elif os.path.basename(textfile).startswith("enc_"):
            click.echo("%s is encrypted already" %str(textfile))
            SystemExit
        # Or if there is such a file called `enc_X` this means the file is already encrypted. We dont want to encrypt it again. 
        #thus, exitting.
    else:        
        #--- In order this lock to work, the message should be divisible by 16, if not, its not gonna work.
        # thus, until it is divisible by 16, we keep adding a byte to the file
        def pad_file(textfile):
            while len(textfile) % 16 != 0:
                textfile = textfile + b'0'
            return textfile
            

        #now filled with extra characters, its ready to be encrypted. Creating the new file:
        
    #changing the name of the original file with the add-on enc in which the encrypted data will be stored
    #encrypted file will be named : enc_nameOfOriginalFile. still not encoded.
        
        
        startTime=time.time()
        with open(textfile,'rb') as padded:
        #opening the textfile and reading as bytes:
            content =padded.read()
            padded_file=pad_file(content)
            encrypted_message=lock.encrypt(padded_file)
            #below, creating the extension to extend the original file after process.
            ext=base.split('.')[1]
            #copying the original file under the name of file_original.ext 
            shutil.copyfile(base, base.split('.')[0] + '_original.'+ ext)
            

            with open(textfile, 'wb') as enc:
        #opening the enc_file in the writing mode:
                enc.write(encrypted_message)
            
            os.rename(base, 'enc_'+ base.split('.')[0])
            print("Encryption of the given file {}  is completed" .format(textfile))                    
            totaltime=round(time.time() - startTime)
            print('Encryption time: %s seconds!' %(totaltime))
            #timetime() is an evergoing function. so using it twice in different times
            # helps us to see the difference of time.
            padded.closed             
    #padded_file = os.path.join("enc_" +os.path.basename(textfile))
          
    # Ask user whether to keep the original file or to remove it after the encryption.:
    if os.path.isfile(base.split('.')[0] + '_original.'+ ext):
        print('Do you want to keep the original file,  %s? (Y)es or (N)o ?' %(base.split('.')[0] + '_original.'+ ext))
        response = input('> ')
    if not response.lower().startswith('y'):
        os.remove(base.split('.')[0] + '_original.'+ ext)
    else:
        pass






############################ Decryption Script ###############################
@main.command('decrypt')
@click.argument('textfile')
@click.argument('passcode')
# Encryption function takes two arguments : a textfile to read from and a passcode for auth.
def decrypt(textfile, passcode):
    '''Requires a textfile(starting with enc_) and a keyword for auth'''
    click.echo("=====Let's Roll Back :)!====")
    # We have to create the unlocker, basically its the same lock we used when defining encryption.
    passcode=passcode.encode()
    # We accepted the passcode as passcode and encoded it to password
    key = hashlib.sha256(passcode).digest()
    #KEY CREATED for AES encryption, of which format is in bytes
    mode = AES.MODE_CBC
    #MODE SET
    #the mode, which is a constant and gives the mode of encryption
    #CBC mode is ciphertext block chaining mode. takes cryptographic key and a mode and IV. IV can be none.
    #If IV is not given, it will create one randomly. 
    IV= Random.new().read(16)
    #IV SET.
    #as the last prerequisite, the initialization vector is defined since the
    #encryption requires a pass a mode to encrypt it and a IV.
    unlock = AES.new(key, mode, IV)
    #LOCK CREATED
    #so we build our lock with these variables.
    # File Existence Check:
    if not os.path.exists(textfile):
            print('The file:  %s does not exist. Program quitting' %(textfile))
        # if there is no such a file, the script will Quit
            SystemExit
    elif not os.path.basename(textfile).startswith("enc_"):
            click.echo("%s is not encryped by me. try to add enc_ as prefix" %str(textfile))
            SystemExit
        # Or if there is such a file called `enc_X` this means the file is already encrypted. We dont want to encrypt it again. 
        #thus, exitting.
    else:
        outputFile = os.path.join(os.path.dirname(textfile), os.path.basename(textfile[4:]))
    #defining an output file
    # the expected encrypted file is already named like enc_text.txt so the first 4 characters need to be removed.
    #reversing from enc_X to X, to its original form.
        startTime=time.time()
        with open(textfile, "rb") as textfile:
            with open(outputFile, "wb") as outputfile:
                outputfile.write(unlock.decrypt(textfile).rstrip())
            print("Decryption of the given file" &str(textfile) + "is completed")
            print("Please find your decrypted file enc_{} in the directory".format(textfile))                    
            totaltime=round(time.time() - startTime)
            print('Decryption time: %s seconds!' %(totaltime))

     # Ask user whether to keep the original file or to remove it after the decryption.:
    if os.path.exists(outputFile):
        print('Do you want to keep the original file,  %s? (Y)es or (N)o ?' %(outputFile))
        response = input('> ')
    if not response.lower().startswith('y'):
        os.remove(outputFile)
    else:
        pass

                

if __name__ == "__main__":
    main()

    
