# from tests.conftest import BaseConfig
#
#
# class TestComment(BaseConfig):
#
#     def test_comment(self, client, user_token_headers):
#         data = {"message": "asdqwdqwdqwdqd"}
#         response = client.post('/posts/1/comments', data=data, headers=user_token_headers)
#         assert response.status_code == 200
#         # return response.json() == {
#         #     "message": "asdqwdqwdqwdqd",
#         #     "id": 1,
#         #     "post_id": 1,
#         #     "owner_comment": {
#         #         "username": "user",
#         #         "id": 3,
#         #         "is_active": 'true'
#         #     },
#         #     "created_date": "2022-05-10T05:46:23.173248"
#         # }
