from brownie import accounts, SimpleStorage, config, network

def deploy_simple_storage():
    account = get_account()
    #account = accounts.load(os.getenv('PRIVATE_KEY'))
    #account = accounts.add(config["wallets"]["from_key"])
    #account = accounts.load('freecodecamp-account')

    simple_storage = SimpleStorage.deploy({'from': account})

    stored_value = simple_storage.retrive()
    print(stored_value)

    transaction = simple_storage.store(15, {'from': account})
    transaction.wait(1)

    stored_value = simple_storage.retrive()
    print(stored_value)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def main():
    deploy_simple_storage()