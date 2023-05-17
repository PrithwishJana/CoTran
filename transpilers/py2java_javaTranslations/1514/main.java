var n = int ( input ( ) );
var array = input ( ) . split ( );
var a = 0;
while (a < n) {
    array { a } = int ( array { a } );
    a += 1;
}
 var smallest = min ( array );
array . sort ( );
var i = 1;
var t_or_f = true;
while (i < n) {
    if (array { i } / smallest != int ( array { i } / smallest )) {
        t_or_f = false;
    }
     i += 1;
}
 if (t_or_f == true) {
    System.out.println ( smallest );
 }
 else{
    System.out.println ( - 1 );
}
