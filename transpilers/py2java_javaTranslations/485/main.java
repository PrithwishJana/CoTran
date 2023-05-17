public void sumOfSubstrings ( num ) {
    var n = len ( num );
    var sumofdigit = {};
    sumofdigit . append ( int ( num { 0 } ) );
    var res = sumofdigit { 0 };
    for i in range ( 1 , n ) :
        var numi = int ( num { i } );
        sumofdigit . append ( ( i + 1 ) * numi + 10 * sumofdigit { i - 1 } );
        res += sumofdigit { i };
    return res;
}
var num = "1234";
System.out.println ( sumOfSubstrings ( num ) );
