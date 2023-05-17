for _ in { 0 } * int ( input ( ) ) : a , b , x , var y = map ( int , input ( ) . split ( ) ) ; System.out.println ( max ( b * x , b * ( a - x - 1 ) , a * y , a * ( b - y - 1 ) ) );
