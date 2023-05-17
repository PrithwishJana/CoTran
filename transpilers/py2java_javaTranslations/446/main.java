public void q1 ( s , i ) {
    if (( var i == len ( s ) )) {
        System.out.println ( "Yes" ) ;;
        return ;;
    }
     if (( s { i } == 'a' )) {
        q1 ( s , i + 1 ) ;;
    }
     else{
        q2 ( s , i + 1 ) ;;
    }
}
public void q2 ( s , i ) {
    if (( i == len ( s ) )) {
        System.out.println ( "No" ) ;;
        return ;;
    }
     if (( s { i } == 'a' )) {
        q1 ( s , i + 1 ) ;;
    }
     else{
        q2 ( s , i + 1 ) ;;
    }
}
public void q3 ( s , i ) {
    if (( i == len ( s ) )) {
        System.out.println ( "Yes" ) ;;
        return ;;
    }
     if (( s { i } == 'a' )) {
        q4 ( s , i + 1 ) ;;
    }
     else{
        q3 ( s , i + 1 ) ;;
    }
}
public void q4 ( s , i ) {
    if (( i == s . length ( ) )) {
        System.out.println ( "No" ) ;;
        return ;;
    }
     if (( s { i } == 'a' )) {
        q4 ( s , i + 1 ) ;;
    }
     else{
        q3 ( s , i + 1 ) ;;
    }
}
public void q0 ( s , i ) {
    if (( i == len ( s ) )) {
        System.out.println ( "No" ) ;;
        return ;;
    }
     if (( s { i } == 'a' )) {
        q1 ( s , i + 1 ) ;;
    }
     else{
        q3 ( s , i + 1 ) ;;
    }
}
if (var __name__ == '__main__') {
    var s = "abbaabb" ;;
    q0 ( s , 0 ) ;;
}
 