list = ['Lissauer, Jack J.', 'Fabrycky, Daniel C.', 'Ford, Eric B.', 'Borucki, William J.', 'Fressin, Francois', 'Marcy, Geoffrey W.', 'Orosz, Jerome A.', 'Rowe, Jason F.', 'Torres, Guillermo', 'Welsh, William F.', 'Batalha, Natalie M.', 'Bryson, Stephen T.', 'Buchhave, Lars A.', 'Caldwell, Douglas A.', 'Carter, Joshua A.', 'Charbonneau, David', 'Christiansen, Jessie L.', 'Cochran, William D.', 'Desert, Jean-Michel', 'Dunham, Edward W.', 'Fanelli, Michael N.', 'Fortney, Jonathan J.', 'Gautier, Thomas N., III', 'Geary, John C.', 'Gilliland, Ronald L.', 'Haas, Michael R.', 'Hall, Jennifer R.', 'Holman, Matthew J.', 'Koch, David G.', 'Latham, David W.', 'Lopez, Eric', 'McCauliff, Sean', 'Miller, Neil', 'Morehead, Robert C.', 'Quintana, Elisa V.', 'Ragozzine, Darin', 'Sasselov, Dimitar', 'Short, Donald R.', 'Steffen, Jason H.']

def search_list(alist, aname):
	count = 0
	author_index = 0
	author_list = alist 
	author_name = aname
	for author in author_list:
		if author == author_name:
			author_index = author_list.index(author)
			count = 1
	return count, author_index


this_count, position = search_list(list, 'Borucki, William')	

print this_count, position