y1 , m1 , var d1 = input ( ) . split ( ":" );
y2 , m2 , var d2 = input ( ) . split ( ":" );
import datetime.*;
var date1 = datetime ( year = int ( y1 ) , month = int ( m1 ) , day = int ( d1 ) );
var date2 = datetime ( year = int ( y2 ) , month = int ( m2 ) , day = int ( d2 ) );
var res = date2 - date1;
System.out.println ( abs ( res . days ) );
