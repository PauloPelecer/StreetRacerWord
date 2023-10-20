import os

def SaveCoins(coin):
    with open('profile/my_coins.txt', 'w') as file:
        file.write(coin)
        

def SaveRecords(record):
    path = 'profile'  # Caminho para a pasta 'profile'
    dir = os.listdir(path)
    record = int(record)  # Convertendo o valor do recorde para inteiro

    if 'my_records.txt' in dir:
        with open(os.path.join(path, 'my_records.txt'), 'r') as file:
            data = int(file.read())  # Convertendo o valor lido do arquivo para inteiro

        if record > data:
            with open(os.path.join(path, 'my_records.txt'), 'w') as file:
                file.write(str(record))  # Convertendo o recorde para string antes de escrever
            return 'Novo Record'
        else:
            return 'Nenhum Novo Record'

    else:
        with open(os.path.join(path, 'my_records.txt'), 'w') as file:
            file.write(str(record))  # Convertendo o recorde para string antes de escrever
        return 'Novo Record'

# Exemplo de uso

def GetValueRecords(record):
    with open('profile/my_records.txt', 'r') as file:
         data = int(file.read())
         result = int(record) + int(data)
         SaveRecord(result)
         return result
def ReadRecords():
    with open('profile/my_records.txt', 'r') as file:
         data = file.read()
         return data
def ReadCoins():
     with open('profile/my_coins.txt', 'r') as file:
         data = int(file.read())
         return data
         
         
if __name__ == '__main__':
    pass