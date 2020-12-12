## Preview

<img width="1481" alt="Screenshot 2020-12-12 at 14 47 50" src="https://user-images.githubusercontent.com/15812620/101983035-15de2c00-3c89-11eb-95a4-86e253df1948.png">


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
