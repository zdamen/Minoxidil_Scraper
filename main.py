import json
from operator import *
from Scraping_Functions import *
import requests
import time
# pre req info serving size
# 1 month of minoxidil foam = 60ml
# 1 month of minoxidil solution = 60g
# 1 month of finasteride = 30 1mg tabs


if __name__ == "__main__":
    data = {
    "MinoxidilFoam": [
        [
            "KirklandCostco",
            [
                8.331666666666667,
                "https://www.costco.com/CatalogSearch?dept=All&keyword=Kirkland+Signature+Hair+Regrowth+Treatment+"
            ]
        ],
        [
            "Keeps",
            [
                11.1,
                "https://www.keeps.com/our-products"
            ]
        ],
        [
            "Rogain",
            [
                17.333333333333332,
                "https://www.amazon.com/Rogaine-Minoxidil-Regrowth-Treatment-Thinning/dp/B0012BNVE8/"
            ]
        ],
        [
            "Hims",
            [
                20.0,
                "https://www.forhims.com/hair-loss/minoxidil-foam"
            ]
        ]
    ],
    "MinoxidilSolution": [
        [
            "KirklandCostco",
            [
                2.998333333333333,
                "https://www.costco.com/CatalogSearch?dept=All&keyword=Kirkland+Signature+Hair+Regrowth+Treatment+"
            ]
        ],
        [
            "Keeps",
            [
                7.333333333333333,
                "https://www.keeps.com/our-products"
            ]
        ],
        [
            "Rogain",
            [
                11.553333333333333,
                "https://www.amazon.com/Rogaine-Strength-Minoxidil-Solution-Treatment/dp/B0000Y8H3S/"
            ]
        ],
        [
            "Hims",
            [
                15.0,
                "https://www.forhims.com/hair-loss/minoxidil"
            ]
        ],
        [
            "Roman",
            [
                16.0,
                "https://ro.co/hair-loss/"
            ]
        ],
        [
            "HappyHead",
            [
                59.0,
                "https://www.happyhead.com/products/topical-minoxidil/"
            ]
        ]
    ],
    "Finasteride": [
        [
            "AmazonPharmacy",
            [
                13.7,
                "https://pharmacy.amazon.com/dp/B084BR2Z6S?keywords=Finasteride&qid=1674104225&sr=8-1"
            ]
        ],
        [
            "Keeps",
            [
                16.666666666666668,
                "https://www.keeps.com/our-products"
            ]
        ],
        [
            "Roman",
            [
                20.0,
                "https://ro.co/hair-loss/"
            ]
        ],
        [
            "HappyHead",
            [
                24.0,
                "https://www.happyhead.com/products/oral-finasteride/"
            ]
        ],
        [
            "Hims",
            [
                26.0,
                "https://www.forhims.com/shop/hair-finasteride"
            ]
        ]
    ]
}




    api_endpoint = 'http://localhost:3000/UpdateData'
    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        print('Data was posted successfully')
    else:
        print('Error posting data')
