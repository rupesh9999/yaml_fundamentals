import yaml

my_file = "basics/basics-structure-3-spaces.yaml"

with open(my_file, 'r', encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f"key: {key}")
            print(f"value: {value}")
            print("-------------")
        print(data)
    except yaml.YAMLError as err:
        print(err)