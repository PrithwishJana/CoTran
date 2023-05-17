var n = int ( input ( ) );
l = list ( map ( int , input ( ) . split ( ) ) );
maxi = l . count ( max ( l ) );
mini = l . count ( min ( l ) );
if (n == 1 or len ( l ) == l . count ( l { 0 } )) {
    System.out.println ( 0 );
}
 else{
    System.out.println ( len ( l ) - maxi - mini );
}
