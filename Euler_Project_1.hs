-- https://projecteuler.net/problem=1
-- answer: 233168

sum_of_mult :: [Integer] -> Integer

sum_of_mult l = helper l 0 1
    where helper l sum count    | count >= 1000     = sum
                                | cycle' count l    = helper l (sum + count) (count + 1)
                                | otherwise         = helper l sum (count + 1)

cycle' count l = helper count l 
    where 
        helper count [] = False
        helper count (x:xs) | mod count x == 0  = True
                            | otherwise         = helper count xs
