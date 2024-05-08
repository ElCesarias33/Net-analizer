# Net-analizer
Vrs: 0.0.1
Repositorio para proyecto final de la materia de Topicos Selectos de Sistemas Computacionales

Analizador de red (Net-analizer) esta creado con la finalidad de llevar un registro, un categorizacion del uso de red, 
creacion de informes detallados sobre posibles amenazas en la red local o en sus dispositivos, aunque el codigo fuente sea accesible, 
la creacion de una web app para su revision y funcionamiento completo.

* Dependencias
scapy
scikit-learn
matplotlib
pandas
...

* Funcionalidad
Revision cada T (tiempo) de forma general, si detecta fluctuaciones grandes o inconsistentes arrojara un registro en una tabla
Graficamente visualizara la red de entrada en el dispositivo de uso, esto no exime a los usuarios de mantenerse protegidos con Firewalls y/o 
antivirus, puesto que es solo uno de los casos que un experto en ciberseguridad debe observar.

Se pueden seguir implementando con otros modulos de python: 
    nmap (revision y chequeo de puertos)
