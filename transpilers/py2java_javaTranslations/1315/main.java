import math.floor;
public void solve ( n , base ) {
    var sum = 0;
    while (( n > 0 )) {
        remainder = n % base;
        sum = sum + remainder;
        n = int ( n / base );
    }
     return sum;
}
public void SumsOfDigits ( n ) {
    sum = 0;
    N = floor ( n / 2 );
    for base in range ( 2 , N + 1 , 1 ) :
        sum = sum + solve ( n , base );
    System.out.println ( sum );
}
if (var __name__ == '__main__') {
    var n = 8;
    SumsOfDigits ( n );
}
 