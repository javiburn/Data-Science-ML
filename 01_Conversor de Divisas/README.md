# Proyecto del Día 2: Cambio de Divisas

### Consigna
Vas a crear un código que simule el funcionamiento de una **máquina de cambio de divisas**. Por el momento nuestra máquina sólo recibe **dólares** y devuelve **euros**.

Tu máquina va a necesitar disponer de variables que le brinden la siguiente información:
- Nombre del usuario
- Fecha en que se realiza la operación
- Momento del día (día, tarde o noche)
- Cantidad de dólares a cambiar

Con todo eso, la máquina va a imprimir en pantalla (en diferentes líneas por supuesto) un mensaje que incluya los siguientes requisitos:

- Un saludo de bienvenida
- Información de la cantidad de dólares que va a entregar el usuario
- Información de la cantidad de euros que va a recibir
- Detalle específico de cuántos billetes de €10, de €1, y el saldo en monedas que le serán entregados
- Un saludo de despedida

### Uso de la aplicación

Esta aplicación utiliza la API gratuita de ExchangeRate-API, para poder utilizarla debes crear una api-key en esta página e introducirla en un archivo .env bajo la variable API_KEY=your_key.