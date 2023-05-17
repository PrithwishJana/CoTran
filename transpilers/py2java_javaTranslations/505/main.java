public void checkIfStartsWithCapital ( string ) {
    if (( string { 0 } >= 'A' and string { 0 } <= 'Z' )) {
        return 1 ;;
    }
     else{
        return 0 ;;
    }
}
public void check ( string ) {
    if (( checkIfStartsWithCapital ( string ) )) {
        System.out.println ( "Accepted" ) ;;
    }
     else{
        System.out.println ( "Not Accepted" ) ;;
    }
}
if (var __name__ == "__main__") {
    var string = "GeeksforGeeks" ;;
    check ( string ) ;;
    string = "geeksforgeeks" ;;
    check ( string ) ;;
}
 