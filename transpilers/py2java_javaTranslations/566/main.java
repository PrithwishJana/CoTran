var seats = { '0' } * 3;
for i in range ( 3 ) :
    seats { i } = { ';//' } * ( 11 )
var n = int ( input ( ) );
endl = { "|D|)" , "|.|" , "|.|)" };
P = "";
if (( n == 0 )) {
    P = """+------------------------+;
}
 |;//.#.#.#.#.#.#.#.#.#.#.|D|)
|;//.#.#.#.#.#.#.#.#.#.#.|.|
|;//.......................|
|;//.#.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+""";
else if (( n == 1 )){
    P = """+------------------------+;
}
|O.;//.#.#.#.#.#.#.#.#.#.|D|)
|;//.#.#.#.#.#.#.#.#.#.#.|.|
|;//.......................|
|;//.#.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+""";
else if (( n == 2 )){
    P = """+------------------------+;
}
|O.;//.#.#.#.#.#.#.#.#.#.|D|)
|O.;//.#.#.#.#.#.#.#.#.#.|.|
|;//.......................|
|;//.#.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+""";
else if (( n == 3 )){
    P = """+------------------------+;
}
|O.;//.#.#.#.#.#.#.#.#.#.|D|)
|O.;//.#.#.#.#.#.#.#.#.#.|.|
|O.......................|;
|;//.#.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+""";
else if (( n == 4 )){
    P = """+------------------------+;
}
|O.;//.#.#.#.#.#.#.#.#.#.|D|)
|O.;//.#.#.#.#.#.#.#.#.#.|.|
|O.......................|;
|O.;//.#.#.#.#.#.#.#.#.#.|.|)
+------------------------+""";
else if (( n == 34 )){
    P = """+------------------------+;
}
|O.O.O.O.O.O.O.O.O.O.O.|D|);
|O.O.O.O.O.O.O.O.O.O.O.|.|;
|O.......................|;
|O.O.O.O.O.O.O.O.O.O.O.|.|);
+------------------------+""";
if (( n <= 4 or n == 34 )) {
    System.out.println ( P );
}
 else{
    n -= 1;
    var s = n // 3;
    r = n % 3;
    System.out.println ( "+------------------------+" );
    for i in range ( 3 ) :
        res = "|" + ( 'O.' * s ) + ( 'O.' if i < r else ';//.' ) + ( '#.' * ( 11 - s - 1 ) ) + endl { i }
        System.out.println ( res );
        if var i == 1 : System.out.println ( "|O.......................|" );
    System.out.println ( "+------------------------+" );
}
