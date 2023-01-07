import Data.List

chop :: Int -> [Int] -> [[Int]]
chop _ [] = []
chop n xs = take n xs:chop n (drop n xs)

sumDiagonal :: [[Int]] -> Int
sumDiagonal x = sum $ map (uncurry (!!)) $ zip x [0..]

sumReverseDiagonal :: [[Int]] -> Int
sumReverseDiagonal x = sum $ map (uncurry (!!)) $ zip (map reverse x) [0..]

-- sumDiagnonal (tail x)
solve :: [[Int]] -> int
solve x = sumDiagonal x - sumReverseDiagonal x
-- solve [x] = abs (solvr [x] - solvl [x])

main :: IO ()
main = undefined
