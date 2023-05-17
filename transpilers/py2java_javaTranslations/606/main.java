var scores_of_the_participants = list ( map ( int , input ( ) . split ( ' ' ) ) );
var total_scores = sum ( scores_of_the_participants );
var chosen_teams = 0;
for i in range ( 6 ) :
    for j in range ( i + 1 , 6 ) :
        for k in range ( j + 1 , 6 ) :
            if (scores_of_the_participants { i } + scores_of_the_participants { j } + scores_of_the_participants { k } == total_scores - ( scores_of_the_participants { i } + scores_of_the_participants { j } + scores_of_the_participants { k } )) {
                chosen_teams += 1;
            }
 if (chosen_teams == 0) {
    System.out.println ( 'NO' );
}
 else{
    System.out.println ( 'YES' );
}
