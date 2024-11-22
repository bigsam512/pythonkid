oldfile=open('010902.py')
oldfiletxt=oldfile.read()

file=open('010902bak.py','w')
file.write(oldfiletxt)
file.close()
