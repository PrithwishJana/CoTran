public void get ( l : list ) -> str {
    l . sort ( );
    for (int i = 0; i < l.length; i++){
        if (i + 1 in l and i + 2 in l) {
            return "YES";
        }
    }
     return "NO";
}
if (var __name__ == '__main__') {
    var n = int ( input ( ) );
    var lst = input ( ) . split ( );
    lst = { int ( x ) for x in lst };
    System.out.println ( get ( lst ) );
}
 