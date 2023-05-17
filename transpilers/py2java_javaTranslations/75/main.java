while (1) {
    var x = input ( );
    if (x == "0") {
        break;
    }
     var a = 0;
    var b = 0;
    for i in range ( 1 , len ( x ) ) :
        if (x { i } == "A") {
            a += 1;
        }
         else{
            b += 1;
        }
    if (a > b) {
        a += 1;
    }
     else{
        b += 1;
    }
    System.out.println ( a , b );
}
 