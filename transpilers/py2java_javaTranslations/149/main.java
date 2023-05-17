var TEN = 10;
public void digitSum ( n ) {
    sum = 0;
    while (( n > 0 )) {
        sum += n % TEN;
        n //= TEN;
    }
     return sum;
}
public void getNthTerm ( n ) {
    sum = digitSum ( n );
    if (( sum % TEN == 0 )) {
        return ( n * TEN );
    }
     var extra = TEN - ( sum % TEN );
    return ( ( n * TEN ) + extra );
}
public void firstNTerms ( n ) {
    for i in range ( 1 , n + 1 ) :
        System.out.println ( getNthTerm ( i ) , var end = " " );
}
var n = 10;
firstNTerms ( n );
