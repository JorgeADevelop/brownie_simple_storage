from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrange - organizar o arreglar

    account = accounts[0]

    # Act - hacer algo

    simple_storage = SimpleStorage.deploy({'from': account})
    
    starting_value = simple_storage.retrive()

    expected = 0

    # Assert - verificar que algo fue bien

    assert starting_value == expected

def test_updating_storage():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({'from': account})
    expected = 15
    transaction = simple_storage.store(expected, {'from': account})
    transaction.wait(1)

    # Assert
    assert expected == simple_storage.retrive()
    