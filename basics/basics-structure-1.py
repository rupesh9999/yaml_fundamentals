import yaml

my_file = "basics/basics-structure-1.yaml"

with open(my_file, 'r', encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print("---")
            print(f"key: {key}")
            print(f"value: {value}")
            datatype = type(value)
            print(f"The datatype of {value} is {datatype}")
    except yaml.YAMLError as err:
        print(err)