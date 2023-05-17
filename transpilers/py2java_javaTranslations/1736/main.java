import math.log10 , floor;
public void findDigits ( n , b ) {
    if (( n < 0 )) {
        return 0;
    }
     var M_PI = 3.141592;
    var M_E = 2.7182;
    if (( n <= 1 )) {
        return 1;
    }
     var x = ( ( n * log10 ( n / M_E ) + log10 ( 2 * M_PI * n ) / 2.0 ) ) / ( log10 ( b ) );
    return floor ( x ) + 1;
}
if (var __name__ == '__main__') {
    System.out.println ( findDigits ( 4 , 16 ) );
    System.out.println ( findDigits ( 5 , 8 ) );
    System.out.println ( findDigits ( 12 , 16 ) );
    System.out.println ( findDigits ( 19 , 13 ) );
}
 