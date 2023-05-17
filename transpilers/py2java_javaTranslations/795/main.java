var n = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var c = 0;
for i in range ( n ) :
    var m = i;
    for j in range ( i , n ) :
        if a { m } > a { j } : m = j;
    if i != m : a { m } , a { i } = a { i } , a { m } ; c += 1;
System.out.println ( * a );
System.out.println ( c );
