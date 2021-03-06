from moneyonchain.manager import ConnectionManager
from moneyonchain.commission import RDOCCommissionSplitter

import logging
import logging.config

# logging module
# Initialize you log configuration using the base class
logging.basicConfig(level=logging.INFO)
# Retrieve the logger instance
log = logging.getLogger()


network = 'rdocMainnet'
connection_manager = ConnectionManager(network=network)
log.info("Connecting to %s..." % network)
log.info("Connected: {conectado}".format(conectado=connection_manager.is_connected))

splitter = RDOCCommissionSplitter(connection_manager)

print("Contract address:")
print(splitter.commission_address())

print("MoC Address")
print(splitter.moc_address())

print("Reserve Address")
print(splitter.reserve_address())

"""
INFO:root:Connecting to rdocTestnet...
INFO:root:Connected: True
Contract address:
0xC67D9EE30d2119A384E02de568BE80fe785074Ba
MoC Address
0x7e2F245F7dc8e78576ECB13AEFc0a101E9BE1AD3
Reserve Address
0x19F64674D8A5B4E652319F5e239eFd3bc969A1fE


INFO:root:Connecting to rdocMainnet...
INFO:root:Connected: True
Contract address:
0x27a3074Db95Ec5f6a0E73DC41a4859F48990e841
MoC Address
0xCfF3fcaeC2352C672C38d77cb1a064B7D50ce7e1
Reserve Address
0x2AcC95758f8b5F583470ba265EB685a8F45fC9D5
"""