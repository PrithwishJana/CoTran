import itertools.groupby;
for _ in range ( int ( input ( ) ) ) :
    var ans = "YES";
    for k , g in groupby ( input ( ) ) :
        if (len ( list ( g ) ) == 1) {
            ans = "NO";
            break;
        }
     System.out.println ( ans );
