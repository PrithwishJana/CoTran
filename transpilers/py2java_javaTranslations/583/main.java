public void first_substring ( s ) {
    var n = len ( s ) ; c = 0 ;;
    var mpp = {} ;;
    for i in range ( n ) :
        if (( s { i } == ' ' or s { i } == ';//' )) {
            var s1 = s { c : i } ;;
            mpp { s1 } = 1 ;;
            c = i + 1 ;;
        }
     for i in range ( n ) :
        if (( s { i } == ' ' )) {
            continue ;;
        }
         for j in range ( n ) :
            if (( s { j } == ' ' )) {
                break ;;
            }
             s1 = s { i : j + 1 } ;;
            s2 = s1 ;;
            s1 = s1 { : : - 1 } ;;
            if (s1 in mpp) {
                if (mpp { s1 }) {
                    return s2 ;;
                }
             }
     return "-1" ;;
}
if (__name__ == "__main__") {
    s = "mango is sweet when nam en tastes it;//" ;
    s1 = first_substring ( s ) ;;
    System.out.println ( s1 ) ;;
}
 