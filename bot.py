import os
import sys
from web3 import Web3
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)
#cek koneks
RPC ='https://eth-sepolia.g.alchemy.com/v2/eojqIrGfDMDyfz-38hs9vpEVSbmL-FYf'
w3 = Web3(Web3.HTTPProvider(RPC))

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def connect():
    if not w3.is_connected():
        print(f'{Fore.RED} Silahkan cek RPC.....RPC erorr!!')
        exit()

def get_block_latest():
    result = w3.eth.get_block()
    return result

if __name__ == '__main__':
    clear_terminal()
    connect()
    
    print(f'{Fore.GREEN} Lanjutkan prosesss........')