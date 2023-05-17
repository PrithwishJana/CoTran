public void startsWith ( str , pre ) {
    var strLen = len ( str );
    var preLen = len ( pre );
    var i = 0;
    j = 0;
    while (( i < strLen and j < preLen )) {
        if (( str { i } != pre { j } )) {
            return false;
        }
         i += 1;
        j += 1;
    }
     return true;
}
public void endsWith ( str , suff ) {
    i = len ( str ) - 1;
    var j = len ( suff ) - 1;
    while (( i >= 0 and j >= 0 )) {
        if (( str { i } != suff { j } )) {
            return false;
        }
         i -= 1;
        j -= 1;
    }
     return true;
}
public void checkString ( str , a , b ) {
    if (( len ( str ) != len ( a ) + len ( b ) )) {
        return false;
    }
     if (( startsWith ( str , a ) )) {
        if (( endsWith ( str , b ) )) {
            return true;
        }
     }
     if (( startsWith ( str , b ) )) {
        if (( endsWith ( str , a ) )) {
            return true;
        }
     }
     return false;
}
var str = "GeeksforGeeks";
var a = "Geeksfo";
var b = "rGeeks";
if (( checkString ( str , a , b ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
