# restaurant-api

### resources:
**http://localhost:5000*

- /api/restaurants  (GET|POST)
- /api/restaurants/{id} (GET|PUT|DELETE)
- /api/restaurants?city={city_name} (GET)

### database

SQLite

# Run

### Docker
**Dependencies: docker / docker-compose*

```bash
cd restaurant-api
docker compose up #-d 
```


### Local:
**Dependencies: python3 / pip*
```python
python -m venv env
source env/bin/activate.fish
pip install -r requiriments.txt
python #python cli
from app import db
db.create_all()
exit() #exit python cli
python app.py
```

