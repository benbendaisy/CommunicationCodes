class Solution:
    """
        Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

        In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

        The canonical path should have the following format:

        The path starts with a single slash '/'.
        Any two directories are separated by a single slash '/'.
        The path does not end with a trailing '/'.
        The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
        Return the simplified canonical path.

        Example 1:

        Input: path = "/home/"
        Output: "/home"
        Explanation: Note that there is no trailing slash after the last directory name.
        Example 2:

        Input: path = "/../"
        Output: "/"
        Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
        Example 3:

        Input: path = "/home//foo/"
        Output: "/home/foo"
        Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
    """
    def simplifyPath1(self, path: str) -> str:
        dir_stack = []
        fields = path.split("/")
        for field in fields:
            if dir_stack and field == "..":
                dir_stack.pop()
            elif field not in [".", "", ".."]:
                dir_stack.append(field)
        return "/" + "/".join(dir_stack)
    
    def simplifyPath2(self, path: str) -> str:
        if not path:
            return path
        
        fields = path.split("/")
        res = ["/"]
        for field in fields:
            match field:
                case ".":
                    continue
                case "":
                    continue
                case "..":
                    if len(res) >= 2:
                        res.pop()
                case _:
                    if len(res) > 1:
                        res.append(f"/{field}")
                    else:
                        res.append(f"{field}")
        return "".join(res)
    
    def simplifyPath3(self, path: str) -> str:
        if not path:
            return path
        
        fields = path.split("/")
        res = []
        for field in fields:
            match field:
                case "." | "":
                    continue
                case "..":
                    if res:
                        res.pop()
                case _:
                    res.append(f"{field}")
                        
        return "/" + "/".join(res)