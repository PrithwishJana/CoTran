public void countEvenOdd ( n ) {
    var even_count = 0;
    var odd_count = 0;
    while (( n > 0 )) {
        var rem = n % 10;
        if (( rem % var 2 == 0 )) {
            even_count += 1;
        }
         else{
            odd_count += 1;
        }
        n = int ( n / 10 );
    }
     System.out.println ( "Even count : " , even_count );
    System.out.println ( "\nOdd count : " , odd_count );
    if (( even_count % 2 == 0 and odd_count % 2 != 0 )) {
        return 1;
    }
     else{
        return 0;
    }
}
var n = 2335453 ;;
var t = countEvenOdd ( n ) ;;
if (( t == 1 )) {
    System.out.println ( "YES" );
}
 else{
    System.out.println ( "NO" );
}
