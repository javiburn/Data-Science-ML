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

### Resolución

Para calcular en tiempo real el valor del dólar con respecto al euro decidí conectar mi aplicación la API ExchangeRate-API (en caso de fallar la conexión establece un valor por defecto de 0.9), almacenando este valor en la clase Rate.
A continuación creamos la clase Calculator, que pide los inputs requeridos al usuario y lleva a cabo una comprobación de estos valores para filtrar los datos (que efectivamente se introduzca un nombre, el formato de la fecha sea válido, los dólares tengan un valor numérico...).
A continuación, la clase Printer imprimirá todos estos valores recibiendo una clase Calculator que los tiene almacenados y la clase Rate para multiplicar el número de dólares introducido por el ususario por su tasa de conversión en el mercado.