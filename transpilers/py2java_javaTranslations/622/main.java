while (1) {
    b , r , g , c , s , var t = list ( map ( int , input ( ) . split ( ) ) );
    if t == 0 : break;
    cnt = b * 5 + r * 3 + s;
    var coins = ( b * 5 + r * 3 ) * ( 15 - 2 );
    coins += b * 15;
    coins += r * 15;
    coins += 7 * g;
    coins += 2 * c;
    coins += 100 - ( t - cnt ) * 3;
    System.out.println ( coins );
}
 