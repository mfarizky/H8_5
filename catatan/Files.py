myfile = open ('text.txt', 'w')
myfile.write('Halo saya siapa ?\n')
myfile.close()

x, y ,z = 43, 44, 45
message = 'Spam'
data = {'a' : 1, 'b' : 2}
file = open('text.txt', 'w')
file.write(message + '\n')
file.write('%s,%s,%s\n' % (x,y,z))
file.write(str(list) + '$' + str(data) + '\n')
file.close()
 