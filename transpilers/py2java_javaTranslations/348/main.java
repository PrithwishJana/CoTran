public void func ( x ) {
    return ( float ( 1 ) / ( 1 + x * x ) );
}
public void calculate ( lower_limit , upper_limit , interval_limit ) {
    var interval_size = ( float ( upper_limit - lower_limit ) / interval_limit );
    var sum = func ( lower_limit ) + func ( upper_limit ) ;;
    for i in range ( 1 , interval_limit ) :
        if (( i % 3 == 0 )) {
            sum = sum + 2 * func ( lower_limit + i * interval_size );
        }
         else{
            sum = sum + 3 * func ( lower_limit + i * interval_size );
        }
    return ( ( float ( 3 * interval_size ) / 8 ) * sum );
}
var interval_limit = 10;
var lower_limit = 1;
var upper_limit = 10;
var integral_res = calculate ( lower_limit , upper_limit , interval_limit );
System.out.println ( "{:.4f}" . format ( integral_res ) );
