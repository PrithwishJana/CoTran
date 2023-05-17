public void aliquotSum ( n ) {
    var sm = 0;
    for i in range ( 1 , n ) :
        if (( n % i == 0 )) {
            sm = sm + i;
        }
     return sm;
}
var n = 12;
System.out.println ( aliquotSum ( n ) );
