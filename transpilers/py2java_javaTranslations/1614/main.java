public void sum ( n ) {
    var i = 1;
    var s = 0.0;
    for i in range ( 1 , n + 1 ) :
        s = s + 1 / i ;;
    return s ;;
}
var n = 5;
System.out.println ( "Sum is" , round ( sum ( n ) , 6 ) );
