var n = int ( input ( ) );
var k = int ( input ( ) );
A = int ( input ( ) );
B = int ( input ( ) );
x = n;
i = 0;
public void f ( x , i ) {
    if (x == 1) {
        return i;
    }
     else if (x % k == 0 and B <= ( x - x // k ) * A){
        return f ( x // k , i + B );
    }
    else if (x % k == 0){
        return f ( 1 , i + A * ( x - 1 ) );
    }
    else{
        return f ( x - x % k , i + A * ( x % k ) );
    }
}
System.out.println ( f ( x , 0 ) );
