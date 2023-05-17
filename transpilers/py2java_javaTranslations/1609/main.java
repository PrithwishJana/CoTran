while (true) {
    var n = int ( input ( ) );
    if n == 0 : break;
    var dic = { 0 : 0 , 1 : 0 , 2 : 0 , 3 : 0 , 4 : 0 , 5 : 0 , 6 : 0 , 7 : 0 , 8 : 0 , 9 : 0 };
    for _ in range ( n ) :
        var c = int ( input ( ) );
        dic { c } += 1;
    for v in dic . values ( ) :
        System.out.println ( '*' * v if v != 0 else '-' );
}
 