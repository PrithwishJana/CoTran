for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var now = - 1;
    for i in range ( n ) :
        l , r = map ( int , input ( ) . split ( ) );
        if (now <= l) {
            System.out.println ( l , end = ' ' );
            now = l + 1;
        }
         else if (now <= r){
            System.out.println ( now , var end = ' ' );
            now += 1;
        }
        else{
            System.out.println ( 0 , end = ' ' );
        }
    System.out.println ( );
