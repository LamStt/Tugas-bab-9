from app.model.user import Users
from app import response, app

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def transform(users):
    array = []
    for i in users:
        array.append({
            'id' : i.id,
            'name' : i.name,
            'email' : i.email
        })
    return array   

# def show(id):
#     try:
#         users = Users.query.filter_by(id=id).first()
#         if not users:
#             return response.badRequest([], 'Empty....')

#         data = singleTransform(users)
#         return response.ok(data) 
