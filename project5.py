import random
import string

urls = {}

def make_short_code():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(4))

def shorten_url(long_url):
    code = make_short_code()
    while code in urls:
        code = make_short_code()  
    urls[code] = long_url
    return code

def get_original_url(code):
    return urls.get(code)

def main():
    print("Welcome to Simple URL Shortener!")
    while True:
        print("\nWhat do you want to do?")
        print("1 - Shorten URL")
        print("2 - Get original URL from short code")
        print("3 - Exit")
        choice = input("Choose 1, 2 or 3: ")

        if choice == '1':
            long_url = input("Enter the full URL to shorten: ")
            short_code = shorten_url(long_url)
            print(f"Your short URL is: https://short.ly/{short_code}")

        elif choice == '2':
            code = input("Enter the short code: ")
            original = get_original_url(code)
            if original:
                print(f"This short code redirects to: {original}")
            else:
                print("Sorry, no URL found for that code.")

        elif choice == '3':
            print("Thanks for using the URL Shortener. Bye!")
            break

        else:
            print("Oops, that's not a valid choice. Try again.")

if __name__ == "__main__":
    main()
