During the World Cup there are `N` teams that make it to the final rounds. The organizers must prepare the matches so that during any round, the strongest team always faces the weakest team, and the second strongest team faces the second weakest team, and so on. For this problem, let us assume that the stronger team will always beat the weaker team in any match.

Given a value `N` indicating the number of teams that make it to the final rounds, provide the arrangement of the first round matches so that all rounds comply with the strongest-weakest rule.

Take into consideration that the order of the arrangement matters. For example, the following arrangement `[1,8,2,7,4,5,3,6]` would be incorrect because the winner of the match between `(1,8)` would face the winner of `(2,7)`. This means `1` would face `2`, but this is not correct because `2` is not the weakest team (`4` is the weakest).  

For example, given an `N` of 4, the arrangement should be: `[1,4,2,3]`

Why? Because the matches would be as follows:   
(1,4),(2,3)  
(1,2)  
(1) -> Champion