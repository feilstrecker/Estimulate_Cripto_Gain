# Imports
from time import sleep
import requests
from os import system
from keyboard import is_pressed

def estimate_gain(used_value, used_value_coin, coin_name):
    '''
    For example:
    used_value = R$ 30,00
    used_value_coin = R$ 16000

    so:
    30 / 16000
    wallet: 0,001875 - rate

    and the current coin price is 17000
    the same used value = R$ 30,00
    the current value = R$ 17000
    30 / 17000
    now price = 0,001764
    gain = (wallet - now price)

    '''
    
    # Get value of current, low and high cripto coin price
    get_values = get_value_coin(coin_name)

    current_coin_value = float(get_values[0])
    low_coin_value = float(get_values[1])
    high_coin_value = float(get_values[2])

    # Current value coin into wallet
    current_cripto_coin_value = used_value / used_value_coin
    # Percent = (value in wallet of coin /100)*1.55
    current_percentage = float((current_cripto_coin_value/100)*1.55)
    # Value with percent
    current_cripto_coin_value = current_cripto_coin_value - current_percentage

    # If buy the coin now with the same money = Used value / Current value coin
    new_cripto_coin_value = used_value / current_coin_value

    # Gain if sell now, in cripto coin value = Current cripto coin - Value if buy now | Using the same value
    current_gain_cripto_coin = f'{(current_cripto_coin_value - new_cripto_coin_value):.8f}'

    # Gain in low and high
    low_gain_cripto_coin = f'{(current_cripto_coin_value - (used_value/low_coin_value)):.8f}'
    high_gain_cripto_coin = f'{(current_cripto_coin_value - (used_value/high_coin_value)):.8f}'

    # Cripto coin to real money
    current_gain = float(current_gain_cripto_coin) * current_coin_value
    low_gain = float(low_gain_cripto_coin) * current_coin_value
    high_gain = float(high_gain_cripto_coin) * current_coin_value
    
    # Print informations
    return print(
        f'Current price: R${current_coin_value:.2f} (R${current_gain:.2f})\n\n'
        f'Low price: R${low_coin_value:.2f} (R${low_gain:.2f})\n'
        f'High price: R${high_coin_value:.2f} (R${high_gain:.2f})\n'
        )

def get_value_coin(coin):

    """
    You can get more coin initials here:

    https://www.mercadobitcoin.com.br/api-doc/

    You can change these or make more elif
    """

    # Make url
    if coin == 'Ethereum':
        coin_initials = 'ETH'

    elif coin == 'Bitcoin':
        coin_initials = 'BTC'

    url = f'https://www.mercadobitcoin.net/api/{coin_initials}/ticker'

    # Get request
    r = requests.get(url)

    # into ['ticker'] have the prices
    r = r.json()['ticker']

    # List of the last price, low price and high price in the last 24 hours
    values = (r['last'], r['low'], r['high'])

    return values

# Press 'Q' to exit
while is_pressed('Q') == False: 
    system('cls')

    # Example: R$ 30,00 (used money), R$ 16372,00 (cripto price when i bought), 'Ethereum' the cripto coin used
    estimate_gain(32, 16372, 'Ethereum')

    # You can change the value or remove this sleep
    sleep(1)
    
