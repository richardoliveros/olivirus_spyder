
import urllib2
from bs4 import BeautifulSoup
import os
import sys

os.system('clear')

spider_olivirus="""
..................M .........M .....................................................................
......... ...... M............M ....................................................................
................M..............M ...................................................................
...............MN..............M ...................................................................
.... ..........M. .............MI...................................................................
...............M ..............~M...............,8+....,. ...:..~.....~ :,...  .....,... ~...,8. ...
.........8 ...MM................M ...M........MM?.,NM..MM....M..MM ..MM.MM .M,.MM..MM...NM..MO ,+...
.........,M ..MD ...............MM ..M .......M: ...M$.MM....M..NM..7M..MM .M,.:M..MM...NM..MM,.....
..........MD .MM............... M ..M$ .......M.....MN.MM....M...MM.MM..MM .MMMM...MM...NM...MMMM...
.......... MD .?M..............M  .MZ.........MM...MM..MM....M...DM~M...MM .M,.MM..MM ..MM.....MM...
............M, ..M...........=M ..MM ..........MMMMM...MMMMM.M....MM8...MM .M,..MM..MMMMM..,MMMM....
............IMN,..M ... . ..NM  .MM.................................................................
... .......... NMM.M:.MOMM.MM?MM : .................................................................
 .................MNMMMMMMMMM= .....................................................................
.................... MMMMMN. .......................................................................
...................MMMMMMMMM$......... .......... ........... ......................................
..........MMN??N7MMMMMMMMMMMMM7DO=IMMM........MM7MI.MMMMMM.MM..MMMMMM..NMMMM..MMMMMI................
................ NMMMMMMMMMMMM,....   ........MO....MM..MM.MM..MM...MM.NM.....MM..MM................
............... MMMMMMMMMMMMM.M7...............MMM..MMMMMM.MM..MM...MM.NMMMM..MMMMM.................
... ...........M+.NMMMMMMMMMM .MM ...............MM.MM.....MM..MM...MM.NM.....MM.MM.................
 ............ M,...MMMMMMMMM+ ..MM ..........OMMMM~.MM.....MM..MMMMMM..NMMMM:.MM..MM................
.............MM......8MMMM,..... M= ................................................................
..............MM ...............MM .................................................................
.... .........:M= .............MM...................................................................
...............MM.............MM. ..................................................................
................MM .......... MN....................................................................
.................M$..........MM ....................................................................
.................?M.........~M  ....................................................................
...................8D .....M  ......................................................................
.....................+M..M. ........................................................................
. .  ......  . ...... .... .......... ....... ........ ............................................."""

print spider_olivirus



try:
	spider_url=sys.argv[1] 
except:
	print 'Para ver el manual de uso: python olivirus_spyder.py -h'
	sys.exit(1)  
	

urls=[]
archivo_salida = 'rutas.html'

if spider_url=='-h':
   print """Modo de uso: >> python oliviru_spider.py dominio
   
   El dominio debe iniciar siempre con http o https segun sea el caso 

   ejemplo: http://midominio.com o https://www.midominio.com

   al finalizar se generara un archivo llamado rutas.html donde encontrara las urls detectadas."""
   sys.exit(1)  	


print spider_url
http_s= spider_url.find(':')
url_domain=spider_url.split("//")[-1].split("/")[0]
path_domain=spider_url[:http_s+3]+url_domain
print path_domain

def extraerdominio(path):
	global url
	url=path.split("//")[-1].split("/")[0].split('?')[0]
	compa= 'www.' in url
	if compa:
		url=url[4:]
	sincom=url.find('.')
	url=url[:sincom]
	
	return [url]

def arreglos( path ):
   global urls
   try:
    page = urllib2.urlopen(path)
    page_content = page.read()
   except:
    page_content='vacio'    
    pass
   
   with open('page_content.html', 'w') as fid:
		fid.write(page_content)
   soup = BeautifulSoup(page_content, 'html.parser') 
   for link in soup.find_all(["a", "script"]):
 	linea=link.get("href")
	tipo=isinstance(linea ,unicode)
 	if tipo:
	   linea=linea.encode("utf-8")
	   extraerdominio(path)
	   dominio=url in linea   
              
	   if dominio :
	      urls.append(linea)
	      
	   elif linea=='':
		a=1	   	      
	   elif linea[0]=='/':
	      urls.append(path_domain+linea)
	   elif linea[0] not in ('h','w','/') :
		  urls.append(path_domain+'/'+linea)
        linea=link.get("src")
	tipo=isinstance(linea ,unicode)
 	if tipo:
	   linea=linea.encode("utf-8")
	   extraerdominio(path)
	   dominio=url in linea   
              
	   if dominio :

	      urls.append(linea)
	      
	   elif linea=='':
		a=1	   	      
	   elif linea[0]=='/':
	      urls.append(path_domain+linea)
	   elif linea[0] not in ('h','w','/') :
		  urls.append(path_domain+'/'+linea)

   urls=list(set(urls))   
   os.remove("page_content.html") 
   #print urls  
   return [urls]



arreglos(spider_url)

for x in urls:
	arreglos(x)


tamano= len (urls)
urls=list(set(urls))
g = open(archivo_salida, 'w') 
for y in urls:
	g.writelines(y+'\n')
g.close()

print 'se creo el archivo ruta.html'

#by Richard Oliveros --> olivirus -->olivirus@outlook.es
