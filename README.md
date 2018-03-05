# magento-python

magento-python is an API wrapper for Magento written in Python

## Installing
```
pip install magento-python
```

## Usage
```
from magento.client import Client

client = Client('SERVER_URL', 'ACCESS_TOKEN') # Host must have trailing slash
```

### Search product
All
```
response = client.search_product({'searchCriteria': ''})
```

Order by created_at, just one item
```
response = client.search_product({'searchCriteria[sortOrders][0][field]': 'created_at', 'searchCriteria[pageSize]': '1'})
```

Filter by created_date greater than 2018-02-26 15:31:09, up to 100 items
```
response = client.search_product({'searchCriteria[filter_groups][0][filters][0][field]': 'created_at', 'searchCriteria[filter_groups][0][filters][0][value]': '2018-02-26 15:31:09', 'searchCriteria[filter_groups][0][filters][0][condition_type]': 'gt', 'searchCriteria[pageSize]': '100'})
```

### Create Product
```
data = {
    "product": {
        "name": 'Perfume Antonio Banderas',
        "sku": 'PAB',
        'type_id': 'simple',
        'attribute_set_id': '4',
        'price': '100000'
    }
}
response = client.create_product(data)
```

### Get Product
By SKU
```
response = client.get_product('SKU')
```

### Delete Product
By SKU
```
response = client.delete_product('SKU')
```

### Search customer
All
```
response = client.search_customer({'searchCriteria': ''})
```

### Create customer
```
data = {
    "customer": {
        "email": "janedoe@jd.com",
        "firstname": "Jane",
        "lastname": "Doe",
        "addresses": [{
            "defaultShipping": True,
            "defaultBilling": True,
            "firstname": "Jane",
            "lastname": "Doe",
            "region": {
                "regionCode": "NY",
                "region": "New York",
                "regionId": 43
            },
            "postcode": "10755",
            "street": ["123 Oak Ave"],
            "city": "Purchase",
            "telephone": "512-555-1111",
            "countryId": "US"
        }]
    },
    "password": "Password1"
}
response = client.create_customer(data)
```

### Get customer
By ID
```
response = client.get_customer('CUSTOMER_ID')
```

### Delete Product
By ID
```
response = client.delete_customer('CUSTOMER_ID')
```

### Search order
All
```
response = client.search_order({'searchCriteria': ''})
```

### Get order
By ID
```
response = client.get_order('ORDER_ID')
```

### Get product types
All
```
response = client.get_product_types({'searchCriteria': ''})
```



### Get product attribute sets
All
```
response = client.get_product_attribute_sets({'searchCriteria': ''})
```



### Get customer groups
All
```
response = client.get_customer_groups({'searchCriteria': ''})
```

## Contributing
```
Fork it ( https://github.com/GearPlug/magento-python/fork )
Create your feature branch (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create a new Pull Request
```
