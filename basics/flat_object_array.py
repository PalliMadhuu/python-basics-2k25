import pprint

class ConvertNestedToFlat:
    @staticmethod
    def flat_nested(obj, parent_key='', separator='_'):
        try:
            final_object = {}
            if isinstance(obj, dict):
                for k, v in obj.items():
                    new_key = f"{parent_key}{separator}{k}" if parent_key else k
                    final_object.update(ConvertNestedToFlat.flat_nested(v, new_key, separator=separator))
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    new_key = f"{parent_key}[{i}]"
                    final_object.update(ConvertNestedToFlat.flat_nested(item, new_key, separator=separator))
            else:
                final_object[parent_key] = obj

        except Exception as e:
            print(f"An Error Occurred: {e}")
        else:
            return final_object

data = {
    "user": {
        "name": "Madhu",
        "skills": [
            {"name": "Python", "level": "Advanced"},
            {"name": "Angular", "level": "Intermediate"}
        ]
    },
    "projects": ["Salesforce", "WebApp"],
    "profile": {
        "location": {"country": "India", "city": "Hyderabad"}
    }
}

flattened = ConvertNestedToFlat.flat_nested(data)
pprint.pprint(flattened)
