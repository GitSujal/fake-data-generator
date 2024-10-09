# Faker 
This module is used to generate fake data that can be used in any data analysis projects. 


## Installation Instructions

**Initialise a virtual environment**

```bash
python3 -m venv venv
```

**Activate the virtual environment**

```bash
source venv/bin/activate
```

**Install all pre-requisites**

```bash
pip install -r requirements.txt
```


## Data Requirements

### 1. User Data
* 3000 Users

- User ID
- First Name
- Last Name
- Email
- Age 
- Gender
- Postcode
- Country



### 2. Items Data

- Scrape from [Sunglass hut](https://www.sunglasshut.com/au)
- At least 300 item

- Item ID
- Brand
- Style
- Model
- Color
- Material
- Shape
- Size
- Price
- Prescription
- Polarized

*  Lens details
- ColorDark 
- Material
- Technology


### 3. User Interaction Data

- 100000 interactions
- Use has from 0 to 10 interactions with mean of 2 and std of 3

- User is 70% likely to buy the same brand
- User is 50% likely to buy the same style
- User is 90% likely to buy the same size
- User is 70% likely to buy the same color
- User is 65% likely to buy the same price range
- User buying prescription glasses is 95% likely to buy prescription glasses again
- User buying polarized glasses is 60% likely to buy polarized glasses again

