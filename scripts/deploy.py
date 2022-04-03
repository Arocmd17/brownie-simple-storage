from brownie import accounts, config, SimpleStorage, network

# import os

# There are 4 ways access an account
def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("ruben-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    store_value = simple_storage.retrieve()
    print(store_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    update_stored_value = simple_storage.retrieve()
    print(update_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    # print(accounts.add(os.getenv("WEB3_INFURA_PROJECT_ID")))
    deploy_simple_storage()
