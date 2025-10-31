# #loops

# #lists
# patients = ["Grace", "Faith", "Hellen"]
# for name in patients:
#     print("Checking vitals for", name)

# #numbers
# for numbers in range(1,4):
#     print(numbers)

# #using values inside a loop
# temperatures = [37.5, 36.5, 38, 40]
# for temp in temperatures:#prints out individual integer indidually
#     if temp >=38:
#         print(f'Fever detected {temp}')
# #range inside loops
# for i in range(5):
#     print(i)# will print o-4
# for x in range(2, 12):
#     print(x)#will print 2-6. last digit always exclusive.

# for y in range(1, 10, 3):
#     print (y)# will print 1,4.7

# for b in range(10,0, -2):
#     print(b) #will print from 10 to zero skipping, 10,8,6,4,2

#sum of numbers
total = 0
for c in range(1,6):
    total += c
print('The sum is:', total)

# #enumerate()

# clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
# for i, client in enumerate(clients, start=1):
#     print(f'Client {i}: {client}')


# #range()
# clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
# for i in range(len(clients)):
#     print(f'Clients {i+1}: {clients[i]}')

# #break and continue



# clients = ['Mercy Chebet','John Mburu', 'Justine Matiba', 'Phelesia Obwayo', 'Moses Chemowo', 'Dismass Loshorwa']
# for client in clients:
#     if client == 'Phelesia Obwayo':
#         print('Client found, stopping the search.')
#         break
        
