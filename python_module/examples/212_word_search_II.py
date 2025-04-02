from typing import List


class Solution:
    class Trie:
        def __init__(self):
            self.root = TrieNode()
        
        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            node.word = word
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        
        # Build Trie
        trie = self.Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        result = []
        
        def dfs(i, j, node):
            # Check if current position is valid
            if (i < 0 or i >= m or j < 0 or j >= n or 
                board[i][j] == '#' or board[i][j] not in node.children):
                return
            
            char = board[i][j]
            current_node = node.children[char]
            
            # If we've found a complete word
            if current_node.is_end:
                result.append(current_node.word)
                current_node.is_end = False  # Avoid duplicates
            
            # Mark cell as visited
            board[i][j] = '#'
            
            # Explore all four directions
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj, current_node)
            
            # Restore the cell
            board[i][j] = char
        
        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        
        return result


class Solution1:
    def findWord0(self, board: List[List[str]], word: str, row: int, col: int, idx: int, visited: List[List[bool]]) -> bool:
        if idx == len(word):
            return True
        elif col < 0 or col >= len(board[0]) or row < 0 or row >= len(board) \
                or visited[row][col] or board[row][col] != word[idx]:
            return False
        visited[row][col] = True
        idx += 1
        discovered = self.findWord(board, word, row + 1, col, idx, visited) \
                     or self.findWord(board, word, row - 1, col, idx, visited) \
                     or self.findWord(board, word, row, col + 1, idx, visited) \
                     or self.findWord(board, word, row, col - 1, idx, visited)

        visited[row][col] = False
        return discovered

    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        arr = []
        for word in words:
            visited = [[False] * len(board[0]) for _ in range(len(board))]
            discovered = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0] and self.findWord(board, word, i, j, 0, visited):
                        arr.append(word)
                        discovered = True
                        break
                if discovered:
                    break
        return arr

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_key = "$" # ending word key
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(ch, {})
            # mark the existence of a word in trie node
            node[word_key] = word

        rows, cols = len(board), len(board[0])
        matched_words = []

        def back_tracking(row, col, parent_trie):
            letter = board[row][col]
            cur_node = parent_trie[letter]

            # check if we find a match of word
            word_match = cur_node.pop(word_key, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() for results.
                matched_words.append(word_match)
            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + dx, col + dy
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue
                if board[new_row][new_col] not in cur_node:
                    continue
                back_tracking(new_row, new_col, cur_node)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not cur_node:
                parent_trie.pop(letter)

        for row in range(rows):
            for col in range(cols):
                # starting from each of the cells
                if board[row][col] in trie:
                    back_tracking(row, col, trie)
        return matched_words
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time limit exceeded for large test cases
        """
        m, n = len(board), len(board[0])
        def helper(idx: int, word: str, row: int, col: int) -> bool:
            if idx == len(word):
                return True
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[idx]:
                return False
            
            visited.add((row, col))

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row = row + dx
                new_col = col + dy
                if (new_row, new_col) not in visited:
                    if helper(idx + 1, word, new_row, new_col):
                        return True
            visited.remove((row, col))
            return False
        
        res = []
        for word in words:
            found = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited = set()
                        if helper(0, word, i, j):
                            res.append(word)
                            found = True
                            break
                if found:
                    break
                
        return res




if __name__ == "__main__":
    nums = [5, 1, 1]
    solution = Solution()
    board = [["b","a","b","a","b","a","b","a","b","a"],
             ["a","b","a","b","a","b","a","b","a","b"],
             ["b","a","b","a","b","a","b","a","b","a"],
             ["a","b","a","b","a","b","a","b","a","b"],
             ["b","a","b","a","b","a","b","a","b","a"],
             ["a","b","a","b","a","b","a","b","a","b"],
             ["b","a","b","a","b","a","b","a","b","a"],
             ["a","b","a","b","a","b","a","b","a","b"],
             ["b","a","b","a","b","a","b","a","b","a"],
             ["a","b","a","b","a","b","a","b","a","b"]]
    words = ["ababababaa","ababababab","ababababac","ababababad",
             "ababababae","ababababaf","ababababag","ababababah",
             "ababababai","ababababaj","ababababak","ababababal",
             "ababababam","ababababan","ababababao","ababababap",
             "ababababaq","ababababar","ababababas","ababababat",
             "ababababau","ababababav","ababababaw","ababababax",
             "ababababay","ababababaz","ababababba","ababababbb",
             "ababababbc","ababababbd","ababababbe","ababababbf",
             "ababababbg","ababababbh","ababababbi","ababababbj",
             "ababababbk","ababababbl","ababababbm","ababababbn",
             "ababababbo","ababababbp","ababababbq","ababababbr",
             "ababababbs","ababababbt","ababababbu","ababababbv",
             "ababababbw","ababababbx","ababababby","ababababbz",
             "ababababca","ababababcb","ababababcc","ababababcd",
             "ababababce","ababababcf","ababababcg","ababababch",
             "ababababci","ababababcj","ababababck","ababababcl",
             "ababababcm","ababababcn","ababababco","ababababcp",
             "ababababcq","ababababcr","ababababcs","ababababct",
             "ababababcu","ababababcv","ababababcw","ababababcx",
             "ababababcy","ababababcz","ababababda","ababababdb",
             "ababababdc","ababababdd","ababababde","ababababdf",
             "ababababdg","ababababdh","ababababdi","ababababdj",
             "ababababdk","ababababdl","ababababdm","ababababdn",
             "ababababdo","ababababdp","ababababdq","ababababdr",
             "ababababds","ababababdt","ababababdu","ababababdv",
             "ababababdw","ababababdx","ababababdy","ababababdz",
             "ababababea","ababababeb","ababababec","ababababed",
             "ababababee","ababababef","ababababeg","ababababeh",
             "ababababei","ababababej","ababababek","ababababel",
             "ababababem","ababababen","ababababeo","ababababep",
             "ababababeq","ababababer","ababababes","ababababet",
             "ababababeu","ababababev","ababababew","ababababex",
             "ababababey","ababababez","ababababfa","ababababfb",
             "ababababfc","ababababfd","ababababfe","ababababff",
             "ababababfg","ababababfh","ababababfi","ababababfj",
             "ababababfk","ababababfl","ababababfm","ababababfn",
             "ababababfo","ababababfp","ababababfq","ababababfr",
             "ababababfs","ababababft","ababababfu","ababababfv",
             "ababababfw","ababababfx","ababababfy","ababababfz",
             "ababababga","ababababgb","ababababgc","ababababgd",
             "ababababge","ababababgf","ababababgg","ababababgh",
             "ababababgi","ababababgj","ababababgk","ababababgl",
             "ababababgm","ababababgn","ababababgo","ababababgp",
             "ababababgq","ababababgr","ababababgs","ababababgt",
             "ababababgu","ababababgv","ababababgw","ababababgx",
             "ababababgy","ababababgz","ababababha","ababababhb",
             "ababababhc","ababababhd","ababababhe","ababababhf",
             "ababababhg","ababababhh","ababababhi","ababababhj",
             "ababababhk","ababababhl","ababababhm","ababababhn",
             "ababababho","ababababhp","ababababhq","ababababhr",
             "ababababhs","ababababht","ababababhu","ababababhv",
             "ababababhw","ababababhx","ababababhy","ababababhz",
             "ababababia","ababababib","ababababic","ababababid",
             "ababababie","ababababif","ababababig","ababababih",
             "ababababii","ababababij","ababababik","ababababil",
             "ababababim","ababababin","ababababio","ababababip",
             "ababababiq","ababababir","ababababis","ababababit",
             "ababababiu","ababababiv","ababababiw","ababababix",
             "ababababiy","ababababiz","ababababja","ababababjb",
             "ababababjc","ababababjd","ababababje","ababababjf",
             "ababababjg","ababababjh","ababababji","ababababjj",
             "ababababjk","ababababjl","ababababjm","ababababjn",
             "ababababjo","ababababjp","ababababjq","ababababjr",
             "ababababjs","ababababjt","ababababju","ababababjv",
             "ababababjw","ababababjx","ababababjy","ababababjz",
             "ababababka","ababababkb","ababababkc","ababababkd",
             "ababababke","ababababkf","ababababkg","ababababkh",
             "ababababki","ababababkj","ababababkk","ababababkl",
             "ababababkm","ababababkn","ababababko","ababababkp",
             "ababababkq","ababababkr","ababababks","ababababkt",
             "ababababku","ababababkv","ababababkw","ababababkx",
             "ababababky","ababababkz","ababababla","abababablb",
             "abababablc","ababababld","abababable","abababablf",
             "abababablg","abababablh","ababababli","abababablj",
             "abababablk","ababababll","abababablm","ababababln",
             "abababablo","abababablp","abababablq","abababablr",
             "ababababls","abababablt","abababablu","abababablv",
             "abababablw","abababablx","abababably","abababablz",
             "ababababma","ababababmb","ababababmc","ababababmd",
             "ababababme","ababababmf","ababababmg","ababababmh",
             "ababababmi","ababababmj","ababababmk","ababababml",
             "ababababmm","ababababmn","ababababmo","ababababmp",
             "ababababmq","ababababmr","ababababms","ababababmt",
             "ababababmu","ababababmv","ababababmw","ababababmx",
             "ababababmy","ababababmz","ababababna","ababababnb",
             "ababababnc","ababababnd","ababababne","ababababnf",
             "ababababng","ababababnh","ababababni","ababababnj",
             "ababababnk","ababababnl","ababababnm","ababababnn",
             "ababababno","ababababnp","ababababnq","ababababnr",
             "ababababns","ababababnt","ababababnu","ababababnv",
             "ababababnw","ababababnx","ababababny","ababababnz",
             "ababababoa","ababababob","ababababoc","ababababod",
             "ababababoe","ababababof","ababababog","ababababoh",
             "ababababoi","ababababoj","ababababok","ababababol",
             "ababababom","ababababon","ababababoo","ababababop",
             "ababababoq","ababababor","ababababos","ababababot",
             "ababababou","ababababov","ababababow","ababababox",
             "ababababoy","ababababoz","ababababpa","ababababpb",
             "ababababpc","ababababpd","ababababpe","ababababpf",
             "ababababpg","ababababph","ababababpi","ababababpj",
             "ababababpk","ababababpl","ababababpm","ababababpn",
             "ababababpo","ababababpp","ababababpq","ababababpr",
             "ababababps","ababababpt","ababababpu","ababababpv",
             "ababababpw","ababababpx","ababababpy","ababababpz",
             "ababababqa","ababababqb","ababababqc","ababababqd",
             "ababababqe","ababababqf","ababababqg","ababababqh",
             "ababababqi","ababababqj","ababababqk","ababababql",
             "ababababqm","ababababqn","ababababqo","ababababqp",
             "ababababqq","ababababqr","ababababqs","ababababqt",
             "ababababqu","ababababqv","ababababqw","ababababqx",
             "ababababqy","ababababqz","ababababra","ababababrb",
             "ababababrc","ababababrd","ababababre","ababababrf",
             "ababababrg","ababababrh","ababababri","ababababrj",
             "ababababrk","ababababrl","ababababrm","ababababrn",
             "ababababro","ababababrp","ababababrq","ababababrr",
             "ababababrs","ababababrt","ababababru","ababababrv",
             "ababababrw","ababababrx","ababababry","ababababrz",
             "ababababsa","ababababsb","ababababsc","ababababsd",
             "ababababse","ababababsf","ababababsg","ababababsh",
             "ababababsi","ababababsj","ababababsk","ababababsl",
             "ababababsm","ababababsn","ababababso","ababababsp",
             "ababababsq","ababababsr","ababababss","ababababst",
             "ababababsu","ababababsv","ababababsw","ababababsx",
             "ababababsy","ababababsz","ababababta","ababababtb",
             "ababababtc","ababababtd","ababababte","ababababtf",
             "ababababtg","ababababth","ababababti","ababababtj",
             "ababababtk","ababababtl","ababababtm","ababababtn",
             "ababababto","ababababtp","ababababtq","ababababtr",
             "ababababts","ababababtt","ababababtu","ababababtv",
             "ababababtw","ababababtx","ababababty","ababababtz",
             "ababababua","ababababub","ababababuc","ababababud",
             "ababababue","ababababuf","ababababug","ababababuh",
             "ababababui","ababababuj","ababababuk","ababababul",
             "ababababum","ababababun","ababababuo","ababababup",
             "ababababuq","ababababur","ababababus","ababababut",
             "ababababuu","ababababuv","ababababuw","ababababux",
             "ababababuy","ababababuz","ababababva","ababababvb",
             "ababababvc","ababababvd","ababababve","ababababvf",
             "ababababvg","ababababvh","ababababvi","ababababvj",
             "ababababvk","ababababvl","ababababvm","ababababvn",
             "ababababvo","ababababvp","ababababvq","ababababvr",
             "ababababvs","ababababvt","ababababvu","ababababvv",
             "ababababvw","ababababvx","ababababvy","ababababvz",
             "ababababwa","ababababwb","ababababwc","ababababwd",
             "ababababwe","ababababwf","ababababwg","ababababwh",
             "ababababwi","ababababwj","ababababwk","ababababwl",
             "ababababwm","ababababwn","ababababwo","ababababwp",
             "ababababwq","ababababwr","ababababws","ababababwt",
             "ababababwu","ababababwv","ababababww","ababababwx",
             "ababababwy","ababababwz","ababababxa","ababababxb",
             "ababababxc","ababababxd","ababababxe","ababababxf",
             "ababababxg","ababababxh","ababababxi","ababababxj",
             "ababababxk","ababababxl","ababababxm","ababababxn",
             "ababababxo","ababababxp","ababababxq","ababababxr",
             "ababababxs","ababababxt","ababababxu","ababababxv",
             "ababababxw","ababababxx","ababababxy","ababababxz",
             "ababababya","ababababyb","ababababyc","ababababyd",
             "ababababye","ababababyf","ababababyg","ababababyh",
             "ababababyi","ababababyj","ababababyk","ababababyl",
             "ababababym","ababababyn","ababababyo","ababababyp",
             "ababababyq","ababababyr","ababababys","ababababyt",
             "ababababyu","ababababyv","ababababyw","ababababyx",
             "ababababyy","ababababyz","ababababza","ababababzb",
             "ababababzc","ababababzd","ababababze","ababababzf",
             "ababababzg","ababababzh","ababababzi","ababababzj",
             "ababababzk","ababababzl","ababababzm","ababababzn",
             "ababababzo","ababababzp","ababababzq","ababababzr",
             "ababababzs","ababababzt","ababababzu","ababababzv",
             "ababababzw","ababababzx","ababababzy","ababababzz"]
    ret = solution.findWords(board, words)
    print(ret)