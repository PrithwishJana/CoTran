while (true) {
    r , var a = input ( ) . split ( );
    if (var r == "0") {
        break;
    }
     var h = 0;
    for x , y in zip ( r , a ) :
        if (var x == y) {
            h += 1;
        }
     var b = - h;
    for (int x = 0; x < r.length; x++){
        if (x in a) {
            b += 1;
        }
    }
     System.out.println ( h , b );
}
 