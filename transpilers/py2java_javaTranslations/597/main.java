a , var b = map ( int , input ( ) . split ( ) );
if (a <= 0 and 0 <= b) {
    System.out.println ( "Zero" );
}
 else if (a < 0 and min ( b - a , - a ) % var 2 == 0){
    System.out.println ( "Negative" );
}
else{
    System.out.println ( "Positive" );
}
