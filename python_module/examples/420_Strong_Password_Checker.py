import itertools


class Solution:
    """
        A password is considered strong if the below conditions are all met:

        It has at least 6 characters and at most 20 characters.
        It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
        It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
        Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

        In one step, you can:

        Insert one character to password,
        Delete one character from password, or
        Replace one character of password with another character.

        Example 1:

        Input: password = "a"
        Output: 5
        Example 2:

        Input: password = "aA1"
        Output: 3
        Example 3:

        Input: password = "1337C0d3"
        Output: 0
    """
    def strongPasswordChecker1(self, password: str) -> int:
        if not password:
            return 6
        n = len(password)

        missing_type = 3
        if any('a' <= c <= 'z' for c in password): missing_type -= 1
        if any('A' <= c <= 'Z' for c in password): missing_type -= 1
        if any(c.isdigit() for c in password): missing_type -= 1

        change = 0
        one = two = 0
        p = 2
        while p < n:
            if password[p] == password[p - 1] == password[p - 2]:
                length = 2
                while p < n and password[p] == password[p - 1]:
                    length += 1
                    p += 1
                change += length // 3
                if length % 3 == 0: one += 1
                elif length % 3 == 1: two += 1
            else:
                p += 1

        if n < 6:
            return max(missing_type, 6 - n)
        elif n <= 20:
            return max(missing_type, change)
        else:
            delete = n - 20
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_type, change)

    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    def strongPasswordChecker(self, password: str) -> int:
        characters = set(password)

        # Check rule (2)
        needs_lowercase = not (characters & self.lowercase)
        needs_uppercase = not (characters & self.uppercase)
        needs_digit = not (characters & self.digit)
        num_required_type_replaces = int(needs_lowercase + needs_uppercase + needs_digit)

        # Check rule (1)
        num_required_inserts = max(0, 6 - len(password))
        num_required_deletes = max(0, len(password) - 20)

        # Check rule (3)
        # Convert s to a list of repetitions for us to manipulate
        # For s = '11aaabB' we have groups = [2, 3, 1, 1]
        groups = [len(list(grp)) for _, grp in itertools.groupby(password)]

        # We apply deletions iteratively and always choose the best one.
        # This should be fine for short passwords :)
        # A delete is better the closer it gets us to removing a group of three.
        # Thus, a group needs to be (a) larger than 3 and (b) minimal wrt modulo 3.
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1

        for _ in range(num_required_deletes):
            apply_best_delete()

        # On the finished groups, we need one repace per 3 consecutive letters.
        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )

        return (
            # Deletes need to be done anyway
                num_required_deletes
                # Type replaces can be eaten up by inserts or group replaces.
                # Note that because of the interplay of rules (1) and (2), the required number of group replaces
                # can never be greater than the number of type replaces and inserts for candidates of length < 6.
                + max(
            num_required_type_replaces,
            num_required_group_replaces,
            num_required_inserts,
        )
        )

