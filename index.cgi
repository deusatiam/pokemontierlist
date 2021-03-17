#!/bin/python
import cgi
import functions as func

print ('Content-type:text/html\n')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>Vote!</title>')
print ('<link href="style.css" rel="stylesheet" type="text/css">')
print ('<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">')
print ('<link rel="icon" href="/favicon.ico" type="image/x-icon">')
print ('</head>')
print ('<body>')
print ('<div class="navbar">')
print ('<ul>')
print ('<li><a class="active" href="index.cgi">Vote</a></li>')
print ('<li><a href="../tierlist.html">Tier List</a></li>')
print ('<li><a href="../about.html">About</a></li>')
print ('</ul>')
print ('</div>')
print ('<h1> Which pokeyman is better? </h1>')
print ('<h1> Please reload after voting! </h1>')
print ('<div class="Voting">')
print ('<div class="Pokemon1">')

form = cgi.FieldStorage()

pokemon1, pokemon2 = func.get_pair()

poke_1_name = func.get_name(pokemon1)
poke_2_name = func.get_name(pokemon2)

print ('<form method=post action=func.vote(pokemon1,pokemon2)>')
print ('<h2> ' + poke_1_name + ' </h2>')
print('<img src="' + func.get_sugimori(pokemon1) + '" style="width:300px;height:300px;">')
print ('<input type="submit" value="Submit" name=' + poke_1_name + ' />') 
print ('</div>')
print ('<div class="Pokemon2">')
print ('<form method=post action=func.vote(pokemon2,pokemon1)>)
print ('<h2> ' + poke_2_name + ' </h2>')
print('<img src="' + func.get_sugimori(pokemon2) + '" style="width:300px;height:300px;">')
print ('<input type="submit" value="Submit" name=' + poke_2_name + ' />') 
print ('</div>')

'''
if poke_1_name in form:
    func.vote(pokemon1,pokemon2)
elif poke_2_name in form:
    func.vote(pokemon2,pokemon1)
else:
    print("Error in cgi form.")
'''
print ('</div>')
print ('</body>')
print ('</html>')
