# mac_changer
Este pequeño proyecto tiene el objetivo de cambiar la dirección MAC de nuestra tarjeta de red.
Es ideal para las ocaciones en las que te encuentras en la lista negra de una red.


# Modo de Uso
Este programa funciona en linux, mediante la interacción en la consola, para ello utilizaremos argumentos.
La sintaxis a usar es simple, ya que solo tendremos que ingresar 2 valores.
El primero de ellos sera la interfaz (Por ejemplo: wlan0, eth0, etc)
El segundo valor seria la dirección mac que querramos usar (Por ejemplo: 00:11:22:33:44:55 o aa:bb:cc:dd:ee:ff).

En los siguientes pasos recuerda cambiar los valores dentro de las comillas y eliminar las comillas.

# Paso 1 
Escribimos "ifconfig" en la terminal.

# Paso 2
Identificamos el nombre de la interfaz (eth0, wlan0, etc) y la dirección mac de ella (ether).

# Paso 3
Abrimos el archivo python (mac_changer.py) escribiendo lo siguiente:
sudo python mac_changer.py -i "interfaz" -m "nueva dirección mac" ó sudo python mac_changer.py --interface "interfaz" --mac "nueva dirección mac"

# Paso 4
Verifica que la dirección mac cambia usando el comando "ifconfig"
