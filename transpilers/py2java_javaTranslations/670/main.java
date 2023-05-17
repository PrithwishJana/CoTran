var t = int ( input ( ) );
for _ in range ( t ) :
    x , y , w , var h = map ( int , input ( ) . split ( ) );
    var n = int ( input ( ) );
    var ans = 0;
    for _ in range ( n ) :
        cx , var cy = map ( int , input ( ) . split ( ) );
        if (x <= cx <= x + w and y <= cy <= y + h) {
            ans += 1;
        }
     System.out.println ( ans );
