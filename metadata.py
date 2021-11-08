import requests


def fromisbn(isbn: str):
    isbn = "".join(filter(str.isnumeric, isbn))
    api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    resp = requests.get(api)
    return resp.json()["items"][0]


if __name__ == "__main__":
    from pprint import pprint

    pprint(fromisbn("9780316029193"))
    pprint(fromisbn("978-0316029193"))
    pprint(fromisbn("0316029193"))
