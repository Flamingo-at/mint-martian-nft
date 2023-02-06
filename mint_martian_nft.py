from loguru import logger
from random import randint

from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
from common import FAUCET_URL, NODE_URL


def create_collection(sender: Account, number: int):
    payload = {
        "function": "0x3::token::create_collection_script",
        "type_arguments": [],
        "arguments": [
            f"Martian Testnet{number}",
            "Martian Testnet NFT",
            "https://aptos.dev",
            "9007199254740991",
            [
                False,
                False,
                False
            ]
        ],

        "type": "entry_function_payload",

    }

    return rest_client.submit_transaction(sender, payload)


def mint_collection(sender: Account,  number: int):
    payload = {
            "function": "0x3::token::create_token_script",
            "type_arguments": [],
            "arguments": [
                f"Martian Testnet{number}",
                f"Martian NFT #{number}",
                "OG Martian",
                "1",
                "9007199254740991",
                "https://gateway.pinata.cloud/ipfs/QmXiSJPXJ8mf9LHijv6xFH1AtGef4h8v5VPEKZgjR4nzvM",
                "0x57c7a3a39d277b198e7acab1cef6ab3081004c17336887d548d64340d491dbff",
                "0",
                "0",
                [
                    False,
                    False,
                    False,
                    False,
                    False
                ],
                [],
                [],
                []
            ],
        "type": "entry_function_payload"
    }
    return rest_client.submit_transaction(sender, payload)


def mint():
    while True:
        try:
            my_wallet = Account.load_key(my_private_key)
            print(my_wallet.account_address)
            print(my_wallet.private_key)

            print(rest_client.account_balance(my_wallet.address()))

            number = randint(1, 99999)

            txn_hash = create_collection(my_wallet, number)
            rest_client.wait_for_transaction(txn_hash)

            txn_hash = mint_collection(my_wallet, number)
            rest_client.wait_for_transaction(txn_hash)

        except:
            logger.error('Error')

                

def main():
    mint()


if __name__ == '__main__':
    print("Bot Mint Martian NFT @flamingoat\n")

    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)

    my_private_key = input('Private key: ')

    main()