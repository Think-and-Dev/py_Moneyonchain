from moneyonchain.manager import ConnectionManager
from moneyonchain.changers import RDOCPriceProviderChanger

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('default')


network = 'rdocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))


contract = RDOCPriceProviderChanger(connection_manager)

#price_provider = '0x2B54819531B7126bDEE2CeFDD9c5342d6c307595'
#price_provider = '0x01a165cC33Ff8Bd0457377379962232886be3DE6'
#price_provider = '0x9d4b2c05818A0086e641437fcb64ab6098c7BbEc'
#price_provider = '0x9315AFD6aEc0bb1C1FB3fdcdC2E43797B0A61853'
price_provider = '0xb856Ca7c722cfb202D81c55DC7925e02ed3f0A2F'
tx_hash, tx_receipt = contract.constructor(price_provider, execute_change=False)
if tx_receipt:
    print("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))
else:
    print("Error deploying changer")

"""
Connecting to rdocTestnetAlpha...
Connected: True
2020-05-07 08:01:06 root         INFO     Deploying new contract...
2020-05-07 08:01:20 root         INFO     Deployed contract done!
2020-05-07 08:01:20 root         INFO     0x709736e7dbe19b6f110a0ff3c46170806bd77316ea6bb4c826fe34c6fa2c9b1c
2020-05-07 08:01:20 root         INFO     AttributeDict({'transactionHash': HexBytes('0x709736e7dbe19b6f110a0ff3c46170806bd77316ea6bb4c826fe34c6fa2c9b1c'), 'transactionIndex': 3, 'blockHash': HexBytes('0x97971bd20799f14cbd89189f4b81335fb3ede91627d65403727d42749b154644'), 'blockNumber': 830882, 'cumulativeGasUsed': 915172, 'gasUsed': 420315, 'contractAddress': '0x6a790e6f9ee18aFBc668C90Fe42075055d204CB8', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 830882, 'blockHash': HexBytes('0x97971bd20799f14cbd89189f4b81335fb3ede91627d65403727d42749b154644'), 'transactionHash': HexBytes('0x709736e7dbe19b6f110a0ff3c46170806bd77316ea6bb4c826fe34c6fa2c9b1c'), 'transactionIndex': 3, 'address': '0x6a790e6f9ee18aFBc668C90Fe42075055d204CB8', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000a8f94d08d3d9c045fe0b86a953df39b14206153c')]})], 'from': '0xa8F94d08d3d9C045fE0b86a953DF39b14206153c', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000800000000000000000000000010000000000000000000000000000000000000000001000000000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000004000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000100000000000000000000000000000000000000000000000000000020000000000000000008000000000000000000000000000000000000000000000000')})
2020-05-07 08:01:20 root         INFO     Changer Contract Address: 0x6a790e6f9ee18aFBc668C90Fe42075055d204CB8
Changer Contract Address: 0x6a790e6f9ee18aFBc668C90Fe42075055d204CB8

onnecting to rdocTestnetAlpha...
Connected: True
2020-05-17 10:07:48 root         INFO     Deploying new contract...
Changer Contract Address: 0xF17DDDa4a91ee0867942CaF524600Aa8BbC961f5
2020-05-17 10:08:39 root         INFO     Deployed contract done!
2020-05-17 10:08:39 root         INFO     0xb43072b3d3a30e51682520bf23ddfd5eceacbedf0cc997ec841bdb075084030a
2020-05-17 10:08:39 root         INFO     AttributeDict({'transactionHash': HexBytes('0xb43072b3d3a30e51682520bf23ddfd5eceacbedf0cc997ec841bdb075084030a'), 'transactionIndex': 11, 'blockHash': HexBytes('0x2fd75d235e87259d9bd3bdc8bcf9c8e35b0b4109fd0d65bceebcb70cfd4890f3'), 'blockNumber': 858624, 'cumulativeGasUsed': 829572, 'gasUsed': 420315, 'contractAddress': '0xF17DDDa4a91ee0867942CaF524600Aa8BbC961f5', 'logs': [AttributeDict({'logIndex': 0, 'blockNumber': 858624, 'blockHash': HexBytes('0x2fd75d235e87259d9bd3bdc8bcf9c8e35b0b4109fd0d65bceebcb70cfd4890f3'), 'transactionHash': HexBytes('0xb43072b3d3a30e51682520bf23ddfd5eceacbedf0cc997ec841bdb075084030a'), 'transactionIndex': 11, 'address': '0xF17DDDa4a91ee0867942CaF524600Aa8BbC961f5', 'data': '0x', 'topics': [HexBytes('0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0'), HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), HexBytes('0x000000000000000000000000a8f94d08d3d9c045fe0b86a953df39b14206153c')]})], 'from': '0xa8F94d08d3d9C045fE0b86a953DF39b14206153c', 'to': None, 'root': '0x01', 'status': 1, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000800000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000020000000000000000000800000000000000000000000000000000400000004000000000000000000000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000020000000000000000008000000000000000000000080000000000000000000000000')})
2020-05-17 10:08:39 root         INFO     Changer Contract Address: 0xF17DDDa4a91ee0867942CaF524600Aa8BbC961f5
"""