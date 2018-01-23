### T-Shirt API
* brand: String
* size: String
* quantity: Integer
* date_added: Timestamp

| Verb   | Descripton                                        | Scope      |
|--------|---------------------------------------------------|------------|
| GET    |  Get the collection of t-shirts by ascending order | Collection |
| GET    | Get a single t-shirt by id                         | T-shirt     |
| PUT    | Update a single t-shirt by id                      | T-shirt     |
| DELETE | Delete a single t-shirt by id                      | T-shirt     |
| POST   | Create a new t-shirt in the collection             | Collection |

### Flow of data
**GET** -> Model -> Serializer -> JSONRenderer -> Response

**POST/PUT** -> JSONParser(request) -> Serializer -> Model -> JSONRenderer -> Response
