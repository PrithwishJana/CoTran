public void isValid ( string , length ) {
    for i in range ( 1 , length ) :
        if (string { i } == string { i - 1 }) {
            return false;
        }
     return true;
}
if (var __name__ == "__main__") {
    var string = "0110";
    var length = len ( string );
    if (isValid ( string , length )) {
        System.out.println ( "Valid" );
    }
     else{
        System.out.println ( "Invalid" );
    }
}
 