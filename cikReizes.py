text = input('Ko velies ierakstit? ')
times = int(input('Cik reizes velies iekrastit so tekstu? '))

new_file = open("cikReizes.txt", "w", encoding="utf-8")

for i in range(times):
    new_file.write(f"{text} \n")
    
new_file.close()