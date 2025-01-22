# shopping_list

Pet project to prepare shopping list for the week based on the meals
I'm planning to make.

I like to head out to the grocery store with a list of items, organized by 
the type of isle they can be found.


## Setting up

1. Install docker to your machine (I work with docker 27.4.0). 
2. Clone the github project to your machine. 
3. Create `.env` under the project directory `shopping_list`. It should contain the following. 
It is recommended to customize whatever is in `<>` in the example.

```
MONGO_DB_DOCKER_NAME=mongo
MONGO_DB_USERNAME=<username>
MONGO_DB_PASSWORD=<password>
MONGO_PORT=27017
APP_HOME=/home/app
```

4. Add your recipies in `shopping_list/src/recipies.json`. The recipies should be given in a list of jsons which are
valid by the defined schema at `shopping_list/src/collection_recipies_schema.json`. 

```json
[
  {
    "name": "My awesome meal",
    "ingredients": [
      {
        "name": "yellow onion",
        "amount": 1,
        "unit": "count",
        "other": null,
        "optional": false,
        "labels": [
          "vegetable"
        ]
      },
      {
        "name": "salt",
        "amount": 34,
        "unit": "pinch",
        "other": null,
        "optional": false,
        "labels": [
          "spice"
        ]
      }
    ], 
    "instruction": "Lorem ipsum dolor sit amet, ..."
  },
  {
    "name": "My favourite meal",
    "ingredients": [
      {
        "name": "apple",
        "amount": 1,
        "unit": "count",
        "other": "large",
        "optional": false,
        "labels": [
          "vegetable"
        ]
      }
    ], 
    "instruction": "Lorem ipsum dolor sit amet, ..."
  }
]

```

5. Run `docker compose up` from your terminal. It installs mongodb, mongo-express, the app container. 
It will load your recipies into the DB if it is valid by the given schema. You can reach the mongo-express UI on [http://0.0.0.0:8081](http://0.0.0.0:8081).
