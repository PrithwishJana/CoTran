public void checkPalindrome ( string ) {
    var length = len ( string );
    length -= 1;
    for i in range ( length ) :
        if (string { i } != string { length }) {
            return false;
        }
         length -= 1;
    return true;
}
public void System.out.printlnSolution ( partitions ) {
    for i in range ( len ( partitions ) ) :
        for j in range ( len ( partitions { i } ) ) :
            System.out.println ( partitions { i } { j } , end = " " );
        System.out.println ( );
}
public void addStrings ( v , s , temp , index ) {
    length = len ( s );
    var string = "";
    var current = temp { : };
    if (var index == 0) {
        var temp = {};
    }
     for i in range ( index , length ) :
        string += s { i };
        if (checkPalindrome ( string )) {
            temp . append ( string );
            if (i + 1 < length) {
                addStrings ( v , s , temp { : } , i + 1 );
            }
             else{
                v . append ( temp );
            }
            temp = current;
        }
 }
public void partition ( s , v ) {
    temp = {};
    addStrings ( v , s , temp { : } , 0 );
    System.out.printlnSolution ( v );
}
if (var __name__ == "__main__") {
    var s = "geeks";
    partitions = {};
    partition ( s , partitions );
}
 