new_file = open('currencies.txt', 'w', encoding='utf-8')
new_file.write('0.90')
new_file.close()
 
file = open('currencies.txt', 'r', encoding='utf-8')
rate = float(file.read())
file.close()

amount = float(input('Ievadi naudas summu(EUR): '))
new_amount = amount * rate

print(f'{amount} EUR = {new_amount} GBP')