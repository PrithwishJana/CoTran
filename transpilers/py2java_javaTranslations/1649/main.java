public void snoob ( x ) {
    var next = 0;
    if (( x )) {
        rightOne = x & - ( x );
        nextHigherOneBit = x + int ( rightOne );
        rightOnesPattern = x ^ int ( nextHigherOneBit );
        rightOnesPattern = ( int ( rightOnesPattern ) / int ( rightOne ) );
        rightOnesPattern = int ( rightOnesPattern ) >> 2;
        next = nextHigherOneBit | rightOnesPattern;
    }
     return next;
}
var x = 156;
System.out.println ( "Next higher number with " + "same number of set bits is" , snoob ( x ) );
