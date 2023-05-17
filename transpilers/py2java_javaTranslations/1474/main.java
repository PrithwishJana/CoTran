m , var b = map ( int , input ( ) . split ( ) );
var maximum = 0;
for y in range ( b + 1 ) :
    sum = ( m * ( b - y ) + y ) * ( m * ( b - y ) + 1 ) * ( y + 1 ) // 2;
    if (maximum <= sum) {
        maximum = sum;
    }
     else{
        break ;;
    }
System.out.println ( maximum );
