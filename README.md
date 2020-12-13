## Preview

<img width="1399" alt="Screenshot 2020-12-13 at 13 15 39" src="https://user-images.githubusercontent.com/15812620/102008961-569b7b00-3d45-11eb-9985-1b04be8b0deb.png">


Nope, it's not a bug. The total price also includes a discount.

## Prerequisites

You will need:

- `Docker`
- `Pipenv`

## Running

Clone repository and go to the project directory (in where Dockerfile is):
```
~ git clone git@github.com:lk-geimfari/tomsc.git
~ cd tomsc
```

and then build FastAPI image:

```
docker build -t tomsc .
```

Run a container based on your image:

```
docker run --name tomsc -p 80:80 tomsc
```

Now you can use frontend, just open file `fronted/index.html` in your browser.


## Tests

First of all, you need to install all the development dependencies, like this:

```
pipenv install --dev
```

Then run tests:

```
pipenv run pytest .
```

or just:

```
pytest .
```
