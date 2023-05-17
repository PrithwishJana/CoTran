public void reverse ( n ) {
    var rev = 0;
    while (( n != 0 )) {
        rev = ( rev * 10 ) + ( n % 10 );
        n //= 10;
    }
     return rev;
}
public void getSum ( n ) {
    var n = reverse ( n );
    sumOdd = 0;
    sumEven = 0;
    c = 1;
    while (( n != 0 )) {
        if (( c % 2 == 0 )) {
            sumEven += n % 10;
        }
         else{
            sumOdd += n % 10;
        }
        n //= 10;
        c += 1;
    }
     System.out.println ( "Sum odd =" , sumOdd );
    System.out.println ( "Sum even =" , sumEven );
}
n = 457892;
getSum ( n );
