increaseValue :: [Int] -> Int -> [Int]
increaseValue [x:y] z
    | z == 0 = [x+1:y]
    | z == 1 = [x:y+1]

awardPoints :: Num a => [a] -> [a] -> [a]
awardPoints [a] [b] = [1]
