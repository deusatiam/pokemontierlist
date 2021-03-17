#!/bin/python

import cgi
import functions as func

print ("Content-type:text/html\n\n")
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
print ('<div class="Voting">')
print ('<div class="Pokemon1">')

pokemon1, pokemon2 = func.get_pair()

print ('<h2> ' + func.get_name(pokemon1) + ' </h2>')
print('<img src="' + func.get_sugimori(pokemon1) + '">')
print ('</div>')
print ('<div class="Pokemon2">')
print ('<h2> ' + func.get_name(pokemon2) + ' </h2>')
print('<img src="' + func.get_sugimori(pokemon2) + '">')
print ('</div>')
print ('</div>')
print ('</body>')
print ('</html>')
