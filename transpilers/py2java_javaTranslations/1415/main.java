a , b , var c = map ( int , input ( ) . split ( ) );
var case_1 = a + b + c;
var case_2 = a + a + b + b;
var case_3 = a + c + c + a;
var case_4 = b + c + c + b;
System.out.println ( min ( case_1 , case_2 , case_3 , case_4 ) );
