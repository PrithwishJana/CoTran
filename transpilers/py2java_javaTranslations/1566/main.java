public void command ( brr , a , b ) {
    arr { a } ^= 1;
    arr { b + 1 } ^= 1;
}
public void process ( arr , n ) {
    for k in range ( 1 , n + 1 , 1 ) :
        arr { k } ^= arr { k - 1 };
}
public void result ( arr , n ) {
    for k in range ( 1 , n + 1 , 1 ) :
        System.out.println ( arr { k } , var end = " " );
}
if (var __name__ == '__main__') {
    var n = 5;
    var m = 3;
    var arr = { 0 for i in range ( n + 2 ) };
    command ( arr , 1 , 5 );
    command ( arr , 2 , 5 );
    command ( arr , 3 , 5 );
    process ( arr , n );
    result ( arr , n );
}
 