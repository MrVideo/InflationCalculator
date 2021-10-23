import pandas as pd

# Lira to Euro conversion value
convert = 1936.27

# Import 'inflation.csv' as a pandas dataframe
df = pd.read_csv('inflation.csv')

# Syntax explaination and valid years
print('Inserisci la valuta da convertire')
print('Sintassi: € Denaro Anno / £ Denaro Anno / exit')
print('Anni validi: dal 1861 al 2015')

# Main loop
while(True):
    try:
        # Asks for query and splits it in 3 array elements
        inq = input('Query: ')
        query = inq.split(' ')

        # Checks for exit sequence
        if query[0] == 'exit':
            exit()
        else:
            # Calculates inflation coefficient from .csv file based on the input year
            k = ((df['Coefficiente'].loc[df['Anno'] == int(query[2])]).to_numpy())[0]

            # Checks query format
            if query[0] == '€':
                result = float(query[1]) * convert / k
                print(query[1] + ' € valgono ' + str(result) + ' £ dell\'anno ' + query[2])
            elif query[0] == '£':
                result = float(query[1]) * k / convert
                print(query[1] + ' £ del ' + query[2] + ' oggi valgono ' + str(result) + ' €')
            else:
                # Wrong currency symbol
                print('Hai digitato un simbolo di valuta non corretto')
    except IndexError:
        # Non-existent year in .csv file raises IndexError exception
        print("L'anno non è valido, riprova.")