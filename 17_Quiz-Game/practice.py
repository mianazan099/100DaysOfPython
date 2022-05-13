# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         self.following += 1
#         user.followers += 1


# user_1 = User('001', 'Mian')
# user_2 = User('002', 'Azan')
# print(f'followers_1: {user_1.followers}')
# print(f'following_1: {user_1.following}')
# print(f'followers_2: {user_2.followers}')
# print(f'following_2: {user_2.following}')
# user_1.follow(user_2)
# user_1.follow(user_2)
# user_2.follow(user_1)
# print(f'followers_1: {user_1.followers}')
# print(f'following_1: {user_1.following}')
# print(f'followers_2: {user_2.followers}')
# print(f'following_2: {user_2.following}')
