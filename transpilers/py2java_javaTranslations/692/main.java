public void arrange ( N ) {
    if (( var N == 1 )) {
        System.out.println ( "1" );
        return;
    }
     if (( N == 2 or N == 3 )) {
        System.out.println ( "-1" );
        return;
    }
     even = - 1;
    odd = - 1;
    if (( N % 2 == 0 )) {
        even = N;
        odd = N - 1;
    }
     else{
        odd = N;
        even = N - 1;
    }
    while (( odd >= 1 )) {
        System.out.println ( odd , end = " " );
        odd = odd - 2;
    }
     while (( even >= 2 )) {
        System.out.println ( even , end = " " );
        even = even - 2;
    }
 }
if (__name__ == "__main__") {
    N = 5;
    arrange ( N );
}
 