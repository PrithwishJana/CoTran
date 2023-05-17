n , var x = map ( int , input ( ) . split ( ) );
a_list = list ( map ( int , input ( ) . split ( ) ) );
a_list . sort ( );
count = 0;
for i in range ( n ) :
    x = x - a_list { i };
    count += 1;
    if (x <= 0) {
        break;
    }
 if (x == 0) {
    System.out.println ( count );
}
 else{
    System.out.println ( count - 1 );
}
