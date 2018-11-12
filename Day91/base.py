import requests

def DadJoke():
    url = r"https://icanhazdadjoke.com/"
    resp = requests.get(url)

    if (resp.ok):
        raw_data = str(resp.content)
        # Could use bs to get the elements, but just going to find
        search_term = "<meta property=\"og:description\" content=\""
        joke_start = raw_data.index(search_term)
        joke_end = raw_data.index("/>", joke_start)
        from_val = joke_start + len(search_term)
        to_val = (joke_end - len(search_term)) - joke_start - 2

        return raw_data[from_val: to_val + from_val]


if __name__ == "__main__":
    print(DadJoke())