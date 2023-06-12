[
    {
        '$lookup': {
            'from': 'Montadoras', 
            'localField': 'Montadora', 
            'foreignField': 'Montadora', 
            'as': 'Montadora_info'
        }
    }, {
        '$addFields': {
            'Pais': '$Montadora_info.Pais'
        }
    }, {
        '$unwind': {
            'path': '$Pais', 
            'includeArrayIndex': 'index', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$project': {
            'index': 0
        }
    }, {
        '$group': {
            '_id': '$Pais', 
            'Carros': {
                '$push': {
                    'Carro': '$Carro', 
                    'Cor': '$Cor', 
                    'Montadora': '$Montadora'
                }
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'País': '$_id', 
            'Carros': 1
        }
    }
]