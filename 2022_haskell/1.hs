split :: String -> Char -> [String]
split [] deim = [""]
split (c:cs) delim
  | c == delim = "" : rest
  | otherwise = (c : head rest) : tail rest
  where
      rest = split cs delim

-- main ::
-- main = do
  -- contents <- readFile "1.txt"
  -- putStrLn contents
main :: IO()
main = do 
  split "hello world" " "
-- putStrLn res
  -- res <- spliton "\n" contents
  -- putStrLn res