import sha3
import os
from ethereum import utils
import time

start = time.time()

a = 1
while (a <=5):
    elapsed_time = time.time() - start
    
    privat_key = utils.sha3(os.urandom(256))
    raw_address = utils.privtoaddr(privat_key)
    account_address= (utils.checksum_encode(raw_address)).lower()
    z= utils.encode_hex(privat_key)
    #for test
    #account_address = "0xB88444C323EC00b31B89BbB9d291B47DEDFBD6Ea"
    wanted = "0xB88444C323EC00b31B89BbB9d291B47DEDFBD6Ea"
    if wanted==account_address:
        print("---EURIKA-----EURIKA-----EURIKA-----EURIKA---")
        print("private key  : "+ z)
        print("Address      : "+ account_address)

        dosya2 = open("extracted.text","a")
        dosya2.write(z + " " + account_address + "\n")
        dosya2.close()

        time.sleep(5)
    else:
        print('private key:'+ z +''+'Address:' +account_address+ ' '+str(a))

    a= a+1
    print("total time %s sn" %elapsed_time) 
