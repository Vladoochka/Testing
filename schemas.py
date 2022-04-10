JOKES_RANDOM = {
    'type': 'object',
    'properties': {
        'categories': {"type": 'array'},
        'created_at': {"type": 'string'},
        'icon_url': {"type": 'string'},
        'id': {"type": 'string'},
        'updated_at': {"type": 'string'},
        'url': {"type": 'string'},
        'value': {"type": 'string'},

    },
    'required': ['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value']
}

JOKES_SEARCH = {
    'properties': {
        'categories': {"type": 'array'},
        'created_at': {"type": 'string'},
        'icon_url': {"type": 'string'},
        'id': {"type": 'string'},
        'updated_at': {"type": 'string'},
        'url': {"type": 'string'},
        'value': {"type": 'string'},

    },
    'required': ['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value']
}

SINGLE_USER = {
    "properties": {
        'id': {"type": 'number'},
        'email': {"type": 'string'},
        'first_name': {"type": 'string'},
        'last_name': {"type": 'string'},
        'avatar': {"type": 'string'},
    },
    'required': ['id', 'email', 'first_name', 'last_name', 'avatar']
}

SINGLE_RESOURCE = {
    "properties": {
        'id': {"type": 'number'},
        'name': {"type": 'string'},
        'year': {"type": 'number'},
        'color': {"type": 'string'},
        'pantone_value': {"type": 'string'},
    },
    'required': ['id', 'name', 'year', 'color', 'pantone_value']
}

DELAYED_RESPONSE = {
    "properties": {
        'page': {"type": "number", 'enum': [1, 2]},
        'per_page': {"type": "number", 'enum': [6]},
        'total': {"type": "number", 'enum': [12]},
        'total_pages': {"type": "number", 'enum': [2]},
        'data': {
            "type": "array",
        }
    },
    'required': ['page', 'per_page', 'total', 'total_pages', 'data']
}

GET_POSTS = {
    "properties": {
        'userId': {"type": "number"},
        'id': {"type": "number"},
        'title': {"type": "string"},
        'body': {"type": "string"},
    },
    'required': ['userId', 'id', 'title', 'body']
}

GET_COMMENTS = {
    "properties": {
        'postId': {"type": "number"},
        'id': {"type": "number"},
        'name': {"type": "string"},
        'email': {"type": "string"},
        'body': {"type": "string"},
    },
    'required': ['postId', 'id', 'name', 'email', 'body']
}

GET_ALBUMS = {
    "properties": {
        'userId': {"type": "number"},
        'id': {"type": "number"},
        'title': {"type": "string"},
    },
    'required': ['userId', 'id', 'title']
}

GET_PHOTOS = {
    "properties": {
        'albumId': {"type": "number"},
        'id': {"type": "number"},
        'title': {"type": "string"},
        'url': {"type": "string"},
        'thumbnailUrl': {"type": "string"},
    },
    'required': ['albumId', 'id', 'title', 'url', 'thumbnailUrl']
}

GET_TODOS = {
    "properties": {
        'userId': {"type": "number"},
        'id': {"type": "number"},
        'title': {"type": "string"},
        'completed': {"type": "boolean"},
    },
    'required': ['userId', 'id', 'title', 'completed']
}
