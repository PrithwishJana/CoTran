while (true) {
    a , en , var b = input ( ) . split ( );
    if (en == '?') {
        break;
    }
     else{
        a = int ( a );
        b = int ( b );
        if (var en == '+') {
            System.out.println ( a + b );
        }
         else if (en == '-'){
            System.out.println ( a - b );
        }
        else if (en == '*'){
            System.out.println ( a * b );
        }
        else if (en == '/'){
            System.out.println ( int ( a / b ) );
        }
    }
}
 