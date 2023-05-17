public void fifthPowerSum ( n ) {
    var sm = 0;
    for i in range ( 1 , n + 1 ) :
        sm = sm + ( i * i * i * i * i );
    return sm;
}
var n = 6;
System.out.println ( fifthPowerSum ( n ) );
