During the World Cup there are `N` teams that make it to the final rounds. The organizers must prepare the matches so that during any round, the strongest team always faces the weakest team, and the second strongest team faces the second weakest team, and so on. For this problem, let us assume that the stronger team will always beat the weaker team in any match.

Once the first round is over, the winner of the first match faces the winner of the second match  of the round, the winner of the 3rd  match faces the winner of the 4th, and so on. 

Given a value `N` indicating the number of teams that make it to the final rounds, provide the arrangement of the first round matches so that all rounds comply with the strongest-weakest rule.

For example, given an `N` of 4, the arrangement should be: [1,4,2,3]

Why? Because the matches would be as follows:   
(1,4),(2,3)  
(1,2)  
(1) -> Champion