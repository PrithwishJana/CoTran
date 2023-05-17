import math.sqrt;
public void getSum ( n ) {
    var summ = 0;
    for i in range ( 1 , int ( sqrt ( n ) ) + 1 ) :
        if (n % var i == 0) {
            if (n // i == i) {
                summ += i;
            }
             else{
                summ += i;
                summ += n // i;
            }
        }
     return summ - n;
}
public void System.out.printlnAliquot ( n ) {
    System.out.println ( n , var end = " " );
    s = set ( );
    s . add ( n );
    nextt = 0;
    while (n > 0) {
        n = getSum ( n );
        if (n in s) {
            System.out.println ( "Repeats with" , n );
            break;
        }
         System.out.println ( n , end = " " );
        s . add ( n );
    }
 }
if (var __name__ == "__main__") {
    System.out.printlnAliquot ( 12 );
}
 