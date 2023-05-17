public void getRemainder ( num , divisor ) {
    return ( num - divisor * ( num // divisor ) );
}
var num = 100;
var divisor = 7;
System.out.println ( getRemainder ( num , divisor ) );
