from collections import deque

def check_palindrome(word):
    palindrome = deque(word)
    while len(palindrome) > 1:
        if palindrome.pop() != palindrome.popleft():
            return False
    return True


def main():
    word = "tacocat"
    print(check_palindrome(word))

if __name__ == "__main__":
    main()