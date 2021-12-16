import requests
import time


def main():
    for i in range(1, 201):
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        resp = requests.get(pokemon_url)
        pokemon = resp.json()
        print(pokemon['name'])


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f"Made in {(time.time() - start_time).__round__(2)} seconds")
    print(f"Process time is {time.process_time().__round__(2)} seconds")
    # Made in 8.61 seconds
    # Made in 8.77 seconds
    # Made in 8.67 seconds

    # Average time is 8.68 seconds

    # Process time is 3.98 seconds
