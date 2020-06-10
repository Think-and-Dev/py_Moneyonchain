"""
ADD PAIRS

[ [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0xA274d994F698Dd09256674960d86aBa22C086669',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xA274d994F698Dd09256674960d86aBa22C086669',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ],
  [ '0xA274d994F698Dd09256674960d86aBa22C086669',
    '0x840871cbb73dC94dcb11b2CEA963553Db71a95b7',
    '1000000000000000000',
    '1000000000000000000' ] ]



"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import DexAddTokenPairChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'dexTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = DexAddTokenPairChanger(connection_manager)

"""
RDOC: 0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8
DOC: 0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0
ERBTC: 0xA274d994F698Dd09256674960d86aBa22C086669
BPRO: 0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf

RIF: 


DOC / RDOC
RDOC / ERBTC


DOC / RDOC 

 [  '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8',
    '1000000000000000000',
    '1000000000000000000' ]
    
    
RDOC / ERBTC    


[   '0xC3De9F38581f83e281f260d0DdbaAc0e102ff9F8',
    '0xA274d994F698Dd09256674960d86aBa22C086669',
    '1000000000000000000',
    '1000000000000000000' ]
    
    
AGREGAR    
    
DOC / BPRO    


[   '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ]
    
    
DOC / ERBTC    


[   '0xCB46c0ddc60D18eFEB0E586C17Af6ea36452Dae0',
    '0xA274d994F698Dd09256674960d86aBa22C086669',
    '1000000000000000000',
    '1000000000000000000' ]    


ERBTC / BPRO


[   '0xA274d994F698Dd09256674960d86aBa22C086669',
    '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf',
    '1000000000000000000',
    '1000000000000000000' ]    
    
        
"""

base_token = '0xA274d994F698Dd09256674960d86aBa22C086669'
secondary_address = '0x4dA7997A819bb46B6758B9102234c289dD2Ad3bf'
init_price = int(1.0 * 10 ** 18)
price_precision = int(1.0 * 10 ** 18)

tx_hash, tx_receipt = contract.constructor(base_token,
                                           secondary_address,
                                           init_price,
                                           price_precision,
                                           execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")


"""

Connecting to dexTestnet...
2020-06-10 11:45:45 root         INFO     Deploying new contract...
Connected: True
2020-06-10 11:46:16 root         INFO     Deployed contract done!
2020-06-10 11:46:16 root         INFO     0x3948fb19cc9bc93f6b85cc707a9728935d91ad37bfe63cb2736510ce44431d5e
2020-06-10 11:46:16 root         INFO     AttributeDict({'transactionHash': HexBytes('0x3948fb19cc9bc93f6b85cc707a9728935d91ad37bfe63cb2736510ce44431d5e'), 'transactionIndex': 5, 'blockHash': HexBytes('0x04814ab7cbb6d2dbc51cc8c742327ca06d06b1bf7b41654085534413534bc420'), 'blockNumber': 921336, 'cumulativeGasUsed': 645450, 'gasUsed': 497400, 'contractAddress': '0x44e11150691c52EfCe7b226eD42BB6068eDfE62e', 'logs': [], 'from': '0xA8342cC05241E0d940E1c74043faCd931562f19a', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-10 11:46:16 root         INFO     Changer Contract Address: 0x44e11150691c52EfCe7b226eD42BB6068eDfE62e
Changer Contract Address: 0x44e11150691c52EfCe7b226eD42BB6068eDfE62e

Connecting to dexTestnet...
Connected: True
2020-06-10 11:48:56 root         INFO     Deploying new contract...
2020-06-10 11:49:26 root         INFO     Deployed contract done!
2020-06-10 11:49:26 root         INFO     0x8953b88903eb797a0f7c53026cf30f9e339205404316a4212bc001d0fb17f31f
2020-06-10 11:49:26 root         INFO     AttributeDict({'transactionHash': HexBytes('0x8953b88903eb797a0f7c53026cf30f9e339205404316a4212bc001d0fb17f31f'), 'transactionIndex': 31, 'blockHash': HexBytes('0x494ca1bae8fe16ecb499f84cdea0740f906a0c50fdffcc0c438eff92b24ae68d'), 'blockNumber': 921342, 'cumulativeGasUsed': 2576214, 'gasUsed': 497400, 'contractAddress': '0x86eEc3Bc23C5Bcd43d8229aA5c10bA89CdeE1c5C', 'logs': [], 'from': '0xA8342cC05241E0d940E1c74043faCd931562f19a', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-10 11:49:26 root         INFO     Changer Contract Address: 0x86eEc3Bc23C5Bcd43d8229aA5c10bA89CdeE1c5C
Changer Contract Address: 0x86eEc3Bc23C5Bcd43d8229aA5c10bA89CdeE1c5C


Connecting to dexTestnet...
Connected: True
2020-06-10 11:52:26 root         INFO     Deploying new contract...
2020-06-10 11:53:23 root         INFO     Deployed contract done!
2020-06-10 11:53:23 root         INFO     0xf83fdcae5060d08a15c2af3a1ebb0d477f4249a8c1cafe53a48b8e4657fdfebf
2020-06-10 11:53:23 root         INFO     AttributeDict({'transactionHash': HexBytes('0xf83fdcae5060d08a15c2af3a1ebb0d477f4249a8c1cafe53a48b8e4657fdfebf'), 'transactionIndex': 5, 'blockHash': HexBytes('0xdddfca81c35c6d3196470fc74228c8c6b68d0e5140c7f39420772a415d5246b4'), 'blockNumber': 921351, 'cumulativeGasUsed': 647274, 'gasUsed': 497400, 'contractAddress': '0x27Ad13D6668e80Fb29652e659bbdf094d63837d3', 'logs': [], 'from': '0xA8342cC05241E0d940E1c74043faCd931562f19a', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})
2020-06-10 11:53:23 root         INFO     Changer Contract Address: 0x27Ad13D6668e80Fb29652e659bbdf094d63837d3
Changer Contract Address: 0x27Ad13D6668e80Fb29652e659bbdf094d63837d3

"""