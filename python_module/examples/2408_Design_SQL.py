class SQL:
    """
    You are given two string arrays, names and columns, both of size n. The ith table is represented by the name names[i] and contains columns[i] number of columns.

    You need to implement a class that supports the following operations:

    Insert a row in a specific table with an id assigned using an auto-increment method, where the id of the first inserted row is 1, and the id of each new row inserted into the same table is one greater than the id of the last inserted row, even if the last row was removed.
    Remove a row from a specific table. Removing a row does not affect the id of the next inserted row.
    Select a specific cell from any table and return its value.
    Export all rows from any table in csv format.
    Implement the SQL class:

    SQL(String[] names, int[] columns)
    Creates the n tables.
    bool ins(String name, String[] row)
    Inserts row into the table name and returns true.
    If row.length does not match the expected number of columns, or name is not a valid table, returns false without any insertion.
    void rmv(String name, int rowId)
    Removes the row rowId from the table name.
    If name is not a valid table or there is no row with id rowId, no removal is performed.
    String sel(String name, int rowId, int columnId)
    Returns the value of the cell at the specified rowId and columnId in the table name.
    If name is not a valid table, or the cell (rowId, columnId) is invalid, returns "<null>".
    String[] exp(String name)
    Returns the rows present in the table name.
    If name is not a valid table, returns an empty array. Each row is represented as a string, with each cell value (including the row's id) separated by a ",".
    """

    def __init__(self, names: List[str], columns: List[int]):
        self.names = names
        self.columns = columns
        self.pos_dict = {v:i for i, v in enumerate(names)}
        self.row_ids_dict = {}
        for name in names:
            self.row_ids_dict[name] = 1
        self.data = {}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.row_ids_dict:
            return False
        if self.columns[self.pos_dict[name]] != len(row):
            return False
        row_id = self.row_ids_dict[name]
        if name in self.data:
            self.data[name][row_id] = row
        else:
            self.data[name] = {row_id: row}
        self.row_ids_dict[name] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.data:
            return False
        if rowId not in self.data[name]:
            return False
        
        del self.data[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if (name not in self.data) or (rowId not in self.data[name]) or (columnId < 0) or (columnId > len(self.data[name][rowId])):
            return "<null>"
        return self.data[name][rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        if name not in self.data:
            return []
        res = []
        for key, value in self.data[name].items():
            arr = [v for v in value]
            res.append(str(key) + "," + ",".join(arr))
        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)