#loops

#enumerate()

clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
for i, client in enumerate(clients, start=1):
    print(f'Client {i}: {client}')


#range()
clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
for i in range(len(clients)):
    print(f'Clients {i+1}: {clients[i]}')

#break and continue

clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
for client in clients:
    if client == 'Phelesia Obwayo':
        print('Client found, stopping the search.')
        break
        
    print(f'client: {client}')