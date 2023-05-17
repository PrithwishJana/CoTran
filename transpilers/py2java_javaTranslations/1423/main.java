public void converthenumber ( n ) {
    var s = str ( n ) ;;
    res = "" ;;
    for i in range ( len ( s ) ) :
        if (( s { i } == '1' or s { i } == '3' or s { i } == '5' or s { i } == '7' or s { i } == '9' )) {
            res += s { i } ;;
        }
         if (( len ( res ) == 2 )) {
            break ;;
        }
     if (( len ( res ) == 2 )) {
        System.out.println ( res ) ;;
    }
     else{
        System.out.println ( "-1" ) ;;
    }
}
if (var __name__ == "__main__") {
    var n = 18720 ;;
    converthenumber ( n ) ;;
}
 