var s = str ( input ( ) );
var my_str = '';
for (int c = 0; c < s.length; c++){
    if (c == '0' or c == '1') {
        my_str += c;
    }
     else if (c == 'B' and len ( my_str ) != 0){
        my_str = my_str { : len ( my_str ) - 1 };
    }
}
System.out.println ( my_str );
