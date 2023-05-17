var n = int ( input ( ) );
var pares = 0;
var bolo = {};
for i in range ( n ) :
    var camada = input ( );
    bolo . append ( camada );
for i in range ( n ) :
    var contador = 0;
    for j in range ( n ) :
        if (bolo { i } { j } == 'C') {
            contador += 1;
        }
     pares += ( ( contador * ( contador - 1 ) ) // 2 );
for j in range ( n ) :
    contador = 0;
    for i in range ( n ) :
        if (bolo { i } { j } == 'C') {
            contador += 1;
        }
     pares += ( ( contador * ( contador - 1 ) ) // 2 );
System.out.println ( pares );
