new_file = open('fails.txt', 'w', encoding='utf-8')
new_file.write('Python')
new_file.write('Datorium')

new_file.close()

new_file = open('fails.txt', 'r', encoding='utf-8')
file_content = new_file.read()
print(file_content)
new_file.close()



# rakstit - write 
# lasit - read
# pievienot - append
