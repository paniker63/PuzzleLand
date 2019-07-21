import random
import bitcoin
import sqlite3

def format_as_hex(number, length=64):
	return f'{hex(number)[2:]:0>{length}}'


def generate_hex_in_range(start, stop):
	return format_as_hex(random.randrange(start, stop))


#1Me6EfpwZK5kQziBwBfvLiHjaPGxCKLoJi

i = 20000000000000000000000000
while i < 21090315766411506144426920:
    result = generate_hex_in_range(61440084647984870139, 61442316437759226781)
    print(result)
    with open('keys/keys61461444.txt', 'a') as f:
        f.writelines(result+"\n")
    #with open("keys.txt","r") as f:
    #    content = f.readlines()

    #content = [x.strip() for x in content]


    #outfile = open("adr.txt","w")
    #for x in content:
    #    outfile.write(bitcoin.privtoaddr(x)+"\n")




'''
with open("addr_uncheck", "a") as file:
    result = m.read().split()
    for ad in result:
        continue
    if addr in add:
        data = open("WinRandom.txt", "a")
        data.write("found " + str(result) + "\n" + str(x) + "\n" "\n")
        data.close()
        
'''