"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import os
import logging
from web3 import Web3
from web3.types import BlockIdentifier

from moneyonchain.contract import Contract


class MoCState(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCState.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCState.bin'))

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCState']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def bitcoin_price(self, formatted: bool = True,
                      block_identifier: BlockIdentifier = 'latest'):
        """Bitcoin price in USD"""

        result = self.sc.functions.getBitcoinPrice().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitcoin_moving_average(self, formatted: bool = True,
                               block_identifier: BlockIdentifier = 'latest'):
        """Bitcoin Moving Average price in USD"""

        result = self.sc.functions.getBitcoinMovingAverage().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def days_to_settlement(self, formatted: bool = True,
                           block_identifier: BlockIdentifier = 'latest'):
        """Days to settlement"""

        result = int(self.sc.functions.daysToSettlement().call(
            block_identifier=block_identifier))

        return result

    def global_coverage(self, formatted: bool = True,
                        block_identifier: BlockIdentifier = 'latest'):
        """Global coverage"""

        result = self.sc.functions.globalCoverage().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitpro_total_supply(self, formatted: bool = True,
                            block_identifier: BlockIdentifier = 'latest'):
        """Bitpro total supply"""

        result = self.sc.functions.bproTotalSupply().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def doc_total_supply(self, formatted: bool = True,
                         block_identifier: BlockIdentifier = 'latest'):
        """DOC total supply"""

        result = self.sc.functions.docTotalSupply().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result


class MoCInrate(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoCInrate.bin'))

    precision = 10 ** 18

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        if not contract_address:
            # load from connection manager
            network = connection_manager.network
            contract_address = connection_manager.options['networks'][network]['addresses']['MoCInrate']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # finally load the contract
        self.load_contract()

    def commision_rate(self, formatted: bool = True,
                       block_identifier: BlockIdentifier = 'latest'):
        """Gets commision rate"""

        result = self.sc.functions.getCommissionRate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def bitpro_rate(self, formatted: bool = True,
                    block_identifier: BlockIdentifier = 'latest'):
        """Gets the rate for BitPro Holders"""

        result = self.sc.functions.getBitProRate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def daily_inrate(self, formatted: bool = True,
                     block_identifier: BlockIdentifier = 'latest'):
        """returns the amount of BTC to pay in concept of interest"""

        result = self.sc.functions.dailyInrate().call(
            block_identifier=block_identifier)
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_commission_value(self, amount, formatted: bool = True):
        """ Calc commission value amount in ether float"""

        result = self.sc.functions.calcCommissionValue(int(amount * self.precision)).call()
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result

    def calc_mint_interest_value(self, amount, formatted: bool = True):
        """ Calc interest value amount in ether float"""

        bucket = str.encode('X2')

        result = self.sc.functions.calcMintInterestValues(bucket, int(amount * self.precision)).call()
        if formatted:
            result = Web3.fromWei(result, 'ether')

        return result


class MoC(Contract):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/MoC.bin'))

    precision = 10 ** 18

    def __init__(self, connection_manager,
                 contract_address=None,
                 contract_abi=None,
                 contract_bin=None,
                 contract_address_inrate=None):

        network = connection_manager.network
        if not contract_address:
            # load from connection manager
            contract_address = connection_manager.options['networks'][network]['addresses']['MoC']

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

        # MoC Inrate contract
        self.moc_inrate = None
        if contract_address_inrate:
            self.contract_address_inrate = contract_address_inrate
        else:
            # load from connection manager
            self.contract_address_inrate = connection_manager.options['networks'][network]['addresses']['MoCInrate']

        # finally load the contract
        self.load_contract()

    def load_inrate_contract(self):

        self.moc_inrate = MoCInrate(self.connection_manager,
                                    contract_address=self.contract_address_inrate)

    def paused(self, formatted: bool = True,
               block_identifier: BlockIdentifier = 'latest'):
        """is Paused"""

        result = self.sc.functions.paused().call(
            block_identifier=block_identifier)

        return result

    def amount_mint_bpro(self, amount: float):
        """Final amount need it to mint bitpro in RBTC"""

        if not self.moc_inrate:
            self.load_inrate_contract()

        commission_value = float(self.moc_inrate.calc_commission_value(amount))
        total_amount = amount + commission_value

        return total_amount, commission_value

    def amount_mint_doc(self, amount: float):
        """Final amount need it to mint doc"""

        if not self.moc_inrate:
            self.load_inrate_contract()

        commission_value = float(self.moc_inrate.calc_commission_value(amount))
        total_amount = amount + commission_value

        return total_amount, commission_value

    def amount_mint_btc2x(self, amount: float):
        """Final amount need it to mint btc2x"""

        if not self.moc_inrate:
            self.load_inrate_contract()

        commission_value = float(self.moc_inrate.calc_commission_value(amount))
        interest_value = float(self.moc_inrate.calc_mint_interest_value(amount))
        total_amount = amount + commission_value + interest_value

        return total_amount, commission_value, interest_value

    def mint_bpro(self, amount: float, default_account=None):
        """ Mint amount bitpro
        NOTE: amount is in RBTC value
        """

        if amount <= 0.00000001:
            raise Exception("Value too low")

        if not self.moc_inrate:
            self.load_inrate_contract()

        total_amount, commission_value = self.amount_mint_bpro(amount)

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintBPro', int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)

        return tx_receipt

    def mint_doc(self, amount: float, default_account=None):
        """ Mint amount DOC
        NOTE: amount is in RBTC value
        """

        if amount <= 0.00000001:
            raise Exception("Value too low")

        if not self.moc_inrate:
            self.load_inrate_contract()

        total_amount, commission_value = self.amount_mint_doc(amount)

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintDoc', int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)

        return tx_receipt

    def mint_btc2x(self, amount: float, default_account=None):
        """ Mint amount BTC2X
        NOTE: amount is in RBTC value
        """

        if amount <= 0.00000001:
            raise Exception("Value too low")

        if not self.moc_inrate:
            self.load_inrate_contract()

        total_amount, commission_value, interest_value = self.amount_mint_btc2x(amount)
        bucket = str.encode('X2')

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'mintBProx', bucket, int(amount * self.precision),
                                                          tx_params={'value': int(total_amount * self.precision)},
                                                          default_account=default_account)

        tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)

        return tx_receipt

    def reedeem_bpro(self, amount_token: float, default_account=None):
        """ Reedem BitPro amount of token """

        if amount_token <= 0.00000001:
            raise Exception("Value too low")

        if not self.moc_inrate:
            self.load_inrate_contract()

        tx_hash = self.connection_manager.fnx_transaction(self.sc, 'redeemBPro', int(amount_token * self.precision),
                                                          default_account=default_account)

        tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)

        return tx_receipt