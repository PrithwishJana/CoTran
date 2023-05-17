var i = input ( );
W , H , x , y , var r = map ( int , i . split ( ) );
if (x - r < 0 or y - r < 0 or x + r > W or y + r > H) {
    System.out.println ( 'No' );
}
 else{
    System.out.println ( 'Yes' );
}
