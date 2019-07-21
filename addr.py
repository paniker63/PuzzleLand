import bitcoin

with open("keys/keys61461444.txt", "r") as f:
    content = f.readlines()

content = [x.strip() for x in content]
f.close()

outfile = open("keys/addr_comp61461444.txt", "w")
for x in content:
    #outfile.write(bitcoin.encode_privkey(x, 'wif') + ":" +
    outfile.write (bitcoin.privtoaddr(x) + "\n")
    #outfile.write(bitcoin.encode_privkey(x, 'wif_compressed')+ "\n")# + ":" + bitcoin.privtoaddr(x) + "\n")


outfile.close()

#1Me6EfpwZK5kQziBwBfvLiHjaPGxCKLoJi