from searchform.repo.mongo_repo import MongoRepo


class FormService:
    def __init__(self):
        self.mongo_repo = MongoRepo()

    def is_subset_dict(self, sub, data):
        doc_copy = sub.copy()
        del doc_copy['_id']
        del doc_copy['name']
        for item in doc_copy.items():
            if item in data.items():
                continue
            return False
        return True

    def check_depth_form_matches(self, data):
        for doc in self.mongo_repo.read_docs_from_collection():
            if self.is_subset_dict(sub=doc, data=data):
                return doc.get('name')
        return data

    def get_form_from_mongo(self, validate_data):
        if find_element := self.mongo_repo.find_element(data=validate_data):
            return find_element.get('name')
        return self.check_depth_form_matches(data=validate_data)
