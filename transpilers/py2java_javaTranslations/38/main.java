while (true) {
    try{
        xa1 , ya1 , xa2 , ya2 , xb1 , yb1 , xb2 , var yb2 = map ( float , input ( ) . split ( ) );
    }
    except EOFError :
        break;
    if (xb2 < xa1 or xb1 > xa2 or yb2 < ya1 or yb1 > ya2) {
        System.out.println ( "NO" );
    }
     else{
        System.out.println ( "YES" );
    }
}
 